# Kraken — Série de postagens "A jornada no GitHub"

> Material de apoio para LinkedIn e Instagram. **Nada foi publicado.** Todo o conteúdo se baseia exclusivamente no repositório analisado e cada post traz as referências do GitHub que o sustentam.
> Data da análise: 11/11/2026.

---

## ⚠️ Premissas e cuidados (leia antes de publicar)

1. **Ligação com a "Kraken":** a palavra "Kraken" **não aparece** em nenhum arquivo do repositório (README, docs, código, issues ou PRs). A ligação entre o repositório `ai-3d-web-builder` e a Kraken parte da **confirmação do usuário** de que os projetos da Kraken ficam na conta `sasroque-beep`. Os posts tratam o AI 3D Web Builder como "o produto que a Kraken está construindo". Se o nome público do produto for outro, ajuste antes de publicar.
2. **IA ainda não está implementada no produto.** O nome é "AI 3D Web Builder", mas a pasta `src/ai/` (orquestrador e agentes) está marcada como *planned — no implementation yet* e o banco só reserva o campo `generated_by: "manual" | "ai"` para o futuro. **Hoje, diagnóstico, estratégia, planejamento, copy e tema são preenchidos manualmente pelo operador** em fluxos estruturados. Os posts deixam isso claro; não afirme que "a IA gera o site" sem atualizar esta análise.
3. **Sem clientes, métricas de negócio ou resultados comerciais.** O repositório não contém nenhum dado de cliente, conversão, receita ou lead real. Os únicos números citados são **métricas técnicas registradas nos próprios PRs** (tamanho de bundle, quantidade de testes, execuções de CI).
4. **Caso-piloto:** a issue #31 cita nominalmente uma empresa para um caso-piloto de demonstração. **Os posts não citam esse nome** (é um terceiro e a issue segue aberta/planejada). Só mencione com autorização expressa.
5. **Segurança:** nenhum segredo, variável de ambiente, dado pessoal ou detalhe sensível de segurança foi copiado. O arquivo `.env.example` não foi reproduzido. Os posts falam de segurança apenas em termos gerais.
6. **Opiniões e frases em primeira pessoa** nos posts são sugestões de redação para o Sérgio validar; elas não afirmam fatos além do que está no GitHub.
7. **Desenvolvimento apoiado por agentes de IA:** o repositório contém `AGENTS.md` e `CLAUDE.md` (instruções para agentes de IA que apoiam o desenvolvimento). Isso é diferente da IA *dentro* do produto (item 2).

---

## 1. Repositórios analisados

| Repositório | Visibilidade | Linguagem | Criado | Último push | Branch padrão |
| --- | --- | --- | --- | --- | --- |
| [sasroque-beep/ai-3d-web-builder](https://github.com/sasroque-beep/ai-3d-web-builder) | Público | TypeScript | 26/08/2026 | 26/09/2026 | `main` |

Único repositório da conta `sasroque-beep`. Descrição oficial: *"Plataforma de IA para criação de sites 3D de alta conversão, integrados à jornada de compra, geração de leads, marketing, dados e otimização."*

**Fontes analisadas**

- **Commits:** histórico completo (o clone já trouxe tudo) — **44 commits** na `main`, de 25/08/2026 a 26/09/2026, todos do autor `sasroque-beep`.
- **Branches remotas:** `main` e `feature/48-editar-experiencia-3d-no-preview` (aberta).
- **Pull requests:** 23 PRs — **22 mergeados** e **1 aberto** (#49).
- **Issues:** 26 issues — **23 fechadas** e **3 abertas** (#31, #47, #48).
- **Releases/tags:** **nenhuma** (o produto ainda não teve release publicada).
- **Documentação:** `README.md`, `AGENTS.md`, `CONTRIBUTING.md` e `docs/` (`PRODUCT_REQUIREMENTS`, `SYSTEM_ARCHITECTURE`, `TECH_STACK`, `DATABASE`, `AI_AGENTS`, `DESIGN_SYSTEM`, `QUALITY_ASSURANCE`, `SECURITY`, `DEPLOYMENT`, `DEVELOPMENT_WORKFLOW`), além dos READMEs de cada módulo em `src/`.

**Stack registrada no README:** Next.js 15 (App Router) · React 19 · TypeScript strict · Tailwind CSS v4 · Biome · Vitest · Playwright · Lefthook + commitlint · pnpm · GitHub Actions · SQLite (libSQL) + Drizzle ORM · Three.js + React Three Fiber + Drei.

---

## 2. Linha do tempo

Legenda: ✅ **Implementado** (código/documento na `main`, PR mergeado) · 🔄 **Em desenvolvimento** (branch/PR aberto, issue em andamento) · 🗺️ **Planejado** (apenas em roadmap, docs ou issue sem código)

### Fase 1 — Visão e documentação primeiro (25/08 a 04/09/2026)

| Data | Status | Marco | Referência |
| --- | --- | --- | --- |
| 25/08 | ✅ | Repositório criado e visão do produto definida no README | [717ceb8](https://github.com/sasroque-beep/ai-3d-web-builder/commit/717ceb8), [3a5a43a](https://github.com/sasroque-beep/ai-3d-web-builder/commit/3a5a43a) |
| 27/08 | ✅ | Instruções para agentes de IA (`AGENTS.md`) | [47a7c67](https://github.com/sasroque-beep/ai-3d-web-builder/commit/47a7c67) |
| 27/08 | ✅ | Templates de issue (bug, feature, melhoria, tarefa técnica) e de PR | [f9726a9](https://github.com/sasroque-beep/ai-3d-web-builder/commit/f9726a9), [78e8956](https://github.com/sasroque-beep/ai-3d-web-builder/commit/78e8956), [ea1ee44](https://github.com/sasroque-beep/ai-3d-web-builder/commit/ea1ee44), [551c0b9](https://github.com/sasroque-beep/ai-3d-web-builder/commit/551c0b9) |
| 27/08–01/09 | ✅ | Fluxo de desenvolvimento (Issue → Branch → Testes → PR → Review → Merge) | [e9b32f3](https://github.com/sasroque-beep/ai-3d-web-builder/commit/e9b32f3), [99dd0db](https://github.com/sasroque-beep/ai-3d-web-builder/commit/99dd0db) |
| 01/09 | ✅ | Arquitetura de sistema, requisitos de produto, stack e banco de dados | [6be29ab](https://github.com/sasroque-beep/ai-3d-web-builder/commit/6be29ab), [4d37ed4](https://github.com/sasroque-beep/ai-3d-web-builder/commit/4d37ed4), [08cdafa](https://github.com/sasroque-beep/ai-3d-web-builder/commit/08cdafa), [822d4c4](https://github.com/sasroque-beep/ai-3d-web-builder/commit/822d4c4) |
| 02–03/09 | ✅ (doc) | Arquitetura de agentes de IA, design system, QA, segurança e deploy | [07c62a0](https://github.com/sasroque-beep/ai-3d-web-builder/commit/07c62a0), [eb822bb](https://github.com/sasroque-beep/ai-3d-web-builder/commit/eb822bb), [ba4dfec](https://github.com/sasroque-beep/ai-3d-web-builder/commit/ba4dfec), [f98b6f8](https://github.com/sasroque-beep/ai-3d-web-builder/commit/f98b6f8), [41c9726](https://github.com/sasroque-beep/ai-3d-web-builder/commit/41c9726) |

> Observação: `docs/PRODUCT_REQUIREMENTS.md` está marcado como *"Seção truncada no commit original. O conteúdo será finalizado em issue dedicada."*

### Fase 2 — Fundação técnica e entrada de dados (10 a 11/09/2026)

| Data | Status | Marco | Referência |
| --- | --- | --- | --- |
| 10/09 | ✅ | Estrutura inicial: Next.js 15, TypeScript strict, Biome, Vitest, Lefthook + commitlint, CI no GitHub Actions | Issue [#2](https://github.com/sasroque-beep/ai-3d-web-builder/issues/2) · PR [#3](https://github.com/sasroque-beep/ai-3d-web-builder/pull/3) · [8f18dcc](https://github.com/sasroque-beep/ai-3d-web-builder/commit/8f18dcc) |
| 11/09 | ✅ | Cadastro de empresas e leads (CRM): banco SQLite + Drizzle com migrations, telas `/leads`, `/leads/new`, `/leads/[id]`, estados de interface acessíveis | Issue [#4](https://github.com/sasroque-beep/ai-3d-web-builder/issues/4) · PR [#5](https://github.com/sasroque-beep/ai-3d-web-builder/pull/5) · [071caf7](https://github.com/sasroque-beep/ai-3d-web-builder/commit/071caf7) |

### Fase 3 — Inteligência de negócio antes do site (12/09/2026)

| Data | Status | Marco | Referência |
| --- | --- | --- | --- |
| 12/09 | ✅ | Enriquecimento manual de dados (status confirmado / não verificado / ausente) | Issue [#6](https://github.com/sasroque-beep/ai-3d-web-builder/issues/6) · PR [#7](https://github.com/sasroque-beep/ai-3d-web-builder/pull/7) |
| 12/09 | ✅ | Diagnóstico estratégico do negócio — só pode ser criado se houver ao menos um dado **confirmado** | Issue [#8](https://github.com/sasroque-beep/ai-3d-web-builder/issues/8) · PR [#9](https://github.com/sasroque-beep/ai-3d-web-builder/pull/9) |
| 12/09 | ✅ | Estratégia de marketing e conversão | Issue [#10](https://github.com/sasroque-beep/ai-3d-web-builder/issues/10) · PR [#11](https://github.com/sasroque-beep/ai-3d-web-builder/pull/11) |
| 12/09 | ✅ | Planejamento estratégico do site — exige estratégia vigente | Issue [#12](https://github.com/sasroque-beep/ai-3d-web-builder/issues/12) · PR [#13](https://github.com/sasroque-beep/ai-3d-web-builder/pull/13) |

### Fase 4 — Do planejamento ao preview do site (15 a 16/09/2026)

| Data | Status | Marco | Referência |
| --- | --- | --- | --- |
| 15/09 | ✅ | Arquitetura de páginas a partir do planejamento | Issue [#14](https://github.com/sasroque-beep/ai-3d-web-builder/issues/14) · PR [#15](https://github.com/sasroque-beep/ai-3d-web-builder/pull/15) |
| 15/09 | ✅ | Conteúdo/copy das seções | Issue [#16](https://github.com/sasroque-beep/ai-3d-web-builder/issues/16) · PR [#17](https://github.com/sasroque-beep/ai-3d-web-builder/pull/17) |
| 15/09 | ✅ | Tema visual e diretrizes de design | Issue [#18](https://github.com/sasroque-beep/ai-3d-web-builder/issues/18) · PR [#19](https://github.com/sasroque-beep/ai-3d-web-builder/pull/19) |
| 15/09 | ✅ | Preview do site (somente leitura) a partir de páginas, conteúdo e tema | Issue [#20](https://github.com/sasroque-beep/ai-3d-web-builder/issues/20) · PR [#21](https://github.com/sasroque-beep/ai-3d-web-builder/pull/21) |
| 16/09 | ✅ | Edição do conteúdo das seções direto no preview | Issue [#22](https://github.com/sasroque-beep/ai-3d-web-builder/issues/22) · PR [#23](https://github.com/sasroque-beep/ai-3d-web-builder/pull/23) |

### Fase 5 — A camada 3D, com responsabilidade (17 a 26/09/2026)

| Data | Status | Marco | Referência |
| --- | --- | --- | --- |
| 17/09 | ✅ | Fundação 3D: Three.js + React Three Fiber + Drei validados com cena de teste | Issue [#24](https://github.com/sasroque-beep/ai-3d-web-builder/issues/24) · PR [#25](https://github.com/sasroque-beep/ai-3d-web-builder/pull/25) |
| 17/09 | ✅ | Decisões arquiteturais registradas (isolamento, progressive enhancement, modos de runtime) | Issue [#26](https://github.com/sasroque-beep/ai-3d-web-builder/issues/26) · PR [#27](https://github.com/sasroque-beep/ai-3d-web-builder/pull/27) |
| 17/09 | ✅ | Detecção de capacidade do dispositivo: WebGL, `prefers-reduced-motion`, modos `FULL_3D` / `REDUCED_3D` / `FALLBACK_2D` | Issue [#28](https://github.com/sasroque-beep/ai-3d-web-builder/issues/28) · PR [#29](https://github.com/sasroque-beep/ai-3d-web-builder/pull/29) |
| 17/09 | ✅ | Contrato de dados da experiência 3D, com fallback 2D obrigatório | Issue [#30](https://github.com/sasroque-beep/ai-3d-web-builder/issues/30) · PR [#32](https://github.com/sasroque-beep/ai-3d-web-builder/pull/32) |
| 17/09 | ✅ | Persistência da experiência 3D por seção | Issue [#33](https://github.com/sasroque-beep/ai-3d-web-builder/issues/33) · PR [#34](https://github.com/sasroque-beep/ai-3d-web-builder/pull/34) |
| 18/09 | ✅ | Correção de testes instáveis (race condition em formulários) | Issue [#35](https://github.com/sasroque-beep/ai-3d-web-builder/issues/35) · PR [#36](https://github.com/sasroque-beep/ai-3d-web-builder/pull/36) |
| 20/09 | ✅ | Correção do hook de commit (caminho com espaço) | Issue [#38](https://github.com/sasroque-beep/ai-3d-web-builder/issues/38) · PR [#39](https://github.com/sasroque-beep/ai-3d-web-builder/pull/39) |
| 20/09 | ✅ | Primeiro preset 3D (**Hero Showcase**) + runtime com fallback 2D + registry de presets; bundle medido | Issue [#37](https://github.com/sasroque-beep/ai-3d-web-builder/issues/37) · PR [#40](https://github.com/sasroque-beep/ai-3d-web-builder/pull/40) |
| 21/09 | ✅ | Testes E2E em navegador real (Playwright/Chromium) em job separado da CI | Issue [#41](https://github.com/sasroque-beep/ai-3d-web-builder/issues/41) · PR [#43](https://github.com/sasroque-beep/ai-3d-web-builder/pull/43) |
| 22/09 | ✅ | Correção: descartar a cena 3D não trava mais o modo automático em 2D | Issue [#42](https://github.com/sasroque-beep/ai-3d-web-builder/issues/42) · PR [#44](https://github.com/sasroque-beep/ai-3d-web-builder/pull/44) |
| 26/09 | ✅ | Experiência 3D exibida no preview real do site (somente leitura) | Issue [#45](https://github.com/sasroque-beep/ai-3d-web-builder/issues/45) · PR [#46](https://github.com/sasroque-beep/ai-3d-web-builder/pull/46) · [11bcba4](https://github.com/sasroque-beep/ai-3d-web-builder/commit/11bcba4) |

### Em desenvolvimento 🔄

| Item | Status | Referência |
| --- | --- | --- |
| Editar a experiência 3D de uma seção direto no preview (formulário do preset Hero Showcase) | 🔄 PR aberto, ainda **não mergeado** | Issue [#48](https://github.com/sasroque-beep/ai-3d-web-builder/issues/48) · PR [#49](https://github.com/sasroque-beep/ai-3d-web-builder/pull/49) · branch `feature/48-editar-experiencia-3d-no-preview` |
| Avaliar tornar o job E2E um check obrigatório da `main` (issue registra 12 execuções verdes desde 21/09) | 🔄 Issue aberta (decisão pendente) | Issue [#47](https://github.com/sasroque-beep/ai-3d-web-builder/issues/47) |

### Planejado 🗺️

| Item | Onde está registrado |
| --- | --- |
| Modo de demonstração segura para casos-piloto (isolar dados de demonstração dos dados reais) | Issue [#31](https://github.com/sasroque-beep/ai-3d-web-builder/issues/31) (aberta, sem código) |
| Agentes de IA e orquestrador (pesquisa, estratégia, copy, design, SEO, 3D, QA, deploy) | `docs/AI_AGENTS.md`, `src/ai/README.md` (*planned — no implementation yet*) |
| Integrações de marketing (Google Analytics, Tag Manager, Meta Pixel, Conversion API, UTMs) | `src/modules/marketing/README.md` (*planned*), README |
| Analytics interno de conversão e relatórios | `src/modules/analytics/README.md` (*planned*) |
| Publicação/deploy dos sites, SEO técnico, observabilidade | README, `docs/DEPLOYMENT.md`, `docs/PRODUCT_REQUIREMENTS.md` |
| Novos presets 3D além do Hero Showcase | PR [#40](https://github.com/sasroque-beep/ai-3d-web-builder/pull/40) (registry extensível), PR [#49](https://github.com/sasroque-beep/ai-3d-web-builder/pull/49) (seletor de preset fica para quando houver um segundo preset) |
| Autenticação e multi-tenant | `src/server/README.md` (*Future issue*), citado na issue #31 |
| Primeira release | Nenhuma release/tag publicada até agora |

---

## 3. Série de postagens

**Sequência sugerida (cronológica):** 9 episódios. Sugestão de cadência: 1 a 2 por semana, sempre LinkedIn + Instagram do mesmo episódio. Cada episódio tem um ângulo diferente para evitar repetição:

| # | Tema | Ângulo |
| --- | --- | --- |
| 1 | Por que estamos construindo | Visão e propósito |
| 2 | Escrever antes de programar | Documentação como estratégia |
| 3 | O processo é o produto | Governança e disciplina |
| 4 | O primeiro dado entra | Fundação técnica + CRM |
| 5 | Entender antes de desenhar | Pesquisa → diagnóstico → estratégia |
| 6 | O site começa a aparecer | Do planejamento ao preview |
| 7 | 3D sem deixar ninguém para trás | Acessibilidade e fallback |
| 8 | Medir, não presumir | Performance e testes |
| 9 | O 3D chega ao produto — e o que vem agora | Status atual + roadmap honesto |

---

### Episódio 1 — Por que estamos construindo

#### LinkedIn

> **Site bonito não paga conta. Site que converte, sim.**
>
> Na Kraken, a gente decidiu construir uma ferramenta própria para resolver um problema que vemos o tempo todo no marketing: empresas sem site, com site desatualizado ou com um site que é só uma "vitrine" e não faz parte da jornada de compra.
>
> Em 25 de agosto de 2026 abrimos o repositório do **AI 3D Web Builder** e a primeira coisa que fizemos não foi código. Foi escrever a visão do produto.
>
> **O contexto:** o mercado costuma vender separado — "faço seu site" de um lado, "faço seu tráfego" do outro. No meio, a estratégia se perde.
>
> **O desafio:** como juntar estratégia, site, jornada de compra, conversão e dados numa coisa só?
>
> **A proposta que registramos:** um fluxo que começa na empresa e passa por pesquisa, estratégia, jornada de compra, copy, arquitetura, design, experiência 3D, conversão, leads, marketing, analytics e otimização.
>
> E um princípio que guia tudo:
> *"Não criamos apenas sites 3D. Criamos experiências digitais de alta conversão, utilizando 3D quando ele aumenta o valor percebido, o entendimento, o engajamento ou a conversão."*
>
> O 3D é uma ferramenta. A conversão é o objetivo.
>
> **Aprendizado até aqui:** escrever o "porquê" antes do "como" obriga a gente a dizer não para muita coisa bonita que não ajuda a vender.
>
> Nos próximos posts vou mostrar, com o histórico real do GitHub, como essa ideia está virando produto — inclusive o que ainda não existe.
>
> #Kraken #MarketingDigital #Produto #Sites3D #Conversão #BuildInPublic

**Referências:** commits [717ceb8](https://github.com/sasroque-beep/ai-3d-web-builder/commit/717ceb8) e [3a5a43a](https://github.com/sasroque-beep/ai-3d-web-builder/commit/3a5a43a) ("docs: define product vision"); [README.md](https://github.com/sasroque-beep/ai-3d-web-builder/blob/main/README.md) (seções "Visão do Produto", "Princípio central", "Objetivo de negócio").

#### Instagram — Carrossel (7 slides)

1. **Capa:** "Site bonito não paga conta. 🐙 A jornada da Kraken começa aqui."
2. "O problema: empresas sem site, com site antigo ou com site que não vende."
3. "O mercado vende separado: site de um lado, tráfego do outro. A estratégia se perde no meio."
4. "Nossa aposta: Estratégia + Site 3D + Jornada de Compra + Conversão + Tráfego + Dados + Otimização."
5. "Princípio: usamos 3D quando ele aumenta valor, entendimento, engajamento ou conversão."
6. "O 3D é ferramenta. A conversão é o objetivo."
7. **CTA:** "Vamos mostrar a construção do AI 3D Web Builder, passo a passo, direto do GitHub. Segue pra acompanhar."

**Legenda:**
Em 25/08/2026 abrimos o repositório do AI 3D Web Builder — e a primeira coisa que fizemos foi escrever a visão, não o código. 🐙
A ideia: um site que faz parte da jornada de compra, e não só uma vitrine.
Esta é a primeira parte de uma série mostrando a construção real do produto, com o que já existe e o que ainda está no papel.
#Kraken #MarketingDigital #Sites3D #Conversão #BuildInPublic

---

### Episódio 2 — Escrever antes de programar

#### LinkedIn

> **Passamos duas semanas sem escrever uma linha de código do produto. E foi de propósito.**
>
> Entre 25 de agosto e 4 de setembro, o repositório do AI 3D Web Builder recebeu só documentação: requisitos de produto, arquitetura do sistema, stack, banco de dados, arquitetura de agentes de IA, design system, padrões de qualidade, diretrizes de segurança e fluxo de deploy.
>
> **Por quê?** Porque um produto que mistura marketing, conversão, design e 3D tem muitas formas de dar errado. Documentar primeiro foi o jeito de alinhar decisões antes de elas virarem retrabalho.
>
> **O desafio:** documento que ninguém lê vira enfeite. Então a documentação foi escrita para ser usada no dia a dia, inclusive pelos agentes de IA que apoiam o desenvolvimento — o repositório tem um `AGENTS.md` com as regras que eles seguem.
>
> **Um cuidado de transparência:** parte desses documentos descreve o que *vai* existir. A arquitetura de agentes de IA dentro do produto, por exemplo, está documentada mas ainda não implementada. E o próprio documento de requisitos está marcado como incompleto, para ser finalizado em uma issue dedicada.
>
> **Aprendizado:** documentação boa não é a que descreve tudo — é a que deixa claro o que é decisão, o que é hipótese e o que ainda está em aberto.
>
> #Kraken #Produto #Documentação #DesenvolvimentoDeSoftware #BuildInPublic

**Referências:** [6be29ab](https://github.com/sasroque-beep/ai-3d-web-builder/commit/6be29ab) (SYSTEM_ARCHITECTURE), [4d37ed4](https://github.com/sasroque-beep/ai-3d-web-builder/commit/4d37ed4) (PRODUCT_REQUIREMENTS), [08cdafa](https://github.com/sasroque-beep/ai-3d-web-builder/commit/08cdafa) (TECH_STACK), [822d4c4](https://github.com/sasroque-beep/ai-3d-web-builder/commit/822d4c4) (DATABASE), [07c62a0](https://github.com/sasroque-beep/ai-3d-web-builder/commit/07c62a0) (AI_AGENTS), [eb822bb](https://github.com/sasroque-beep/ai-3d-web-builder/commit/eb822bb) (DESIGN_SYSTEM), [ba4dfec](https://github.com/sasroque-beep/ai-3d-web-builder/commit/ba4dfec) (QUALITY_ASSURANCE), [f98b6f8](https://github.com/sasroque-beep/ai-3d-web-builder/commit/f98b6f8) (SECURITY), [41c9726](https://github.com/sasroque-beep/ai-3d-web-builder/commit/41c9726) (DEPLOYMENT), [47a7c67](https://github.com/sasroque-beep/ai-3d-web-builder/commit/47a7c67) (AGENTS.md); pasta [docs/](https://github.com/sasroque-beep/ai-3d-web-builder/tree/main/docs).

#### Instagram — Carrossel (6 slides)

1. **Capa:** "2 semanas sem código. De propósito."
2. "Antes de programar, escrevemos: requisitos, arquitetura, stack, banco de dados, design system, qualidade, segurança e deploy."
3. "Por quê? Produto que mistura marketing, design e 3D tem muitos jeitos de dar errado."
4. "Os documentos também orientam os agentes de IA que apoiam o desenvolvimento (AGENTS.md)."
5. "Transparência: parte disso é plano. Os agentes de IA dentro do produto, por exemplo, ainda não existem."
6. **Fechamento:** "Documentação boa separa decisão, hipótese e o que ainda está em aberto."

**Legenda:**
De 25/08 a 04/09 o repositório do AI 3D Web Builder só recebeu documentação. 📚
Foi a forma de alinhar decisões antes de elas virarem retrabalho — e de deixar claro o que é plano e o que é realidade.
#Kraken #Produto #Documentação #BuildInPublic

---

### Episódio 3 — O processo é o produto

#### LinkedIn

> **Toda mudança no AI 3D Web Builder passa pelo mesmo caminho: issue, branch, testes, pull request, revisão, merge.**
>
> Parece burocracia? No começo, um pouco. Mas foi o que nos permitiu construir rápido sem perder o controle.
>
> **O que montamos antes do primeiro código de produto:**
> • Templates de issue para bug, nova funcionalidade, melhoria e tarefa técnica
> • Template de pull request com objetivo, o que foi feito e testes realizados
> • Um fluxo de desenvolvimento documentado
> • Depois, na estrutura inicial: verificação automática de padrão de commit e uma CI no GitHub Actions que roda lint, checagem de tipos, testes e build
>
> **O desafio:** disciplina não pode depender de memória. Tem que estar no fluxo.
>
> **O resultado que dá para ver no GitHub:** até agora, 22 pull requests mergeados — cada um ligado a uma issue que explica o porquê da mudança. Quem chega ao projeto consegue reconstruir a história de cada decisão.
>
> **Aprendizado:** quando o processo é claro, ele vira memória do produto. E isso vale ouro quando se trabalha com agentes de IA no desenvolvimento: eles seguem regras escritas, não intenções.
>
> #Kraken #GestãoDeProduto #Processos #GitHub #BuildInPublic

**Referências:** templates [f9726a9](https://github.com/sasroque-beep/ai-3d-web-builder/commit/f9726a9), [78e8956](https://github.com/sasroque-beep/ai-3d-web-builder/commit/78e8956), [bd297e2](https://github.com/sasroque-beep/ai-3d-web-builder/commit/bd297e2), [551c0b9](https://github.com/sasroque-beep/ai-3d-web-builder/commit/551c0b9), [ea1ee44](https://github.com/sasroque-beep/ai-3d-web-builder/commit/ea1ee44); fluxo [e9b32f3](https://github.com/sasroque-beep/ai-3d-web-builder/commit/e9b32f3) / [docs/DEVELOPMENT_WORKFLOW.md](https://github.com/sasroque-beep/ai-3d-web-builder/blob/main/docs/DEVELOPMENT_WORKFLOW.md); estrutura inicial com CI e commitlint: PR [#3](https://github.com/sasroque-beep/ai-3d-web-builder/pull/3); [.github/workflows/ci.yml](https://github.com/sasroque-beep/ai-3d-web-builder/blob/main/.github/workflows/ci.yml); lista de [PRs](https://github.com/sasroque-beep/ai-3d-web-builder/pulls?q=is%3Apr+is%3Amerged).

#### Instagram — Carrossel (6 slides)

1. **Capa:** "Nosso processo também é produto."
2. "Issue → Branch → Testes → Pull Request → Revisão → Merge."
3. "Templates para bug, feature, melhoria e tarefa técnica. Template de PR com objetivo e testes."
4. "CI automática: lint, tipos, testes e build a cada mudança."
5. "22 PRs mergeados até agora, cada um ligado a uma issue com o porquê."
6. **Fechamento:** "Disciplina não pode depender de memória. Tem que estar no fluxo."

**Legenda:**
Construir rápido sem perder o controle: esse é o papel do processo no AI 3D Web Builder. ⚙️
Cada mudança tem uma issue explicando o motivo e um PR mostrando o que foi feito e testado.
#Kraken #Processos #Produto #BuildInPublic

---

### Episódio 4 — O primeiro dado entra

#### LinkedIn

> **Todo site de alta conversão começa com uma pergunta simples: quem é essa empresa?**
>
> Em 10 de setembro, a estrutura técnica do AI 3D Web Builder foi ao ar no repositório: Next.js 15, React 19, TypeScript em modo estrito, Tailwind, testes com Vitest e CI no GitHub Actions.
>
> No dia seguinte, entrou o primeiro módulo real de produto: o **cadastro de empresas e leads**.
>
> **O que ele faz hoje:**
> • Lista as empresas cadastradas (com estado vazio quando não há nenhuma)
> • Formulário com campos obrigatórios, validação e mensagens de erro por campo
> • Página de detalhe de cada empresa
> • Telas de carregamento, erro e sucesso pensadas para acessibilidade e para quem prefere menos animação
>
> **Por que começar por aqui e não pelo 3D?** Porque, na nossa visão, o site é consequência da estratégia. E estratégia sem dados da empresa é chute.
>
> **Aprendizado:** a base "sem graça" — cadastro, validação, estados de tela — é o que sustenta tudo que vem depois. Pular essa etapa para chegar logo na parte bonita é o caminho mais curto para um produto frágil.
>
> #Kraken #Produto #CRM #MarketingDigital #BuildInPublic

**Referências:** Issue [#2](https://github.com/sasroque-beep/ai-3d-web-builder/issues/2) / PR [#3](https://github.com/sasroque-beep/ai-3d-web-builder/pull/3) (estrutura inicial, [8f18dcc](https://github.com/sasroque-beep/ai-3d-web-builder/commit/8f18dcc)); Issue [#4](https://github.com/sasroque-beep/ai-3d-web-builder/issues/4) / PR [#5](https://github.com/sasroque-beep/ai-3d-web-builder/pull/5) (cadastro, [071caf7](https://github.com/sasroque-beep/ai-3d-web-builder/commit/071caf7)); arquivos [src/modules/crm/](https://github.com/sasroque-beep/ai-3d-web-builder/tree/main/src/modules/crm), [src/ui/states/](https://github.com/sasroque-beep/ai-3d-web-builder/tree/main/src/ui/states), [src/app/leads/](https://github.com/sasroque-beep/ai-3d-web-builder/tree/main/src/app/leads).

#### Instagram — Carrossel (6 slides)

1. **Capa:** "Antes do 3D: quem é essa empresa?"
2. "10/09: a estrutura técnica entra no ar (Next.js, React, TypeScript, testes, CI)."
3. "11/09: primeiro módulo de produto — cadastro de empresas e leads."
4. "Lista, formulário com validação, página de detalhe e telas de carregamento/erro/sucesso acessíveis."
5. "Por que começar aqui? O site é consequência da estratégia. Estratégia sem dados é chute."
6. **Fechamento:** "A base 'sem graça' é o que segura a parte bonita."

**Legenda:**
O primeiro dado entrou no AI 3D Web Builder em 11/09: o cadastro de empresas e leads. 🗂️
Antes de qualquer efeito visual, a gente precisava saber quem é o cliente.
#Kraken #Produto #CRM #BuildInPublic

---

### Episódio 5 — Entender antes de desenhar

#### LinkedIn

> **Um site não deveria nascer de um template. Deveria nascer de um diagnóstico.**
>
> Em 12 de setembro, o AI 3D Web Builder ganhou quatro etapas que transformam o cadastro de uma empresa em inteligência estratégica:
>
> 1. **Enriquecimento de dados** — cada informação é marcada como *confirmada*, *não verificada* ou *ausente*.
> 2. **Diagnóstico estratégico do negócio** — só pode ser criado se existir pelo menos uma informação **confirmada**.
> 3. **Estratégia de marketing e conversão** da empresa.
> 4. **Planejamento estratégico do site** — que só é liberado quando já existe uma estratégia.
>
> **O desafio:** evitar o erro clássico de construir estratégia em cima de suposição.
>
> **A solução:** regras explícitas no sistema. Sem dado confirmado, não tem diagnóstico. Sem estratégia, não tem planejamento de site. A ordem não é sugestão — é regra do produto.
>
> **Transparência importante:** hoje essas etapas são preenchidas manualmente pelo operador, em formulários estruturados. O banco já reserva espaço para indicar quando um conteúdo for gerado por IA, mas os agentes de IA ainda estão no planejamento. Preferimos primeiro acertar o fluxo e as regras — a automação vem em cima de um processo que já funciona.
>
> **Aprendizado:** a IA vai acelerar o que for bem definido. Se o processo for confuso, ela só acelera a confusão.
>
> #Kraken #Estratégia #MarketingDigital #Diagnóstico #BuildInPublic

**Referências:** PR [#7](https://github.com/sasroque-beep/ai-3d-web-builder/pull/7) (enriquecimento, Issue [#6](https://github.com/sasroque-beep/ai-3d-web-builder/issues/6)); PR [#9](https://github.com/sasroque-beep/ai-3d-web-builder/pull/9) (diagnóstico e regra de dado confirmado, Issue [#8](https://github.com/sasroque-beep/ai-3d-web-builder/issues/8)); PR [#11](https://github.com/sasroque-beep/ai-3d-web-builder/pull/11) (estratégia, Issue [#10](https://github.com/sasroque-beep/ai-3d-web-builder/issues/10)); PR [#13](https://github.com/sasroque-beep/ai-3d-web-builder/pull/13) (planejamento do site, Issue [#12](https://github.com/sasroque-beep/ai-3d-web-builder/issues/12)); [src/modules/research/](https://github.com/sasroque-beep/ai-3d-web-builder/tree/main/src/modules/research), [src/modules/strategy/](https://github.com/sasroque-beep/ai-3d-web-builder/tree/main/src/modules/strategy), [src/modules/site-planning/](https://github.com/sasroque-beep/ai-3d-web-builder/tree/main/src/modules/site-planning); IA planejada: [src/ai/README.md](https://github.com/sasroque-beep/ai-3d-web-builder/blob/main/src/ai/README.md); campo `generated_by` em [src/server/db/schema.ts](https://github.com/sasroque-beep/ai-3d-web-builder/blob/main/src/server/db/schema.ts).

#### Instagram — Carrossel (7 slides)

1. **Capa:** "Site não nasce de template. Nasce de diagnóstico."
2. "Etapa 1: enriquecer os dados — confirmado, não verificado ou ausente."
3. "Etapa 2: diagnóstico do negócio. Regra: só com pelo menos um dado confirmado."
4. "Etapa 3: estratégia de marketing e conversão."
5. "Etapa 4: planejamento do site — só depois que existe estratégia."
6. "Hoje é manual, em formulários estruturados. A IA está no plano — primeiro acertamos o fluxo."
7. **Fechamento:** "IA acelera o que é bem definido. Processo confuso, ela só acelera a confusão."

**Legenda:**
Em 12/09 o AI 3D Web Builder ganhou o caminho da pesquisa até o planejamento do site. 🔎
Sem dado confirmado, não tem diagnóstico. Sem estratégia, não tem site. A ordem é regra do produto.
#Kraken #Estratégia #MarketingDigital #BuildInPublic

---

### Episódio 6 — O site começa a aparecer

#### LinkedIn

> **15 de setembro foi o dia em que os formulários viraram página.**
>
> Até ali, o AI 3D Web Builder organizava informação: empresa, diagnóstico, estratégia, planejamento. Faltava o momento de ver o site tomar forma.
>
> Em dois dias, entraram cinco etapas encadeadas:
> • **Arquitetura de páginas** a partir do planejamento estratégico
> • **Conteúdo/copy** de cada seção a partir dessa arquitetura
> • **Tema visual** e diretrizes de design
> • **Preview do site**, montando páginas, conteúdo e tema numa tela real
> • **Edição do conteúdo direto no preview**
>
> **O desafio:** cada etapa depende da anterior. Se a arquitetura muda, o conteúdo precisa acompanhar. Se o tema muda, o preview precisa refletir.
>
> **A escolha que fizemos:** preview somente leitura primeiro, edição depois. Primeiro garantir que o que é mostrado está certo; só então deixar editar. Esse mesmo padrão voltou a ser usado depois, na camada 3D.
>
> **Aprendizado:** entregar em fatias pequenas e encadeadas deixa cada passo verificável. Ninguém precisa esperar o "produto completo" para saber se está no caminho certo.
>
> #Kraken #Produto #UX #Copywriting #BuildInPublic

**Referências:** PR [#15](https://github.com/sasroque-beep/ai-3d-web-builder/pull/15) (arquitetura de páginas), PR [#17](https://github.com/sasroque-beep/ai-3d-web-builder/pull/17) (copy), PR [#19](https://github.com/sasroque-beep/ai-3d-web-builder/pull/19) (tema visual), PR [#21](https://github.com/sasroque-beep/ai-3d-web-builder/pull/21) (preview), PR [#23](https://github.com/sasroque-beep/ai-3d-web-builder/pull/23) (edição no preview); [src/modules/design/](https://github.com/sasroque-beep/ai-3d-web-builder/tree/main/src/modules/design), [src/modules/copy/](https://github.com/sasroque-beep/ai-3d-web-builder/tree/main/src/modules/copy), [src/modules/site-builder/](https://github.com/sasroque-beep/ai-3d-web-builder/tree/main/src/modules/site-builder), [src/app/leads/[id]/site-builder/](https://github.com/sasroque-beep/ai-3d-web-builder/tree/main/src/app/leads/%5Bid%5D/site-builder).

#### Instagram — Carrossel (7 slides)

1. **Capa:** "O dia em que os formulários viraram página."
2. "Planejamento → Arquitetura de páginas."
3. "Arquitetura → Conteúdo de cada seção."
4. "Tema visual e diretrizes de design."
5. "Preview: tudo montado numa tela real."
6. "Depois: editar o conteúdo direto no preview."
7. **Fechamento:** "Primeiro mostrar certo. Depois deixar editar."

**Legenda:**
Entre 15 e 16/09, o AI 3D Web Builder saiu da planilha mental e começou a mostrar o site. 🖥️
Cinco etapas encadeadas, entregues em fatias pequenas e verificáveis.
#Kraken #Produto #UX #BuildInPublic

---

### Episódio 7 — 3D sem deixar ninguém para trás

#### LinkedIn

> **O 3D mais caro é aquele que faz o cliente desistir da página.**
>
> Em 17 de setembro começamos a camada 3D do AI 3D Web Builder. E antes de criar qualquer efeito, registramos as regras do jogo.
>
> **As decisões que documentamos:**
> • **Progressive enhancement:** o 3D é uma camada a mais. Conteúdo e botão de ação nunca dependem dele.
> • **Detecção de capacidade:** o sistema verifica se o navegador suporta WebGL e se a pessoa prefere menos movimento.
> • **Três modos:** 3D completo, 3D reduzido (imagem estática, sem animação contínua) e fallback 2D.
> • **Fallback 2D obrigatório** no contrato de dados de toda experiência 3D.
> • **Isolamento:** o restante do sistema não importa as bibliotecas 3D diretamente — e há um teste automatizado que verifica isso.
>
> **O desafio:** como ter impacto visual sem punir quem tem celular mais simples, conexão fraca ou sensibilidade a movimento?
>
> **A resposta:** o 3D se adapta ao visitante, e não o contrário. Se algo falhar — sem WebGL, perda do contexto gráfico, erro ao carregar — a página volta para a versão 2D, com o mesmo conteúdo e o mesmo CTA.
>
> **Aprendizado:** acessibilidade não é um "extra" do 3D. É o que decide se ele ajuda ou atrapalha a conversão.
>
> #Kraken #Acessibilidade #Sites3D #UX #BuildInPublic

**Referências:** PR [#25](https://github.com/sasroque-beep/ai-3d-web-builder/pull/25) (fundação 3D com React Three Fiber + Drei); PR [#27](https://github.com/sasroque-beep/ai-3d-web-builder/pull/27) / Issue [#26](https://github.com/sasroque-beep/ai-3d-web-builder/issues/26) (decisões arquiteturais); PR [#29](https://github.com/sasroque-beep/ai-3d-web-builder/pull/29) (capability detection, [src/lib/capability/](https://github.com/sasroque-beep/ai-3d-web-builder/tree/main/src/lib/capability)); PR [#32](https://github.com/sasroque-beep/ai-3d-web-builder/pull/32) (contrato com fallback 2D obrigatório); PR [#34](https://github.com/sasroque-beep/ai-3d-web-builder/pull/34) (persistência); PR [#40](https://github.com/sasroque-beep/ai-3d-web-builder/pull/40) (comportamento de volta ao 2D); [src/modules/experience-3d/README.md](https://github.com/sasroque-beep/ai-3d-web-builder/blob/main/src/modules/experience-3d/README.md); teste [isolation.test.ts](https://github.com/sasroque-beep/ai-3d-web-builder/blob/main/src/modules/experience-3d/isolation.test.ts).

#### Instagram — Carrossel (7 slides)

1. **Capa:** "O 3D mais caro é o que faz o cliente ir embora."
2. "Regra 1: o 3D é camada extra. Conteúdo e CTA nunca dependem dele."
3. "Regra 2: o sistema detecta WebGL e preferência por menos movimento."
4. "Três modos: 3D completo · 3D reduzido · 2D."
5. "Falhou? Volta para o 2D com o mesmo conteúdo e o mesmo botão."
6. "Fallback 2D é obrigatório em toda experiência 3D."
7. **Fechamento:** "O 3D se adapta ao visitante — não o contrário."

**Legenda:**
Em 17/09 começamos a camada 3D do AI 3D Web Builder — pelas regras, não pelos efeitos. 🧊
Acessibilidade é o que decide se o 3D ajuda ou atrapalha a conversão.
#Kraken #Acessibilidade #Sites3D #BuildInPublic

---

### Episódio 8 — Medir, não presumir

#### LinkedIn

> **"Medido, não presumido." Essa frase está escrita num dos nossos pull requests e virou quase um lema.**
>
> Entre 20 e 22 de setembro, o AI 3D Web Builder ganhou o primeiro preset 3D real — o **Hero Showcase** — e uma bateria de testes em navegador real. Os números abaixo estão registrados nos próprios PRs:
>
> **Performance do primeiro preset:**
> • As bibliotecas 3D só são baixadas sob demanda, depois que a página carrega
> • Nenhuma das 13 rotas sem 3D aumentou de tamanho com a entrada do preset
> • Quem cai no modo 2D não baixa o pacote 3D
>
> **Testes de ponta a ponta (Playwright, navegador Chromium):**
> • 25 testes cobrindo os modos 3D completo, reduzido e 2D, perda do contexto gráfico, carregamento sob demanda e erros de console
> • Conteúdo e CTA verificados como clicáveis em todos os modos
>
> **O desafio que apareceu:** rodando dois testes em paralelo, cerca de 10% das execuções falhavam por excesso de carga na máquina. Em vez de esconder o problema, registramos o número, passamos para execução em fila e repetimos a suíte 10 vezes: 250 execuções, 0 falhas.
>
> **E os bugs?** Apareceram — e estão públicos. Um deles fazia o modo automático "travar" no 2D depois que a cena 3D era descartada. Foi documentado numa issue, explicado no PR e corrigido com testes novos.
>
> **Aprendizado:** confiança em produto vem de evidência. Mostrar o bug corrigido diz mais sobre qualidade do que fingir que ele nunca existiu.
>
> #Kraken #Qualidade #Performance #Testes #BuildInPublic

**Referências:** PR [#40](https://github.com/sasroque-beep/ai-3d-web-builder/pull/40) (preset Hero Showcase, tabela de bundle e "Nenhuma das 13 rotas sem 3D cresceu"); PR [#43](https://github.com/sasroque-beep/ai-3d-web-builder/pull/43) / Issue [#41](https://github.com/sasroque-beep/ai-3d-web-builder/issues/41) (E2E: 25 testes, ~10% de falhas com 2 workers, 250/0 com 1 worker, seção "Estabilidade (medida, não presumida)"); PR [#44](https://github.com/sasroque-beep/ai-3d-web-builder/pull/44) / Issue [#42](https://github.com/sasroque-beep/ai-3d-web-builder/issues/42) (bug do modo automático travado em 2D); também PR [#36](https://github.com/sasroque-beep/ai-3d-web-builder/pull/36) (testes instáveis) e PR [#39](https://github.com/sasroque-beep/ai-3d-web-builder/pull/39) (hook de commit); pasta [e2e/experience-3d/](https://github.com/sasroque-beep/ai-3d-web-builder/tree/main/e2e/experience-3d).

#### Instagram — Carrossel (7 slides)

1. **Capa:** "Medido, não presumido. 📏"
2. "Primeiro preset 3D: Hero Showcase."
3. "3D só baixa quando precisa. Nenhuma das 13 rotas sem 3D ficou mais pesada."
4. "25 testes em navegador real: 3D completo, reduzido, 2D e falhas."
5. "Em paralelo, ~10% falhavam por carga. Ajustamos: 250 execuções, 0 falhas."
6. "Bug encontrado, documentado e corrigido — tudo público no GitHub."
7. **Fechamento:** "Confiança vem de evidência."

**Legenda:**
Entre 20 e 22/09, o AI 3D Web Builder ganhou o primeiro preset 3D e testes em navegador real. 🧪
Os números estão nos PRs — inclusive os que não eram bonitos no começo.
#Kraken #Qualidade #Performance #BuildInPublic

---

### Episódio 9 — O 3D chega ao produto (e o que vem agora)

#### LinkedIn

> **Em 26 de setembro, as duas metades se encontraram: a experiência 3D passou a aparecer no preview real do site.**
>
> Até então, o 3D existia numa rota interna de validação. Agora, cada seção do site pode exibir sua experiência 3D logo abaixo do título — sempre como camada extra, nunca no lugar do conteúdo ou do CTA.
>
> **Onde estamos, com honestidade:**
>
> ✅ **Implementado:** cadastro de empresas, enriquecimento, diagnóstico, estratégia, planejamento do site, arquitetura de páginas, copy, tema visual, preview editável e experiência 3D no preview (somente leitura), com fallback 2D e testes automatizados.
>
> 🔄 **Em desenvolvimento:** editar a experiência 3D de cada seção direto no preview — o pull request está aberto, ainda não foi incorporado. E uma decisão pendente sobre tornar os testes em navegador real obrigatórios antes de cada merge.
>
> 🗺️ **Planejado:** modo de demonstração seguro para casos-piloto, agentes de IA que automatizem as etapas, integrações de marketing (Analytics, Tag Manager, Meta Pixel, Conversion API), analytics de conversão, publicação dos sites e novos presets 3D.
>
> Ainda não temos release publicada. E está tudo bem: o objetivo desta série foi mostrar a construção real, não um lançamento.
>
> **Aprendizado:** construir em público obriga a separar o que existe do que é promessa. E essa clareza é exatamente o que queremos levar para os sites que a Kraken vai entregar.
>
> Próximos capítulos quando os próximos PRs forem mergeados.
>
> #Kraken #Produto #Sites3D #Roadmap #BuildInPublic

**Referências:** PR [#46](https://github.com/sasroque-beep/ai-3d-web-builder/pull/46) / Issue [#45](https://github.com/sasroque-beep/ai-3d-web-builder/issues/45) (3D no preview, [11bcba4](https://github.com/sasroque-beep/ai-3d-web-builder/commit/11bcba4)); **em desenvolvimento:** PR [#49](https://github.com/sasroque-beep/ai-3d-web-builder/pull/49) (aberto) / Issue [#48](https://github.com/sasroque-beep/ai-3d-web-builder/issues/48), Issue [#47](https://github.com/sasroque-beep/ai-3d-web-builder/issues/47); **planejado:** Issue [#31](https://github.com/sasroque-beep/ai-3d-web-builder/issues/31), [src/ai/README.md](https://github.com/sasroque-beep/ai-3d-web-builder/blob/main/src/ai/README.md), [src/modules/marketing/README.md](https://github.com/sasroque-beep/ai-3d-web-builder/blob/main/src/modules/marketing/README.md), [src/modules/analytics/README.md](https://github.com/sasroque-beep/ai-3d-web-builder/blob/main/src/modules/analytics/README.md), [README.md](https://github.com/sasroque-beep/ai-3d-web-builder/blob/main/README.md); ausência de releases: [releases](https://github.com/sasroque-beep/ai-3d-web-builder/releases).

#### Instagram — Carrossel (8 slides)

1. **Capa:** "O 3D chegou ao produto. E agora? 🐙"
2. "26/09: a experiência 3D aparece no preview real do site — como camada extra, nunca no lugar do CTA."
3. "✅ Já existe: cadastro → pesquisa → diagnóstico → estratégia → planejamento → páginas → copy → tema → preview."
4. "✅ Também: 3D no preview, com fallback 2D e testes automáticos."
5. "🔄 Em andamento: editar o 3D direto no preview (PR aberto)."
6. "🗺️ No plano: agentes de IA, integrações de marketing, analytics, publicação e novos presets 3D."
7. "Ainda sem release. O objetivo foi mostrar a construção real."
8. **CTA:** "Os próximos capítulos chegam com os próximos merges. Segue a Kraken para acompanhar."

**Legenda:**
Fechamos esta temporada da jornada do AI 3D Web Builder com o 3D aparecendo no preview real do site. 🧊
Separamos o que já existe, o que está em andamento e o que ainda é plano — porque transparência também é estratégia.
#Kraken #Produto #Sites3D #Roadmap #BuildInPublic

---

## Checklist antes de publicar

- [ ] Confirmar que o AI 3D Web Builder é o produto/projeto da Kraken e o nome que será usado publicamente.
- [ ] Revisar as frases em primeira pessoa (são sugestões).
- [ ] Antes do Episódio 9, reconferir o status do PR #49 e das issues #47 e #31 — se algo mudou, atualizar o post.
- [ ] Não citar o nome da empresa do caso-piloto (issue #31) sem autorização.
- [ ] Não afirmar que a IA já gera sites: no momento da análise, os agentes de IA do produto estão apenas planejados.
- [ ] Os links apontam para um repositório **público**; confirmar que é desejável expô-lo nos posts.
