"""Confere os acessos sem publicar nada. Uso: python3 verificar_acessos.py"""
import requests
from publicar import CONFIG, config_do_ambiente, ler_json

cfg = ler_json(CONFIG, {}) or config_do_ambiente()
li, ig = cfg.get("linkedin", {}), cfg.get("instagram", {})

if li.get("access_token"):
    r = requests.get("https://api.linkedin.com/v2/userinfo", timeout=30,
                     headers={"Authorization": f"Bearer {li['access_token']}"})
    if r.ok:
        print(f"LinkedIn OK: {r.json().get('name')} -> author_urn para perfil: urn:li:person:{r.json()['sub']}")
    else:
        print(f"LinkedIn: token não leu o perfil ({r.status_code}). Precisa dos escopos openid e profile.")
else:
    print("LinkedIn: sem token.")

if ig.get("access_token"):
    host = "graph.instagram.com" if ig.get("login", "instagram") == "instagram" else "graph.facebook.com"
    alvo = "me" if host == "graph.instagram.com" else ig.get("ig_user_id", "me")
    r = requests.get(f"https://{host}/v23.0/{alvo}", timeout=30,
                     params={"fields": "user_id,username,account_type" if alvo == "me" else "username",
                             "access_token": ig["access_token"]})
    print(f"Instagram {'OK' if r.ok else 'ERRO'}: {r.json()}")
else:
    print("Instagram: sem token.")

if ig.get("public_base_url"):
    url = ig["public_base_url"].rstrip("/") + "/slides/ep01/ig_manha/slide_01.jpg"
    r = requests.head(url, timeout=30, allow_redirects=True)
    print(f"Imagens públicas: {r.status_code} {r.headers.get('content-type')} em {url}")
