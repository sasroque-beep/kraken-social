# Kraken: série "A jornada no GitHub" (LinkedIn + Instagram)

O projeto gera os slides, o calendário e os textos da série. Ele também traz o publicador agendado.

## Cadência (16/11 a 24/11/2026, horário de Brasília)

| Horário | Canal | Conteúdo |
| --- | --- | --- |
| 08:00 | LinkedIn | Texto do episódio mais um carrossel em PDF (post de documento) |
| 12:00 | Instagram | Carrossel principal do episódio |
| 19:00 | Instagram | Carrossel "Bastidores", que aprofunda um fato do episódio |

São 9 dias e 27 publicações. A tabela completa está em `saida/calendario.md`.

## Estrutura

- `fonte_serie_posts.md`: textos aprovados da série, com as referências do GitHub.
- `conteudo_extra.py`: o 2º post diário do Instagram (Bastidores).
- `build.py`: gera `saida/` com os slides PNG/JPG, os PDFs do LinkedIn, `calendario.csv`/`.md`, `posts_por_dia.md` e `conteudo.json`.
- `publicar.py`: publica o que já venceu no calendário. Por padrão, só simula.
- `config.example.json`: modelo de credenciais. Copie para `config.json`, que não vai para o git.

## Uso

```bash
python3 build.py                 # regenera tudo; use --inicio AAAA-MM-DD para mudar a data
python3 publicar.py              # simulação
python3 publicar.py --publicar   # publica de verdade (rodar de hora em hora)
```

## Requisitos para a publicação automática

O passo a passo completo está em **`GUIA_ACESSOS.md`**. A automação roda no GitHub Actions (`.github/workflows/publicar.yml`, criado a partir de `automacao/publicar.yml`; veja o guia), e `verificar_acessos.py` testa os tokens sem publicar nada.


- **LinkedIn:** token OAuth com escopo `w_member_social` (perfil) ou `w_organization_social` (página), além do URN do autor.
- **Instagram:** conta profissional ligada a uma Página do Facebook e token com `instagram_business_content_publish` (API com Login do Instagram, sem precisar de Página do Facebook). Também é preciso o `ig_user_id` e uma URL pública onde os JPGs de `saida/` estejam hospedados, porque a API só aceita imagens por URL.
- **Liberação:** `"publicacao_liberada": true` no `config.json`, depois da revisão.

## Proteções

- Um item nunca é publicado duas vezes, porque o controle fica em `estado.json`.
- Itens atrasados mais que `tolerancia_horas` não saem sozinhos.
- Tudo fica registrado em `publicacoes.log`.
