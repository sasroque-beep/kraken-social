# Guia: como liberar a publicação automática da série Kraken

Tempo estimado: de 40 a 60 minutos. Faça até **sex 13/11** para dar tempo de testar antes da 1ª publicação, em **seg 16/11 às 08h**.

> Recomendo rodar a automação no **GitHub Actions**. Ele fica ligado mesmo quando esta máquina de trabalho desliga, e o GitHub Pages hospeda os slides de graça, com o link público que o Instagram exige.

---

## Etapa 1: repositório da automação no GitHub (10 min)

1. Em https://github.com/new, crie o repositório **`kraken-social`** na conta `sasroque-beep`.
   - Ele precisa ser **público** para o GitHub Pages gratuito funcionar. Assim, os slides ficam acessíveis por link antes da data de cada post.
   - Não marque "Add README".
2. ✅ Feito: o acesso do app da Abacus.AI foi liberado, e os arquivos já foram enviados.
3. **Ative o agendador.** O GitHub não deixa apps externos criarem arquivos de automação, então este passo é manual:
   - no repositório, clique em **Add file → Create new file**;
   - no nome do arquivo, digite exatamente `.github/workflows/publicar.yml`;
   - cole o conteúdo do arquivo `automacao/publicar.yml`, que já está no repositório (abra-o e use o botão de copiar);
   - clique em **Commit changes** e depois em **Commit changes** de novo.
4. Depois do envio, abra **Settings → Pages**. Em *Source*, escolha **Deploy from a branch**, depois **main** e **/(root)**, e salve.
   - Os slides ficam em `https://sasroque-beep.github.io/kraken-social/saida/`.

## Etapa 2: LinkedIn (15 min)

**Decisão: perfil pessoal ou Página da Kraken?**

| Destino | Permissão | Dificuldade |
| --- | --- | --- |
| Seu perfil pessoal | `w_member_social` (produto "Share on LinkedIn") | Liberação automática |
| Página da Kraken | `w_organization_social` (Community Management API) | Exige aprovação do LinkedIn, que pode levar dias |

Para cumprir a data de 16/11, o caminho seguro é o **perfil pessoal**.

1. Em https://www.linkedin.com/developers/apps, clique em **Create app**.
   - Nome: "Kraken Social".
   - LinkedIn Page: a Página da Kraken, que é obrigatória para criar o app, mesmo para posts no perfil.
   - Faça upload do logo.
2. Na aba **Products**, adicione:
   - **Share on LinkedIn**;
   - **Sign In with LinkedIn using OpenID Connect**.
3. Na aba **Auth**, abra **OAuth 2.0 tools → Create token**.
   - Marque os escopos `openid`, `profile` e `w_member_social`.
   - Autorize com sua conta.
4. Copie o **Access token**. Ele vale **60 dias**, o que cobre a série inteira.
5. O `author_urn` (`urn:li:person:...`) aparece quando você roda `verificar_acessos.py` (etapa 5).

## Etapa 3: Instagram (15 min)

**Pré-requisito:** a conta da Kraken precisa ser **Profissional (Empresa ou Criador)**. No app, o caminho é Configurações → Tipo de conta e ferramentas. Para usar a API com Login do Instagram, não é preciso ter Página do Facebook.

1. Em https://developers.facebook.com/apps, clique em **Criar app** e escolha o caso de uso **Gerenciar mensagens e conteúdo no Instagram**.
2. Em **API com Login do Instagram**, abra **Gerar tokens de acesso** e adicione a conta da Kraken.
   - A conta precisa estar cadastrada como *testador do Instagram* no app e aceitar o convite em Configurações → Apps e sites.
3. Gere o token com as permissões `instagram_business_basic` e `instagram_business_content_publish`.
   - Esse é o token de longa duração, válido por **60 dias**.
4. Anote o **ID da conta do Instagram**, que aparece ao lado do nome da conta nessa mesma tela.

> Com o app em modo de desenvolvimento, você publica na **sua própria conta** (cadastrada como testadora). Isso basta para a série, sem precisar da revisão do app pela Meta.

## Etapa 4: cadastrar os acessos no GitHub (5 min)

No repositório `kraken-social`, abra **Settings → Secrets and variables → Actions**.

**Secrets** (ficam criptografados; ninguém os vê depois de salvos):

| Nome | Valor |
| --- | --- |
| `LINKEDIN_ACCESS_TOKEN` | Token da etapa 2 |
| `LINKEDIN_AUTHOR_URN` | `urn:li:person:...` (etapa 5) |
| `INSTAGRAM_ACCESS_TOKEN` | Token da etapa 3 |
| `INSTAGRAM_USER_ID` | ID da conta da etapa 3 |

**Variables:**

| Nome | Valor |
| --- | --- |
| `PUBLIC_BASE_URL` | `https://sasroque-beep.github.io/kraken-social/saida` |
| `INSTAGRAM_LOGIN` | `instagram` |
| `PUBLICACAO_LIBERADA` | `false` (mude para `true` só depois da revisão) |

> **Nunca envie tokens pelo chat nem os coloque em arquivos do repositório.** Cadastre-os apenas em *Secrets*.

## Etapa 5: testar sem publicar (5 min)

1. No repositório, abra **Actions → Publicar série Kraken → Run workflow**.
2. Com `PUBLICACAO_LIBERADA=false`, o log mostra **BLOQUEADO**, e nada é publicado.
3. Para conferir os tokens e descobrir o `author_urn`, rode este comando no seu computador, com os tokens em variáveis de ambiente:

   ```bash
   LINKEDIN_ACCESS_TOKEN=... INSTAGRAM_ACCESS_TOKEN=... python3 verificar_acessos.py
   ```

   O script só lê dados: ele mostra o nome do perfil, o `urn:li:person:...`, o `@` do Instagram e se as imagens públicas abrem.

## Etapa 6: liberar

1. Revise `saida/posts_por_dia.md` e os slides.
2. Mude a variável `PUBLICACAO_LIBERADA` para `true`.

A partir daí, o GitHub roda o publicador **a cada hora**, e cada post sai no 1º ciclo depois do seu horário. Por isso, o horário real fica entre **HH:05 e HH:20**, porque o GitHub pode atrasar execuções agendadas.

---

## Calendário (horário de Brasília)

| Horário | Canal | Conteúdo |
| --- | --- | --- |
| 08h | LinkedIn | Episódio (texto + PDF) |
| 12h | Instagram | Carrossel principal |
| 19h | Instagram | Carrossel de bastidores |

A série vai de 16/11 a 24/11, com 27 publicações.

## Proteções embutidas

- **Nada sai sem liberação:** é preciso `PUBLICACAO_LIBERADA=true`.
- **Sem posts duplicados:** o `estado.json` é salvo no repositório depois de cada execução.
- **Atraso controlado:** um post com mais de 3 horas de atraso **não** sai sozinho e fica marcado como "perdido" no log. Para publicá-lo, rode manualmente com `--id <item> --forcar`.
- **Pausa imediata:** volte `PUBLICACAO_LIBERADA` para `false`.

## Se algo der errado

| Sintoma no log | Causa provável |
| --- | --- |
| `401` / `403` no LinkedIn | Token vencido ou sem `w_member_social` |
| `ERRO ... media` no Instagram | Imagem não acessível pelo link público (confira o GitHub Pages) ou token sem `instagram_business_content_publish` |
| Nada acontece | Variável `PUBLICACAO_LIBERADA` diferente de `true`, ou workflow desativado na aba Actions |

## Alternativa sem API

Use os arquivos prontos para agendar manualmente:

- **Instagram:** no Meta Business Suite (Planejador → Criar post → Carrossel), com os JPGs de `saida/slides/epXX/ig_manha` e `ig_noite`.
- **LinkedIn:** no próprio LinkedIn (Começar publicação → ícone de relógio → Agendar), anexando o PDF como documento.
