![Cabeçalho](../imagens/cabecalho.png)

# Consulta rápida de HTML

Aqui tens o esqueleto de uma página e as etiquetas de HTML que mais vais usar, cada uma com um exemplo.

## O esqueleto de uma página

Todas as páginas começam assim:

```html
<!doctype html>
<html lang="pt-PT">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Título do separador</title>
  </head>
  <body>
    <h1>Título da página</h1>
    <p>O primeiro parágrafo.</p>
  </body>
</html>
```

- `<!doctype html>`: diz ao browser que a página usa o HTML atual. Vai sempre na primeira linha.
- `<html>`: contém a página inteira. O `lang="pt-PT"` diz que a página está em português de Portugal.
- `<head>`: guarda informação sobre a página, que não aparece nela.
- `<meta charset="utf-8">`: faz os acentos aparecerem bem. Não tem etiqueta de fecho.
- `<meta name="viewport" ...>`: faz o telemóvel mostrar a página à largura do ecrã. Não tem etiqueta de fecho.
- `<title>`: o texto que aparece no separador do browser.
- `<body>`: contém tudo o que aparece na página.

## Comentários

Um comentário é uma nota para quem lê o código. O browser não o mostra na página, mas quem abre o código lê-o.

Exemplo:

```html
<!-- O menu tem uma ligação por página do site. -->
```

## Texto

### `<h1>` a `<h6>`

Cria um título. O `<h1>` é o título principal da página, e os outros são subtítulos, do mais importante (`<h2>`) ao menos importante (`<h6>`). Usa um só `<h1>` por página.

Exemplo:

```html
<h1>Inventário da sala</h1>
<h2>Material em falta</h2>
```

### `<p>`

Cria um parágrafo.

Exemplo:

```html
<p>Isto é um parágrafo.</p>
```

### `<strong>`

Marca um texto como importante. Aparece em negrito.

Exemplo:

```html
<p>O caderno está <strong>esgotado</strong>.</p>
```

### `<em>`

Dá ênfase a um texto. Aparece em itálico.

Exemplo:

```html
<p>A loja abre <em>só</em> de manhã.</p>
```

### `<br>`

Muda de linha dentro de um parágrafo. Não tem etiqueta de fecho.

Exemplo:

```html
<p>Rua Direita, 10<br>Lisboa</p>
```

### `<hr>`

Desenha uma linha horizontal, que separa duas partes da página. Não tem etiqueta de fecho.

Exemplo:

```html
<p>Primeira parte.</p>
<hr>
<p>Segunda parte.</p>
```

## Listas

### `<ul>`

Cria uma lista com pontos, para quando a ordem não interessa. Cada item vai num `<li>`.

Exemplo:

```html
<ul>
  <li>Caderno</li>
  <li>Caneta</li>
</ul>
```

### `<ol>`

Cria uma lista numerada, para quando a ordem interessa. Cada item vai num `<li>`.

Exemplo:

```html
<ol>
  <li>Abre o ficheiro.</li>
  <li>Guarda as alterações.</li>
</ol>
```

### `<li>`

Cria um item de uma lista. Vai sempre dentro de um `<ul>` ou de um `<ol>`.

Exemplo:

```html
<li>Caderno</li>
```

## Ligações e imagens

### `<a>`

Cria uma ligação para outra página ou outro sítio. O texto entre as etiquetas é o que se clica.

Exemplo:

```html
<a href="contactos.html">Contactos</a>
<a href="https://www.example.com">Um sítio de exemplo</a>
```

Atributos:

- `href`: o endereço para onde a ligação leva. Pode ser um caminho relativo, como `contactos.html`, ou um endereço completo, como `https://www.example.com`.
- `target`: onde a ligação abre. Com `target="_blank"`, abre num separador novo. Não o uses por hábito: quem lê é que decide se quer um separador novo.

### `<img>`

Mostra uma imagem. Não tem etiqueta de fecho.

Exemplo:

```html
<img src="imagens/caderno.png" alt="Caderno azul de capa dura" width="300" height="200">
```

Atributos:

- `src`: o caminho da imagem.
- `alt`: o texto que diz o que a imagem mostra. Aparece se a imagem não carregar, e os leitores de ecrã leem-no em voz alta.
- `width` e `height`: a largura e a altura da imagem, em píxeis.

### `<figure>` e `<figcaption>`

Junta uma imagem e a sua legenda. A legenda vai no `<figcaption>`, no princípio ou no fim do `<figure>`.

Exemplo:

```html
<figure>
  <img src="imagens/caderno.png" alt="Caderno azul de capa dura" width="300" height="200">
  <figcaption>O caderno que a sala recebeu este ano.</figcaption>
</figure>
```

A legenda vê-se por toda a gente e acrescenta contexto. O `alt` diz o que a imagem mostra, a quem não a vê. Por isso, os dois não repetem o mesmo texto.

### `<button>`

Cria um botão, que faz uma ação na própria página, como enviar um formulário. Para ir para outro sítio, usa-se uma ligação, e não um botão.

Exemplo:

```html
<button>Mostrar o material em falta</button>
```

## A estrutura da página

### `<div>`

Agrupa elementos numa caixa, para lhes aplicar estilos ou organizar a disposição com CSS.

Exemplo:

```html
<div class="aviso">
  <p><strong>Material em falta</strong></p>
  <p>Faltam 3 canetas.</p>
</div>
```

O atributo `class="aviso"` dá um nome ao grupo, que o CSS pode escolher com o seletor `.aviso`. A mesma classe pode aparecer em vários elementos.

Por omissão, o `<div>` começa numa linha nova e ocupa a largura disponível. Não acrescenta cor, borda nem espaçamento por si só.

O `<div>` não indica o significado do conteúdo. Quando o grupo é um menu, usa `<nav>`; quando é o conteúdo principal, usa `<main>`.

### `<header>`

Cria o cabeçalho da página, com o nome do site e, muitas vezes, o menu.

Exemplo:

```html
<header>
  <p>Inventário da sala</p>
</header>
```

### `<nav>`

Cria o menu, com as ligações para as outras páginas.

Exemplo:

```html
<nav>
  <a href="index.html">Início</a>
  <a href="material.html">Material</a>
</nav>
```

### `<main>`

Marca o conteúdo principal da página. Há só um por página.

Exemplo:

```html
<main>
  <h1>Material da sala</h1>
  <p>A sala tem 12 cadernos.</p>
</main>
```

### `<section>`

Cria uma parte do conteúdo, com o seu título.

Exemplo:

```html
<section>
  <h2>Material em falta</h2>
  <p>Faltam 3 canetas.</p>
</section>
```

### `<article>`

Cria um conteúdo que faz sentido sozinho, como uma notícia ou o cartão de um produto.

Exemplo:

```html
<article>
  <h3>Caderno A01</h3>
  <p>Caderno azul de capa dura. Restam 6 unidades.</p>
</article>
```

### `<aside>`

Marca um conteúdo relacionado com o resto, mas secundário, que se pode saltar, como uma dica ou uma nota ao lado.

Exemplo:

```html
<aside>
  <p>Dica: as canetas estão na gaveta de cima.</p>
</aside>
```

### `<footer>`

Cria o rodapé da página.

Exemplo:

```html
<footer>
  <p>Inventário da sala, 2026/2027</p>
</footer>
```

## Tabelas

### `<table>`

Cria uma tabela. Dentro dela vão as linhas e as células.

Exemplo:

```html
<table>
  <caption>Material da sala</caption>
  <thead>
    <tr>
      <th scope="col">Código</th>
      <th scope="col">Nome</th>
      <th scope="col">Quantidade</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>A01</td>
      <td>Caderno</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
```

### `<caption>`

Dá um nome à tabela. Vai logo a seguir à etiqueta de abertura `<table>`. O leitor de ecrã anuncia-o quando chega à tabela.

Exemplo:

```html
<caption>Material da sala</caption>
```

### `<thead>`

Junta a linha dos cabeçalhos da tabela.

Exemplo:

```html
<thead>
  <tr>
    <th scope="col">Código</th>
    <th scope="col">Nome</th>
  </tr>
</thead>
```

### `<tbody>`

Junta as linhas com os dados da tabela.

Exemplo:

```html
<tbody>
  <tr>
    <td>A01</td>
    <td>Caderno</td>
  </tr>
</tbody>
```

### `<tr>`

Cria uma linha da tabela.

Exemplo:

```html
<tr>
  <td>A01</td>
  <td>Caderno</td>
</tr>
```

### `<th>`

Cria uma célula de cabeçalho. Aparece em negrito e centrada.

Exemplo:

```html
<th scope="col">Nome</th>
```

Atributos:

- `scope`: a que se aplica o cabeçalho. Com `scope="col"`, à coluna; com `scope="row"`, à linha. O leitor de ecrã usa-o para dizer a que coluna e a que linha pertence cada valor.

### `<td>`

Cria uma célula de dados.

Exemplo:

```html
<td>Caderno</td>
```

![Rodapé](../imagens/rodape.png)
