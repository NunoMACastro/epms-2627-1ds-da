![Cabeçalho](../../imagens/cabecalho.png)

# Ficha de exercícios: Guardar versões com o Git

Praticas os comandos do Git e a leitura das respostas dele, sempre num repositório de treino. Os exercícios 1 a 7 são obrigatórios. Cria uma pasta para esta ficha, fora da pasta do teu site. Escreve as respostas lá, num ficheiro `respostas.md`, com o número do exercício e a letra da alínea. O exercício 5 faz-se numa pasta `banda-da-escola`, dentro da pasta da ficha. Entrega a pasta da ficha onde o professor indicar. Para rever: o [guia do tema](../01-guardar-versoes-com-o-git.md) e o [laboratório](../laboratorios/01-guardar-versoes-com-o-git-laboratorio.md).

## O cenário

A Banda da Escola é um site imaginário, com uma página inicial, `index.html`, e uma página dos concertos, `concertos.html`. Os exercícios passam-se neste site.

## Exercício 1: Git, GitHub ou cópia de segurança

Para cada situação, diz se é o Git, o GitHub ou uma cópia de segurança, e justifica numa frase.

**a)** A Rita copia a pasta do site para uma pen, antes das férias.

**b)** No computador dele, na pasta do site, o Tiago vê o que mudou na semana passada na página dos concertos, e quem e porquê.

**c)** A turma abre no browser a página dos materiais da disciplina e descarrega-os em ZIP.

**d)** No comboio, sem Internet, o Duarte guarda uma versão da página dos concertos com a mensagem "Acrescenta o concerto de Natal".

Rever: [Guardar cópias não chega](../01-guardar-versoes-com-o-git.md#guardar-cópias-não-chega) e [O Git e o GitHub não são a mesma coisa](../01-guardar-versoes-com-o-git.md#o-git-e-o-github-não-são-a-mesma-coisa).

## Exercício 2: Ler o git status

Esta é a resposta do `git status` no repositório da Banda da Escola, a meio de uma tarde de trabalho:

```text
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   concertos.html

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   index.html

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	musicos.html
```

**a)** Em que zona está a alteração de cada um dos três ficheiros?

**b)** Se agora fizeres um commit, que ficheiros entram nele?

**c)** Escreve o comando que junta ao próximo commit a página nova dos músicos, sem o `index.html`.

Rever: [O comando git status diz em que zona está cada ficheiro](../01-guardar-versoes-com-o-git.md#o-comando-git-status-diz-em-que-zona-está-cada-ficheiro).

## Exercício 3: Prever o git status

O repositório da Banda da Escola acabou de receber um commit, e o `git status` diz `nothing to commit, working tree clean`. A seguir, fazes isto, por esta ordem:

1. crias o ficheiro `contactos.html`;
2. mudas o título do `index.html` e guardas;
3. escreves `git add contactos.html`.

**a)** Em que grupo do `git status` aparece cada um dos dois ficheiros, e com que palavra à frente?

**b)** A seguir, fazes `git commit -m "Acrescenta a página dos contactos"`. O que diz o `git status` agora?

Rever: [O comando git add escolhe o que entra no commit](../01-guardar-versoes-com-o-git.md#o-comando-git-add-escolhe-o-que-entra-no-commit).

## Exercício 4: Mensagens de commit

Para cada alteração, escreve a mensagem do commit. Se achares que devia ser dividida em mais do que um commit, escreve uma mensagem para cada um e diz porquê.

**a)** Trocaste a fotografia da banda na página inicial por uma mais recente.

**b)** No menu das duas páginas, corrigiste "Musicos" para "Músicos".

**c)** Na página inicial, vais mudar o título e, já que lá estás, acrescentar ao rodapé o ano de fundação da banda.

**d)** Um colega fez um commit com a mensagem "update". Diz o que falta a esta mensagem.

Rever: [Um commit guarda uma alteração com sentido](../01-guardar-versoes-com-o-git.md#um-commit-guarda-uma-alteração-com-sentido).

## Exercício 5: Um histórico com três commits

Dentro da pasta da ficha, cria a pasta `banda-da-escola`, com estes dois ficheiros, copiados tal como estão.

O `index.html`:

```html
<!doctype html>
<!-- Página inicial da Banda da Escola. Conteúdo fictício. -->
<html lang="pt-PT">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Início | Banda da Escola</title>
  </head>
  <body>
    <main>
      <h1>A banda da nossa escola</h1>
      <p>Tocamos nas festas da escola e ensaiamos às sextas-feiras.</p>
      <p><a href="concertos.html">Os próximos concertos</a></p>
    </main>
  </body>
</html>
```

O `concertos.html`:

```html
<!doctype html>
<!-- Página dos concertos da Banda da Escola. Conteúdo fictício. -->
<html lang="pt-PT">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Concertos | Banda da Escola</title>
  </head>
  <body>
    <main>
      <h1>Próximos concertos</h1>
      <ul>
        <li>Festa de Natal, 12 de dezembro, no ginásio.</li>
        <li>Dia da Escola, 15 de março, no pátio.</li>
      </ul>
      <p><a href="index.html">Voltar à página inicial</a></p>
    </main>
  </body>
</html>
```

Põe a pasta `banda-da-escola` no Git, com uma identidade inventada e o mesmo `.gitignore` do laboratório. Faz o `git init` com a pasta `banda-da-escola` aberta no VS Code, e não a pasta da ficha. O histórico tem de contar esta história, do commit mais antigo para o mais recente:

1. entram o `.gitignore` e a página inicial;
2. entra a página dos concertos;
3. o `h1` da página inicial passa a "A Banda da Escola".

As mensagens são tuas. No fim, o `git status` diz `nothing to commit, working tree clean`. Cola no `respostas.md` a resposta do `git log --oneline`.

Rever: [O .gitignore diz o que fica de fora](../01-guardar-versoes-com-o-git.md#o-gitignore-diz-o-que-fica-de-fora) e [Exemplo guiado: a Estante Digital no Git](../01-guardar-versoes-com-o-git.md#exemplo-guiado-a-estante-digital-no-git).

<details>
<summary>Pista</summary>

Antes de cada commit, o `git status` tem de mostrar em `Changes to be committed` só os ficheiros desse passo da história. Se aparecer lá mais algum, ainda o podes tirar da área de preparação.

</details>

## Exercício 6: Ler um git diff

Mais tarde, alguém mudou a página dos concertos. O `git diff` responde isto:

```text
diff --git a/concertos.html b/concertos.html
index bf85c3b..6e1f071 100644
--- a/concertos.html
+++ b/concertos.html
@@ -10,8 +10,9 @@
     <main>
       <h1>Próximos concertos</h1>
       <ul>
-        <li>Festa de Natal, 12 de dezembro, no ginásio.</li>
+        <li>Festa de Natal, 13 de dezembro, no ginásio.</li>
         <li>Dia da Escola, 15 de março, no pátio.</li>
+        <li>Concerto de fim de ano, 5 de junho, no auditório.</li>
       </ul>
       <p><a href="index.html">Voltar à página inicial</a></p>
     </main>
```

**a)** Quantas linhas foram apagadas, e quantas foram acrescentadas?

**b)** Diz por palavras tuas as duas coisas que mudaram na página.

**c)** Esta alteração já está na área de preparação? Como o sabes?

Rever: [O comando git diff mostra o que mudou](../01-guardar-versoes-com-o-git.md#o-comando-git-diff-mostra-o-que-mudou).

## Exercício 7: Desfazer o engano certo

Para cada situação, escreve o comando, ou os comandos, que resolvem o engano, e diz se alguma alteração se perde.

**a)** Fizeste `git add index.html` por engano. As alterações do ficheiro estão boas, mas são para o commit seguinte.

**b)** Apagaste sem querer metade da página dos concertos e guardaste. Ainda não fizeste `git add`, e queres a página como estava no último commit.

**c)** Mudaste a data do concerto de Natal para 13 de dezembro, que está certa, e fizeste `git add concertos.html`. Depois, apagaste sem querer metade da página e guardaste. Queres ficar com a data nova e recuperar o resto.

Rever: [Desfazer antes do commit](../01-guardar-versoes-com-o-git.md#desfazer-antes-do-commit).

## Desafios

1. Na pasta `banda-da-escola`, cria um ficheiro vazio chamado `desktop.ini` e outro chamado `notas.txt`. Mostra, com o `git status`, que só um deles aparece, e explica porquê no `respostas.md`. No fim, apaga os dois ficheiros.
2. Um colega fez o primeiro commit do site sem `.gitignore`, e o `Thumbs.db` entrou no histórico. Ele acrescentou depois o `.gitignore`, com o `Thumbs.db` lá escrito. Explica no `respostas.md` porque é que o ficheiro continua no histórico e continua a ser seguido.

## Critérios de conclusão

- O `respostas.md` tem as respostas aos exercícios 1 a 4, 6 e 7, com o número do exercício e a letra da alínea.
- A pasta `banda-da-escola` é um repositório com três commits, pela ordem pedida, e o `git status` diz `nothing to commit, working tree clean`.
- O `respostas.md` tem a resposta do `git log --oneline` da pasta `banda-da-escola`.
- Nenhum commit tem o teu email verdadeiro.

![Rodapé](../../imagens/rodape.png)
