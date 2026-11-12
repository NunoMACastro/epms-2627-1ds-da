![Cabeçalho](../../imagens/cabecalho.png)

# Ficha de exercícios: CSS e Flexbox

Praticas as regras de CSS, a forma como o browser decide qual ganha, o modelo de caixa e o Flexbox. Os exercícios 1 a 8 são obrigatórios. Trabalha numa pasta só para esta ficha, fora da pasta do teu site. As respostas dos exercícios 1 a 5 vão para um ficheiro `respostas.md`, com o número do exercício e a letra da alínea. Os exercícios 6 a 8 fazem-se numa pasta `banda-da-escola`, dentro da pasta da ficha. No fim, entrega a pasta da ficha, com o `respostas.md` e a pasta `banda-da-escola`, como o professor indicar. Para rever: o [guia do tema](../03-css-e-flexbox.md) e o [laboratório](../laboratorios/03-css-e-flexbox-laboratorio.md).

## O cenário

Os exercícios voltam ao site imaginário da Banda da Escola. A página dos concertos tem um cabeçalho, com o nome da banda e um menu, e a lista dos próximos concertos. Nos exercícios 6 a 8, dás-lhe o aspeto todo, com uma folha de estilos tua.

## Exercício 1: As partes de uma regra

**a)** Nesta regra, escreve qual é o seletor e quais são as propriedades e os valores:

```css
.concertos h2 {
  color: #7a1f3d;
  font-size: 1.5rem;
}
```

**b)** Esta regra devia pôr o texto do rodapé ao centro e cinzento, mas não faz nada disso. Encontra os dois erros e escreve a regra corrigida:

```css
footer {
  text-align center;
  color: #55555;
}
```

Rever: [Uma regra de CSS: seletor, propriedade e valor](../03-css-e-flexbox.md#uma-regra-de-css-seletor-propriedade-e-valor).

## Exercício 2: Que elementos apanha cada seletor

Este é um pedaço do HTML de uma página da Banda da Escola:

```html
<header>
  <p class="nome">Banda da Escola</p>
  <nav>
    <a href="index.html">Início</a>
    <a href="concertos.html">Concertos</a>
  </nav>
</header>
<main>
  <h1>Próximos concertos</h1>
  <p class="destaque">Os bilhetes custam 2 euros.</p>
  <p>Os ensaios são abertos a toda a escola.</p>
  <p>Mais informação na <a href="contactos.html">página dos contactos</a>.</p>
</main>
```

Para cada seletor, diz quantos elementos apanha e quais são:

**a)** `p`

**b)** `.destaque`

**c)** `nav a`

**d)** `main a`

**e)** `header p`

Rever: [O seletor de classe](../03-css-e-flexbox.md#o-seletor-de-classe) e [O seletor descendente](../03-css-e-flexbox.md#o-seletor-descendente).

## Exercício 3: Que regra ganha

Em cada alínea, diz de que cor fica o texto e qual é a razão. A razão pode ser a ordem no ficheiro, a especificidade, a herança ou uma regra do browser. Usa o HTML do exercício 2.

**a)** De que cor ficam os parágrafos do `main`?

```css
p {
  color: #222222;
}

p {
  color: #444444;
}
```

**b)** De que cor fica o parágrafo dos bilhetes?

```css
.destaque {
  color: #7a1f3d;
}

p {
  color: #222222;
}
```

**c)** Com esta única regra, de que cor fica o parágrafo "Os ensaios são abertos a toda a escola"? E a ligação "página dos contactos"?

```css
main {
  color: #333333;
}
```

Rever: [A herança](../03-css-e-flexbox.md#a-herança), [A ordem no ficheiro: a última regra ganha](../03-css-e-flexbox.md#a-ordem-no-ficheiro-a-última-regra-ganha) e [A especificidade: o seletor mais preciso ganha](../03-css-e-flexbox.md#a-especificidade-o-seletor-mais-preciso-ganha).

## Exercício 4: A largura de um bilhete

Um bilhete do concerto é uma caixa com esta regra:

```css
.bilhete {
  width: 200px;
  padding: 10px;
  border: 2px solid #7a1f3d;
  margin: 20px;
}
```

**a)** Que largura ocupa a caixa no ecrã, da borda esquerda à borda direita, sem o `box-sizing`?

**b)** E com `box-sizing: border-box`?

**c)** E quanto espaço ocupa a caixa na linha, contando também a margem, sem o `box-sizing`?

Rever: [O modelo de caixa](../03-css-e-flexbox.md#o-modelo-de-caixa) e [A largura de uma caixa e o box-sizing](../03-css-e-flexbox.md#a-largura-de-uma-caixa-e-o-box-sizing).

## Exercício 5: rem em píxeis

O título do concerto tem `font-size: 1.75rem`, o texto tem `font-size: 0.875rem` e o espaço entre os cartões é `gap: 2rem`.

**a)** Quantos píxeis tem cada um, com a letra da página a 16 píxeis?

**b)** Uma pessoa que vê mal aumenta a letra do browser para 20 píxeis. Quantos píxeis passa a ter cada um?

**c)** Noutra página, o texto tem `font-size: 1.25rem` e o título tem `font-size: 22px`. Com a letra do browser a 20 píxeis, qual fica maior, o texto ou o título? Porquê?

Rever: [As unidades: px e rem](../03-css-e-flexbox.md#as-unidades-px-e-rem).

## Exercício 6: O cabeçalho da banda

Dentro da pasta da ficha, cria a pasta `banda-da-escola`, com este `concertos.html`, copiado tal como está, e um `estilos.css` vazio:

```html
<!doctype html>
<!-- Página dos concertos da Banda da Escola. Conteúdo fictício. -->
<html lang="pt-PT">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Concertos | Banda da Escola</title>
    <link rel="stylesheet" href="estilos.css">
  </head>
  <body>
    <header>
      <p>Banda da Escola</p>
      <nav>
        <a href="concertos.html">Concertos</a>
        <a href="#contactos">Contactos</a>
      </nav>
    </header>
    <main>
      <h1>Próximos concertos</h1>
      <ul class="concertos">
        <li>Festa de Natal: 12 de dezembro, no ginásio.</li>
        <li>Dia da Escola: 15 de março, no pátio.</li>
        <li>Fim de ano: 5 de junho, no auditório.</li>
      </ul>
      <section id="contactos">
        <h2>Contactos</h2>
        <p>Fala com a banda nos ensaios, às sextas-feiras, na sala de música.</p>
      </section>
    </main>
  </body>
</html>
```

No `estilos.css`, sem mudar o HTML, dá ao cabeçalho este aspeto:

- o nome da banda à esquerda e o menu à direita, alinhados pelo meio da altura;
- as duas ligações do menu lado a lado, com espaço entre elas;
- um fundo escuro e o texto e as ligações claros, com um contraste de 4,5 ou mais;
- nenhum espaço branco entre o cabeçalho e os lados da janela.

Num comentário no `estilos.css`, por cima da regra do cabeçalho, escreve o contraste que o browser mede entre o texto e o fundo.

Rever: [O Flexbox põe os filhos lado a lado](../03-css-e-flexbox.md#o-flexbox-põe-os-filhos-lado-a-lado) e [O espaço entre os itens e o alinhamento](../03-css-e-flexbox.md#o-espaço-entre-os-itens-e-o-alinhamento). Rever também: [A herança](../03-css-e-flexbox.md#a-herança), [O contraste entre o texto e o fundo](../03-css-e-flexbox.md#o-contraste-entre-o-texto-e-o-fundo) e [O browser já tem estilos](../03-css-e-flexbox.md#o-browser-já-tem-estilos).

<details>
<summary>Pista</summary>

Para cada coisa que queres pôr lado a lado, procura na árvore do HTML o pai direto delas. Para o espaço branco à volta, procura no separador Styles que elemento tem uma margem que vem dos estilos do browser.

</details>

## Exercício 7: Os cartões dos concertos

Na mesma página, sem mudar o HTML, cada concerto passa a ser um cartão:

- cada cartão tem fundo claro, uma borda, os cantos redondos e espaço entre o texto e a borda;
- o conteúdo principal tem espaço entre o texto e os lados da janela;
- numa janela larga, com o browser no ecrã todo, os três cartões ficam na mesma linha, com o mesmo tamanho e espaço entre eles;
- numa janela estreita, a mais estreita que o browser deixar, ficam um por baixo do outro, cada um com a largura toda;
- em nenhuma largura aparece uma barra de deslocamento horizontal.

Testa as duas larguras com a janela do browser. Num comentário no `estilos.css`, escreve a largura de partida que escolheste para cada cartão e porquê.

Rever: [Os itens que passam à linha seguinte e crescem](../03-css-e-flexbox.md#os-itens-que-passam-à-linha-seguinte-e-crescem) e [Fundos, bordas e cantos redondos](../03-css-e-flexbox.md#fundos-bordas-e-cantos-redondos).

<details>
<summary>Pista</summary>

A largura de partida decide quantos cartões cabem numa linha. Experimenta valores no painel Styles e vê quando é que o terceiro cartão salta para baixo.

</details>

## Exercício 8: O foco no cabeçalho

Percorre a página com a tecla Tab. Faz com que o foco nas duas ligações do menu se veja bem. A moldura contrasta com o fundo escuro do cabeçalho e não encosta ao texto da ligação. O foco tem de continuar a ver-se se alguém, mais tarde, mudar a cor do texto das ligações. Para o confirmares, muda por um momento a cor das ligações do menu para a cor do fundo do cabeçalho. A moldura tem de continuar a ver-se. Depois volta a pôr a cor que tinhas.

Rever: [As pseudo-classes :hover e :focus-visible](../03-css-e-flexbox.md#as-pseudo-classes-hover-e-focus-visible) e [O foco tem de se ver](../03-css-e-flexbox.md#o-foco-tem-de-se-ver).

## Desafios

1. No teu `estilos.css`, há cores que se repetem? Passa-as para variáveis de CSS, com nomes que digam para que servem, e confirma que a página fica igual.
2. Um colega escreveu esta folha para a página dos concertos. Num comentário no fim do teu `estilos.css`, diz que dois problemas de acessibilidade ela cria e como os corrigias:

   ```css
   a {
     text-decoration: none;
   }

   a:focus {
     outline: none;
   }
   ```

3. Quando o rato passa por cima de um cartão, a borda do cartão muda de cor. Escolhe uma cor com contraste com o fundo da página.

## Critérios de conclusão

- O `respostas.md` tem as respostas aos exercícios 1 a 5, com o número do exercício e a letra da alínea.
- O `concertos.html` está igual ao da ficha, e todo o aspeto vem do `estilos.css`.
- O cabeçalho e os cartões ficam como os exercícios 6 e 7 pedem, numa janela larga e numa estreita.
- Não aparece nenhuma barra de deslocamento horizontal.
- O foco vê-se nas duas ligações do menu.
- O `estilos.css` tem os dois comentários pedidos: o contraste do cabeçalho e a largura de partida dos cartões.

![Rodapé](../../imagens/rodape.png)
