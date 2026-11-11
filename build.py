"""Gera conteúdo estruturado, slides (PNG/PDF) e calendário da série Kraken.

Uso: python3 build.py [--inicio 2026-11-16]
Saídas em ./saida/: conteudo.json, calendario.csv, calendario.md, slides/...
"""
import argparse
import base64
import csv
import html
import json
import re
from datetime import date, datetime, timedelta
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright

from conteudo_extra import IG_NOITE

BASE = Path(__file__).parent
FONTE = BASE / "fonte_serie_posts.md"
SAIDA = BASE / "saida"
REPO = "github.com/sasroque-beep/ai-3d-web-builder"
HORARIOS = {"linkedin": "08:00", "instagram_manha": "12:00", "instagram_noite": "19:00"}
TZ = "-03:00"  # America/Sao_Paulo (sem horário de verão)
W, H = 1080, 1350

EMOJI = re.compile("[\U0001F000-\U0001FAFF\u2600-\u27BF\uFE0F\u2705]")


def limpar_slide(linha: str) -> tuple[str, str]:
    """'1. **Capa:** "texto"' -> ('capa', 'texto')."""
    linha = re.sub(r"^\d+\.\s*", "", linha.strip())
    tipo = "normal"
    m = re.match(r"\*\*(Capa|CTA|Fechamento):\*\*\s*", linha)
    if m:
        tipo = {"Capa": "capa", "CTA": "cta", "Fechamento": "fecho"}[m.group(1)]
        linha = linha[m.end():]
    linha = linha.strip().strip('"').strip("“”")
    linha = EMOJI.sub("", linha).replace("  ", " ").strip()
    return tipo, linha


def parse_serie() -> list[dict]:
    texto = FONTE.read_text(encoding="utf-8")
    partes = re.split(r"^### Episódio (\d+) — (.+)$", texto, flags=re.M)
    eps = []
    for i in range(1, len(partes), 3):
        num, titulo, corpo = int(partes[i]), partes[i + 1].strip(), partes[i + 2]
        corpo = corpo.split("\n## Checklist")[0]
        li_bloco = corpo.split("#### LinkedIn")[1].split("**Referências:**")[0]
        linkedin = "\n".join(
            l[2:] if l.startswith("> ") else ("" if l.strip() == ">" else l)
            for l in li_bloco.strip().splitlines()
            if l.startswith(">")
        ).strip()
        linkedin = re.sub(r"\*\*(.+?)\*\*", r"\1", linkedin)  # LinkedIn não renderiza markdown
        linkedin = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"\1", linkedin)
        linkedin = linkedin.replace("`", "")
        refs = corpo.split("**Referências:**")[1].split("####")[0].strip()
        ig_bloco = corpo.split("#### Instagram")[1]
        slides_txt, legenda_txt = ig_bloco.split("**Legenda:**")
        slides = [limpar_slide(l) for l in slides_txt.splitlines() if re.match(r"^\d+\.", l.strip())]
        legenda = legenda_txt.split("\n---")[0].strip()
        eps.append({
            "episodio": num,
            "titulo": titulo,
            "linkedin_texto": linkedin,
            "referencias_md": refs,
            "ig_manha": {"slides": [{"tipo": t, "texto": s} for t, s in slides], "legenda": legenda},
            "ig_noite": IG_NOITE[num],
        })
    assert len(eps) == 9, f"esperava 9 episódios, achei {len(eps)}"
    return eps


def resumo_refs(refs_md: str) -> list[str]:
    prs = sorted({int(n) for n in re.findall(r"PR \[#(\d+)\]", refs_md)})
    issues = sorted({int(n) for n in re.findall(r"Issue \[#(\d+)\]", refs_md)})
    commits = list(dict.fromkeys(re.findall(r"commit/([0-9a-f]{7})", refs_md)))
    linhas = []
    if prs:
        linhas.append("Pull requests: " + ", ".join(f"#{n}" for n in prs))
    if issues:
        linhas.append("Issues: " + ", ".join(f"#{n}" for n in issues))
    if commits and len(linhas) < 2:
        linhas.append("Commits: " + ", ".join(commits[:6]))
    return linhas


CSS = """
@font-face { font-family: 'KInter'; src: url(data:font/ttf;base64,%(inter)s) format('truetype'); font-weight: 100 900; }
@font-face { font-family: 'KGrotesk'; src: url(data:font/ttf;base64,%(grotesk)s) format('truetype'); font-weight: 300 700; }
* { margin:0; padding:0; box-sizing:border-box; }
body { width:%(w)dpx; height:%(h)dpx; overflow:hidden; font-family:KInter, sans-serif; }
.s { position:relative; width:100%%; height:100%%; padding:96px 88px; display:flex; flex-direction:column; }
.top { display:flex; justify-content:space-between; align-items:center; font-family:KGrotesk; letter-spacing:.18em; font-size:26px; font-weight:700; }
.top small { font-family:KInter; letter-spacing:.04em; font-weight:500; font-size:24px; opacity:.7; }
.mid { flex:1; display:flex; flex-direction:column; justify-content:center; }
.kicker { font-family:KGrotesk; font-size:28px; font-weight:600; letter-spacing:.08em; text-transform:uppercase; margin-bottom:36px; }
.txt { font-weight:600; line-height:1.22; letter-spacing:-.01em; }
.capa .txt { font-family:KGrotesk; font-weight:700; line-height:1.08; letter-spacing:-.02em; }
.bar { width:120px; height:10px; border-radius:6px; margin-bottom:44px; }
.refs { list-style:none; font-size:40px; line-height:1.5; font-weight:500; }
.refs li { margin-bottom:18px; }
.foot { display:flex; justify-content:space-between; align-items:flex-end; font-size:24px; font-weight:500; opacity:.75; }
.dots { display:flex; gap:10px; }
.dots i { width:14px; height:14px; border-radius:50%%; display:block; opacity:.3; }
.dots i.on { opacity:1; }
.ring { position:absolute; border-radius:50%%; pointer-events:none; }
/* Instagram: escuro */
.ig { background: radial-gradient(1200px 900px at 85%% 0%%, #12384a 0%%, #0a1626 55%%, #070e1a 100%%); color:#eef6fb; }
.ig .kicker, .ig .top span { color:#2fe0c6; }
.ig .bar, .ig .dots i { background:#2fe0c6; }
.ig .ring { border:2px solid rgba(47,224,198,.18); }
.ig.fecho, .ig.cta { background: linear-gradient(160deg, #0f5e63 0%%, #0a2a3a 60%%, #070e1a 100%%); }
/* LinkedIn: claro */
.li { background:#f6f8fb; color:#0b1b2e; }
.li .kicker, .li .top span { color:#0a66c2; }
.li .bar, .li .dots i { background:#0a66c2; }
.li .ring { border:2px solid rgba(10,102,194,.12); }
.li.capa { background: linear-gradient(165deg, #ffffff 0%%, #e7f0fb 100%%); }
.li.fecho, .li.cta { background:#0b1b2e; color:#f6f8fb; }
.li.fecho .kicker, .li.fecho .top span, .li.cta .kicker, .li.cta .top span { color:#5fb0ff; }
.li.fecho .bar, .li.fecho .dots i, .li.cta .bar, .li.cta .dots i { background:#5fb0ff; }
"""


FONTS_B64 = {k: base64.b64encode((BASE / "fonts" / f).read_bytes()).decode()
             for k, f in (("inter", "Inter.ttf"), ("grotesk", "SpaceGrotesk.ttf"))}
CSS_FINAL = CSS % {**FONTS_B64, "w": W, "h": H}


def tamanho_fonte(texto: str, tipo: str) -> int:
    n = len(texto)
    if tipo == "capa":
        return 112 if n < 40 else 100 if n < 60 else 88 if n < 85 else 74
    return 80 if n < 50 else 70 if n < 80 else 62 if n < 120 else 54


def slide_html(plataforma: str, ep: int, titulo: str, idx: int, total: int,
               slide: dict, serie: str, refs: list[str] | None = None) -> str:
    tipo = slide.get("tipo", "normal")
    texto = html.escape(slide["texto"])
    if refs is not None:
        kicker, miolo = "Fontes no GitHub", "<ul class='refs'>" + "".join(
            f"<li>{html.escape(r)}</li>" for r in refs + [REPO]) + "</ul>"
    else:
        kicker = {"capa": f"Episódio {ep} · {html.escape(titulo)}", "fecho": "Para levar", "cta": "Acompanhe"}.get(tipo, f"{idx}/{total}")
        miolo = f"<div class='txt' style='font-size:{tamanho_fonte(slide['texto'], tipo)}px'>{texto}</div>"
    dots = "".join(f"<i class='{'on' if i == idx else ''}'></i>" for i in range(1, total + 1))
    return f"""<!doctype html><html><head><meta charset='utf-8'><style>{CSS_FINAL}</style></head>
<body><div class='s {plataforma} {tipo}'>
<div class='ring' style='width:900px;height:900px;right:-420px;top:-380px'></div>
<div class='ring' style='width:600px;height:600px;right:-270px;top:-230px'></div>
<div class='top'><span>KRAKEN</span><small>{html.escape(serie)}</small></div>
<div class='mid'><div class='kicker'>{kicker}</div><div class='bar'></div>{miolo}</div>
<div class='foot'><span>Ep. {ep}/9 · AI 3D Web Builder</span><span class='dots'>{dots}</span></div>
</div></body></html>"""


def render(eps: list[dict]) -> None:
    with sync_playwright() as p:
        nav = p.chromium.launch()
        pg = nav.new_page(viewport={"width": W, "height": H})

        def foto(doc: str, destino: Path) -> None:
            destino.parent.mkdir(parents=True, exist_ok=True)
            pg.set_content(doc, wait_until="load")
            pg.evaluate("document.fonts.ready")
            pg.screenshot(path=str(destino))

        for e in eps:
            n, pasta = e["episodio"], SAIDA / "slides" / f"ep{e['episodio']:02d}"
            for chave, serie in (("ig_manha", "A jornada no GitHub"), ("ig_noite", "Bastidores")):
                slides = e[chave]["slides"]
                arquivos = []
                for i, s in enumerate(slides, 1):
                    f = pasta / chave / f"slide_{i:02d}.png"
                    foto(slide_html("ig", n, e["titulo"] if chave == "ig_manha" else e["ig_noite"]["titulo"],
                                    i, len(slides), s, serie), f)
                    arquivos.append(str(f.relative_to(SAIDA)))
                e[chave]["arquivos"] = arquivos
                # A API do Instagram só aceita JPEG
                jpgs = []
                for a in arquivos:
                    j = (SAIDA / a).with_suffix(".jpg")
                    Image.open(SAIDA / a).convert("RGB").save(j, quality=92)
                    jpgs.append(str(j.relative_to(SAIDA)))
                e[chave]["arquivos_jpg"] = jpgs
            # LinkedIn: slides do episódio em versão clara + slide de fontes -> PDF (post de documento)
            li_slides = e["ig_manha"]["slides"] + [{"tipo": "normal", "texto": ""}]
            total = len(li_slides)
            pngs = []
            for i, s in enumerate(li_slides, 1):
                f = pasta / "linkedin" / f"slide_{i:02d}.png"
                refs = resumo_refs(e["referencias_md"]) if i == total else None
                foto(slide_html("li", n, e["titulo"], i, total, s, "Build in public", refs), f)
                pngs.append(f)
            pdf = pasta / "linkedin" / f"kraken_ep{n:02d}_linkedin.pdf"
            imgs = [Image.open(x).convert("RGB") for x in pngs]
            imgs[0].save(pdf, save_all=True, append_images=imgs[1:], resolution=144)
            e["linkedin_slides"] = [str(x.relative_to(SAIDA)) for x in pngs]
            e["linkedin_pdf"] = str(pdf.relative_to(SAIDA))
        nav.close()


def calendario(eps: list[dict], inicio: date) -> list[dict]:
    linhas = []
    for e in eps:
        dia = inicio + timedelta(days=e["episodio"] - 1)
        for canal, chave, formato in (
            ("linkedin", "linkedin", "Documento/carrossel PDF + texto"),
            ("instagram", "instagram_manha", "Carrossel principal"),
            ("instagram", "instagram_noite", "Carrossel de bastidores"),
        ):
            linhas.append({
                "id": f"ep{e['episodio']:02d}-{chave}",
                "data": dia.isoformat(),
                "horario": HORARIOS[chave],
                "quando_iso": f"{dia.isoformat()}T{HORARIOS[chave]}:00{TZ}",
                "canal": canal,
                "slot": chave,
                "episodio": e["episodio"],
                "tema": e["titulo"] if chave != "instagram_noite" else e["ig_noite"]["titulo"],
                "formato": formato,
            })
    return linhas


NOME_CANAL = {"linkedin": "LinkedIn", "instagram": "Instagram"}
DIAS = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]


def escrever_calendario(cal: list[dict]) -> None:
    with open(SAIDA / "calendario.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(cal[0].keys()))
        w.writeheader()
        w.writerows(cal)
    md = ["# Calendário de publicação — Série Kraken \"A jornada no GitHub\"", "",
          "Horários de Brasília. LinkedIn: 1 post por dia · Instagram: 2 posts por dia.", "",
          "| Data | Horário | Canal | Ep. | Tema | Formato |", "| --- | --- | --- | --- | --- | --- |"]
    for c in cal:
        d = date.fromisoformat(c["data"])
        md.append(f"| {DIAS[d.weekday()]} {d:%d/%m} | {c['horario']} | {NOME_CANAL[c['canal']]} | {c['episodio']} | {c['tema']} | {c['formato']} |")
    (SAIDA / "calendario.md").write_text("\n".join(md) + "\n", encoding="utf-8")


def escrever_posts_por_dia(eps: list[dict], cal: list[dict]) -> None:
    md = ["# Posts prontos, dia a dia — Série Kraken", "",
          "Textos finais exatamente como serão enviados pela automação. Revise antes de liberar.", ""]
    por_ep = {e["episodio"]: e for e in eps}
    for c in cal:
        e = por_ep[c["episodio"]]
        d = date.fromisoformat(c["data"])
        if c["slot"] == "linkedin":
            md += [f"## {DIAS[d.weekday()]} {d:%d/%m} — Episódio {e['episodio']}: {e['titulo']}", ""]
        md += [f"### {c['horario']} · {NOME_CANAL[c['canal']]} · {c['formato']}", ""]
        if c["slot"] == "linkedin":
            md += [f"Slides: `{e['linkedin_pdf']}` ({len(e['linkedin_slides'])} páginas)", "", "```text",
                   e["linkedin_texto"], "```", "", f"Referências: {e['referencias_md']}", ""]
        else:
            post = e["ig_manha"] if c["slot"] == "instagram_manha" else e["ig_noite"]
            md += [f"Slides ({len(post['arquivos_jpg'])}): `{Path(post['arquivos_jpg'][0]).parent}/`", ""]
            md += [f"{i}. {s['texto']}" for i, s in enumerate(post["slides"], 1)]
            md += ["", "Legenda:", "", "```text", post["legenda"], "```", ""]
    (SAIDA / "posts_por_dia.md").write_text("\n".join(md) + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--inicio", default="2026-11-16")
    a = ap.parse_args()
    SAIDA.mkdir(exist_ok=True)
    eps = parse_serie()
    render(eps)
    cal = calendario(eps, date.fromisoformat(a.inicio))
    escrever_calendario(cal)
    escrever_posts_por_dia(eps, cal)
    (SAIDA / "conteudo.json").write_text(json.dumps(
        {"gerado_em": datetime.now().isoformat(timespec="seconds"), "episodios": eps, "calendario": cal},
        ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"OK: {len(eps)} episódios, {len(cal)} publicações no calendário")


if __name__ == "__main__":
    main()
