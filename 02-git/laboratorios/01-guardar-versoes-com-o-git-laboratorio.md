![Cabeçalho](../../imagens/cabecalho.png)

# Laboratório: Guardar versões com o Git

## O que vais construir

Pões o teu site no Git, com os primeiros commits do histórico. Primeiro treinas todos os comandos numa cópia da pasta do site, que podes estragar à vontade, e no fim fazes o mesmo na pasta verdadeira. Os exemplos usam o site do clube de xadrez do laboratório de HTML: escreve os teus nomes e as tuas mensagens. No fim, a pasta onde tens o site fica assim:

```text
clube-de-xadrez/        o teu site, agora um repositório
├── .git/               escondida
├── .gitignore
├── README.md
├── index.html
├── torneios.html
└── imagens/
treino-git/             a cópia de treino, com o histórico do treino
registo.md
```

1. [Fase 1: O terminal recebe comandos](#fase-1-o-terminal-recebe-comandos)
2. [Fase 2: Um repositório é uma pasta com memória](#fase-2-um-repositório-é-uma-pasta-com-memória)
3. [Fase 3: A identidade do autor](#fase-3-a-identidade-do-autor)
4. [Fase 4: O .gitignore diz o que fica de fora](#fase-4-o-gitignore-diz-o-que-fica-de-fora)
5. [Fase 5: O comando git add escolhe o que entra no commit](#fase-5-o-comando-git-add-escolhe-o-que-entra-no-commit)
6. [Fase 6: Um commit guarda uma alteração com sentido](#fase-6-um-commit-guarda-uma-alteração-com-sentido)
7. [Fase 7: O comando git diff mostra o que mudou](#fase-7-o-comando-git-diff-mostra-o-que-mudou)
8. [Fase 8: O comando git log mostra o histórico](#fase-8-o-comando-git-log-mostra-o-histórico)
9. [Fase 9: Desfazer antes do commit](#fase-9-desfazer-antes-do-commit)
10. [Fase 10: O painel Source Control](#fase-10-o-painel-source-control)
11. [Fase 11: O teu site no Git](#fase-11-o-teu-site-no-git)

## O que precisas

- O VS Code, o editor das aulas.
- O Git. Confirmas que está instalado na fase 1, com `git --version`.
- A pasta do teu site, do [laboratório de HTML](../../01-frontend/laboratorios/02-html-e-semantica-laboratorio.md), com as páginas e o plano, e o `registo.md` ao lado dela. Se não a tens, cria a pasta `clube-de-xadrez`, com as páginas das paragens 4 e 6 desse laboratório. Junta-lhe a pasta `imagens`, com a [imagem provisória](../../01-frontend/laboratorios/02-html-e-semantica-laboratorio/imagem-provisoria.svg), e cria o `registo.md` ao lado.

## Preparar o projeto

1. Confirma os nomes dos ficheiros da pasta do teu site, também as fotografias e a cópia do brief do plano, se as guardaste lá. Todos têm de estar em minúsculas, sem espaços e sem acentos, com hífenes entre as palavras, porque vais escrevê-los nos comandos do Git. Um nome como `Foto do mapa (1).jpg` muda-se para `mapa.jpg`: carrega no ficheiro, no Explorador de Ficheiros, e na tecla F2, no Windows, ou em Enter, no Mac.

2. Faz a cópia de treino. No Explorador de Ficheiros, abre a pasta onde tens a pasta do teu site e o `registo.md`. Carrega na pasta do site, depois em Ctrl+C e em Ctrl+V. Aparece uma pasta com o mesmo nome e a palavra "Copy" ou "Cópia". No Mac, no Finder, carrega com o botão direito na pasta e escolhe Duplicar.

3. Muda o nome da cópia para `treino-git`. Carrega nela e na tecla F2, no Windows, ou em Enter, no Mac, escreve o nome e carrega em Enter. O que deves ver: ao lado da pasta do teu site, a pasta `treino-git`, com os mesmos ficheiros lá dentro.

4. Abre a cópia no VS Code: no menu File, escolhe Open Folder... e depois a pasta `treino-git`. Se o VS Code perguntar se confias nos autores dos ficheiros, carrega em "Yes, I trust the authors". O que deves ver: no painel Explorer, à esquerda, o nome `TREINO-GIT`, com as tuas páginas e a pasta `imagens`.

## Fase 1: O terminal recebe comandos

Abres o terminal dentro da cópia de treino e confirmas que o Git está instalado. Rever: [O terminal recebe comandos](../01-guardar-versoes-com-o-git.md#o-terminal-recebe-comandos).

1. Abre o terminal: no menu Terminal, escolhe New Terminal. O que deves ver: um painel em baixo, com uma linha que acaba no caminho da pasta, como `PS C:\Users\aluno\Documents\treino-git>`. O caminho acaba em `treino-git`, e por isso os comandos vão trabalhar na cópia. Se acabar noutra pasta, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

2. Escreve este comando e carrega em Enter:

   ```bash
   git --version
   ```

   O que deves ver: uma linha como `git version 2.51.0.windows.1`. Isto quer dizer que o Git está instalado, e os números são os da versão. Se aparecer uma mensagem que começa por `git : The term 'git' is not recognized`, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

### Paragem 1

O terminal está aberto na pasta `treino-git` e responde ao `git --version`.

Pensa antes de continuares: porque é que, antes de cada comando do Git, convém olhar para o fim da linha do terminal? A resposta: os comandos do Git trabalham na pasta onde o terminal está. Se ela não for a que querias, o comando mexe noutra pasta.

## Fase 2: Um repositório é uma pasta com memória

Transformas a cópia num repositório e vês o que o Git encontra lá dentro. Rever: [Um repositório é uma pasta com memória](../01-guardar-versoes-com-o-git.md#um-repositório-é-uma-pasta-com-memória).

1. Antes de criares o repositório, prevê o que responde o `git status` numa pasta que ainda não é um repositório. Depois corre:

   ```bash
   git status
   ```

   O que deves ver: `fatal: not a git repository (or any of the parent directories): .git`. Isto quer dizer que esta pasta ainda não é um repositório, e o Git não tem nada para dizer sobre ela.

2. Cria o repositório:

   ```bash
   git init -b main
   ```

   O que deves ver: `Initialized empty Git repository in` e o caminho da pasta, acabado em `treino-git/.git/`. A pasta `.git` foi criada, escondida.

3. Corre outra vez o `git status`. O que deves ver, no exemplo:

   ```text
   On branch main

   No commits yet

   Untracked files:
     (use "git add <file>..." to include in what will be committed)
   	imagens/
   	index.html
   	torneios.html

   nothing added to commit but untracked files present (use "git add" to track)
   ```

   Os teus ficheiros estão todos em `Untracked files`: existem na pasta de trabalho, mas o Git ainda não os segue. No teu site, a lista tem também os ficheiros do plano, se os guardaste nesta pasta.

### Paragem 2

A cópia é um repositório, ainda sem commits.

Pensa antes de continuares: se apagasses a pasta `.git`, o que perdias? A resposta: todas as versões guardadas. As páginas ficavam na pasta, mas a pasta deixava de ser um repositório, sem nenhum commit.

## Fase 3: A identidade do autor

Dizes ao Git quem assina os commits desta pasta, com uma identidade inventada, porque é um repositório de treino. Rever: [A identidade do autor](../01-guardar-versoes-com-o-git.md#a-identidade-do-autor).

1. Vê se já há um nome guardado:

   ```bash
   git config user.name
   ```

   O que deves ver: nada, só uma linha nova para escreveres. Isto quer dizer que ainda não há identidade. Se aparecer um nome, alguém o guardou para o portátil inteiro. Avisa o professor e continua: o passo seguinte guarda a identidade desta pasta, que vale mais do que a do portátil.

2. Guarda a identidade inventada, só nesta pasta:

   ```bash
   git config user.name "Aluno de Treino"
   git config user.email "aluno.treino@example.com"
   ```

   O que deves ver: nada. Os comandos de configuração não respondem quando correm bem.

3. Confirma com `git config user.name`. O que deves ver: `Aluno de Treino`.

### Paragem 3

A pasta `treino-git` tem uma identidade, que vai ficar em todos os commits desta pasta.

Pensa antes de continuares: porque é que os comandos não levam `--global`? A resposta: com `--global`, a identidade ficava para o portátil inteiro, e ia parar aos commits do colega que o usasse a seguir.

## Fase 4: O .gitignore diz o que fica de fora

Crias o `.gitignore` antes do primeiro commit e confirmas que ele funciona. Rever: [O .gitignore diz o que fica de fora](../01-guardar-versoes-com-o-git.md#o-gitignore-diz-o-que-fica-de-fora).

1. No painel Explorer, carrega num espaço sem ficheiros, para o `.gitignore` não ir parar à pasta `imagens`. Carrega no ícone New File..., no topo do painel, escreve `.gitignore` e carrega em Enter. Escreve lá estas linhas e guarda, com Ctrl+S, ou Cmd+S no Mac:

   ```text
   # Ficheiros que o sistema operativo cria sozinho e que não fazem parte do site.
   .DS_Store
   Thumbs.db
   desktop.ini
   ```

2. Para pôr o `.gitignore` à prova, cria da mesma maneira um ficheiro vazio chamado `desktop.ini`. Antes de continuares, prevê: o `desktop.ini` vai aparecer no `git status`?

3. Corre o `git status`. O que deves ver: em `Untracked files`, o `.gitignore` aparece, e o `desktop.ini` não. Isto quer dizer que o Git está a ignorar o `desktop.ini`, como o `.gitignore` manda.

4. Apaga o `desktop.ini` de teste: no painel Explorer, carrega nele com o botão direito, escolhe Delete e confirma.

### Paragem 4

O `.gitignore` está na pasta e funciona, e ainda não há nenhum commit.

Pensa antes de continuares: porque é que o `.gitignore` se faz antes do primeiro commit? A resposta: só vale para os ficheiros que o Git ainda não segue. Um ficheiro que entrou num commit fica no histórico, mesmo que depois o escrevas no `.gitignore`.

## Fase 5: O comando git add escolhe o que entra no commit

Pões ficheiros na área de preparação, em duas vezes, e vês o `git status` mudar. Rever: [O comando git add escolhe o que entra no commit](../01-guardar-versoes-com-o-git.md#o-comando-git-add-escolhe-o-que-entra-no-commit).

1. Junta só o `.gitignore` e a página inicial:

   ```bash
   git add .gitignore index.html
   git status
   ```

   O que deves ver, no exemplo:

   ```text
   On branch main

   No commits yet

   Changes to be committed:
     (use "git rm --cached <file>..." to unstage)
   	new file:   .gitignore
   	new file:   index.html

   Untracked files:
     (use "git add <file>..." to include in what will be committed)
   	imagens/
   	torneios.html
   ```

   Os dois ficheiros passaram para a área de preparação, e os outros ficaram onde estavam.

2. Junta agora o resto: escreve `git add` seguido dos nomes que ainda aparecem em `Untracked files`. No exemplo:

   ```bash
   git add torneios.html imagens
   git status
   ```

   O que deves ver: todos os ficheiros em `Changes to be committed`, com `new file` à frente, e nenhum em `Untracked files`. A pasta `imagens` deu lugar aos ficheiros que tem, como `imagens/imagem-provisoria.svg`. No Windows, pode aparecer antes um aviso que acaba em `LF will be replaced by CRLF`: vê [Se alguma coisa falhar](#se-alguma-coisa-falhar). Se aparecer `fatal: pathspec`, um nome está mal escrito, e nada foi preparado: vê também [Se alguma coisa falhar](#se-alguma-coisa-falhar).

### Paragem 5

Tudo está na área de preparação, e ainda nada está no histórico.

Pensa antes de continuares: se agora mudasses o `index.html` e guardasses, que versão entrava no primeiro commit, a que preparaste ou a nova? A resposta: a que preparaste. O `git add` copiou o ficheiro como estava, e a mudança nova ficava em `Changes not staged for commit`, até a juntares outra vez.

## Fase 6: Um commit guarda uma alteração com sentido

Fazes o primeiro commit e confirmas que a pasta ficou igual ao que guardaste. Rever: [Um commit guarda uma alteração com sentido](../01-guardar-versoes-com-o-git.md#um-commit-guarda-uma-alteração-com-sentido).

1. Faz o commit, com uma mensagem que diz o que ele guarda:

   ```bash
   git commit -m "Guarda a primeira versão do site"
   ```

   O que deves ver, no exemplo:

   ```text
   [main (root-commit) 7199e9b] Guarda a primeira versão do site
    4 files changed, 91 insertions(+)
    create mode 100644 .gitignore
    create mode 100644 imagens/imagem-provisoria.svg
    create mode 100644 index.html
    create mode 100644 torneios.html
   ```

   O `root-commit` diz que é o primeiro, e o código a seguir identifica-o. O teu código e os teus números vão ser outros. Se aparecer `Author identity unknown`, ou um ecrã com linhas começadas por `~`, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

2. Corre o `git status`. O que deves ver: `nothing to commit, working tree clean`. A pasta de trabalho é igual ao último commit.

### Paragem 6

O histórico tem um commit, com todos os ficheiros da cópia.

Pensa antes de continuares: se agora mudares uma página, o commit que acabaste de fazer muda também? A resposta: não. O commit guardou as páginas como estavam. A mudança fica na pasta de trabalho, até a preparares e fazeres outro commit.

## Fase 7: O comando git diff mostra o que mudou

Mudas o título da página inicial, vês a mudança com o `git diff` e guarda-la num commit. Rever: [O comando git diff mostra o que mudou](../01-guardar-versoes-com-o-git.md#o-comando-git-diff-mostra-o-que-mudou).

1. Em `index.html`, muda o texto do `h1`. No exemplo, passa a "Aprende xadrez connosco, às quartas-feiras". Guarda o ficheiro.

2. Antes de correres, prevê em que grupo do `git status` aparece o `index.html`. Depois corre o `git status`. O que deves ver: o `index.html` em `Changes not staged for commit`, com `modified` à frente. O ficheiro é seguido e mudou, mas ainda não o preparaste.

3. Vê o que mudou:

   ```bash
   git diff
   ```

   O que deves ver, no exemplo:

   ```text
   diff --git a/index.html b/index.html
   index 50c9c7c..314de35 100644
   --- a/index.html
   +++ b/index.html
   @@ -18,7 +18,7 @@
          </nav>
        </header>
        <main>
   -      <h1>Aprende a jogar xadrez connosco</h1>
   +      <h1>Aprende xadrez connosco, às quartas-feiras</h1>
          <p>O clube reúne-se todas as semanas para jogar, aprender aberturas e preparar torneios.</p>
    
          <section>
   ```

   A linha antiga aparece com `-` e a nova com `+`. Se a última linha do terminal for `:` ou `(END)`, sai com a tecla `q`.

4. Prepara a mudança e confirma o que vai entrar no commit:

   ```bash
   git add index.html
   git diff
   git diff --staged
   ```

   O que deves ver: o `git diff` não mostra nada, porque já não há nada por preparar. O `git diff --staged` mostra a mesma mudança do passo 3, agora na área de preparação.

5. Faz o commit:

   ```bash
   git commit -m "Muda o título da página inicial"
   ```

   O que deves ver: `1 file changed, 1 insertion(+), 1 deletion(-)`. Uma linha alterada conta como uma linha apagada e uma acrescentada.

### Paragem 7

O histórico tem dois commits, e o `git status` diz `nothing to commit, working tree clean`.

Pensa antes de continuares: se tivesses criado uma página nova, `contactos.html`, ela aparecia no `git diff` do passo 3? A resposta: não. O Git só compara ficheiros que já segue. Uma página nova aparece no `git status`, em `Untracked files`.

## Fase 8: O comando git log mostra o histórico

Lês o histórico da cópia e guardas a versão curta no `registo.md`. Rever: [O comando git log mostra o histórico](../01-guardar-versoes-com-o-git.md#o-comando-git-log-mostra-o-histórico).

1. Corre o `git log`. O que deves ver: os dois commits, do mais recente para o mais antigo. Cada um tem o identificador, o autor `Aluno de Treino <aluno.treino@example.com>`, a data e a mensagem.

2. Corre a versão curta:

   ```bash
   git log --oneline
   ```

   O que deves ver, no exemplo:

   ```text
   f2be26a (HEAD -> main) Muda o título da página inicial
   7199e9b Guarda a primeira versão do site
   ```

3. Abre o `registo.md`: no menu File, escolhe Open Recent e depois o `registo.md` que está na pasta onde tens a pasta do teu site. Confirma o caminho, porque o portátil pode mostrar o `registo.md` de outro colega. No fim, escreve o título `## Laboratório do Git` e, por baixo, cola as duas linhas do `git log --oneline`. Para as copiar, seleciona-as com o rato, no terminal, e carrega em Ctrl+C, ou Cmd+C no Mac. Guarda o `registo.md`.

### Paragem 8

O `registo.md` tem o histórico curto da cópia de treino.

Pensa antes de continuares: porque é que no registo se cola o `git log --oneline`, e não o `git log`? A resposta: a versão curta tem o que interessa, as mensagens e os identificadores, e não mostra o email do autor.

## Fase 9: Desfazer antes do commit

Estragas uma página de propósito e desfazes o engano, em dois passos, sem perder nada que querias. Rever: [Desfazer antes do commit](../01-guardar-versoes-com-o-git.md#desfazer-antes-do-commit).

1. Em `torneios.html`, apaga as três linhas inteiras do rodapé, do `<footer>` ao `</footer>`, e guarda. Para apagar uma linha inteira, põe o cursor nela e carrega em Ctrl+Shift+K, ou Cmd+Shift+K no Mac. Este é o engano.

2. Junta o engano à área de preparação, como se não tivesses reparado:

   ```bash
   git add torneios.html
   git status
   ```

   O que deves ver: o `torneios.html` em `Changes to be committed`, com `modified` à frente.

3. Tira-o da área de preparação:

   ```bash
   git restore --staged torneios.html
   git status
   ```

   O que deves ver: o `torneios.html` voltou a `Changes not staged for commit`. O rodapé continua apagado no ficheiro, porque este comando não lhe mexe.

4. Vê com o `git diff` o que vais perder. O que deves ver: as três linhas do rodapé, cada uma com `-` à frente, e mais nada. É só o engano, e por isso podes deitá-lo fora.

5. Deita fora a alteração:

   ```bash
   git restore torneios.html
   git status
   ```

   O que deves ver: `nothing to commit, working tree clean`, e, no VS Code, o rodapé de volta ao `torneios.html`.

### Paragem 9

A página está como no último commit, e o histórico não mudou.

Pensa antes de continuares: no passo 5, porque é que se viu primeiro o `git diff`? A resposta: o `git restore` deita fora as alterações, e o Git não as guarda. O `git diff` mostra antes o que se vai perder.

## Fase 10: O painel Source Control

Fazes um commit só com o rato, no painel do Git do VS Code, e confirmas no terminal. Rever: [O painel Source Control](../01-guardar-versoes-com-o-git.md#o-painel-source-control).

1. Abre o painel: na barra da esquerda, carrega no ícone Source Control, ou em Ctrl+Shift+G. O que deves ver: os grupos Changes e Staged Changes vazios, ou nenhum grupo, porque a pasta é igual ao último commit. Pode aparecer um botão Publish Branch, que envia o repositório para o GitHub: não carregues nele, porque o GitHub fica para o tema seguinte.

2. Em `torneios.html`, a seguir ao primeiro parágrafo do `main`, acrescenta uma frase, como `<p>As inscrições para o torneio deste ano abrem em janeiro.</p>`, e guarda. O que deves ver: o `torneios.html` no grupo Changes, com a letra `M` à direita.

3. Carrega no nome do ficheiro, no painel. O que deves ver: as duas versões lado a lado, a do último commit à esquerda e a tua à direita. A frase nova está marcada. Fecha esse separador.

4. Passa o rato pelo `torneios.html`, no grupo Changes, e carrega no `+`, Stage Changes. O que deves ver: o ficheiro passa para o grupo Staged Changes. É o mesmo que um `git add`.

5. Na caixa Message, por cima dos grupos, escreve `Acrescenta a data das inscrições do torneio` e carrega no botão Commit. O que deves ver: os grupos ficam vazios. Se o VS Code perguntar se quer preparar todas as alterações, fecha a pergunta, sem carregar em Always, e repete o passo 4.

6. No terminal, corre o `git log --oneline`. O que deves ver: três commits, com `Acrescenta a data das inscrições do torneio` em cima. O commit feito no painel está no mesmo histórico.

### Paragem 10

O histórico da cópia tem três commits, um deles feito no painel Source Control.

Pensa antes de continuares: no painel, um ficheiro novo aparece com que letra, e o que acontece se carregares em Discard Changes nesse ficheiro? A resposta: com a letra `U`. O Discard Changes apaga-o, e ele vai para a Reciclagem, porque não há nenhum commit dele para onde voltar.

## Fase 11: O teu site no Git

Fazes na pasta verdadeira do site o que treinaste na cópia, com a tua identidade, e acabas com dois commits. Rever: [Exemplo guiado: a Estante Digital no Git](../01-guardar-versoes-com-o-git.md#exemplo-guiado-a-estante-digital-no-git).

1. Abre a pasta verdadeira do site: no menu File, escolhe Open Folder... e depois a pasta do teu site, como `clube-de-xadrez`. Abre um terminal novo, com New Terminal, no menu Terminal. O que deves ver: a linha do terminal acaba no nome da pasta do teu site, e não em `treino-git`.

2. Corre o `git status`. O que deves ver: `fatal: not a git repository`. A pasta do site ainda não é um repositório, como devia.

3. Cria o repositório e guarda a tua identidade, só nesta pasta. No lugar de `Nome Apelido`, escreve o teu nome e apelido; no email, o teu nome e apelido sem acentos, como `joana.silva@example.com`:

   ```bash
   git init -b main
   git config user.name "Nome Apelido"
   git config user.email "nome.apelido@example.com"
   git config user.name
   ```

   O que deves ver: `Initialized empty Git repository in` e o caminho da pasta do site, e no fim o teu nome.

4. Cria o `.gitignore`, como na fase 4, com as mesmas quatro linhas, e guarda.

5. Corre o `git status` e junta o `.gitignore` e todos os ficheiros e pastas que aparecem em `Untracked files`. As fotografias e a cópia do brief do plano também entram neste commit, porque são parte do site. No exemplo:

   ```bash
   git add .gitignore index.html torneios.html imagens
   git status
   ```

   O que deves ver: todos em `Changes to be committed`, e nenhum em `Untracked files`. Um ficheiro que não é do teu site, como um ficheiro de testes, não se escreve no comando: fica em `Untracked files`, e apaga-lo da pasta.

6. Faz o primeiro commit:

   ```bash
   git commit -m "Guarda a primeira versão do site"
   ```

   O que deves ver: `root-commit`, o número de ficheiros do teu site e um `create mode` para cada um.

7. Cria o README do site. Abre no browser o [modelo do README do site](../../projeto/modelos/readme-do-projeto.md), carrega em Raw e copia o texto todo. No VS Code, cria na pasta do site o ficheiro `README.md` e cola o texto. Apaga a primeira e a última linha, que são as imagens da disciplina. Cada campo do modelo está entre chavetas duplas. Troca estes cinco pelo teu texto, sem as chavetas:

   - o título, no topo: o nome do teu site;
   - a linha "Para quem é o site": para quem é o site e para que serve, numa frase;
   - o primeiro campo da secção "Como abrir": "Abre o `index.html` no browser.";
   - a linha "Como guardaste as versões": "Guardo as versões com o Git, com um commit por alteração.";
   - o campo da secção "Imagens e tipos de letra de outros": de onde vem cada imagem que não fizeste tu. A imagem provisória, por exemplo, "vem dos materiais da disciplina". Apaga também a frase de instruções dessa secção.

   Nos outros campos, escreve "Ainda por fazer." Guarda o ficheiro.

8. Guarda o README num commit à parte:

   ```bash
   git add README.md
   git commit -m "Acrescenta o README do site"
   git status
   ```

   O que deves ver: `1 file changed` e um número de linhas, e depois `nothing to commit, working tree clean`.

9. Corre o `git log --oneline`. O que deves ver: dois commits, `Acrescenta o README do site` em cima e `Guarda a primeira versão do site` em baixo.

10. No `registo.md`, por baixo do que escreveste na fase 8, escreve o título `### O meu site` e cola a resposta do `git log --oneline` da pasta do site. Por baixo, explica por palavras tuas, em duas ou três frases, a pasta de trabalho, a área de preparação e o histórico. Guarda o `registo.md`.

### Paragem 11

O teu site é um repositório, com a tua identidade, o `.gitignore`, o README e dois commits. O `registo.md` tem os dois históricos e a tua explicação das três zonas.

Pensa antes de continuares: daqui em diante, quando mudares o teu site, o que fazes para guardar a mudança? A resposta: vês o `git status` e o `git diff`, e preparas os ficheiros dessa mudança com `git add`. Confirmas com o `git diff --staged` e fazes um commit com uma mensagem que diz o que mudou.

## Se alguma coisa falhar

Primeiro, três verificações rápidas:

1. Estás na pasta certa? Olha para o fim da linha do terminal. Se não for a pasta onde queres trabalhar, abre-a no VS Code, com Open Folder, e abre um terminal novo.
2. O que diz o `git status`? Lê-o antes de tentares outra coisa, e lê também as sugestões entre parênteses.
3. Guardaste o ficheiro? No VS Code, um ficheiro por guardar tem uma bolinha no separador, e o Git só vê o que está guardado.

### O terminal diz que git não é reconhecido

A mensagem começa por `git : The term 'git' is not recognized`. Fecha o VS Code e volta a abri-lo, porque um VS Code aberto antes da instalação do Git não o encontra. Se continuar, chama o professor.

### O terminal acaba noutra pasta

A linha do terminal não acaba em `treino-git` nem no nome do teu site, porque o VS Code tem outra pasta aberta. Abre a pasta certa, com Open Folder, no menu File, e abre um terminal novo. Não corras o `git init` noutra pasta.

### fatal: not a git repository

Se aparece na fase 2, passo 1, ou na fase 11, passo 2, está certo. Noutro passo, o terminal está numa pasta que não é um repositório, ou o `git init` ainda não foi feito nela. Vê a primeira verificação rápida.

### Author identity unknown

O commit falhou porque a pasta não tem identidade. A mensagem do Git sugere os comandos com `--global`: não os copies. Faz a fase 3 nesta pasta, sem `--global`, e repete o commit.

### O terminal enche-se de linhas começadas por ~

Escreveste o `git commit` sem o `-m`, e o Git abriu um editor no terminal. Carrega em Esc, escreve `:q!` e carrega em Enter. O commit é cancelado. Repete-o com o `-m` e a mensagem entre aspas. Se em vez disso se abriu um separador `COMMIT_EDITMSG` no VS Code, fecha-o sem escrever nada.

### A última linha do terminal é : ou (END)

A resposta do Git não cabia no terminal e está a ser mostrada aos bocados. Anda com as setas e sai com a tecla `q`.

### fatal: could not resolve HEAD

Usaste o `git restore --staged` antes do primeiro commit. Nesse momento, tira um ficheiro da área de preparação com `git rm --cached` e o nome do ficheiro, como sugere o `git status`.

### fatal: pathspec '...' did not match any files

O `git add` não encontrou um dos nomes que escreveste, e não preparou nenhum, nem os outros. O nome está mal escrito, ou tem espaços ou acentos. Copia o nome tal como o `git status` o mostra e repete o `git add`. Se o nome tiver espaços ou acentos, muda-o primeiro, como no passo 1 de "Preparar o projeto".

### warning: in the working copy of '...', LF will be replaced by CRLF

No Windows, o Git avisa que vai mudar a forma como as linhas acabam nesse ficheiro. Não é um erro, e o ficheiro não se estraga. Continua.

### O commit não guarda nada

O `git commit` responde `nothing added to commit` ou `no changes added to commit`. A área de preparação está vazia: faz o `git add` do ficheiro e repete o commit.

### O git status mostra pastas que não são do site

Aparecem pastas como `01-frontend/` e `exemplos/`, ou `Desktop/` e `Downloads/`, porque o `git init` foi feito com outra pasta aberta no VS Code. Não faças nenhum commit e chama o professor.

### O registo.md não aparece no painel Explorer

Está certo: o `registo.md` está ao lado da pasta do site, e não dentro dela, e por isso também não entra no Git. Abre-o com Open Recent, no menu File, ou com Open File..., no mesmo menu, indo à pasta onde está a pasta do teu site.

## Desafios

1. Na cópia de treino, muda uma frase no `index.html` e outra no `torneios.html`. Guarda-as em dois commits, um para cada página, só com o painel Source Control. Pista: cada commit leva só o que está em Staged Changes no momento em que carregas em Commit.
2. Na cópia de treino, descobre que commits mudaram o `torneios.html`. Pista: o `git log --oneline` aceita, no fim, o nome de um ficheiro.

## Antes de terminares

- [ ] A pasta `treino-git` é um repositório com pelo menos três commits, com a identidade `Aluno de Treino`.
- [ ] A pasta do teu site é um repositório com dois commits, com o teu nome e o email `example.com`.
- [ ] A pasta do teu site tem o `.gitignore` e o `README.md`, e o `git status` diz `nothing to commit, working tree clean`.
- [ ] O `registo.md` tem os dois históricos curtos e a tua explicação das três zonas.
- [ ] Nenhum comando de identidade levou `--global`.
- [ ] Entregaste o `registo.md` como o professor indicou.

![Rodapé](../../imagens/rodape.png)
