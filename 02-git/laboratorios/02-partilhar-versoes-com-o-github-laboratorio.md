![Cabeçalho](../../imagens/cabecalho.png)

# Laboratório: Partilhar versões com o GitHub

## O que vais construir

Pões o teu site no GitHub, com o histórico inteiro, e ligas o portátil à tua conta com uma chave SSH. Primeiro treinas numa cópia da pasta do site, com uma pasta que faz de GitHub, como se trabalhasses na escola e em casa. Depois fazes o mesmo no GitHub e crias a tua página pessoal. Os exemplos usam o clube de xadrez: escreve os teus nomes e as tuas mensagens. No fim, a pasta que tem o teu site fica assim:

```text
clube-de-xadrez/        o teu site, agora também no GitHub
github-de-treino.git/   a pasta que faz de GitHub no treino
treino-casa/            o clone, que faz de computador de casa
treino-escola/          a cópia de treino, que faz de computador da escola
treino-git/             a cópia de treino do laboratório do tema 01 do Git
registo.md
```

1. [Fase 1: Para treinar, uma pasta faz de GitHub](#fase-1-para-treinar-uma-pasta-faz-de-github)
2. [Fase 2: O remoto tem um nome e um endereço](#fase-2-o-remoto-tem-um-nome-e-um-endereço)
3. [Fase 3: O git push envia os commits](#fase-3-o-git-push-envia-os-commits)
4. [Fase 4: Clonar copia um repositório inteiro](#fase-4-clonar-copia-um-repositório-inteiro)
5. [Fase 5: O git fetch traz os commits sem mexer nos teus ficheiros](#fase-5-o-git-fetch-traz-os-commits-sem-mexer-nos-teus-ficheiros)
6. [Fase 6: O git pull junta os commits do remoto aos teus](#fase-6-o-git-pull-junta-os-commits-do-remoto-aos-teus)
7. [Fase 7: Antes de começar, pull; no fim, push](#fase-7-antes-de-começar-pull-no-fim-push)
8. [Fase 8: O git commit --amend substitui o último commit](#fase-8-o-git-commit---amend-substitui-o-último-commit)
9. [Fase 9: O painel Source Control com um remoto](#fase-9-o-painel-source-control-com-um-remoto)
10. [Fase 10: A conta e o email privado](#fase-10-a-conta-e-o-email-privado)
11. [Fase 11: A chave cria-se uma vez, com uma frase-passe](#fase-11-a-chave-cria-se-uma-vez-com-uma-frase-passe)
12. [Fase 12: Um repositório no GitHub](#fase-12-um-repositório-no-github)
13. [Fase 13: O repositório escolhe a chave](#fase-13-o-repositório-escolhe-a-chave)
14. [Fase 14: A página pessoal](#fase-14-a-página-pessoal)

## O que precisas

- O VS Code e o Git: confirma com `git --version`.
- A pasta do teu site no Git, com o `registo.md` ao lado. Se ainda não está no Git, faz primeiro a [fase 11 do laboratório do tema 01 do Git](01-guardar-versoes-com-o-git-laboratorio.md#fase-11-o-teu-site-no-git).
- Um email que consigas abrir na aula, o da escola ou um teu, para criar a conta do GitHub.
- Internet, a partir da fase 10.

## Preparar o projeto

1. No VS Code, abre a pasta do teu site, com Open Folder..., no menu File, e abre um terminal, com New Terminal, no menu Terminal. Corre o `git status`. O que deves ver: no fim, `nothing to commit, working tree clean`. Se aparecerem ficheiros mudados, guarda-os primeiro num commit, como no tema 01.

2. Corre o `git remote -v`. O que deves ver: nenhuma resposta, só a linha seguinte do terminal. O site ainda não tem remoto, como devia.

3. Faz a cópia de treino. No Explorador de Ficheiros, vai à pasta que tem o teu site e o `registo.md`. Carrega na pasta do site e copia-a com Ctrl+C e Ctrl+V. Muda o nome da cópia para `treino-escola`, com a tecla F2. No Mac, no Finder, carrega com o botão direito na pasta, escolhe Duplicar e muda o nome com Enter. A cópia leva a pasta `.git` escondida, e por isso é um repositório com o histórico inteiro do site.

4. Abre a cópia no VS Code, com Open Folder... e a pasta `treino-escola`, e abre um terminal novo. O que deves ver: a linha do terminal acaba em `treino-escola`.

5. A cópia trouxe a tua identidade, e no treino usas uma inventada. Guarda-a só nesta pasta e confirma:

   ```bash
   git config user.name "Aluno de Treino"
   git config user.email "aluno.treino@example.com"
   git config user.name
   ```

   O que deves ver: `Aluno de Treino`. Os commits antigos ficam com o teu nome, e os que fizeres no treino levam o nome inventado.

## Fase 1: Para treinar, uma pasta faz de GitHub

Crias, ao lado da pasta do site, a pasta que faz de GitHub no treino: um repositório só com o histórico, sem pasta de trabalho. Rever: [Para treinar, uma pasta faz de GitHub](../02-partilhar-versoes-com-o-github.md#para-treinar-uma-pasta-faz-de-github).

1. No terminal da `treino-escola`, cria a pasta, com o `../` para ela ficar ao lado e não dentro:

   ```bash
   git init --bare -b main ../github-de-treino.git
   ```

   O que deves ver: `Initialized empty Git repository in` e o caminho, acabado em `github-de-treino.git/`. Se o caminho acabar em `treino-escola/github-de-treino.git/`, esqueceste o `../`: vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

2. Confirma no Explorador de Ficheiros. O que deves ver: ao lado da pasta do teu site e da `treino-escola`, a pasta `github-de-treino.git`. Lá dentro há pastas como `objects` e `refs`, e nenhuma página do site. Não mexas em nada lá dentro.

### Paragem 1

A pasta que faz de GitHub existe, ao lado da cópia de treino, ainda sem commits.

Pensa antes de continuares: porque é que não abres a `github-de-treino.git` no VS Code para editar as páginas? A resposta: não tem pasta de trabalho, só o histórico. As páginas editam-se num repositório com pasta de trabalho, e chegam ao remoto num envio.

## Fase 2: O remoto tem um nome e um endereço

Dizes à cópia de treino onde está o remoto, com o nome `origin`. Rever: [O remoto tem um nome e um endereço](../02-partilhar-versoes-com-o-github.md#o-remoto-tem-um-nome-e-um-endereço).

1. Junta o remoto e vê os remotos da pasta:

   ```bash
   git remote add origin ../github-de-treino.git
   git remote -v
   ```

   O que deves ver:

   ```text
   origin	../github-de-treino.git (fetch)
   origin	../github-de-treino.git (push)
   ```

   O mesmo endereço aparece duas vezes, um para trazer e outro para enviar. Se aparecer `error: remote origin already exists.`, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

### Paragem 2

A cópia de treino tem um remoto, chamado `origin`.

Pensa antes de continuares: o `git remote add` enviou algum commit? A resposta: não. Só guardou o nome e o endereço do remoto. A pasta que faz de GitHub continua vazia.

## Fase 3: O git push envia os commits

Envias o histórico inteiro da cópia para o remoto de treino e vês o que muda no `git status` e no `git log`. Rever: [O git push envia os commits](../02-partilhar-versoes-com-o-github.md#o-git-push-envia-os-commits).

1. Envia, ligando o teu `main` ao do remoto:

   ```bash
   git push -u origin main
   ```

   O que deves ver, no fim:

   ```text
   To ../github-de-treino.git
    * [new branch]      main -> main
   branch 'main' set up to track 'origin/main'.
   ```

   Antes destas, aparecem linhas com contagens, como `Writing objects: 100% (25/25)`, com os números do teu site. O teu `main` foi para o `main` do remoto, e os dois ficaram ligados.

2. Corre o `git status`. O que deves ver: a linha `Your branch is up to date with 'origin/main'.`, a seguir a `On branch main`. O remoto tem tudo o que tu tens.

3. Corre o `git log --oneline`. O que deves ver, no exemplo:

   ```text
   fc1af33 (HEAD -> main, origin/main) Torna o foco visível nas ligações
   283dc75 Mostra a coleção em cartões
   f0f283e Arruma o cabeçalho e o menu com o Flexbox
   5d8d9a3 Acrescenta as cores e a letra do site
   c624bc5 Acrescenta o README do site
   dbbb345 Guarda a primeira versão do site
   ```

   O `main` e o `origin/main` estão no commit mais recente. Os teus identificadores e as tuas mensagens vão ser outros.

### Paragem 3

O remoto de treino tem o histórico inteiro do teu site.

Pensa antes de continuares: porque é que o `-u origin main` só faz falta da primeira vez? A resposta: o `-u` ligou o teu `main` ao `main` do remoto. Das outras vezes, o Git já sabe para onde enviar, e basta `git push`.

## Fase 4: Clonar copia um repositório inteiro

Clonas o remoto de treino para uma pasta nova, que faz de computador de casa, e abre-la numa segunda janela do VS Code. Rever: [Clonar copia um repositório inteiro](../02-partilhar-versoes-com-o-github.md#clonar-copia-um-repositório-inteiro).

1. No terminal da `treino-escola`, clona o remoto para uma pasta ao lado:

   ```bash
   git clone ../github-de-treino.git ../treino-casa
   ```

   O que deves ver:

   ```text
   Cloning into '../treino-casa'...
   done.
   ```

2. Abre uma segunda janela do VS Code, com New Window, no menu File. Nessa janela, abre a pasta `treino-casa`, com Open Folder..., e abre um terminal. O que deves ver: a linha do terminal acaba em `treino-casa`. A partir daqui, a janela da `treino-escola` faz de computador da escola, e a da `treino-casa` de computador de casa. Mudas de janela com Alt+Tab, ou Cmd+Tab no Mac.

3. No terminal da `treino-casa`, corre o `git log --oneline`. O que deves ver: os mesmos commits da escola, com `(HEAD -> main, origin/main, origin/HEAD)` no mais recente. O clone trouxe o histórico inteiro.

   Corre também o `git remote -v`. O que deves ver: o `origin`, com o caminho completo da pasta que faz de GitHub. O caminho passa pela `treino-escola`, porque clonaste a partir de lá. Estás na janela certa: o fim da linha do terminal continua a dizer `treino-casa`.

4. O clone não trouxe a identidade. Guarda a do treino, também nesta pasta:

   ```bash
   git config user.name "Aluno de Treino"
   git config user.email "aluno.treino@example.com"
   git config user.name
   ```

   O que deves ver: `Aluno de Treino`.

### Paragem 4

Tens dois repositórios locais, a escola e a casa, ligados ao mesmo remoto, com o mesmo histórico.

Pensa antes de continuares: que diferença há entre a `treino-casa` e uma cópia descarregada em ZIP? A resposta: o clone tem a pasta `.git`, com o histórico e o remoto já configurado. O ZIP só traz os ficheiros.

## Fase 5: O git fetch traz os commits sem mexer nos teus ficheiros

Fazes um commit em casa e envia-lo. Depois, na escola, trazes esse commit com o `git fetch` e vês que os teus ficheiros não mudaram. Rever: [O git fetch traz os commits sem mexer nos teus ficheiros](../02-partilhar-versoes-com-o-github.md#o-git-fetch-traz-os-commits-sem-mexer-nos-teus-ficheiros).

1. Na janela de casa, no `README.md`, troca o "Ainda por fazer." da secção "Funcionalidades" por uma frase sobre o teu site. No exemplo: "Duas páginas: a inicial, com as peças do xadrez em cartões, e a dos torneios." Guarda o ficheiro.

2. Faz o commit e envia:

   ```bash
   git add README.md
   git commit -m "Descreve as funcionalidades no README"
   git status
   git push
   ```

   O que deves ver: antes do envio, o `git status` diz `Your branch is ahead of 'origin/main' by 1 commit.`. O `git push` acaba numa linha como `fc1af33..a7f3483  main -> main`, com os teus identificadores. O `main` do remoto avançou um commit.

3. Muda para a janela da escola. Antes de correres o `git status`, prevê: o portátil da escola já sabe do commit de casa? Depois corre-o. O que deves ver: `Your branch is up to date with 'origin/main'.`. Esta resposta está desatualizada: o `git status` não foi ao remoto, e compara com o que o portátil sabia da última vez.

4. Traz o que há no remoto e vê o estado outra vez:

   ```bash
   git fetch
   git status
   ```

   O que deves ver: o `git fetch` acaba numa linha como `fc1af33..a7f3483  main       -> origin/main`. O `git status` passa a dizer `Your branch is behind 'origin/main' by 1 commit, and can be fast-forwarded.`.

5. Abre o `README.md` na janela da escola. O que deves ver: a secção "Funcionalidades" ainda diz "Ainda por fazer.". O commit está na pasta `.git`, mas ainda não chegou aos teus ficheiros.

6. Vê o que esse commit muda:

   ```bash
   git diff main origin/main
   ```

   O que deves ver: o `README.md`, com a linha "Ainda por fazer." com `-` à frente e a tua frase com `+`. Se o terminal acabar em `:` ou `(END)`, carrega em `q` para sair.

### Paragem 5

A escola sabe que o remoto tem um commit novo, e os ficheiros da escola ainda estão como estavam.

Pensa antes de continuares: depois do `git fetch`, porque é que o `README.md` da escola ainda não mudou? A resposta: o `git fetch` só trouxe o commit para a pasta `.git` e mudou o `origin/main`. Os teus ficheiros e o teu `main` só mudam com o `git pull`.

## Fase 6: O git pull junta os commits do remoto aos teus

Juntas o commit de casa aos ficheiros da escola. Rever: [O git pull junta os commits do remoto aos teus](../02-partilhar-versoes-com-o-github.md#o-git-pull-junta-os-commits-do-remoto-aos-teus).

1. Na janela da escola, corre o `git pull`. O que deves ver, no exemplo:

   ```text
   Updating fc1af33..a7f3483
   Fast-forward
    README.md | 2 +-
    1 file changed, 1 insertion(+), 1 deletion(-)
   ```

   O teu `main` avançou até ao commit de casa, sem precisar de um commit novo, porque a escola não tinha commits diferentes.

2. Olha para o `README.md` aberto no VS Code. O que deves ver: a tua frase na secção "Funcionalidades". O VS Code mostra logo o ficheiro mudado.

3. Corre o `git log --oneline`. O que deves ver: o commit de casa em cima, com `(HEAD -> main, origin/main, origin/HEAD)`.

### Paragem 6

A escola e a casa têm o mesmo histórico e os mesmos ficheiros.

Pensa antes de continuares: se correres o `git pull` outra vez, o que responde? A resposta: `Already up to date.`, porque o remoto não tem nada que a escola não tenha.

## Fase 7: Antes de começar, pull; no fim, push

Esqueces de propósito o `git push` no fim de um trabalho, para veres um envio recusado, e resolve-lo. Rever: [Antes de começar, pull; no fim, push](../02-partilhar-versoes-com-o-github.md#antes-de-começar-pull-no-fim-push).

1. Na janela da escola, na tua segunda página, `torneios.html` no exemplo, acrescenta uma frase a seguir ao primeiro parágrafo do `main`, e guarda. No exemplo:

   ```html
   <p>As inscrições para o torneio deste ano abrem em janeiro.</p>
   ```

   Faz o commit, com o nome da tua página no `git add`, e não envies:

   ```bash
   git add torneios.html
   git commit -m "Acrescenta a data das inscrições do torneio"
   ```

2. Na janela de casa, começa pela rotina, com o `git pull`. O que deves ver: `Already up to date.`. O commit da escola não foi enviado, e por isso o remoto não o tem.

3. Ainda em casa, muda uma frase do `index.html`, que é outra página. No exemplo, a sala dos encontros passa de 12 para 14. Guarda, faz o commit e envia:

   ```bash
   git add index.html
   git commit -m "Muda a sala dos encontros"
   git push
   ```

   O que deves ver: o `git push` acaba em `main -> main`.

4. Na janela da escola, corre o `git push`. O que deves ver:

   ```text
   To ../github-de-treino.git
    ! [rejected]        main -> main (fetch first)
   error: failed to push some refs to '../github-de-treino.git'
   ```

   A seguir vêm linhas `hint`, que sugerem um `git pull`. O remoto tem o commit de casa, que a escola não tem, e o Git recusou o envio para não o apagar.

5. Junta as duas histórias:

   ```bash
   git pull --no-rebase --no-edit
   ```

   O que deves ver, no fim:

   ```text
   Merge made by the 'ort' strategy.
    index.html | 2 +-
    1 file changed, 1 insertion(+), 1 deletion(-)
   ```

   O Git trouxe o commit de casa e fez um commit de junção, que tem o teu commit e o de casa antes dele. Se aparecer `CONFLICT` ou `fatal: Need to specify how to reconcile divergent branches.`, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

6. Corre o `git log --oneline -4`, que mostra só os quatro últimos commits. O que deves ver, no exemplo:

   ```text
   c6316bb (HEAD -> main) Merge branch 'main' of ../github-de-treino
   e067f7c (origin/main, origin/HEAD) Muda a sala dos encontros
   4086a04 Acrescenta a data das inscrições do torneio
   a7f3483 Descreve as funcionalidades no README
   ```

7. Envia outra vez e confirma:

   ```bash
   git push
   git status
   ```

   O que deves ver: o `git push` acaba em `main -> main`, e o `git status` diz `Your branch is up to date with 'origin/main'.`.

8. Na janela de casa, corre o `git pull`. O que deves ver: `Fast-forward` e `torneios.html | 1 +`. A casa ficou com a data das inscrições.

### Paragem 7

O remoto, a escola e a casa têm o mesmo histórico, com o commit de junção.

Pensa antes de continuares: que passo da rotina faltou na escola, e o que teria evitado a recusa? A resposta: o `git push` no fim do trabalho, depois do commit das inscrições. Com ele, o `git pull` de casa tinha trazido esse commit antes da mudança da sala.

## Fase 8: O git commit --amend substitui o último commit

Fazes um commit com um erro na mensagem e corrige-lo antes de o enviar. Rever: [O git commit --amend substitui o último commit](../02-partilhar-versoes-com-o-github.md#o-git-commit---amend-substitui-o-último-commit).

1. Na janela da escola, em `index.html`, acrescenta um item a uma lista e guarda. No exemplo, `<li>Um lápis.</li>`, na lista "O que precisas de trazer". Faz o commit com uma mensagem sem acentos, de propósito:

   ```bash
   git add index.html
   git commit -m "Acrescenta um lapis a lista"
   git status
   ```

   O que deves ver: o `git status` diz `Your branch is ahead of 'origin/main' by 1 commit.`. O commit ainda não foi enviado, e por isso podes corrigi-lo.

2. Corrige a mensagem:

   ```bash
   git commit --amend -m "Acrescenta um lápis à lista do que trazer"
   ```

   O que deves ver: uma linha como `[main 9a78d65] Acrescenta um lápis à lista do que trazer`, com um identificador novo, e uma linha `Date`, com a data do commit original.

3. Confirma e envia:

   ```bash
   git log --oneline -2
   git push
   ```

   O que deves ver: no `git log`, só o commit com a mensagem certa, em cima do commit de junção. O commit com a mensagem errada desapareceu. O `git push` acaba em `main -> main`.

### Paragem 8

O remoto tem o commit com a mensagem certa, e nunca teve o errado.

Pensa antes de continuares: se só reparasses no erro depois do `git push`, o que fazias? A resposta: um commit novo com a correção, se fosse preciso. Depois do envio, o `--amend` fazia o envio seguinte ser recusado, porque o remoto já tinha o commit antigo.

## Fase 9: O painel Source Control com um remoto

Na janela de casa, recebes e envias commits só com o rato, no painel Source Control. Rever: [O painel Source Control com um remoto](../02-partilhar-versoes-com-o-github.md#o-painel-source-control-com-um-remoto).

1. Na janela de casa, abre o painel Source Control, com Ctrl+Shift+G. Na barra do fundo da janela, à esquerda, ao lado de `main`, carrega no ícone das duas setas em círculo, Synchronize Changes. Se o VS Code perguntar `This action will pull and push commits from and to "origin/main".`, carrega em OK. Nunca carregues em OK, Don't Show Again, porque grava a escolha para todos os colegas do portátil. O que deves ver: o `index.html` de casa passa a ter o item que acrescentaste na fase 8. O VS Code fez um `git pull`.

   A seguir, o VS Code pode perguntar `Would you like Visual Studio Code to periodically run "git fetch"?`. Carrega em No: com o GitHub, ia pedir-te a frase-passe de poucos em poucos minutos.

2. Na tua segunda página, a seguir à frase das inscrições, acrescenta outra frase e guarda. No exemplo, `<p>Os jogos são à melhor de três partidas.</p>`. No painel, passa o rato pelo ficheiro, no grupo Changes, e carrega no `+`. Na caixa Message, escreve `Acrescenta como se jogam as partidas do torneio` e carrega em Commit. O que deves ver: um botão azul, Sync Changes, com o número 1 e uma seta para cima. Há um commit por enviar.

3. Carrega em Sync Changes, e em OK se aparecer a pergunta. O que deves ver: na barra do fundo, deixa de haver números ao lado das setas.

4. Na secção Graph do painel, procura o commit que acabaste de fazer. O que deves ver: ao lado dele, a etiqueta do `main` e a do `origin/main`. O remoto tem o teu commit.

5. Na janela da escola, corre o `git pull` no terminal. O que deves ver: um `Fast-forward`, com o `torneios.html`. O que enviaste com o rato é igual ao que se envia com o terminal.

### Paragem 9

A escola, a casa e a pasta que faz de GitHub têm o mesmo histórico, e um dos commits foi enviado só com o painel.

Pensa antes de continuares: o que faz o botão de sincronizar, em comandos? A resposta: um `git pull` e depois um `git push`.

## Fase 10: A conta e o email privado

Crias a tua conta do GitHub e vais buscar o email privado que vais usar nos commits do site. A partir daqui, precisas de Internet. Rever: [A conta e o email privado](../02-partilhar-versoes-com-o-github.md#a-conta-e-o-email-privado).

1. Abre uma janela privada do browser, com Ctrl+Shift+N, no Chrome e no Edge, ou Cmd+Shift+N no Mac. É nesta janela que usas o GitHub até ao fim do laboratório. Abre `github.com` e carrega em Sign up.

2. Preenche o email, uma palavra-passe e o nome de utilizador. O GitHub diz, por baixo de cada campo, se o valor serve. Escolhe um nome de utilizador sem a data de nascimento, a escola nem a morada, e uma palavra-passe que não uses em mais nenhum sítio. Escolhe o país e deixa desligada a caixa de receber novidades por email. Se o browser se oferecer para guardar a palavra-passe, aqui ou no email, carrega em Nunca, ou Never. Senão, ficava no portátil para o colega seguinte. Continua até ao fim do registo. O GitHub pede que resolvas um pequeno puzzle, para confirmar que és uma pessoa, e que escrevas o código que mandou para o teu email. Abre o email noutro separador da mesma janela privada.

   O que deves ver: a página inicial do GitHub, com a tua conta aberta. Se o GitHub disser que o nome de utilizador já existe, escolhe outro.

3. Vai às definições do email: carrega na tua imagem, no canto de cima, à direita, escolhe Settings e, no menu da esquerda, Emails. Confirma que a opção "Keep my email addresses private" está marcada e, se não estiver, marca-a. O que deves ver: por baixo dela, uma frase com o teu email privado, acabado em `@users.noreply.github.com`.

4. Abre o `registo.md`, com Open Recent, no menu File. Confirma o caminho, como no tema 01, porque o portátil pode mostrar o de outro colega. Escreve no fim o título `## Laboratório do GitHub`. Por baixo, escreve o teu nome de utilizador e o teu email privado. A palavra-passe nunca entra no registo. Guarda o `registo.md`.

### Paragem 10

Tens uma conta do GitHub, com o email privado à vista, e o registo tem o teu nome de utilizador.

Pensa antes de continuares: porque é que, na escola, o GitHub se abre numa janela privada? A resposta: quando a fechas, o browser esquece o início de sessão. O colega que usar o portátil a seguir não fica com a tua conta aberta.

## Fase 11: A chave cria-se uma vez, com uma frase-passe

Crias a tua chave SSH no portátil e copias a chave pública para a tua conta do GitHub. Rever: [A chave cria-se uma vez, com uma frase-passe](../02-partilhar-versoes-com-o-github.md#a-chave-cria-se-uma-vez-com-uma-frase-passe).

1. Fecha a janela do VS Code da `treino-casa`. Na outra janela, abre a pasta do teu site, com Open Folder..., e abre um terminal novo. O que deves ver: a linha do terminal acaba no nome da pasta do teu site.

2. Escolhe a tua frase-passe, com quatro palavras ou mais. Não a escrevas em lado nenhum: vais escrevê-la só no terminal.

3. Cria a pasta das chaves:

   ```powershell
   New-Item -ItemType Directory -Force $HOME\.ssh
   ```

   O que deves ver: uma pequena tabela com a pasta `.ssh`. No Mac, o comando é `mkdir -p ~/.ssh`, e não responde nada.

4. Cria a chave. No lugar de `UTILIZADOR`, aqui e nos passos seguintes, escreve o teu nome de utilizador do GitHub:

   ```powershell
   ssh-keygen -t ed25519 -f $HOME\.ssh\gh-UTILIZADOR -C "UTILIZADOR"
   ```

   No Mac, o caminho é `~/.ssh/gh-UTILIZADOR`. O `ssh-keygen` pede a frase-passe, com `Enter passphrase`, e depois outra vez, com `Enter same passphrase again`. Escreve-a nas duas, sem ver nada no ecrã, e carrega em Enter. Não a deixes vazia: uma chave sem frase-passe fica aberta para quem usar o portátil. Se aparecer `Passphrases do not match.`, as duas não batem certo: escreve-a outra vez nas duas. O que deves ver: `Your identification has been saved in` e `Your public key has been saved in`, com os caminhos das duas chaves, e um quadrado de símbolos. Se aparecer `Overwrite (y/n)?`, escreve `n` e vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

5. Mostra a chave pública:

   ```powershell
   Get-Content $HOME\.ssh\gh-UTILIZADOR.pub
   ```

   No Mac, o comando é `cat ~/.ssh/gh-UTILIZADOR.pub`. O que deves ver: uma só linha, que começa por `ssh-ed25519` e acaba no teu nome de utilizador. Seleciona-a toda com o rato, no terminal, e copia-a com Ctrl+C, ou Cmd+C no Mac.

6. No GitHub, na janela privada, carrega na tua imagem, escolhe Settings e, no menu da esquerda, SSH and GPG keys. Carrega em New SSH key. Em Title, escreve "Portátil da escola". Em Key type, deixa Authentication Key. Em Key, cola a linha. Carrega em Add SSH key. Se o GitHub pedir outra vez a palavra-passe, escreve-a.

   O que deves ver: a chave na lista, com o título "Portátil da escola" e um código que começa por `SHA256:`.

### Paragem 11

A chave pública está na tua conta do GitHub, e a chave privada está no portátil, fechada com a tua frase-passe.

Pensa antes de continuares: que ficheiro nunca sai do portátil, e porquê? A resposta: o `gh-UTILIZADOR`, sem `.pub`, que é a chave privada. Quem o tivesse, e soubesse a frase-passe, enviava commits como se fosse tu.

## Fase 12: Um repositório no GitHub

Crias no GitHub o repositório do teu site, vazio, e copias o endereço SSH dele. Rever: [Um repositório no GitHub](../02-partilhar-versoes-com-o-github.md#um-repositório-no-github).

1. No GitHub, carrega no botão `+`, no canto de cima, e escolhe New repository. Em Repository name, escreve o nome da pasta do teu site, como `clube-de-xadrez`. Escolhe Public. Deixa desligadas as opções do README, do `.gitignore` e da licença. Carrega em Create repository.

   O que deves ver: a página Quick setup, com o endereço do repositório.

2. Na caixa do endereço, carrega em SSH, ao lado de HTTPS. O que deves ver: um endereço como `git@github.com:UTILIZADOR/clube-de-xadrez.git`, com o teu nome de utilizador. Copia-o, com o botão ao lado dele.

### Paragem 12

O repositório do teu site existe no GitHub, vazio.

Pensa antes de continuares: porque é que se deixa desligada a opção do README? A resposta: o teu site já tem README. Com ela, o GitHub fazia um primeiro commit que o teu repositório não tem, e o teu primeiro envio era recusado.

## Fase 13: O repositório escolhe a chave

Na pasta do teu site, trocas o email pelo privado, escolhes a chave e envias o site para o GitHub. Rever: [O repositório escolhe a chave](../02-partilhar-versoes-com-o-github.md#o-repositório-escolhe-a-chave).

1. No terminal da pasta do site, troca o email do autor pelo teu email privado, que está no `registo.md`, e confirma:

   ```bash
   git config user.email "12345678+UTILIZADOR@users.noreply.github.com"
   git config user.email
   ```

   No primeiro comando, escreve o teu email privado no lugar do exemplo, com o teu número e o teu nome de utilizador. O que deves ver: o teu email privado.

2. Escolhe a chave que este repositório usa:

   ```bash
   git config core.sshCommand "ssh -i ~/.ssh/gh-UTILIZADOR -o IdentitiesOnly=yes"
   ```

   O que deves ver: nada. Esta linha escreve-se igual no Windows e no Mac, com `~/.ssh`.

3. Copia outra vez o endereço SSH na página Quick setup, no GitHub. Junta o remoto, com esse endereço, e confirma:

   ```bash
   git remote add origin git@github.com:UTILIZADOR/clube-de-xadrez.git
   git remote -v
   ```

   O que deves ver: o `origin`, com o teu endereço, duas vezes.

4. Envia o site:

   ```bash
   git push -u origin main
   ```

   Na primeira ligação, o SSH pergunta `Are you sure you want to continue connecting (yes/no/[fingerprint])?`. Confirma que a linha `ED25519 key fingerprint is` diz `SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU`, escreve `yes` e carrega em Enter. Depois, aparece uma linha que começa por `Enter passphrase for key`: escreve a tua frase-passe, sem ver nada, e carrega em Enter. Se o envio não pedir a frase-passe, chama o professor.

   O que deves ver: as linhas com contagens, e no fim `main -> main` e `branch 'main' set up to track 'origin/main'.`. Se aparecer `Permission denied (publickey)` ou `Repository not found`, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

5. No GitHub, recarrega a página do repositório, com F5. O que deves ver: os ficheiros do teu site, e por baixo deles o README. No topo da lista dos ficheiros está o último commit, com o identificador curto. Corre o `git log --oneline -1` no terminal e confirma que o identificador é o mesmo.

6. No `README.md` do site, na linha "Como guardaste as versões", acrescenta onde está o repositório. No exemplo: "Guardo as versões com o Git, com um commit por alteração, e envio-as para o GitHub, em https://github.com/UTILIZADOR/clube-de-xadrez." Guarda o ficheiro.

7. Faz este commit no painel Source Control: carrega no `+` do `README.md`, escreve na caixa Message `Acrescenta ao README o endereço do GitHub` e carrega em Commit. Depois carrega em Sync Changes, e em OK se aparecer a pergunta. O que deves ver: uma caixa no topo da janela, com a palavra `Passphrase`. Escreve a tua frase-passe e carrega em Enter. A caixa aparece duas vezes, uma para trazer e outra para enviar: escreve a frase-passe nas duas. No fim, deixa de haver números ao lado das setas, na barra do fundo.

8. No GitHub, recarrega a página do repositório. O que deves ver: o README com a frase nova, e o último commit com o teu nome de utilizador. O GitHub ligou o commit à tua conta pelo email privado.

9. No `registo.md`, por baixo do teu nome de utilizador, escreve o endereço do repositório do site e cola a resposta do `git log --oneline -3`. Por baixo, explica por palavras tuas, em duas frases, a diferença entre o `git fetch` e o `git pull`. Guarda o `registo.md`.

### Paragem 13

O teu site está no GitHub, com o histórico inteiro, e o README diz onde. O `registo.md` tem o endereço, o histórico curto e a tua explicação.

Pensa antes de continuares: daqui em diante, quando mudares o site na aula, que comandos fazes do princípio ao fim? A resposta: o `git pull` no início, com a tua frase-passe. Depois, o `git status`, o `git add`, o `git diff --staged` e o commit de cada alteração. No fim, o `git push`, outra vez com a frase-passe.

## Fase 14: A página pessoal

Crias o repositório especial da tua página pessoal e escreves nele uma apresentação do teu trabalho, sem dados pessoais. Rever: [A página pessoal](../02-partilhar-versoes-com-o-github.md#a-página-pessoal).

1. No GitHub, carrega no `+` e em New repository. Em Repository name, escreve o teu nome de utilizador, exatamente igual. O que deves ver: uma mensagem do GitHub a dizer que este repositório é especial e que o README dele aparece no teu perfil.

2. Escolhe Public e, desta vez, liga a opção do README. Carrega em Create repository. O que deves ver: o repositório, com um README que o GitHub escreveu.

3. Na página do repositório, carrega no README e depois no lápis, Edit this file. Apaga todo o texto que o GitHub escreveu. Escreve três ou quatro frases sobre o teu trabalho: o que estás a aprender e o teu site, com o endereço dele. Não escrevas o teu nome completo, a escola, a localidade, a idade, uma fotografia tua nem contactos.

4. Carrega em Commit changes... e, na caixa que abre, escreve a mensagem `Apresenta o meu trabalho na página pessoal`. Carrega outra vez em Commit changes. O que deves ver: o README com o teu texto. Fizeste um commit no GitHub, sem passar pelo portátil.

5. Carrega na tua imagem, no canto de cima, e escolhe Your profile. O que deves ver: a tua página pessoal, com o README no topo e o repositório do site na lista.

### Paragem 14

A tua página pessoal apresenta o teu trabalho, e o repositório do site aparece nela.

Pensa antes de continuares: o que não pode estar na tua página pessoal? A resposta: os teus dados pessoais, como o nome completo, a escola, a localidade, a idade, uma fotografia tua ou contactos. A página é pública, e fala do teu trabalho, e não de ti.

## Se alguma coisa falhar

Primeiro, três verificações rápidas:

1. Estás na janela e na pasta certas? Olha para o fim da linha do terminal: `treino-escola`, `treino-casa` ou o nome do teu site.
2. O que dizem o `git status` e o `git remote -v`? Lê-os antes de tentares outra coisa, também as linhas `hint` e as sugestões entre parênteses.
3. Guardaste o ficheiro? Um ficheiro por guardar tem uma bolinha no separador, e o Git só vê o que está guardado.

### A pasta github-de-treino.git ficou dentro da treino-escola

O `git init --bare` foi feito sem o `../`. No Explorador de Ficheiros, apaga a pasta `github-de-treino.git` que está dentro da `treino-escola` e repete o passo 1 da fase 1, com o `../`. Se já fizeste a fase 2, troca também o endereço, com `git remote set-url origin ../github-de-treino.git`.

### error: remote origin already exists.

O repositório já tem um remoto `origin`. Vê o endereço com `git remote -v`. Se não for o certo, muda-o com `git remote set-url origin` e o endereço certo.

### fatal: 'origin' does not appear to be a git repository

O repositório ainda não tem o remoto `origin`, e o `git push` não sabe para onde enviar. Faz o `git remote add origin` da fase 2, ou da fase 13 na pasta do site, e repete o envio.

### fatal: destination path '../treino-casa' already exists

Já fizeste o clone antes, e a pasta `treino-casa` existe. Não precisas de o repetir: abre essa pasta na segunda janela do VS Code.

### O envio é recusado com (fetch first)

O remoto tem commits que tu não tens. Corre o `git pull --no-rebase --no-edit` e depois o `git push`, como na fase 7.

### fatal: Need to specify how to reconcile divergent branches.

Correste o `git pull` sem opções com as duas histórias diferentes. Repete com `git pull --no-rebase --no-edit`. Não corras os comandos com `--global` que as linhas `hint` sugerem, porque mudavam o Git para todos os alunos do portátil.

### O envio é recusado com (non-fast-forward)

O remoto tem commits que tu não tens, e o teu portátil já os conhece por um `git fetch`. Ou fizeste um `--amend` num commit que já tinhas enviado. Nos dois casos, junta as duas histórias com `git pull --no-rebase --no-edit` e envia com `git push`. Não se perde nada.

### O git pull diz CONFLICT

Mudaste a mesma linha na escola e em casa. Corre o `git merge --abort`, que põe tudo como estava antes do `git pull`, e chama o professor.

### git@github.com: Permission denied (publickey).

O GitHub não conhece a chave que o Git usou, e por isso nem pediu a frase-passe. Confirma com `git config core.sshCommand` que o nome da chave é `gh-` seguido do teu nome de utilizador. No GitHub, em Settings, SSH and GPG keys, confirma que a tua chave está na lista. Se não estiver, repete os passos 5 e 6 da fase 11.

### Repository not found

O endereço do remoto tem um erro. Compara o do `git remote -v` com o da página do repositório no GitHub, letra a letra, e corrige-o com `git remote set-url origin`, seguido do endereço certo.

### A primeira ligação ao GitHub fica parada

O `git push` não responde durante muito tempo e acaba numa mensagem com `port 22`. A rede da escola pode estar a fechar o caminho do SSH. Chama o professor, que te diz que endereço usar.

### A frase-passe não é aceite

O SSH volta a pedir a frase-passe e acaba em `Permission denied`. Confirma que a escreves igual, com os mesmos espaços. Se a esqueceste, não se recupera: repete o passo 4 da fase 11, escreve `y` quando aparecer `Overwrite (y/n)?`, e cria uma frase-passe nova. Depois, no GitHub, apaga a chave antiga, em SSH and GPG keys, e repete o passo 6 com a chave nova.

### fatal: pathspec '...' did not match any files

O `git add` não encontrou o ficheiro com o nome que escreveste. Escreveste o nome do exemplo, como `torneios.html`, em vez do da tua página, ou o nome tem um erro. Vê o nome certo no `git status` e repete o `git add` com ele.

### Author identity unknown

A pasta não tem identidade, e o Git não fez o commit. Na `treino-casa`, faz o passo 4 da fase 4, sem `--global`, e repete o commit.

### A aula acabou a meio das fases do GitHub

Na aula seguinte, abre outra janela privada, vai a `github.com` e carrega em Sign in. Escreve o teu email ou nome de utilizador e a palavra-passe. Se o GitHub mandar um código para o teu email, escreve-o. Depois continua na fase onde paraste.

### O ssh-keygen pergunta Overwrite (y/n)?

Já existe uma chave com esse nome no portátil. Se a criaste tu e sabes a frase-passe, escreve `n` e usa essa: passa ao passo 5 da fase 11. Se não sabes de quem é, escreve `n` e chama o professor.

### O VS Code não pede a frase-passe no Sync Changes

Se o Sync Changes mostrar um erro em vez da caixa `Passphrase`, envia pelo terminal, com `git push`. O envio é o mesmo, e o terminal pede a frase-passe.

### O GitHub pede a verificação em dois passos

O GitHub pode pedir para ativares a verificação em dois passos, *two-factor authentication*, com o telemóvel. Não a ativas na aula sem o professor, porque precisas de guardar uns códigos de recuperação. Chama-o.

### O código do GitHub não chega ao email

Procura na pasta do lixo eletrónico, ou spam. Se não estiver lá, pede ao GitHub para o reenviar, na página onde o escreves.

## Desafios

1. Na janela da escola, corre o `git log --oneline --graph` e encontra o commit de junção da fase 7. No `registo.md`, escreve o identificador dele e os dos dois commits que ele juntou. Pista: o commit de junção é onde as duas linhas do desenho se voltam a juntar.
2. Clona o repositório dos materiais da disciplina para uma pasta fora da pasta do teu site, com o endereço HTTPS. Depois vê os cinco commits mais recentes, sem fazer commits nessa pasta. Pista: o endereço está no botão verde Code, na página dos materiais no GitHub, e o `git log` aceita `-5`.

## Antes de terminares

- [ ] A `treino-escola` e a `treino-casa` têm o mesmo histórico, com o commit de junção, e o `git status` diz `up to date` nas duas.
- [ ] O teu site está no GitHub, num repositório público, com o histórico inteiro.
- [ ] O último commit do site tem o teu email privado, e o README diz o endereço do repositório.
- [ ] A tua página pessoal tem o README, sem dados pessoais.
- [ ] O `registo.md` tem o teu nome de utilizador, o endereço do repositório, o `git log --oneline -3` e a explicação do `git fetch` e do `git pull`.
- [ ] Nenhum comando levou `--global`, e a frase-passe não está escrita em nenhum ficheiro.
- [ ] Fechaste a janela privada do browser.
- [ ] Enviaste ao professor o endereço do repositório do site, como ele indicou.

![Rodapé](../../imagens/rodape.png)
