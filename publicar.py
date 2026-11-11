"""Publicador agendado da série Kraken (LinkedIn + Instagram).

Lê saida/conteudo.json (gerado por build.py) e publica tudo que já venceu no
calendário e ainda não foi publicado. Pensado para rodar de hora em hora.

  python3 publicar.py                 # simulação (padrão): mostra o que publicaria
  python3 publicar.py --publicar      # publica de verdade (exige config.json válido)
  python3 publicar.py --id ep01-linkedin --publicar --forcar   # um item específico

Segurança:
  * Só publica se config.json tiver "publicacao_liberada": true.
  * Itens atrasados mais de "tolerancia_horas" NÃO são publicados (evita rajadas).
  * Estado em estado.json: nunca publica o mesmo item duas vezes.
"""
import argparse
import json
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

BASE = Path(__file__).parent
SAIDA = BASE / "saida"
CONFIG = BASE / "config.json"
ESTADO = BASE / "estado.json"
LOG = BASE / "publicacoes.log"


def log(msg: str) -> None:
    linha = f"{datetime.now(timezone.utc).isoformat(timespec='seconds')} {msg}"
    print(linha)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(linha + "\n")


def config_do_ambiente() -> dict:
    """Monta a configuração a partir de variáveis de ambiente (GitHub Actions Secrets)."""
    import os
    e = os.environ.get
    if not (e("LINKEDIN_ACCESS_TOKEN") or e("INSTAGRAM_ACCESS_TOKEN")):
        return {}
    return {
        "publicacao_liberada": e("PUBLICACAO_LIBERADA", "false").lower() == "true",
        "tolerancia_horas": float(e("TOLERANCIA_HORAS", "3")),
        "linkedin": {"access_token": e("LINKEDIN_ACCESS_TOKEN", ""), "author_urn": e("LINKEDIN_AUTHOR_URN", ""),
                     "api_version": e("LINKEDIN_API_VERSION", "202610")},
        "instagram": {"access_token": e("INSTAGRAM_ACCESS_TOKEN", ""), "ig_user_id": e("INSTAGRAM_USER_ID", ""),
                      "public_base_url": e("PUBLIC_BASE_URL", ""), "login": e("INSTAGRAM_LOGIN", "instagram"),
                      "api_version": e("INSTAGRAM_API_VERSION", "v23.0")},
    }


def ler_json(p: Path, padrao):
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else padrao


# ---------------------------------------------------------------- LinkedIn
LI_API = "https://api.linkedin.com/rest"
LI_RESERVADOS = re.compile(r"([\\|{}@\[\]()<>*_~])")


def li_commentary(texto: str) -> str:
    """Converte para o formato 'little text' da API: escapa reservados e cria hashtags."""
    partes = re.split(r"(#[\wÀ-ÿ]+)", texto)
    out = []
    for p in partes:
        if re.fullmatch(r"#[\wÀ-ÿ]+", p):
            out.append("{hashtag|\\#|" + p[1:] + "}")
        else:
            out.append(LI_RESERVADOS.sub(r"\\\1", p))
    return "".join(out)


def li_headers(cfg: dict) -> dict:
    return {
        "Authorization": f"Bearer {cfg['linkedin']['access_token']}",
        "LinkedIn-Version": cfg["linkedin"].get("api_version", "202610"),
        "X-Restli-Protocol-Version": "2.0.0",
        "Content-Type": "application/json",
    }


def li_autor(cfg: dict) -> str:
    """URN do autor. Se não foi configurado, descobre o perfil dono do token
    (precisa dos escopos openid + profile). O link /in/... do perfil NÃO serve."""
    autor = (cfg["linkedin"].get("author_urn") or "").strip()
    if autor.startswith("urn:li:"):
        return autor
    r = requests.get("https://api.linkedin.com/v2/userinfo", timeout=30,
                     headers={"Authorization": f"Bearer {cfg['linkedin']['access_token']}"})
    r.raise_for_status()
    return f"urn:li:person:{r.json()['sub']}"


def publicar_linkedin(cfg: dict, ep: dict) -> str:
    h = li_headers(cfg)
    autor = li_autor(cfg)
    r = requests.post(f"{LI_API}/documents?action=initializeUpload", headers=h,
                      json={"initializeUploadRequest": {"owner": autor}}, timeout=60)
    r.raise_for_status()
    v = r.json()["value"]
    pdf = (SAIDA / ep["linkedin_pdf"]).read_bytes()
    up = requests.put(v["uploadUrl"], data=pdf,
                      headers={"Authorization": h["Authorization"]}, timeout=300)
    up.raise_for_status()
    corpo = {
        "author": autor,
        "commentary": li_commentary(ep["linkedin_texto"]),
        "visibility": "PUBLIC",
        "distribution": {"feedDistribution": "MAIN_FEED", "targetEntities": [],
                         "thirdPartyDistributionChannels": []},
        "content": {"media": {"title": f"Kraken · Ep. {ep['episodio']} — {ep['titulo']}",
                              "id": v["document"]}},
        "lifecycleState": "PUBLISHED",
        "isReshareDisabledByAuthor": False,
    }
    r = requests.post(f"{LI_API}/posts", headers=h, json=corpo, timeout=60)
    r.raise_for_status()
    return r.headers.get("x-restli-id", "ok")


# ---------------------------------------------------------------- Instagram
def publicar_instagram(cfg: dict, post: dict) -> str:
    ig = cfg["instagram"]
    # "instagram" = API com Login do Instagram (graph.instagram.com, sem Página do Facebook)
    # "facebook"  = API com Login do Facebook (graph.facebook.com, conta ligada a uma Página)
    host = "graph.instagram.com" if ig.get("login", "instagram") == "instagram" else "graph.facebook.com"
    api = f"https://{host}/{ig.get('api_version', 'v23.0')}"
    uid, tok = ig["ig_user_id"], ig["access_token"]
    base_url = ig["public_base_url"].rstrip("/")
    filhos = []
    for arq in post["arquivos_jpg"]:
        r = requests.post(f"{api}/{uid}/media", timeout=60, data={
            "image_url": f"{base_url}/{arq}", "is_carousel_item": "true", "access_token": tok})
        r.raise_for_status()
        filhos.append(r.json()["id"])
    r = requests.post(f"{api}/{uid}/media", timeout=60, data={
        "media_type": "CAROUSEL", "children": ",".join(filhos),
        "caption": post["legenda"], "access_token": tok})
    r.raise_for_status()
    container = r.json()["id"]
    for _ in range(30):  # aguarda o processamento do contêiner
        st = requests.get(f"{api}/{container}", timeout=30,
                          params={"fields": "status_code", "access_token": tok}).json()
        if st.get("status_code") == "FINISHED":
            break
        if st.get("status_code") == "ERROR":
            raise RuntimeError(f"Instagram recusou o carrossel: {st}")
        time.sleep(5)
    r = requests.post(f"{api}/{uid}/media_publish", timeout=60,
                      data={"creation_id": container, "access_token": tok})
    r.raise_for_status()
    return r.json()["id"]


# ---------------------------------------------------------------- Agendador
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--publicar", action="store_true", help="publica de verdade (padrão: simulação)")
    ap.add_argument("--id", help="processa só este item do calendário")
    ap.add_argument("--forcar", action="store_true", help="ignora horário (use com --id)")
    a = ap.parse_args()

    conteudo = ler_json(SAIDA / "conteudo.json", None)
    if not conteudo:
        log("ERRO: saida/conteudo.json não existe. Rode build.py antes.")
        return 1
    cfg = ler_json(CONFIG, {}) or config_do_ambiente()
    estado = ler_json(ESTADO, {})
    eps = {e["episodio"]: e for e in conteudo["episodios"]}
    tolerancia = timedelta(hours=cfg.get("tolerancia_horas", 3))
    agora = datetime.now(timezone.utc)

    if a.publicar and not cfg.get("publicacao_liberada"):
        log("BLOQUEADO: config.json sem \"publicacao_liberada\": true. Nada foi publicado.")
        return 2

    falhas = 0
    for item in conteudo["calendario"]:
        if a.id and item["id"] != a.id:
            continue
        if item["id"] in estado and estado[item["id"]].get("status") == "publicado":
            continue
        quando = datetime.fromisoformat(item["quando_iso"])
        if not a.forcar:
            if quando > agora:
                continue
            if agora - quando > tolerancia:
                if estado.get(item["id"], {}).get("status") != "perdido":
                    estado[item["id"]] = {"status": "perdido", "em": agora.isoformat()}
                    log(f"PERDIDO (fora da janela de {tolerancia}): {item['id']} — publique manualmente ou com --id --forcar")
                continue
        ep = eps[item["episodio"]]
        if not a.publicar:
            log(f"SIMULAÇÃO: publicaria {item['id']} ({item['canal']}, {item['quando_iso']})")
            continue
        try:
            if item["canal"] == "linkedin":
                ref = publicar_linkedin(cfg, ep)
            else:
                post = ep["ig_manha"] if item["slot"] == "instagram_manha" else ep["ig_noite"]
                ref = publicar_instagram(cfg, post)
            estado[item["id"]] = {"status": "publicado", "em": agora.isoformat(), "ref": ref}
            log(f"PUBLICADO: {item['id']} -> {ref}")
        except Exception as e:  # registra e segue para o próximo item
            falhas += 1
            detalhe = getattr(getattr(e, "response", None), "text", "")[:500]
            estado[item["id"]] = {"status": "erro", "em": agora.isoformat(), "erro": f"{e} {detalhe}"}
            log(f"ERRO: {item['id']}: {e} {detalhe}")
        ESTADO.write_text(json.dumps(estado, ensure_ascii=False, indent=2), encoding="utf-8")
    ESTADO.write_text(json.dumps(estado, ensure_ascii=False, indent=2), encoding="utf-8")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
