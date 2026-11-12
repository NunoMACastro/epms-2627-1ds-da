![Cabeçalho](../../imagens/cabecalho.png)

# Laboratório: CSS e Flexbox

## O que vais construir

Dás aspeto às páginas do teu site com uma folha de estilos, sem mudar o que o HTML diz. Ficam com cores, letra, um cabeçalho com o menu ao lado do nome e uma lista de cartões que se arruma sozinha. Guardas cada passo grande num commit. Os exemplos usam o site do clube de xadrez: escolhe as tuas cores e escreve os teus textos. No fim, a página inicial do exemplo fica assim, numa janela larga:

```text
┌──────────────────────────────────────────────────────────────┐
│ Clube de Xadrez                            Início   Torneios │  faixa verde
├──────────────────────────────────────────────────────────────┤
│ Aprende a jogar xadrez connosco                              │
│ ...                                                          │
│ As peças e como se movem                                     │
│ ┌────────────────┐  ┌────────────────┐  ┌────────────────┐   │
│ │ Rei: ...       │  │ Dama: ...      │  │ Torre: ...     │   │
│ └────────────────┘  └────────────────┘  └────────────────┘   │
│ ┌────────────────┐  ┌────────────────┐  ┌────────────────┐   │
│ │ Bispo: ...     │  │ Cavalo: ...    │  │ Peão: ...      │   │
│ └────────────────┘  └────────────────┘  └────────────────┘   │
├──────────────────────────────────────────────────────────────┤
│        Site do Clube de Xadrez, feito na disciplina...       │
└──────────────────────────────────────────────────────────────┘
```

1. [Fase 1: A folha de estilos externa](#fase-1-a-folha-de-estilos-externa)
2. [Fase 2: O browser já tem estilos](#fase-2-o-browser-já-tem-estilos)
3. [Fase 3: As cores](#fase-3-as-cores)
4. [Fase 4: As variáveis de CSS](#fase-4-as-variáveis-de-css)
5. [Fase 5: O tipo de letra e o tamanho do texto](#fase-5-o-tipo-de-letra-e-o-tamanho-do-texto)
6. [Fase 6: O seletor descendente](#fase-6-o-seletor-descendente)
7. [Fase 7: O Flexbox põe os filhos lado a lado](#fase-7-o-flexbox-põe-os-filhos-lado-a-lado)
8. [Fase 8: O espaço entre os itens e o alinhamento](#fase-8-o-espaço-entre-os-itens-e-o-alinhamento)
9. [Fase 9: O seletor de classe](#fase-9-o-seletor-de-classe)
10. [Fase 10: O modelo de caixa](#fase-10-o-modelo-de-caixa)
11. [Fase 11: A largura de uma caixa e o box-sizing](#fase-11-a-largura-de-uma-caixa-e-o-box-sizing)
12. [Fase 12: Os itens que passam à linha seguinte e crescem](#fase-12-os-itens-que-passam-à-linha-seguinte-e-crescem)
13. [Fase 13: O foco tem de se ver](#fase-13-o-foco-tem-de-se-ver)

## O que precisas

- O VS Code e o Chrome ou o Edge, com as ferramentas do programador, que se abrem com F12.
- A pasta do teu site, já no Git, do [laboratório do tema 01 do Git](../../02-git/laboratorios/01-guardar-versoes-com-o-git-laboratorio.md), com o `registo.md` ao lado dela. Se não a tens, faz primeiro esse laboratório, que diz como montar o site a partir do clube de xadrez.

## Preparar o projeto

1. Abre a pasta do teu site no VS Code, com Open Folder..., no menu File, e abre o terminal, com New Terminal, no menu Terminal.

2. Corre o `git status`. Deve responder `nothing to commit, working tree clean`. Isto quer dizer que o teu site está todo guardado, e cada mudança deste laboratório vai aparecer no `git diff`. Se aparecerem ficheiros mudados, guarda-os primeiro num commit, como no laboratório do Git.

3. Abre o `registo.md`, com Open Recent, no menu File, e escreve no fim o título `## Laboratório de CSS`. É aí que vais registar o que o laboratório pede.

4. Abre a página inicial do teu site no Chrome ou no Edge e deixa-a aberta num separador, porque vais recarregá-la muitas vezes.

## Fase 1: A folha de estilos externa

Crias a folha de estilos e ligas-lhe as duas páginas, com uma primeira regra que se nota logo. Rever: [A folha de estilos externa](../03-css-e-flexbox.md#a-folha-de-estilos-externa).

1. No painel Explorer, carrega num espaço sem ficheiros, para o ficheiro novo não ir parar à pasta `imagens`. Carrega em New File..., escreve `estilos.css` e carrega em Enter. Cria `estilos.css` com esta primeira versão, que só muda o fundo da página. Escolhe a cor do teu fundo, clara:

   ```css
   /* estilos.css: a folha de estilos do site do Clube de Xadrez.
      As duas páginas ligam-se a ela com o elemento link, no head. */

   /* Um fundo cor de papel, para confirmar que a folha está ligada. */
   body {
     background-color: #f4f1ea;
   }
   ```

2. Em `index.html`, a seguir à linha do `title`, acrescenta:

   ```html
   <!-- A folha de estilos: o mesmo ficheiro dá o aspeto às duas páginas. -->
   <link rel="stylesheet" href="estilos.css">
   ```

   Faz o mesmo na segunda página, `torneios.html` no exemplo. Guarda os três ficheiros.

3. Antes de recarregares, prevê o que muda na página. Depois recarrega, com F5, ou Cmd+R no Mac. O que deves ver: o fundo da página com a tua cor, e tudo o resto igual. Isto quer dizer que o browser encontrou o `estilos.css`. Se o fundo continuar branco, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

4. Abre a segunda página, pelo menu. O que deves ver: o mesmo fundo, porque as duas páginas usam a mesma folha.

### Paragem 1

As duas páginas estão ligadas ao `estilos.css`, e a primeira regra funciona.

Pensa antes de continuares: o HTML das tuas páginas mudou? A resposta: só ganhou o `link`. O que cada elemento é continua igual, e o aspeto passou a vir do `estilos.css`.

## Fase 2: O browser já tem estilos

Vês no inspetor os estilos que o browser dá aos elementos e tiras a margem que ele põe à volta da página. Rever: [O browser já tem estilos](../03-css-e-flexbox.md#o-browser-já-tem-estilos).

1. Abre as ferramentas do programador, com F12. No separador Elements, carrega no `h1`. Do lado direito, no separador Styles, procura uma regra marcada `user agent stylesheet`, com `font-size: 2em` e `font-weight: bold`. É dos estilos do browser que vem o título grande e a negrito.

2. Carrega agora no `body`, no separador Elements. No separador Styles, a regra `user agent stylesheet` do `body` tem `margin: 8px`. É essa margem que deixa um espaço entre o conteúdo e os lados da janela.

3. Em `estilos.css`, na regra do `body`, acrescenta a linha `margin: 0;`, a seguir à abertura da chaveta. Guarda e recarrega. O que deves ver: o texto encostado aos lados da janela. No separador Styles, a margem do browser aparece agora riscada, porque a tua regra ganhou.

### Paragem 2

A página já não tem a margem do browser, e sabes encontrar no inspetor de onde vem cada estilo.

Pensa antes de continuares: a tua regra do `body` e a do browser apanham o mesmo elemento. Porque é que ganhou a tua? A resposta: quando uma regra tua e uma do browser discordam, ganha sempre a tua.

## Fase 3: As cores

Dás cor ao texto, aos títulos e ao cabeçalho, e medes no inspetor se o texto se lê bem. Rever: [As cores](../03-css-e-flexbox.md#as-cores) e [O contraste entre o texto e o fundo](../03-css-e-flexbox.md#o-contraste-entre-o-texto-e-o-fundo).

1. Em `estilos.css`, acrescenta à regra do `body` a cor do texto, e a seguir à regra do `body` acrescenta duas regras novas. O ficheiro fica assim, com as tuas cores:

   ```css
   /* estilos.css: a folha de estilos do site do Clube de Xadrez.
      As duas páginas ligam-se a ela com o elemento link, no head. */

   /* O corpo da página: as cores que os outros elementos herdam. */
   body {
     margin: 0;
     color: #222222;
     background-color: #f4f1ea;
   }

   /* Os títulos na cor principal do site. */
   h1,
   h2 {
     color: #2f4f3a;
   }

   /* O cabeçalho: texto claro sobre a cor principal. */
   header {
     color: #ffffff;
     background-color: #2f4f3a;
   }
   ```

2. Guarda e recarrega. O que deves ver: os títulos na cor principal, e o cabeçalho numa faixa dessa cor, com o nome do site a branco. Por cima da faixa fica uma tira da cor do fundo, que é a margem que o browser dá ao parágrafo do nome. As ligações do menu continuam azuis e quase não se veem.

3. Mede o contraste dos títulos. No separador Elements, carrega no `h1`. No separador Styles, na regra `h1, h2`, carrega no quadrado colorido ao lado da cor. Na janela de escolher cores, procura a linha `Contrast ratio`. O que deves ver: um número, que no exemplo é perto de 8, e uma marca a dizer que chega. Se o número for menor do que 4,5, escolhe uma cor mais escura e volta a medir.

4. Mede o contraste do texto do cabeçalho. No separador Elements, carrega no parágrafo do nome do site. No separador Styles, a cor dele aparece em `Inherited from header`: carrega no quadrado colorido dessa cor e lê o `Contrast ratio`. No `registo.md`, por baixo do título do laboratório, escreve os dois números.

### Paragem 3

O site tem as suas cores, e os dois contrastes estão no `registo.md`.

Pensa antes de continuares: porque é que o parágrafo do nome do site ficou branco, se a regra é do `header`? A resposta: a cor do texto herda-se. O parágrafo está dentro do `header` e herda o branco.

## Fase 4: As variáveis de CSS

Dás nomes às tuas cores e ao espaço do site, e trocas as cores escritas nas regras pelos nomes. Rever: [As variáveis de CSS](../03-css-e-flexbox.md#as-variáveis-de-css).

1. Em `estilos.css`, a seguir ao comentário do início, acrescenta:

   ```css
   /* As cores do site, cada uma com um nome. */
   :root {
     --cor-principal: #2f4f3a;
     --cor-texto: #222222;
     --cor-fundo: #f4f1ea;
   }
   ```

2. Nas regras do `body`, do `h1, h2` e do `header`, troca cada cor pela variável com o mesmo valor. A regra do `body`, por exemplo, fica assim:

   ```css
   body {
     margin: 0;
     color: var(--cor-texto);
     background-color: var(--cor-fundo);
   }
   ```

   O branco do texto do cabeçalho fica escrito como está, `#ffffff`, porque só se usa no cabeçalho.

3. Guarda e recarrega. O que deves ver: a página exatamente igual. Isto quer dizer que as variáveis têm os mesmos valores.

4. Para pôr as variáveis à prova, muda o valor de `--cor-principal` para uma cor bem diferente, como `#8b1e3f`, e recarrega. O que deves ver: os títulos e o cabeçalho com a cor nova ao mesmo tempo. Volta a pôr a tua cor.

### Paragem 4

Todas as cores do site estão escritas uma só vez, no `:root`, menos o branco do texto do cabeçalho.

Pensa antes de continuares: o que tens de mudar para pôr o site inteiro noutra cor principal? A resposta: só a linha da `--cor-principal`, no `:root`.

## Fase 5: O tipo de letra e o tamanho do texto

Escolhes a letra e os tamanhos do texto, em `rem`, e guardas no Git a primeira parte do aspeto. Rever: [O tipo de letra e o tamanho do texto](../03-css-e-flexbox.md#o-tipo-de-letra-e-o-tamanho-do-texto) e [As unidades: px e rem](../03-css-e-flexbox.md#as-unidades-px-e-rem).

1. Na regra do `body`, a seguir ao `margin: 0;`, acrescenta:

   ```css
   font-family: system-ui, "Segoe UI", Arial, sans-serif;
   font-size: 1rem;
   line-height: 1.5;
   ```

2. Na regra `h1, h2`, acrescenta `line-height: 1.2;`, para os títulos de várias linhas não ficarem com as linhas tão afastadas como as do texto.

3. Guarda e recarrega. O que deves ver: a letra do sistema e as linhas dos parágrafos mais afastadas.

4. Guarda esta parte num commit. No terminal:

   ```bash
   git status
   git add estilos.css index.html torneios.html
   git diff --staged
   git commit -m "Acrescenta as cores e a letra do site"
   ```

   O que deves ver: no `git status`, o `estilos.css` em `Untracked files` e as duas páginas em `Changes not staged for commit`. No `git diff --staged`, as duas linhas novas de cada página, o comentário e o `link`, com `+`, e o `estilos.css` inteiro com `+`. Se a resposta do `git diff --staged` não couber, sai com a tecla `q`. No fim, o commit responde `3 files changed`.

### Paragem 5

A primeira parte do aspeto do site está no histórico do Git.

Pensa antes de continuares: porque é que o `font-size` do `body` se escreve `1rem`, e não `16px`, se no teu browser dá o mesmo? A resposta: em `rem`, o tamanho cresce quando alguém aumenta a letra nas definições do browser. Em `px`, ficava igual.

## Fase 6: O seletor descendente

Mudas só o que está dentro do cabeçalho, o nome do site, o menu e as ligações, sem lhes dares classes. Rever: [O seletor descendente](../03-css-e-flexbox.md#o-seletor-descendente).

1. A seguir à regra do `header`, acrescenta a regra do nome do site, que escolhe só os parágrafos que estão dentro do `header`:

   ```css
   /* O nome do site, maior e a negrito, sem a margem dos parágrafos. */
   header p {
     margin: 0;
     font-size: 1.25rem;
     font-weight: bold;
   }
   ```

   Guarda e recarrega. O que deves ver: o nome do site maior e a negrito, e a tira clara por cima da faixa desapareceu. O parágrafo do rodapé não mudou, porque não está dentro do `header`.

2. A seguir à regra `header p`, acrescenta:

   ```css
   /* O menu: a lista sem bolinhas nem o recuo onde elas ficavam. */
   nav ul {
     margin: 0;
     padding: 0;
     list-style: none;
   }
   ```

3. Guarda e recarrega. O que deves ver: o menu sem bolinhas e sem recuo. A lista "O que precisas de trazer", no conteúdo principal, continua com as suas bolinhas, porque não está dentro do `nav`.

4. No separador Elements, carrega na ligação "Início" do menu. No separador Styles, procura a cor. O que deves ver: o `color` do `header` aparece mais abaixo, em `Inherited from header`, riscado. A cor que vale vem de uma regra `user agent stylesheet`, chamada `a:-webkit-any-link`, com `color: -webkit-link`, que é o azul das ligações.

5. A seguir à regra do `nav ul`, acrescenta:

   ```css
   /* As ligações do cabeçalho brancas: a cor das ligações não se herda. */
   header a {
     color: #ffffff;
   }
   ```

   Guarda e recarrega. O que deves ver: as ligações do menu brancas. Na segunda página, a ligação de voltar à página inicial continua azul.

6. Carrega outra vez na ligação "Início", no separador Elements. O que deves ver: a regra `header a` em cima, com o `color` a valer, e a regra do browser mais abaixo, com a cor riscada. Ao lado da regra `header a` está `estilos.css` e o número da linha.

7. No `registo.md`, escreve numa linha a regra que ganhou na cor da ligação "Início" e porque ganhou. Junta o ficheiro e a linha que o separador Styles mostra.

### Paragem 6

O nome do site está maior, o menu não tem bolinhas, e as ligações do cabeçalho são brancas.

Pensa antes de continuares: porque é que a ligação não herdou o branco do `header`, como o parágrafo do nome? A resposta: o browser tem uma regra para o `a`, que lhe dá o azul. Uma regra para o elemento ganha sempre à herança.

## Fase 7: O Flexbox põe os filhos lado a lado

Pões os itens do menu lado a lado, com o Flexbox. Rever: [O Flexbox põe os filhos lado a lado](../03-css-e-flexbox.md#o-flexbox-põe-os-filhos-lado-a-lado).

1. Antes de mexeres, prevê: se puseres `display: flex` no `nav`, os itens do menu ficam lado a lado? Experimenta no separador Styles: carrega no `nav`, no separador Elements. No topo do Styles, carrega dentro das chavetas de `element.style`, escreve `display`, carrega em Tab e escreve `flex`. O que deves ver: nada muda no menu. O `nav` tem um só filho, o `ul`, e é esse que fica sozinho na linha. Recarrega a página, para tirar a experiência.

2. No `:root`, a seguir à `--cor-fundo`, acrescenta a variável do espaço do site, `--espaco: 1rem;`, e muda o comentário por cima dele para `/* As cores e o espaço do site, cada um com um nome. */`. Na regra do `nav ul`, a seguir à abertura da chaveta, acrescenta:

   ```css
   display: flex;
   gap: var(--espaco);
   ```

3. Guarda e recarrega. O que deves ver: as ligações do menu lado a lado, com um espaço entre elas. O contentor é o `ul`, e os itens são os `li`.

### Paragem 7

O menu está numa linha, por baixo do nome do site.

Pensa antes de continuares: as ligações estão dentro dos `li`. São itens do contentor flex? A resposta: não. Os itens são só os filhos diretos do `ul`, os `li`. As ligações estão um nível abaixo.

## Fase 8: O espaço entre os itens e o alinhamento

Pões o nome do site e o menu na mesma linha, um em cada ponta, e guardas a arrumação num commit. Rever: [O espaço entre os itens e o alinhamento](../03-css-e-flexbox.md#o-espaço-entre-os-itens-e-o-alinhamento) e [Os itens que passam à linha seguinte e crescem](../03-css-e-flexbox.md#os-itens-que-passam-à-linha-seguinte-e-crescem).

1. Na regra do `header`, a seguir à abertura da chaveta, acrescenta:

   ```css
   display: flex;
   flex-wrap: wrap;
   justify-content: space-between;
   align-items: center;
   gap: var(--espaco);
   padding: var(--espaco);
   ```

2. Guarda e recarrega. O que deves ver: o nome do site à esquerda e o menu à direita, na mesma linha, alinhados pelo meio. A faixa tem espaço à volta.

3. Estreita a janela do browser o mais que dá, arrastando o lado direito. Depois aumenta o zoom para 200%, com Ctrl e a tecla +, ou Cmd e + no Mac. O que deves ver: quando o nome e o menu já não cabem lado a lado, o menu passa para baixo do nome. É o `flex-wrap`. Volta o zoom a 100%, com Ctrl e 0, ou Cmd e 0 no Mac, e alarga a janela.

4. Guarda a arrumação num commit:

   ```bash
   git add estilos.css
   git commit -m "Arruma o cabeçalho e o menu com o Flexbox"
   ```

   O que deves ver: `1 file changed`.

### Paragem 8

O cabeçalho tem o nome e o menu na mesma linha, como no wireframe largo, e a arrumação está no Git.

O ficheiro `estilos.css` do exemplo, como deve estar agora:

```css
/* estilos.css: a folha de estilos do site do Clube de Xadrez.
   As duas páginas ligam-se a ela com o elemento link, no head. */

/* As cores e o espaço do site, cada um com um nome. */
:root {
  --cor-principal: #2f4f3a;
  --cor-texto: #222222;
  --cor-fundo: #f4f1ea;
  --espaco: 1rem;
}

/* O corpo da página: as cores que os outros elementos herdam. */
body {
  margin: 0;
  font-family: system-ui, "Segoe UI", Arial, sans-serif;
  font-size: 1rem;
  line-height: 1.5;
  color: var(--cor-texto);
  background-color: var(--cor-fundo);
}

/* Os títulos na cor principal do site. */
h1,
h2 {
  color: var(--cor-principal);
  line-height: 1.2;
}

/* O cabeçalho: texto claro sobre a cor principal. */
header {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  gap: var(--espaco);
  padding: var(--espaco);
  color: #ffffff;
  background-color: var(--cor-principal);
}

/* O nome do site, maior e a negrito, sem a margem dos parágrafos. */
header p {
  margin: 0;
  font-size: 1.25rem;
  font-weight: bold;
}

/* O menu: a lista sem bolinhas nem o recuo onde elas ficavam. */
nav ul {
  display: flex;
  gap: var(--espaco);
  margin: 0;
  padding: 0;
  list-style: none;
}

/* As ligações do cabeçalho brancas: a cor das ligações não se herda. */
header a {
  color: #ffffff;
}
```

As regras vão do geral para o particular. Primeiro as variáveis, o corpo da página e os títulos, e por fim o cabeçalho e o que está dentro dele. Cada regra usa as variáveis do `:root`, menos o branco do cabeçalho.

Pensa antes de continuares: no `header`, o que faria o `justify-content: center`, em vez do `space-between`? A resposta: o nome e o menu juntavam-se ao centro da faixa, com o `gap` entre eles.

## Fase 9: O seletor de classe

Acrescentas à página inicial a lista dos itens do teu site, que vão ser cartões, e dás-lhe uma classe. Rever: [O seletor de classe](../03-css-e-flexbox.md#o-seletor-de-classe).

1. Em `index.html`, dentro do `main`, a seguir à última secção, acrescenta uma secção com os itens da coleção do teu site. Põe pelo menos quatro, numa lista com a classe `cartoes`. No exemplo, são as peças do xadrez:

   ```html
   <section>
     <h2>As peças e como se movem</h2>
     <!-- A classe "cartoes" diz ao CSS que cada peça aparece num cartão. -->
     <ul class="cartoes">
       <li>Rei: anda uma casa, em qualquer direção.</li>
       <li>Dama: anda as casas que quiser, em qualquer direção.</li>
       <li>Torre: anda em linha reta, na horizontal ou na vertical.</li>
       <li>Bispo: anda as casas que quiser, na diagonal.</li>
       <li>Cavalo: anda em L e é a única peça que salta por cima das outras.</li>
       <li>Peão: anda uma casa para a frente e come na diagonal.</li>
     </ul>
   </section>
   ```

2. Em `estilos.css`, no fim, acrescenta:

   ```css
   /* A lista dos cartões, sem bolinhas nem recuo. */
   .cartoes {
     padding: 0;
     list-style: none;
   }
   ```

3. Guarda os dois ficheiros e recarrega. O que deves ver: a lista nova sem bolinhas e encostada à esquerda. A lista "O que precisas de trazer" continua com bolinhas, porque não tem a classe.

### Paragem 9

A página inicial tem a lista da tua coleção, com a classe `cartoes`.

Pensa antes de continuares: porque é que a classe se chama `cartoes`, e não `lista-verde`? A resposta: o nome diz o que os elementos são. Se um dia mudares a cor, o nome continua certo.

## Fase 10: O modelo de caixa

Transformas cada item da lista num cartão, com espaço interior, borda, cantos redondos e margem, e dás uma borda ao rodapé. Rever: [O modelo de caixa](../03-css-e-flexbox.md#o-modelo-de-caixa) e [Fundos, bordas e cantos redondos](../03-css-e-flexbox.md#fundos-bordas-e-cantos-redondos).

1. No `:root`, a seguir à `--cor-fundo`, acrescenta as duas cores dos cartões, `--cor-cartao: #ffffff;` e `--cor-borda: #cfd8cf;`, com as tuas cores. A seguir à regra do `.cartoes`, acrescenta:

   ```css
   /* Cada cartão: uma caixa clara com borda e cantos redondos. */
   .cartoes li {
     margin-bottom: var(--espaco);
     padding: var(--espaco);
     border: 1px solid var(--cor-borda);
     border-radius: 0.5rem;
     background-color: var(--cor-cartao);
   }
   ```

2. Guarda e recarrega. O que deves ver: cada item numa caixa branca, com uma borda fina e os cantos redondos. Os cartões ficam uns por baixo dos outros, separados por um espaço.

3. No separador Elements, carrega num dos `li` dos cartões e abre o separador Computed. O que deves ver: no topo, o desenho da caixa, com a margem, a borda, o espaço interior e o conteúdo. Os tamanhos são `16` na margem de baixo, `1` na borda e `16` no espaço interior.

4. A seguir à regra do `header a`, acrescenta a regra do rodapé:

   ```css
   /* O rodapé: letra mais pequena, ao centro, com uma linha por cima. */
   footer {
     padding: var(--espaco);
     border-top: 1px solid var(--cor-borda);
     font-size: 0.875rem;
     text-align: center;
   }
   ```

   Guarda e recarrega. O que deves ver: o rodapé com letra mais pequena, ao centro, separado do conteúdo por uma linha.

### Paragem 10

Os itens da tua coleção são cartões, uns por baixo dos outros.

Pensa antes de continuares: no cartão, o fundo branco pinta a margem? A resposta: não. O fundo pinta o conteúdo e o espaço interior. A margem fica sempre transparente, e por isso vês o fundo da página entre os cartões.

## Fase 11: A largura de uma caixa e o box-sizing

Dás uma largura ao conteúdo principal, encontras no inspetor a caixa que sai da página e corriges a conta da largura. Rever: [A largura de uma caixa e o box-sizing](../03-css-e-flexbox.md#a-largura-de-uma-caixa-e-o-box-sizing).

1. A seguir à regra `h1, h2`, acrescenta:

   ```css
   /* O conteúdo principal ao centro, sem passar de uma largura confortável. */
   main {
     width: 100%;
     max-width: 60rem;
     margin: 0 auto;
     padding: var(--espaco);
   }
   ```

2. Guarda e recarrega. Numa janela larga, o conteúdo fica numa coluna ao centro. Agora estreita a janela até a meio do ecrã. O que deves ver: aparece em baixo uma barra de deslocamento horizontal, e a página mexe para o lado. Este é o erro.

3. Procura a causa. No separador Elements, passa o rato pelo `main`. O que deves ver: a caixa do `main` sai pelo lado direito da janela. No separador Computed, o desenho da caixa mostra o conteúdo com a largura da janela e 16 de espaço interior de cada lado. A caixa inteira tem a largura da janela mais 32 píxeis.

4. Corrige a causa, e não o sítio onde o erro se vê. A seguir à regra do `:root`, acrescenta:

   ```css
   /* A largura de cada caixa passa a incluir o espaço interior e a borda. */
   * {
     box-sizing: border-box;
   }
   ```

5. Guarda e recarrega, com a janela estreita. O que deves ver: a barra horizontal desapareceu, e o `main` cabe na janela. No desenho da caixa, o conteúdo passa a ter a largura da janela menos 32, e a caixa inteira cabe na janela.

6. No `registo.md`, escreve o erro em três linhas: o que viste, a causa que encontraste no inspetor e a regra que o corrigiu.

### Paragem 11

O conteúdo principal está ao centro e cabe na janela em qualquer largura.

Pensa antes de continuares: porque é que, com a janela larga, a barra não aparecia? A resposta: com a janela larga, o `max-width` limitava o `main` a `60rem`, e sobrava espaço para os 32 píxeis. Só quando os `100%` passavam a contar é que a caixa ficava mais larga do que a janela.

## Fase 12: Os itens que passam à linha seguinte e crescem

Pões os cartões lado a lado, a passar à linha seguinte quando não cabem, e guardas a lista de cartões num commit. Rever: [Os itens que passam à linha seguinte e crescem](../03-css-e-flexbox.md#os-itens-que-passam-à-linha-seguinte-e-crescem).

1. Na regra do `.cartoes`, a seguir à abertura da chaveta, acrescenta:

   ```css
   display: flex;
   flex-wrap: wrap;
   gap: var(--espaco);
   ```

2. Na regra do `.cartoes li`, tira a linha `margin-bottom: var(--espaco);`, porque agora é o `gap` que afasta os cartões. No lugar dela, acrescenta:

   ```css
   flex-basis: 15rem;
   flex-grow: 1;
   ```

3. Antes de recarregares, prevê: numa janela larga, quantos cartões ficam em cada linha? Depois recarrega. O que deves ver, no exemplo: três cartões em cada linha, todos com a mesma largura, a ocupar a linha toda. Com o teu número de itens, a última linha pode ter menos cartões, que crescem até a preencher.

4. Estreita a janela devagar. O que deves ver: os cartões passam a dois por linha, e depois a um por linha, sem nunca aparecer a barra horizontal.

5. Guarda os cartões num commit:

   ```bash
   git add index.html estilos.css
   git commit -m "Mostra a coleção em cartões"
   ```

   O que deves ver: `2 files changed`.

### Paragem 12

Os cartões arrumam-se sozinhos em qualquer largura, e estão no Git.

Pensa antes de continuares: o que acontecia sem o `flex-grow: 1`? A resposta: cada cartão ficava com os `15rem` de partida, e o espaço que sobra ficava vazio, à direita da linha.

## Fase 13: O foco tem de se ver

Provocas o erro de esconder o foco, corriges, e pões uma moldura que se vê em todos os fundos do site. Rever: [O foco tem de se ver](../03-css-e-flexbox.md#o-foco-tem-de-se-ver) e [As pseudo-classes :hover e :focus-visible](../03-css-e-flexbox.md#as-pseudo-classes-hover-e-focus-visible).

1. Abre a segunda página do teu site, que tem ligações no cabeçalho e uma no conteúdo, a de voltar à página inicial. Carrega num espaço vazio da página e depois na tecla Tab, várias vezes. O que deves ver: a moldura do browser a passar de ligação em ligação.

2. Provoca o erro. No fim do `estilos.css`, acrescenta:

   ```css
   a:focus {
     outline: none;
   }
   ```

   Guarda, recarrega e percorre outra vez a página com a tecla Tab. O que deves ver: nenhuma moldura. Não sabes em que ligação estás, e é isto que acontece a quem usa o teclado num site assim. Apaga estas três linhas e guarda.

3. No fim do `estilos.css`, acrescenta a moldura do site:

   ```css
   /* O foco do teclado bem visível, afastado da ligação. */
   a:focus-visible {
     outline: 3px solid var(--cor-principal);
     outline-offset: 2px;
   }
   ```

4. Guarda, recarrega e percorre a página com a tecla Tab. O que deves ver: no conteúdo, a ligação de voltar tem uma moldura grossa da cor principal. No cabeçalho, as ligações também a têm, mas não se vê, porque o fundo é da mesma cor.

5. A seguir à regra anterior, acrescenta:

   ```css
   /* No cabeçalho, o fundo é da cor principal: a moldura passa a branca. */
   header a:focus-visible {
     outline-color: #ffffff;
   }
   ```

6. Guarda e recarrega, e percorre outra vez a página com a tecla Tab. O que deves ver: a moldura branca nas ligações do cabeçalho e da cor principal na do conteúdo. Para o confirmares no inspetor, carrega numa ligação do cabeçalho, no separador Elements, depois em `:hov`, no separador Styles, e marca `:focus-visible`. A regra `header a:focus-visible` aparece em cima, e o `outline` da regra geral fica com a cor riscada, porque o seletor é menos específico.

7. Guarda o foco num commit:

   ```bash
   git add estilos.css
   git commit -m "Torna o foco visível nas ligações"
   git log --oneline
   ```

   O que deves ver: os commits do laboratório no topo do histórico, por cima dos do laboratório do Git.

8. No `registo.md`, cola a resposta do `git log --oneline`.

### Paragem 13

As duas páginas têm o aspeto completo, o foco vê-se em todas as ligações, e cada passo grande está num commit.

O ficheiro `estilos.css` do exemplo, completo:

```css
/* estilos.css: a folha de estilos do site do Clube de Xadrez.
   As duas páginas ligam-se a ela com o elemento link, no head. */

/* As cores e o espaço do site, cada um com um nome. */
:root {
  --cor-principal: #2f4f3a;
  --cor-texto: #222222;
  --cor-fundo: #f4f1ea;
  --cor-cartao: #ffffff;
  --cor-borda: #cfd8cf;
  --espaco: 1rem;
}

/* A largura de cada caixa passa a incluir o espaço interior e a borda. */
* {
  box-sizing: border-box;
}

/* O corpo da página: as cores que os outros elementos herdam. */
body {
  margin: 0;
  font-family: system-ui, "Segoe UI", Arial, sans-serif;
  font-size: 1rem;
  line-height: 1.5;
  color: var(--cor-texto);
  background-color: var(--cor-fundo);
}

/* Os títulos na cor principal do site. */
h1,
h2 {
  color: var(--cor-principal);
  line-height: 1.2;
}

/* O conteúdo principal ao centro, sem passar de uma largura confortável. */
main {
  width: 100%;
  max-width: 60rem;
  margin: 0 auto;
  padding: var(--espaco);
}

/* O cabeçalho: texto claro sobre a cor principal. */
header {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  gap: var(--espaco);
  padding: var(--espaco);
  color: #ffffff;
  background-color: var(--cor-principal);
}

/* O nome do site, maior e a negrito, sem a margem dos parágrafos. */
header p {
  margin: 0;
  font-size: 1.25rem;
  font-weight: bold;
}

/* O menu: a lista sem bolinhas nem o recuo onde elas ficavam. */
nav ul {
  display: flex;
  gap: var(--espaco);
  margin: 0;
  padding: 0;
  list-style: none;
}

/* As ligações do cabeçalho brancas: a cor das ligações não se herda. */
header a {
  color: #ffffff;
}

/* O rodapé: letra mais pequena, ao centro, com uma linha por cima. */
footer {
  padding: var(--espaco);
  border-top: 1px solid var(--cor-borda);
  font-size: 0.875rem;
  text-align: center;
}

/* A lista dos cartões, sem bolinhas nem recuo. */
.cartoes {
  display: flex;
  flex-wrap: wrap;
  gap: var(--espaco);
  padding: 0;
  list-style: none;
}

/* Cada cartão: uma caixa clara com borda e cantos redondos. */
.cartoes li {
  flex-basis: 15rem;
  flex-grow: 1;
  padding: var(--espaco);
  border: 1px solid var(--cor-borda);
  border-radius: 0.5rem;
  background-color: var(--cor-cartao);
}

/* O foco do teclado bem visível, afastado da ligação. */
a:focus-visible {
  outline: 3px solid var(--cor-principal);
  outline-offset: 2px;
}

/* No cabeçalho, o fundo é da cor principal: a moldura passa a branca. */
header a:focus-visible {
  outline-color: #ffffff;
}
```

O ficheiro começa pelas variáveis e pelas regras gerais, passa às zonas da página e acaba nos casos particulares, os cartões e o foco. As duas regras do foco ficam no fim, e a do cabeçalho ganha à outra pela especificidade, e não pela ordem.

Pensa antes de continuares: se tirasses a regra `header a:focus-visible`, o foco das ligações do cabeçalho deixava de existir? A resposta: não. O foco continuava lá, com a moldura da regra geral, mas da mesma cor que o fundo, e por isso ninguém o via. Um foco que não se vê é o mesmo que nenhum para quem usa o teclado.

## Se alguma coisa falhar

Primeiro, três verificações rápidas:

1. Guardaste o ficheiro? No VS Code, um ficheiro por guardar tem uma bolinha no separador. Guarda com Ctrl+S, ou Cmd+S no Mac.
2. Recarregaste a página? O browser só lê o `estilos.css` outra vez quando recarregas, com F5, ou Cmd+R no Mac.
3. O que diz o separador Styles? Carrega no elemento que não mudou e vê se a tua regra aparece, se está riscada ou se tem um triângulo amarelo.

### O fundo continua branco na fase 1

O browser não encontrou o `estilos.css`. Confirma que o ficheiro está na pasta do site, ao lado das páginas, e não dentro de `imagens`. Confirma letra a letra o `href` do `link` e o `rel="stylesheet"`. Se o ficheiro se chamar `estilos.css.txt`, apaga-o e cria-o outra vez no VS Code.

### Uma regra nova não faz nada

No separador Styles, a declaração aparece riscada com um triângulo amarelo: a propriedade ou o valor estão mal escritos. Se a regra nem aparece, o seletor não apanha o elemento: confere o nome, o ponto da classe e o espaço do seletor descendente. Pode faltar também a chaveta de fecho de uma regra anterior.

### Não encontro a linha Contrast ratio

Carregaste no quadrado colorido de uma cor de fundo, e não de uma cor de texto. O contraste só aparece na janela de escolher cores da propriedade `color`, mesmo quando ela está em `Inherited from`.

### As ligações do menu continuam azuis depois da fase 6

A regra `header a` não está a ser aplicada. Confirma que tem um espaço entre `header` e `a`. Sem espaço, `headera` é o nome de um elemento que não existe.

### A barra horizontal não desaparece na fase 11

O `* { box-sizing: border-box; }` não está a ser aplicado. Confirma que a regra tem o asterisco e as chavetas. Se continuar, passa o rato pelas caixas no separador Elements e procura outra que saia pelo lado direito.

### Os cartões não ficam lado a lado na fase 12

O `display: flex` foi para a regra `.cartoes li`, e não para a `.cartoes`. O contentor é a lista, e os itens são os `li`.

### O git status mostra o registo.md

O `registo.md` fica ao lado da pasta do site, e por isso o `git status` não o devia mostrar. Se aparece, foi criado dentro da pasta do site. Move-o para a pasta de cima, no Explorador de Ficheiros, ou no Finder, no Mac.

## Desafios

1. Dá à segunda página do teu site um aspeto próprio para a imagem: uma borda e cantos redondos, sem mudar o HTML. Pista: o seletor pode escolher o `img` só dentro do `main`.
2. Quando o rato passa por cima de um cartão, a borda muda para a cor principal. Pista: há uma pseudo-classe para o rato por cima, e ela pode juntar-se ao seletor do cartão.
3. Mede o contraste da ligação de voltar à página inicial, no conteúdo, sobre o fundo da página. Se for menor do que 4,5, escolhe uma cor para as ligações do conteúdo e escreve o número novo no `registo.md`. Pista: a regra para as ligações do conteúdo não pode apanhar as do cabeçalho.

## Antes de terminares

- [ ] As duas páginas estão ligadas ao `estilos.css`, e o HTML só ganhou o `link` e a secção com a classe `cartoes`.
- [ ] As cores estão no `:root` e as regras usam as variáveis.
- [ ] O cabeçalho tem o nome e o menu na mesma linha, e as ligações do menu têm contraste com o fundo.
- [ ] Os cartões passam de três para um por linha quando estreitas a janela, sem barra horizontal.
- [ ] O foco vê-se em todas as ligações das duas páginas.
- [ ] O `registo.md` tem os contrastes, a regra que ganhou na fase 6, o erro da fase 11 e o histórico do Git.
- [ ] O `git status` diz `nothing to commit, working tree clean`, e o histórico tem os quatro commits deste laboratório.

![Rodapé](../../imagens/rodape.png)
