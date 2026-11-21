![Cabeçalho](../imagens/cabecalho.png)

# Consulta rápida de CSS

Aqui tens as três formas de pôr CSS numa página e como se escreve uma regra. A seguir vêm as propriedades que mais vais usar, com o que fazem e um exemplo de cada uma.

## Como se escreve uma regra

O CSS diz como aparecem os elementos da página. Escreve-se em **regras**. Cada regra começa por um **seletor**, que escolhe os elementos, e diz entre chavetas o que muda neles, uma propriedade por linha, na forma `propriedade: valor;`.

```css
/* Os parágrafos ficam azul-escuros e com letra maior. */
p {
  color: #1f4e8c;
  font-size: 1.125rem;
}
```

- `p`: o seletor. Esta regra escolhe todos os parágrafos.
- `color` e `font-size`: as propriedades, o que muda.
- `#1f4e8c` e `1.125rem`: os valores, como muda.
- `/* ... */`: um comentário, que o browser ignora.

Cada linha acaba em `;`. Se uma propriedade estiver mal escrita, o browser não mostra nenhum erro: ignora-a e continua.

## As três formas de pôr CSS numa página

### No atributo `style`

O CSS vai dentro da etiqueta de abertura, no atributo `style`. Só muda aquele elemento.

Exemplo:

```html
<p style="color: #b00020; font-weight: bold;">Esgotado</p>
```

Serve para experimentar depressa. Numa página a sério, evita-o: o mesmo estilo tem de se repetir em cada elemento, e mudar uma cor obriga a mudá-la em todos.

### Na etiqueta `<style>`

As regras vão dentro de uma etiqueta `<style>`, no `head`. Mudam a página toda, mas só essa página.

Exemplo:

```html
<head>
  <meta charset="utf-8">
  <title>Inventário da sala</title>
  <style>
    p {
      color: #1f4e8c;
    }
  </style>
</head>
```

### Num ficheiro à parte

As regras vão num ficheiro `.css`, a **folha de estilos**. A página liga-o no `head` com a etiqueta `<link>`, que não tem etiqueta de fecho. O mesmo ficheiro serve todas as páginas que o ligam.

Exemplo, no `index.html`:

```html
<head>
  <meta charset="utf-8">
  <title>Inventário da sala</title>
  <link rel="stylesheet" href="estilos.css">
</head>
```

E no `estilos.css`, na mesma pasta:

```css
p {
  color: #1f4e8c;
}
```

O `rel="stylesheet"` diz que o ficheiro é uma folha de estilos, e o `href` diz onde ele está. É a forma mais usada, porque o HTML fica só com o conteúdo, e o estilo de todas as páginas muda num só sítio.

### As três lado a lado

| Forma | Onde se escreve | O que muda |
| --- | --- | --- |
| Atributo `style` | Na etiqueta | Só esse elemento |
| Etiqueta `<style>` | Dentro do `<style>`, no `head` | A página onde está |
| Ficheiro | Num ficheiro `.css`, ligado com `<link>` | Todas as páginas que o ligam |

Quando a mesma propriedade do mesmo elemento aparece em mais de um sítio, ganha o atributo `style`. Entre a etiqueta `<style>` e o ficheiro, com o mesmo seletor, ganha a regra que o browser lê por último. É a que está mais abaixo no `head`.

## Os seletores

| Seletor | O que escolhe | Exemplo |
| --- | --- | --- |
| `p` | Todos os elementos dessa etiqueta | `p { color: navy; }` |
| `h1, h2` | Vários elementos, separados por vírgulas | `h1, h2 { color: navy; }` |
| `.aviso` | Os elementos com `class="aviso"` | `.aviso { color: red; }` |
| `#total` | O elemento com `id="total"` | `#total { font-weight: bold; }` |
| `nav a` | Os `a` que estão dentro de um `nav` | `nav a { color: white; }` |
| `a:hover` | Os `a` quando o rato está por cima | `a:hover { color: red; }` |
| `a:focus-visible` | Os `a` quando têm o foco do teclado, como com a tecla Tab | `a:focus-visible { outline: 3px solid navy; }` |

Uma `class` pode estar em vários elementos da página, e um `id` só pode estar num. Para dar aspeto, usa-se de preferência a classe.

## Que regra ganha

Quando duas regras dão valores diferentes à mesma propriedade do mesmo elemento, o browser decide assim, por esta ordem:

1. As tuas regras ganham aos estilos que o browser dá a cada elemento.
2. Ganha a regra com o seletor mais específico: uma classe ganha a um elemento, e `header a` ganha a `a`.
3. Com a mesma especificidade, ganha a regra que está mais abaixo no ficheiro.

O separador Styles das ferramentas do programador mostra a regra que ganhou, e risca as que perderam.

## As cores e as medidas

As cores escrevem-se de três maneiras:

| Forma | Exemplo | O que é |
| --- | --- | --- |
| Nome | `red`, `white`, `navy` | Uma cor com nome, em inglês |
| Hexadecimal | `#1f4e8c` | Um `#` e três pares de símbolos, para o vermelho, o verde e o azul, de `00` a `ff` |
| `rgb()` | `rgb(31, 78, 140)` | As mesmas três cores, de 0 a 255 |

As medidas levam sempre a unidade, colada ao número:

| Unidade | O que vale | Exemplo |
| --- | --- | --- |
| `px` | Píxeis do ecrã | `16px` |
| `rem` | O tamanho da letra normal do browser, quase sempre 16 píxeis | `2rem` |
| `%` | Uma parte do tamanho do elemento que o contém | `50%` |

## As variáveis de CSS

Uma variável guarda um valor com um nome, começado por dois hífens. Cria-se no `:root`, o elemento que contém a página toda, e usa-se com `var()`.

Exemplo:

```css
:root {
  --cor-principal: #1f4e8c;
  --espaco: 1rem;
}

h1 {
  color: var(--cor-principal);
  margin-bottom: var(--espaco);
}
```

Para mudar a cor principal no site todo, muda-se só a linha do `:root`.

## Texto

As propriedades do texto passam do elemento para os que estão dentro dele. A isto chama-se **herança**. Uma `color` no `body` muda o texto da página toda, menos o das ligações, que o browser pinta de azul.

### `color`

Muda a cor do texto.

Exemplo:

```css
body {
  color: #1f1f1f;
}
```

### `font-family`

Escolhe o tipo de letra. Leva uma lista separada por vírgulas, e o browser usa a primeira que tiver.

Exemplo:

```css
body {
  font-family: system-ui, sans-serif;
}
```

Valores:

- `system-ui`: a letra do sistema operativo.
- `sans-serif`: uma letra sem os pequenos traços nas pontas.
- `serif`: uma letra com os pequenos traços nas pontas, como a dos jornais.
- `monospace`: uma letra em que todas as letras têm a mesma largura, como no editor de código.

### `font-size`

Muda o tamanho da letra.

Exemplo:

```css
h1 {
  font-size: 2rem;
}
```

### `font-weight`

Põe a letra em negrito ou tira o negrito.

Exemplo:

```css
th {
  font-weight: normal;
}
```

Valores:

- `normal`: a letra normal.
- `bold`: negrito.

### `font-style`

Põe a letra em itálico ou tira o itálico.

Exemplo:

```css
em {
  font-style: normal;
}
```

Valores:

- `normal`: a letra normal.
- `italic`: itálico.

### `text-align`

Alinha o texto dentro do elemento.

Exemplo:

```css
h1 {
  text-align: center;
}
```

Valores:

- `left`: à esquerda.
- `center`: ao centro.
- `right`: à direita.
- `justify`: justificado, com as linhas todas do mesmo comprimento.

### `text-decoration`

Põe ou tira uma linha no texto.

Exemplo:

```css
nav a {
  text-decoration: none;
}
```

Valores:

- `none`: sem linha. Tira o sublinhado das ligações, o que só se faz no menu: no meio do texto, as ligações continuam sublinhadas.
- `underline`: sublinhado.
- `line-through`: riscado.

### `line-height`

Muda a altura de cada linha. O valor `1.5` dá uma vez e meia o tamanho da letra.

Exemplo:

```css
body {
  line-height: 1.5;
}
```

## Fundo

### `background-color`

Muda a cor do fundo.

Exemplo:

```css
button {
  background-color: #1f4e8c;
}
```

### `background-image`

Põe uma imagem no fundo. O caminho vai dentro de `url()`. Com `background-size: cover`, a imagem estica até cobrir o elemento todo.

Exemplo:

```css
header {
  background-image: url("imagens/fundo.png");
  background-size: cover;
}
```

## A caixa de cada elemento

Cada elemento é uma caixa. De dentro para fora, tem o conteúdo, o espaço por dentro (`padding`), a borda (`border`) e o espaço por fora (`margin`).

```text
┌─────────────── margin ────────────────┐
│ ┌───────────── border ──────────────┐ │
│ │ ┌─────────── padding ───────────┐ │ │
│ │ │           conteúdo            │ │ │
│ │ └───────────────────────────────┘ │ │
│ └───────────────────────────────────┘ │
└───────────────────────────────────────┘
```

### `width` e `height`

Mudam a largura e a altura da caixa.

Exemplo:

```css
img {
  width: 300px;
  height: 200px;
}
```

O `max-width` diz a largura máxima: a caixa encolhe com a janela, mas não passa desse valor.

Exemplo:

```css
main {
  max-width: 60rem;
}
```

### `box-sizing`

Diz o que o `width` mede. Por omissão, mede só o conteúdo, e o `padding` e a borda somam-se por fora. Com `border-box`, o `width` mede a caixa inteira, até à borda. Põe-se em todos os elementos, com o seletor `*`, que os escolhe a todos.

Exemplo:

```css
* {
  box-sizing: border-box;
}
```

### `padding`

Muda o espaço por dentro, entre o conteúdo e a borda. Com um valor, fica igual nos quatro lados. Com dois, o primeiro é para cima e para baixo, e o segundo para os lados. Para um lado só, há `padding-top`, `padding-right`, `padding-bottom` e `padding-left`.

Exemplo:

```css
button {
  padding: 0.5rem 1rem;
}
```

### `border`

Desenha uma borda à volta da caixa. Leva três valores: a grossura, o tipo de linha e a cor.

Exemplo:

```css
th, td {
  border: 1px solid #1f1f1f;
}
```

Valores do tipo de linha:

- `solid`: contínua.
- `dashed`: tracejada.
- `dotted`: pontilhada.

### `border-radius`

Arredonda os cantos da caixa.

Exemplo:

```css
button {
  border-radius: 8px;
}
```

### `margin`

Muda o espaço por fora, entre a caixa e as que estão à volta. Os valores funcionam como no `padding`, e há também `margin-top`, `margin-right`, `margin-bottom` e `margin-left`. Com `margin: 0 auto`, uma caixa com `max-width` fica ao centro.

Exemplo:

```css
main {
  max-width: 60rem;
  margin: 0 auto;
}
```

### `outline`

Desenha uma moldura por fora da borda. O browser usa-a para mostrar onde está o foco de quem usa o teclado. Nunca o apagues com `outline: none` sem pores outro no lugar.

Exemplo:

```css
button:focus-visible {
  outline: 3px solid #b35c00;
  outline-offset: 2px;
}
```

O `outline-offset` afasta a moldura da caixa, para não encostar ao texto.

## A disposição

### `display`

Diz como a caixa se arruma na página.

Exemplo:

```css
nav {
  display: flex;
}
```

Valores:

- `block`: ocupa a linha toda, e o elemento seguinte vai para baixo, como o `p` e o `h1`.
- `inline`: fica na mesma linha que o texto, como o `a` e o `strong`. Não aceita `width` nem `height`.
- `inline-block`: fica na mesma linha, mas aceita `width` e `height`.
- `none`: esconde o elemento.
- `flex`: põe lado a lado os filhos diretos do elemento, que passam a ser os itens.
- `grid`: organiza os filhos diretos numa grelha de linhas e colunas.

### `gap`

Com `display: flex` ou `display: grid`, muda o espaço entre os itens.

Exemplo:

```css
nav {
  display: flex;
  gap: 1rem;
}
```

### `justify-content`

Com `display: flex`, arruma os itens na horizontal.

Exemplo:

```css
nav {
  display: flex;
  justify-content: space-between;
}
```

Valores:

- `flex-start`: à esquerda.
- `center`: ao centro.
- `flex-end`: à direita.
- `space-between`: espalhados, com o espaço todo entre eles.

### `align-items`

Com `display: flex`, alinha os itens na vertical.

Exemplo:

```css
header {
  display: flex;
  align-items: center;
}
```

Valores:

- `stretch`: esticam até à altura do mais alto, por omissão.
- `flex-start`: em cima.
- `center`: ao meio.
- `flex-end`: em baixo.

### `flex-wrap`

Com `display: flex`, deixa os itens passar à linha seguinte quando não cabem numa só.

Exemplo:

```css
.cartoes {
  display: flex;
  flex-wrap: wrap;
}
```

Valores:

- `nowrap`: todos na mesma linha, a encolher, por omissão.
- `wrap`: passam à linha seguinte quando não cabem.

### `flex-basis` e `flex-grow`

Aplicam-se aos itens de um contentor flex. O `flex-basis` diz a largura de partida de cada um. O `flex-grow` diz se cresce para ocupar o espaço que sobra na linha: com `1`, cresce, e com `0`, o valor por omissão, não cresce.

Exemplo:

```css
.cartoes li {
  flex-basis: 15rem;
  flex-grow: 1;
}
```

Cada cartão parte de `15rem` e cresce até a linha ficar cheia.

## A grelha com Grid

O Flexbox organiza elementos sobretudo numa direção, numa linha ou numa coluna. O Grid permite coordenar as linhas e as colunas ao mesmo tempo.

Aplica `display: grid` no elemento que contém o grupo. Os seus filhos diretos, os elementos imediatamente dentro dele, passam a ocupar as células da grelha.

### `grid-template-columns`

Define quantas colunas há e a largura de cada uma. A unidade `fr` representa uma parte do espaço disponível, depois de descontar os intervalos entre colunas.

Exemplo, no HTML:

```html
<div class="grelha">
  <div class="caixa">Caderno</div>
  <div class="caixa">Caneta</div>
  <div class="caixa">Borracha</div>
  <div class="caixa">Régua</div>
</div>
```

No CSS:

```css
.grelha {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.caixa {
  padding: 1rem;
  border: 1px solid #1f1f1f;
}
```

Ficam duas colunas com a mesma largura. O caderno e a caneta ficam na primeira linha; a borracha e a régua, na segunda.

O browser cria as linhas necessárias à medida que entram mais elementos. O `gap` deixa `1rem` entre as linhas e entre as colunas.

Outros valores para `grid-template-columns`:

| Valor | Resultado |
| --- | --- |
| `1fr 2fr` | Duas colunas; a segunda recebe o dobro do espaço da primeira |
| `200px 1fr` | A primeira tem 200 píxeis; a segunda recebe o espaço que sobra |
| `repeat(3, 1fr)` | Três colunas iguais; repete `1fr` três vezes |

### `grid-template-rows`

Define a altura das linhas indicadas. Sem esta propriedade, a altura das linhas do exemplo ajusta-se ao conteúdo.

Exemplo:

```css
.grelha {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 80px auto;
  gap: 1rem;
}
```

A primeira linha tem 80 píxeis de altura. A segunda ajusta-se ao conteúdo com `auto`. Se forem precisas mais linhas, o browser cria-as automaticamente.

### `gap`, `row-gap` e `column-gap`

Com um valor, o `gap` dá o mesmo intervalo às linhas e às colunas. Com dois, o primeiro é entre linhas e o segundo entre colunas.

Exemplo:

```css
.grelha {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem 2rem;
}
```

Aqui, há `1rem` entre linhas e `2rem` entre colunas. Para mudar só um deles, usa `row-gap` para as linhas ou `column-gap` para as colunas.

### `grid-column` e `grid-row`

Aplicam-se aos elementos de dentro da grelha. Permitem escolher a posição ou fazer um elemento ocupar várias células.

Exemplo, para uma caixa com `class="caixa destaque"`:

```css
.destaque {
  grid-column: span 2;
}
```

O `span 2` faz essa caixa ocupar duas colunas. Duas classes no mesmo elemento separam-se por um espaço.

Os números em `grid-column` referem-se aos limites verticais das colunas. Numa grelha de duas colunas, há três: à esquerda, ao meio e à direita.

O `1` indica o primeiro limite e o `-1` indica o último.

| Declaração | O que faz |
| --- | --- |
| `grid-column: span 2;` | Ocupa duas colunas |
| `grid-row: span 2;` | Ocupa duas linhas |
| `grid-column: 1 / -1;` | Ocupa todas as colunas, do primeiro ao último limite vertical |

### `justify-items` e `align-items`

No Grid, `justify-items` alinha cada elemento na horizontal dentro da sua célula. O `align-items` faz o mesmo na vertical.

Exemplo:

```css
.grelha {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 80px 80px;
  gap: 1rem;
  justify-items: center;
  align-items: center;
}
```

Cada caixa fica centrada na sua célula, nas duas direções.

Valores para as duas propriedades:

- `start`: no início, à esquerda ou em cima.
- `center`: ao centro.
- `end`: no fim, à direita ou em baixo.
- `stretch`: estica a caixa para preencher a célula, quando não tem uma dimensão fixa nessa direção.

## O posicionamento

Por omissão, o browser põe cada caixa no seu lugar, pela ordem do HTML, e esse lugar empurra as seguintes. Esta arrumação chama-se **fluxo normal**.

### `position`

Diz como a caixa se põe na página.

| Valor | O que faz |
| --- | --- |
| `static` | A posição normal, no fluxo, por omissão. Não usa o `top`, o `right`, o `bottom` nem o `left` |
| `relative` | Desloca a caixa a partir do seu lugar, que continua reservado |
| `absolute` | Tira a caixa do fluxo e põe-na num ponto exato da caixa de referência |
| `fixed` | Tira a caixa do fluxo e prende-a à janela do browser, mesmo quando desces a página |
| `sticky` | Deixa a caixa no fluxo e prende-a à janela, enquanto o elemento que a contém está à vista |

Usa o Flexbox ou o Grid para arrumar a página. O `position` serve, por exemplo, para pôr uma etiqueta no canto de um cartão.

### `top`, `right`, `bottom` e `left`

Dizem a distância a que a caixa fica, e de que lado. Com `position: static`, não fazem nada. As medidas são, por exemplo, `10px` ou `1rem`, e o `0` não precisa de unidade.

Cada propriedade diz de que lado a caixa se afasta. O `top: 10px` afasta-a 10 píxeis de cima, e por isso, com `relative`, a caixa desce.

### Deslocar com `relative`

O deslocamento parte do lugar onde a caixa estaria.

Exemplo, para um elemento com `class="aviso"`:

```css
.aviso {
  position: relative;
  top: 10px;
  left: 20px;
}
```

A caixa desce 10 píxeis e avança 20 para a direita. O lugar dela continua reservado, e os elementos seguintes não sobem para o ocupar.

Com `right: 20px`, ia para a esquerda. Com `bottom: 10px`, subia. A caixa deslocada pode ficar por cima de outra.

### Pôr uma etiqueta num canto com `absolute`

A caixa com `absolute` não ocupa lugar no fluxo, e fica a uma distância exata da caixa de referência. Neste exemplo, a referência é o cartão, que tem `position: relative`.

No HTML:

```html
<div class="cartao">
  <p class="etiqueta">Novo</p>
  <p>Caderno azul de capa dura.</p>
</div>
```

No CSS:

```css
.cartao {
  position: relative;
  padding: 1rem;
  padding-top: 3rem;
  border: 1px solid #1f1f1f;
}

.etiqueta {
  position: absolute;
  top: 0.5rem;
  right: 0.5rem;
  margin: 0;
}
```

A etiqueta fica a `0.5rem` do topo e da direita, por dentro da borda do cartão. O `padding-top` do cartão deixa-lhe espaço, para não tapar o texto.

Para encontrar a caixa de referência, o browser sobe na árvore a partir da etiqueta: o pai, o pai do pai, e assim por diante. A primeira caixa com um `position` diferente de `static` é a referência. Se nenhuma tiver, a referência é a primeira janela da página, a que vês antes de descer.

### Prender à janela com `fixed`

A caixa fica sempre no mesmo sítio da janela, mesmo quando desces a página.

Exemplo, para uma ligação com `class="ajuda"`:

```css
.ajuda {
  position: fixed;
  right: 1rem;
  bottom: 1rem;
}
```

A ligação fica a `1rem` da direita e de baixo da janela. Não ocupa lugar e pode tapar o conteúdo, sobretudo num telemóvel.

### Prender ao topo com `sticky`

A caixa fica no seu lugar até chegar ao limite indicado, quando desces a página. Aí fica presa, enquanto o elemento que a contém está à vista.

Exemplo, para um menu com `class="menu"`:

```css
.menu {
  position: sticky;
  top: 0;
  background-color: white;
}
```

O menu fica preso ao topo da janela enquanto desces. O lugar dele continua reservado no fluxo. Precisa de um limite, como o `top: 0`.

### `z-index`

Escolhe que caixa fica à frente quando duas se sobrepõem. Entre caixas com um `position` diferente de `static`, a do número maior fica à frente. Sem `z-index`, fica à frente a que vem depois no HTML.

Exemplo, para um menu preso ao topo e cartões com `position: relative`, que passavam por cima dele:

```css
.menu {
  position: sticky;
  top: 0;
  z-index: 1;
}
```

O menu fica à frente dos cartões, que não têm `z-index`.

## Listas e tabelas

### `list-style-type`

Muda a marca dos itens de uma lista.

Exemplo:

```css
ul {
  list-style-type: square;
}
```

Valores:

- `disc`: um ponto.
- `square`: um quadrado.
- `decimal`: números.
- `none`: sem marca.

O atalho `list-style: none` faz o mesmo que `list-style-type: none`.

### `border-collapse`

Junta as bordas das células de uma tabela numa só linha, em vez de duas.

Exemplo:

```css
table {
  border-collapse: collapse;
}
```

![Rodapé](../imagens/rodape.png)
