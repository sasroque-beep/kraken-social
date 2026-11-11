"""Segundo post diário do Instagram (noite) por episódio.

Cada carrossel aprofunda UM fato do episódio do dia, sempre com base no
GitHub (mesmas referências do episódio). Nada aqui é novo fato fora do repositório.
"""

IG_NOITE = {
    1: {
        "titulo": "O fluxo completo do produto",
        "slides": [
            {"tipo": "capa", "texto": "O caminho que o site percorre antes de existir."},
            {"texto": "Começa na empresa. Depois: pesquisa, estratégia e jornada de compra."},
            {"texto": "Em seguida: copy, arquitetura, design e experiência 3D."},
            {"texto": "E continua depois do site: conversão, leads, marketing, analytics e otimização."},
            {"tipo": "fecho", "texto": "O site é consequência da estratégia, não o ponto de partida."},
        ],
        "legenda": (
            "Esse é o fluxo que registramos no README do AI 3D Web Builder logo no primeiro dia. 🧭\n"
            "Hoje parte dele já existe e parte ainda é plano — ao longo da série mostramos qual é qual.\n"
            "#Kraken #MarketingDigital #Estratégia #BuildInPublic"
        ),
    },
    2: {
        "titulo": "Os documentos antes do código",
        "slides": [
            {"tipo": "capa", "texto": "O que escrevemos antes da primeira linha de código do produto."},
            {"texto": "Requisitos de produto · Arquitetura do sistema · Stack técnica"},
            {"texto": "Banco de dados · Arquitetura de agentes de IA · Design system"},
            {"texto": "Qualidade · Segurança · Deploy"},
            {"tipo": "fecho", "texto": "Documentado não é o mesmo que implementado. E a gente deixa isso claro."},
        ],
        "legenda": (
            "Nove documentos na pasta docs/ antes do primeiro código de produto. 📂\n"
            "Alguns descrevem o que já existe; outros, como os agentes de IA dentro do produto, ainda são plano.\n"
            "#Kraken #Produto #Documentação #BuildInPublic"
        ),
    },
    3: {
        "titulo": "Anatomia de uma mudança",
        "slides": [
            {"tipo": "capa", "texto": "Como uma mudança entra no produto."},
            {"texto": "1. Uma issue explica o porquê: bug, funcionalidade, melhoria ou tarefa técnica."},
            {"texto": "2. Um pull request mostra o objetivo, o que foi feito e os testes realizados."},
            {"texto": "3. A CI roda lint, checagem de tipos, testes e build automaticamente."},
            {"tipo": "fecho", "texto": "Só depois disso acontece o merge."},
        ],
        "legenda": (
            "Issue → PR → CI → merge. Esse é o caminho de cada mudança no AI 3D Web Builder. 🔁\n"
            "Templates e automação garantem que ninguém precise lembrar das regras de cabeça.\n"
            "#Kraken #Processos #GitHub #BuildInPublic"
        ),
    },
    4: {
        "titulo": "A stack que escolhemos",
        "slides": [
            {"tipo": "capa", "texto": "As ferramentas por trás do AI 3D Web Builder."},
            {"texto": "Next.js 15 + React 19, com TypeScript em modo estrito."},
            {"texto": "Tailwind CSS v4 no visual. SQLite (libSQL) + Drizzle ORM nos dados."},
            {"texto": "Vitest e Playwright nos testes. GitHub Actions na CI."},
            {"texto": "Three.js + React Three Fiber + Drei na camada 3D."},
            {"tipo": "fecho", "texto": "Ferramenta escolhida e registrada em documento, não por moda."},
        ],
        "legenda": (
            "A stack do AI 3D Web Builder está registrada no README e em docs/TECH_STACK.md. 🛠️\n"
            "#Kraken #Tecnologia #Produto #BuildInPublic"
        ),
    },
    5: {
        "titulo": "Confirmado, não verificado, ausente",
        "slides": [
            {"tipo": "capa", "texto": "Três palavras que protegem a estratégia."},
            {"texto": "CONFIRMADO: a informação foi checada."},
            {"texto": "NÃO VERIFICADO: existe, mas ainda não foi checada."},
            {"texto": "AUSENTE: a informação não existe ainda."},
            {"texto": "Regra do produto: sem pelo menos um dado confirmado, não existe diagnóstico."},
            {"tipo": "fecho", "texto": "Estratégia em cima de suposição não passa."},
        ],
        "legenda": (
            "No AI 3D Web Builder, cada dado de uma empresa tem um status. 🏷️\n"
            "E o diagnóstico do negócio só pode ser criado se houver ao menos um dado confirmado.\n"
            "#Kraken #Estratégia #Dados #BuildInPublic"
        ),
    },
    6: {
        "titulo": "Mostrar certo, depois editar",
        "slides": [
            {"tipo": "capa", "texto": "Um padrão que usamos duas vezes."},
            {"texto": "15/09: preview do site, somente leitura."},
            {"texto": "16/09: edição do conteúdo direto no preview."},
            {"texto": "26/09: experiência 3D no preview, somente leitura."},
            {"texto": "Agora: edição do 3D no preview — PR aberto, ainda não incorporado."},
            {"tipo": "fecho", "texto": "Primeiro garantir que o que aparece está certo. Depois deixar mexer."},
        ],
        "legenda": (
            "Leitura primeiro, edição depois: o mesmo padrão no site e na camada 3D. 🖊️\n"
            "A edição do 3D ainda está em desenvolvimento (PR #49 aberto).\n"
            "#Kraken #Produto #UX #BuildInPublic"
        ),
    },
    7: {
        "titulo": "Os 3 modos do 3D",
        "slides": [
            {"tipo": "capa", "texto": "Como o sistema decide o que cada visitante vê."},
            {"texto": "Sem suporte a WebGL ou com falha na cena: versão 2D."},
            {"texto": "Aparelho de menor capacidade ou preferência por menos movimento: 3D reduzido."},
            {"texto": "Nenhuma restrição: 3D completo."},
            {"tipo": "fecho", "texto": "Em todos os modos: o mesmo conteúdo e o mesmo botão de ação."},
        ],
        "legenda": (
            "A regra de decisão dos modos 3D está no código (src/lib/capability). 🧩\n"
            "O 3D se adapta ao visitante, e o conteúdo nunca depende dele.\n"
            "#Kraken #Acessibilidade #Sites3D #BuildInPublic"
        ),
    },
    8: {
        "titulo": "Um bug do início ao fim",
        "slides": [
            {"tipo": "capa", "texto": "Um bug real, contado em público."},
            {"texto": "O problema: depois que a cena 3D era descartada, o modo automático ficava preso no 2D."},
            {"texto": "Issue #42: o bug foi descrito e registrado."},
            {"texto": "PR #44: a causa foi explicada e corrigida, com testes novos."},
            {"tipo": "fecho", "texto": "Bug corrigido e documentado vale mais que bug escondido."},
        ],
        "legenda": (
            "Todo produto tem bug. A diferença está no que se faz com ele. 🐞\n"
            "Esse caso está público no GitHub: issue #42 e PR #44.\n"
            "#Kraken #Qualidade #Testes #BuildInPublic"
        ),
    },
    9: {
        "titulo": "O que ainda é plano",
        "slides": [
            {"tipo": "capa", "texto": "O que ainda não existe — e está no plano."},
            {"texto": "Modo de demonstração seguro para casos-piloto."},
            {"texto": "Agentes de IA para automatizar as etapas."},
            {"texto": "Integrações de marketing e analytics de conversão."},
            {"texto": "Publicação dos sites e novos presets 3D."},
            {"tipo": "fecho", "texto": "Plano é plano. A gente avisa quando virar produto."},
        ],
        "legenda": (
            "Fechando o dia com o roadmap, sem maquiagem: tudo aqui ainda está planejado. 🗺️\n"
            "Os próximos capítulos chegam com os próximos merges.\n"
            "#Kraken #Roadmap #Produto #BuildInPublic"
        ),
    },
}
