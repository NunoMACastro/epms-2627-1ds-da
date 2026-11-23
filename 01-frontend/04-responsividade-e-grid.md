![Cabeçalho](../imagens/cabecalho.png)

# Responsividade e Grid

Neste guia aprendes a pôr o teu site a funcionar num telemóvel e num ecrã largo, com o mesmo HTML. Testas outras larguras nas ferramentas do programador e impedes que uma imagem ou uma palavra saiam da página. Arrumas em linhas e colunas com a Grid e mudas a arrumação a partir de uma largura, com uma media query, na Estante Digital.

Usa o CSS do tema 03, sobretudo a largura das caixas, as unidades e o Flexbox. Rever: [A largura de uma caixa e o box-sizing](03-css-e-flexbox.md#a-largura-de-uma-caixa-e-o-box-sizing), [As unidades: px e rem](03-css-e-flexbox.md#as-unidades-px-e-rem) e [Os itens que passam à linha seguinte e crescem](03-css-e-flexbox.md#os-itens-que-passam-à-linha-seguinte-e-crescem). Para praticar: [laboratório](laboratorios/04-responsividade-e-grid-laboratorio.md) e [ficha de exercícios](exercicios/04-responsividade-e-grid-exercicios.md).

## Neste guia

1. [Parte 1: Uma página para todos os ecrãs](#parte-1-uma-página-para-todos-os-ecrãs)
2. [Parte 2: As imagens que se adaptam](#parte-2-as-imagens-que-se-adaptam)
3. [Parte 3: Arrumar com a Grid](#parte-3-arrumar-com-a-grid)
4. [Parte 4: As media queries](#parte-4-as-media-queries)
5. [Parte 5: Testar a página](#parte-5-testar-a-página)
6. [Exemplo guiado: a Estante Digital responsiva](#exemplo-guiado-a-estante-digital-responsiva)

## Parte 1: Uma página para todos os ecrãs

### Uma página, muitos ecrãs

O mesmo site abre-se num telemóvel com 360 píxeis de largura e num portátil com 1280. Uma página feita só para o portátil, com uma caixa de `width: 900px`, não cabe no telemóvel. Aparece uma barra de deslocamento horizontal, e o visitante tem de andar para o lado para ler cada linha.

Uma **página responsiva** é uma página que se adapta à largura do ecrã, com o mesmo HTML e a mesma folha de estilos. No telemóvel, o conteúdo fica numa coluna; num ecrã largo, aproveita o espaço. Nada sai pelo lado em nenhuma largura.

A base é não fixar larguras em píxeis. Uma **largura fluida** acompanha a largura do ecrã. A Estante Digital do tema 03 já tem uma: o `main` tem `max-width: 60rem`, e não `width`. Até aos 60rem, ocupa a largura toda da janela, e daí para cima deixa de crescer, para as linhas não ficarem compridas demais para ler.

Os ecrãs não são três tamanhos fixos. Para testar, usam-se três larguras como amostras: 320 píxeis para um telemóvel pequeno, 768 para um tablet e 1280 para um portátil. Mas a página tem de funcionar também em todas as larguras pelo meio.

### As ferramentas do programador simulam outros ecrãs

A janela do browser não fica mais estreita do que uns 500 píxeis, e por isso não chega para ver a página como num telemóvel. As ferramentas do programador têm uma **barra de dispositivos**, que mostra a página com a largura que escolheres.

Abres as ferramentas com F12 e ligas a barra com Ctrl+Shift+M, ou Cmd+Shift+M no Mac. Também a ligas no ícone do telemóvel e do tablet, Toggle device toolbar, no canto de cima das ferramentas. Por cima da página aparece uma barra com Dimensions: Responsive e duas caixas, a largura e a altura, em píxeis. Escreves a largura na primeira caixa, como 320, e a página passa a ter essa largura. Também podes arrastar a margem direita da página, e a largura atualiza-se enquanto arrastas.

Na lista Dimensions há nomes de telemóveis, como iPhone SE, com as medidas de cada um. Para testar, a opção Responsive chega: a página não se faz para um telemóvel, faz-se para todas as larguras.

### O viewport diz ao telemóvel a largura da página

Desde o tema 02, as tuas páginas têm esta linha no `head`:

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

O **viewport** é a zona da janela onde a página aparece. A linha diz ao browser do telemóvel duas coisas. O viewport tem a largura do ecrã do aparelho, `width=device-width`, e a página começa sem zoom, `initial-scale=1`.

Sem esta linha, o browser de um telemóvel faz de conta que o ecrã tem 980 píxeis. Desenha a página com essa largura e encolhe-a até caber. O texto fica minúsculo, e a página fica com a arrumação pensada para os ecrãs largos. Por isso, a linha vai em todas as páginas.

## Parte 2: As imagens que se adaptam

### Uma imagem não pode ser mais larga do que a caixa

A imagem provisória do laboratório 02 tem `width="400"` no HTML. Num ecrã de 320 píxeis, o conteúdo do `main` tem 288 píxeis, os 320 menos os 16 do `padding` de cada lado. A imagem continua com 400, passa 112 píxeis da caixa do `main`, e a página inteira fica com 416 de largura.

A regra que resolve isto vale para todas as imagens do site:

```css
img {
  max-width: 100%;
  height: auto;
}
```

O `max-width: 100%` diz que a imagem nunca passa da largura da caixa onde está. Uma imagem mais pequena do que a caixa fica como está, e uma maior encolhe. O `height: auto` faz a altura acompanhar a largura, na mesma proporção.

Sem o `height: auto`, a altura escrita no HTML ficava igual. A imagem provisória ficava com 288 por 300 píxeis, mais alta do que devia. Uma fotografia ficava esticada, e a imagem provisória ganhava espaço vazio por cima e por baixo. Com o `height: auto`, fica com 288 por 216, a mesma proporção de 400 por 300.

O erro típico é escrever `width: 100%` em vez de `max-width: 100%`. Com o `width`, as imagens pequenas também esticam até à largura da caixa. O logótipo de 48 píxeis do cabeçalho da Estante ficava com 108.

## Parte 3: Arrumar com a Grid

### A Grid arruma em linhas e colunas

No laboratório 03, os cartões ficaram com o Flexbox, com `flex-basis: 15rem` e `flex-grow: 1`. Com mais um cartão, sete ao todo, numa janela de 1280 píxeis, cabem três por linha, e o sétimo fica sozinho na terceira linha. Cresce até ocupar a linha toda e fica com 928 píxeis de largura, quando os outros têm cerca de 299.

Isto acontece porque o Flexbox arruma numa só direção. Cada linha é tratada à parte, e os cartões de uma linha crescem para ocupar o espaço dessa linha, sem olhar para as outras.

A **Grid**, ou grelha, arruma em duas direções: em linhas e em colunas. As colunas são as mesmas para todas as linhas, e por isso os cartões ficam alinhados uns por baixo dos outros. Liga-se no contentor, como o Flexbox, e diz-se que colunas tem:

```css
.cartoes {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 1rem;
}
```

O `grid-template-columns` diz quantas colunas há e a largura de cada uma, separadas por espaços. O **fr**, de fração, é uma parte do espaço que sobra. Com `1fr 1fr 1fr`, as três colunas dividem o espaço em partes iguais. Com `2fr 1fr`, a primeira coluna fica com o dobro da segunda.

Num contentor de 928 píxeis, com dois espaços de 16 entre as colunas, sobram 896 píxeis, e cada coluna fica com um terço, 298,67. Os cartões entram pela ordem do HTML, da esquerda para a direita e de cima para baixo. O sétimo fica na primeira coluna da terceira linha, com a mesma largura dos outros.

```text
Flexbox: cada linha à parte          Grid: as mesmas colunas
┌────────┐ ┌────────┐ ┌────────┐     ┌────────┐ ┌────────┐ ┌────────┐
│   1    │ │   2    │ │   3    │     │   1    │ │   2    │ │   3    │
└────────┘ └────────┘ └────────┘     └────────┘ └────────┘ └────────┘
┌────────┐ ┌────────┐ ┌────────┐     ┌────────┐ ┌────────┐ ┌────────┐
│   4    │ │   5    │ │   6    │     │   4    │ │   5    │ │   6    │
└────────┘ └────────┘ └────────┘     └────────┘ └────────┘ └────────┘
┌──────────────────────────────┐     ┌────────┐
│              7               │     │   7    │
└──────────────────────────────┘     └────────┘
```

O desenho mostra os sete cartões nas duas arrumações, pela ordem do HTML. No Flexbox, o cartão 7 estica até ocupar a linha toda. Na Grid, fica na primeira coluna, por baixo do 1, com a largura dos outros.

Como os cartões seguem a ordem do HTML, o teclado e o leitor de ecrã continuam a ler pela mesma ordem. O Flexbox continua a servir para o que arruma numa só direção, como o cabeçalho e o menu.

### O minmax e o auto-fill escolhem o número de colunas

Três colunas fixas servem num ecrã largo, mas não num telemóvel. A 320 píxeis, cada coluna fica com uns 100 píxeis, e o texto dos cartões fica com uma ou duas palavras por linha. As palavras que não cabem numa coluna tão estreita não se partem e empurram a página para o lado. No exemplo do laboratório, a página ficou com 351 píxeis.

O que se quer é tantas colunas quantas couberem, cada uma com pelo menos 15rem, como o `flex-basis` do tema 03. Escreve-se assim:

```css
.cartoes {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(15rem, 1fr));
  gap: 1rem;
}
```

Lê-se de dentro para fora. O `minmax(15rem, 1fr)` é uma coluna que tem pelo menos 15rem e cresce para dividir o espaço que sobra em partes iguais. O `repeat` repete uma coluna: `repeat(3, 1fr)` é o mesmo que `1fr 1fr 1fr`. Com `auto-fill`, que quer dizer encher, no lugar do número, repete-se tantas vezes quantas couberem no contentor.

Com os sete cartões do laboratório, o browser faz as contas sozinho, no exemplo:

| Largura do ecrã | Espaço dos cartões | Colunas | Largura de cada cartão |
| ---: | ---: | ---: | ---: |
| 320 píxeis | 288 píxeis | 1 | 288 píxeis |
| 768 píxeis | 736 píxeis | 2 | 360 píxeis |
| 1280 píxeis | 928 píxeis | 3 | 298,67 píxeis |

A 768, cada coluna precisa de 15rem, que são 240 píxeis. Duas colunas, com o espaço entre elas, precisam de 496 píxeis; três precisavam de 752, e só há 736. Cabem duas, que crescem até encher os 736. A mesma regra serve as três larguras, sem nenhuma conta tua.

<details>
<summary>Para ires mais longe: o auto-fit e as células que ocupam várias colunas</summary>

Com o `auto-fill`, as colunas que cabem existem mesmo vazias. Se couberem três colunas e houver só dois cartões, a terceira fica vazia. Com `auto-fit` no lugar de `auto-fill`, as colunas vazias desaparecem, e os dois cartões crescem até encher a linha.

Um item da grelha pode ocupar mais do que uma coluna, com `grid-column: span 2`. E as zonas de uma página podem ter nomes, com `grid-template-areas`, para se arrumar a página inteira numa grelha.

</details>

### Um texto comprido não pode sair da caixa

Uma palavra não se parte a meio, e um endereço como `www.clubedexadrezdaescola.example.com` também não, porque não tem espaços. Num parágrafo, num ecrã de 320 píxeis, este endereço é mais largo do que a caixa. Sai pelo lado e cria a barra de deslocamento horizontal, como a imagem da Parte 2.

Numa grelha, a palavra comprida faz mais uma coisa. Uma coluna de `1fr` nunca fica mais estreita do que a palavra mais comprida que tem. No exemplo do laboratório, numa grelha com `1fr 1fr` a 640 píxeis, as duas colunas deviam ter 296. O endereço alargou a primeira para cerca de 315 e apertou a segunda para 277. Num cartão do `minmax(15rem, 1fr)`, a coluna não alarga, e o endereço sai do cartão.

A propriedade `overflow-wrap: anywhere` deixa o browser partir uma palavra em qualquer sítio, mas só quando ela não cabe na linha. As outras palavras continuam inteiras. Como se herda, escreve-se uma vez, no `body`, e vale para o texto todo:

```css
body {
  overflow-wrap: anywhere;
}
```

No exemplo, o endereço parte-se depois de `example.`, e o `com.` passa à linha seguinte. A página fica com os 320 píxeis do ecrã, e as duas colunas voltam a ter 296.

## Parte 4: As media queries

### Uma media query muda a arrumação a partir de uma largura

O wireframe largo da Estante Digital, do tema 01, põe os três grupos de recursos lado a lado. O estreito põe-nos uns por baixo dos outros. O `auto-fill` não serve aqui, porque se quer exatamente uma coluna num ecrã estreito e exatamente três num largo.

Uma **media query** é um bloco de CSS que só se aplica quando o viewport cumpre uma condição, como ter pelo menos uma certa largura:

```css
.grupos {
  display: grid;
  gap: 1rem;
}

@media (min-width: 49rem) {
  .grupos {
    grid-template-columns: repeat(3, 1fr);
  }
}
```

A primeira regra vale sempre: a grelha tem uma só coluna, porque não diz nenhuma. O `@media (min-width: 49rem)` quer dizer "quando o viewport tiver pelo menos 49rem de largura". Abaixo disso, as regras de dentro das chavetas não contam. A partir de 49rem, contam, e a grelha passa a ter três colunas.

A media query fica no fim da folha de estilos. Quando ela e outra regra com o mesmo seletor dão valores diferentes à mesma propriedade, ganha a que vem depois, como no tema 03. No fim da folha, a media query ganha sempre. Rever: [A ordem no ficheiro: a última regra ganha](03-css-e-flexbox.md#a-ordem-no-ficheiro-a-última-regra-ganha).

Esta forma de escrever chama-se **começar pelo ecrã estreito**. As regras de base são as do telemóvel, que é o caso mais simples, com uma coluna. As media queries com `min-width` só acrescentam o que muda nos ecrãs mais largos. Nem tudo precisa de uma media query. O cabeçalho da Estante, com o `flex-wrap`, já funciona em todas as larguras.

### O ponto de mudança escolhe-se pelo conteúdo

Porquê 49rem, e não 768 píxeis, a largura de um tablet? Há telemóveis, tablets e portáteis de todas as larguras, e uma lista de aparelhos fica sempre incompleta. O que interessa é a largura a partir da qual o conteúdo cabe na arrumação nova.

O **ponto de mudança** é a largura onde uma media query começa a valer. Escolhe-se pelo conteúdo. Na Estante, cada grupo tem cartões com pelo menos 15rem, por isso cada coluna precisa de 15rem:

| Parte | Largura |
| --- | ---: |
| Três colunas de 15rem | 45rem |
| Dois espaços de 1rem entre as colunas | 2rem |
| O `padding` do `main`, à esquerda e à direita | 2rem |
| Total | 49rem |

A partir de 49rem, que são 784 píxeis, os três grupos cabem lado a lado, cada um com 15rem. É esse o ponto de mudança.

Quando não há uma conta destas, o ponto de mudança encontra-se a olhar. Escreves a media query com um valor baixo, de experiência. Depois, na barra de dispositivos, estreitas a página aos poucos, a partir de uma largura grande, até o conteúdo deixar de caber na arrumação larga. Divides essa largura por 16, para a passar a `rem`, e arredondas para cima.

O ponto de mudança escreve-se em `rem`, e não em píxeis. Quem aumenta o tamanho da letra nas definições do browser fica com o `rem` maior. Assim, a arrumação larga só aparece quando o texto maior também cabe nela.

## Parte 5: Testar a página

### A página testa-se em várias larguras, com o zoom e com o teclado

Uma página responsiva não se dá por pronta numa só largura. Para cada página do site, faz-se esta verificação:

1. Na barra de dispositivos, as larguras de 320, 768 e 1280 píxeis, e as do meio, arrastando a margem da página devagar.
2. Em nenhuma largura aparece uma barra de deslocamento horizontal, nem a página mexe para o lado.
3. Com a barra de dispositivos desligada, põe o zoom do browser a 200%, com Ctrl e a tecla +, ou Cmd e + no Mac. A página continua a ler-se. O zoom a 200% numa janela de 1280 píxeis faz a página ter 640 de largura, e as media queries respondem a isso.
4. Com um texto mais comprido do que o previsto, como um nome grande num cartão, nada sai da caixa.
5. Com a tecla Tab, o foco passa pelas ligações pela ordem do HTML, e vê-se, em todas as larguras.

Quando a página mexe para o lado, há uma caixa mais larga do que o ecrã. Para a encontrar, no separador Elements, passa o rato pelos elementos, de fora para dentro. O browser pinta cada um na página, e o culpado é o que passa da margem direita. No separador Computed, vês a largura dele.

Um defeito encontrado regista-se com quatro coisas: o que viste, em que largura, a causa e a correção. Assim, quem ler o registo consegue repetir o teste e confirmar que o defeito desapareceu.

## Exemplo guiado: a Estante Digital responsiva

Neste exemplo, a Estante Digital do tema 03 passa a adaptar-se ao ecrã e cumpre finalmente o wireframe largo do tema 01. A folha de estilos ganha a regra das imagens, a dos grupos e uma media query, e mudam as regras do `body` e dos cartões. A página inicial ganha uma caixa nova. Os ficheiros completos estão na pasta [estante-digital-responsiva](../exemplos/frontend/estante-digital-responsiva/README.md) dos exemplos.

### Passo 1: Partir dos wireframes

Antes de mexer no CSS, comparam-se os dois wireframes da página inicial, do tema 01. Rever: [Passo 6: O wireframe estreito da página inicial](01-web-e-planeamento.md#passo-6-o-wireframe-estreito-da-página-inicial) e [Passo 7: O wireframe largo da página inicial](01-web-e-planeamento.md#passo-7-o-wireframe-largo-da-página-inicial).

| No wireframe estreito | No wireframe largo | Na Estante do tema 03 |
| --- | --- | --- |
| O menu por baixo do nome | O menu na linha do nome | Já está, com o `flex-wrap` do cabeçalho |
| Os três grupos uns por baixo dos outros | Os três grupos lado a lado | Ficam sempre uns por baixo dos outros |

Só a segunda linha falta, e é ela que este exemplo resolve.

### Passo 2: Testar antes de mudar

Abre-se a página inicial da [Estante Digital com CSS](../exemplos/frontend/estante-digital-com-css/README.md) na barra de dispositivos, nas três larguras de amostra. A 320 píxeis, os cartões ficam um por linha e não há barra horizontal. A 768 e a 1280, os grupos continuam uns por baixo dos outros, com dois cartões lado a lado. Funciona em todas as larguras, mas o ecrã largo não usa o espaço como o wireframe pede.

Na página do livro, a 320 píxeis, a capa tem 240 de largura. A caixa da figura só tem 208 por dentro, por causa das margens do `figure`. A capa passa da caixa, ainda sem criar a barra horizontal, mas uma capa um pouco maior já a criava.

### Passo 3: As imagens e as palavras compridas

Uma linha no `body` e uma regra nova protegem o site todo. No `body`, junta-se o `overflow-wrap`, e, a seguir ao `body`, a regra das imagens:

```css
body {
  /* As regras do tema 03 ficam; esta linha junta-se no fim. */
  overflow-wrap: anywhere;
}

img {
  max-width: 100%;
  height: auto;
}
```

A 320 píxeis, a capa do livro encolhe para a largura da figura, 208 píxeis, e a altura acompanha: 277. O logótipo do cabeçalho, com 48 píxeis, não muda, porque já é mais pequeno do que a caixa.

### Passo 4: Os cartões numa grelha

A regra dos cartões troca o Flexbox pela Grid. A regra de cada cartão perde o `flex-basis` e o `flex-grow`, que só servem no Flexbox:

```css
.cartoes {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(15rem, 1fr));
  gap: var(--espaco);
  padding: 0;
  list-style: none;
}

.cartoes li {
  padding: var(--espaco);
  border: 1px solid var(--cor-borda);
  border-radius: 0.5rem;
  background-color: var(--cor-cartao);
}
```

A 768 píxeis, os dois cartões de cada grupo ficam lado a lado, com 360 píxeis cada. A 320, ficam um por linha, como no tema 03. A 1280, cabem três colunas de cartões, e os dois cartões de cada grupo ocupam só as duas primeiras. A terceira fica vazia, até ao passo 6, porque o `auto-fill` cria as colunas que cabem, mesmo vazias.

### Passo 5: A caixa dos três grupos

Para pôr os três grupos lado a lado, eles têm de ser os filhos do mesmo contentor de grelha. O `main` não serve, porque tem também o título e os dois parágrafos. Por isso, as três `section` passam para dentro de uma caixa nova, e a árvore da página inicial fica assim:

```text
main
├── h1
├── p
├── p
└── div.grupos          a grelha dos grupos
    ├── section         Livros
    │   ├── h2
    │   └── ul.cartoes  a grelha dos cartões, dentro da dos grupos
    ├── section         Vídeos
    └── section         Sítios e aplicações
```

Em `index.html`:

```html
<div class="grupos">
  <section>
    <h2>Livros</h2>
    ...
  </section>
  <section>
    <h2>Vídeos</h2>
    ...
  </section>
  <section>
    <h2>Sítios e aplicações</h2>
    ...
  </section>
</div>
```

É um `div` porque não diz nada sobre o conteúdo: só serve para o CSS arrumar os grupos. No `estilos.css`, a caixa passa a ser uma grelha, ainda com uma só coluna:

```css
.grupos {
  display: grid;
  gap: var(--espaco);
}
```

Os grupos continuam uns por baixo dos outros, um pouco mais afastados.

### Passo 6: A media query

No fim do `estilos.css`, a media query dá três colunas à caixa dos grupos, a partir dos 49rem calculados na Parte 4:

```css
@media (min-width: 49rem) {
  .grupos {
    grid-template-columns: repeat(3, 1fr);
  }
}
```

A 784 píxeis, os três grupos ficam lado a lado, com 240 píxeis cada, os 15rem de um cartão. Os cartões de cada grupo ficam um por baixo do outro. Numa coluna de 240 píxeis, só cabe uma coluna de cartões, e o `auto-fill` resolve isso sozinho.

### Passo 7: Verificar

Repete-se o teste da Parte 5 nas três páginas:

| Largura | Os três grupos | Os cartões de cada grupo | Barra horizontal |
| ---: | --- | --- | --- |
| 320 píxeis | Uns por baixo dos outros | Um por linha | Não |
| 768 píxeis | Uns por baixo dos outros | Dois lado a lado | Não |
| 784 píxeis | Lado a lado | Um por baixo do outro | Não |
| 1280 píxeis | Lado a lado | Um por baixo do outro | Não |


Com o zoom a 200% numa janela de 1280 píxeis, a página fica com 640 de largura. Os grupos voltam a ficar uns por baixo dos outros. Com a tecla Tab, o foco passa por "Início", "Sobre" e "Primeiros passos na Web", pela ordem do HTML, em todas as larguras.

## Erros frequentes

### A media query nunca se aplica

O que se vê: em nenhuma largura a arrumação muda. No separador Styles, a declaração de dentro da media query aparece riscada.

Porque acontece: uma regra com o mesmo seletor, mais abaixo na folha, dá outro valor à mesma propriedade, e ganha por vir depois.

Como se corrige: passa a media query para o fim da folha de estilos, depois de todas as regras com o mesmo seletor.

### As colunas não aparecem

O que se vê: o `grid-template-columns` está escrito, mas os cartões continuam uns por baixo dos outros. Ou o texto de cada cartão fica em colunas estranhas.

Porque acontece: o `display: grid` e o `grid-template-columns` estão no elemento errado: no `li`, em vez do `ul`. A grelha liga-se no contentor, e são os filhos dele que se arrumam.

Como se corrige: passa as duas declarações para a regra do contentor, como `.cartoes`.

## Palavras novas deste guia

- Página responsiva: uma página que se adapta à largura do ecrã, com o mesmo HTML e a mesma folha de estilos.
- Largura fluida: uma largura que acompanha a do ecrã, com `max-width` em vez de `width`.
- Barra de dispositivos: a parte das ferramentas do programador que mostra a página com a largura que escolheres.
- Viewport: a zona da janela onde a página aparece.
- Grid: a forma de arrumar os filhos de uma caixa em linhas e colunas, com `display: grid`.
- fr: uma fração do espaço que sobra numa grelha, depois dos espaços entre as colunas.
- Media query: um bloco de CSS que só se aplica quando o viewport cumpre uma condição, como ter pelo menos uma certa largura.
- Começar pelo ecrã estreito: escrever as regras de base para o telemóvel e acrescentar, com media queries, o que muda nos ecrãs largos.
- Ponto de mudança: a largura onde uma media query começa a valer, escolhida pelo conteúdo.

As propriedades novas, e o que cada uma faz:

- `max-width: 100%` numa imagem: a imagem nunca passa da largura da caixa. `height: auto`: a altura acompanha a largura, na mesma proporção.
- `overflow-wrap: anywhere`: parte uma palavra só quando ela não cabe na linha.
- `display: grid`: liga a grelha no contentor.
- `grid-template-columns`: diz as colunas da grelha e a largura de cada uma.
- `repeat(3, 1fr)`: três colunas iguais. `repeat(auto-fill, minmax(15rem, 1fr))`: tantas colunas quantas couberem, cada uma com pelo menos 15rem.
- `@media (min-width: 49rem) { }`: as regras de dentro só valem com o viewport de 49rem ou mais.

## O que vem a seguir

No tema 05, revês o teu site para quem só usa o teclado e comparas o teu CSS com o de um framework.

## Para saber mais

- MDN Web Docs, [Conceitos básicos do layout em grid](https://developer.mozilla.org/pt-BR/docs/Web/CSS/CSS_grid_layout/Basic_concepts_of_grid_layout), em português do Brasil: a Grid, com exemplos que se podem experimentar.
- MDN Web Docs, [Usando media queries](https://developer.mozilla.org/pt-BR/docs/Web/CSS/CSS_media_queries/Using_media_queries), em português do Brasil: as media queries e as condições que podem ter.
- Chrome for Developers, [Device mode](https://developer.chrome.com/docs/devtools/device-mode), em inglês: a barra de dispositivos do Chrome, com imagens.

![Rodapé](../imagens/rodape.png)
