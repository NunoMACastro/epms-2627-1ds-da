![Cabeçalho](../../imagens/cabecalho.png)

# Ficha de exercícios: Responsividade e Grid

Praticas as contas das grelhas, as media queries e a forma de pôr uma página a funcionar em todas as larguras. Os exercícios 1 a 6 são obrigatórios. Guarda numa pasta desta ficha, fora do teu site, o `respostas.md` dos exercícios 1 a 3 e a pasta `banda-da-escola-musicos` dos exercícios 4 a 6. Entrega a pasta da ficha como o professor indicar. Para rever: o [guia do tema](../04-responsividade-e-grid.md) e o [laboratório](../laboratorios/04-responsividade-e-grid-laboratorio.md).

## O cenário

A Banda da Escola, das fichas anteriores, tem agora uma página dos músicos. Tem uma fotografia da banda, um cartão para cada músico e uma caixa para quem quer entrar na banda. Nos exercícios 1 a 3, lês regras de CSS. Nos exercícios 4 a 6, pões a página dos músicos a funcionar num telemóvel e num ecrã largo.

## Exercício 1: Quantas colunas cabem

A lista dos músicos tem esta regra:

```css
.musicos {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(12rem, 1fr));
  gap: 1rem;
}
```

Para cada largura do contentor da lista, diz quantas colunas tem a grelha e com que largura fica cada coluna, em píxeis.

**a)** 288 píxeis.

**b)** 400 píxeis.

**c)** 600 píxeis.

**d)** 928 píxeis.

Rever: [O minmax e o auto-fill escolhem o número de colunas](../04-responsividade-e-grid.md#o-minmax-e-o-auto-fill-escolhem-o-número-de-colunas) e [As unidades: px e rem](../03-css-e-flexbox.md#as-unidades-px-e-rem).

## Exercício 2: Que regra vale em cada largura

A página dos concertos tem estas três regras, por esta ordem, no fim do `estilos.css`:

```css
.concertos {
  display: grid;
  gap: 1rem;
}

@media (min-width: 36rem) {
  .concertos {
    grid-template-columns: 1fr 1fr;
  }
}

@media (min-width: 60rem) {
  .concertos {
    grid-template-columns: 1fr 1fr 1fr;
  }
}
```

Para cada largura do viewport, diz quantas colunas tem a lista dos concertos.

**a)** 500 píxeis.

**b)** 576 píxeis.

**c)** 800 píxeis.

**d)** 1280 píxeis.

**e)** Na alínea d), as duas media queries valem. Explica qual das duas dá as colunas, e porquê.

Rever: [Uma media query muda a arrumação a partir de uma largura](../04-responsividade-e-grid.md#uma-media-query-muda-a-arrumação-a-partir-de-uma-largura).

## Exercício 3: A grelha que não funciona

Um colega quis arrumar assim a página das fotografias da banda:

- as fotografias em colunas com pelo menos 12rem;
- a partir de 40rem de largura, a página em duas colunas, a da esquerda com o dobro da largura da da direita.

Escreveu isto:

```css
.fotografias {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(12rem 1fr));
  gap: 1rem;
}

.pagina-das-fotos {
  display: grid;
  gap: 1rem;
}

@media (max-width: 40rem) {
  .pagina-das-fotos {
    grid-template-columns: 2fr 1fr;
  }
}
```

No browser, as fotografias ficam uma por linha em todas as larguras. E as duas colunas da página aparecem no telemóvel e desaparecem no computador.

**a)** Encontra o erro que deixa as fotografias numa só coluna, diz porque acontece e escreve a linha corrigida.

**b)** Encontra o erro que troca os telemóveis pelos computadores, diz porque acontece e escreve a linha corrigida.

Rever: [O minmax e o auto-fill escolhem o número de colunas](../04-responsividade-e-grid.md#o-minmax-e-o-auto-fill-escolhem-o-número-de-colunas) e [Uma media query muda a arrumação a partir de uma largura](../04-responsividade-e-grid.md#uma-media-query-muda-a-arrumação-a-partir-de-uma-largura).

## Exercício 4: Nada sai da página dos músicos

Dentro da pasta da ficha, cria a pasta `banda-da-escola-musicos`. Copia para lá a [imagem provisória](../laboratorios/02-html-e-semantica-laboratorio/imagem-provisoria.svg) do laboratório 02, com o mesmo nome. Cria lá também estes dois ficheiros, copiados tal como estão.

O `musicos.html`:

```html
<!doctype html>
<!-- Página dos músicos da Banda da Escola. Conteúdo fictício. -->
<html lang="pt-PT">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Músicos | Banda da Escola</title>
    <link rel="stylesheet" href="estilos.css">
  </head>
  <body>
    <main>
      <h1>Os músicos da banda</h1>
      <div class="pagina">
        <section>
          <img src="imagem-provisoria.svg" alt="Imagem provisória" width="600" height="450">
          <ul class="musicos">
            <li>Inês: voz.</li>
            <li>Tomás: guitarra.</li>
            <li>Leonor: baixo.</li>
            <li>Rui: bateria.</li>
            <li>Beatriz: teclado.</li>
            <li>Gonçalo: saxofone.</li>
            <li>Marta: violino.</li>
          </ul>
        </section>
        <aside>
          <h2>Queres entrar na banda?</h2>
          <p>Aparece num ensaio, às sextas-feiras, na sala de música, e traz o teu instrumento.</p>
        </aside>
      </div>
    </main>
  </body>
</html>
```

O `estilos.css`:

```css
/* estilos.css: a folha de estilos da página dos músicos da Banda da Escola. */

/* A largura de cada caixa inclui o padding e a borda. */
* {
  box-sizing: border-box;
}

/* A letra e o espaço entre as linhas, para a página toda. */
body {
  margin: 0;
  font-family: system-ui, "Segoe UI", Arial, sans-serif;
  line-height: 1.5;
}

/* O conteúdo ao centro, sem passar de uma largura confortável para ler. */
main {
  max-width: 60rem;
  margin: 0 auto;
  padding: 1rem;
}

/* A lista dos músicos, sem bolinhas nem recuo. */
.musicos {
  padding: 0;
  list-style: none;
}

/* Cada músico num cartão com borda e cantos redondos. */
.musicos li {
  padding: 1rem;
  border: 1px solid #b8c4d6;
  border-radius: 0.5rem;
}

/* A caixa de quem quer entrar na banda, com um fundo claro. */
aside {
  width: 25rem;
  padding: 1rem;
  background-color: #eef2f8;
}
```

Abre a página na barra de dispositivos, a 320 píxeis: há uma barra de deslocamento horizontal. Sem mudar o HTML, corrige o `estilos.css` para que se cumpram estes casos:

- a 320, a 768 e a 1280 píxeis, não aparece a barra horizontal;
- em todas as larguras, a imagem mantém a proporção;
- a 1280, a imagem tem os 600 por 450 píxeis do HTML.

Num comentário no `estilos.css`, por cima de cada regra ou linha que acrescentaste ou mudaste, escreve que causa ela corrige.

Rever: [Uma página, muitos ecrãs](../04-responsividade-e-grid.md#uma-página-muitos-ecrãs) e [Uma imagem não pode ser mais larga do que a caixa](../04-responsividade-e-grid.md#uma-imagem-não-pode-ser-mais-larga-do-que-a-caixa). Rever também: [A página testa-se em várias larguras, com o zoom e com o teclado](../04-responsividade-e-grid.md#a-página-testa-se-em-várias-larguras-com-o-zoom-e-com-o-teclado).

<details>
<summary>Pista</summary>

No separador Elements, passa o rato pelos elementos, de fora para dentro, até encontrares o que passa da margem direita. Depois de cada correção, volta a testar.

</details>

## Exercício 5: Os cartões dos músicos

Na mesma página, sem mudar o HTML, os músicos passam a uma grelha de cartões com a mesma largura, com `1rem` de espaço entre eles. O número de colunas muda sozinho com a largura, sem nenhuma media query, e tem de cumprir estes casos, antes do exercício 6:

| Largura do ecrã | Colunas |
| ---: | ---: |
| 320 píxeis | 1 |
| 768 píxeis | 3 |
| 1280 píxeis | 4 |

Escolhe a largura mínima de cada cartão, num número inteiro de `rem`. Num comentário, escreve a conta que mostra que ela cumpre os três casos. Em todas as larguras, o cartão da Marta, o último, tem a largura dos outros.

Rever: [A Grid arruma em linhas e colunas](../04-responsividade-e-grid.md#a-grid-arruma-em-linhas-e-colunas) e [O minmax e o auto-fill escolhem o número de colunas](../04-responsividade-e-grid.md#o-minmax-e-o-auto-fill-escolhem-o-número-de-colunas).

## Exercício 6: A página em duas colunas

Nos ecrãs largos, a caixa de quem quer entrar na banda fica à direita da secção dos músicos, mais estreita do que ela. Nos ecrãs estreitos, fica por baixo, como está. Sem mudar o HTML:

- a 320 píxeis, a caixa fica por baixo da secção dos músicos;
- a 1280, fica à direita, mais estreita do que a secção;
- o ponto de mudança vem do conteúdo, e um comentário por cima da media query diz que conta ou que observação o escolheu;
- em nenhuma largura aparece a barra horizontal.

Testa também a largura do teu ponto de mudança e uma largura logo abaixo dele, e confirma no browser o que o comentário diz.

Rever: [Uma media query muda a arrumação a partir de uma largura](../04-responsividade-e-grid.md#uma-media-query-muda-a-arrumação-a-partir-de-uma-largura) e [O ponto de mudança escolhe-se pelo conteúdo](../04-responsividade-e-grid.md#o-ponto-de-mudança-escolhe-se-pelo-conteúdo).

## Desafios

1. Na página dos músicos, troca o `auto-fill` por `auto-fit` e apaga cinco músicos do HTML, ficando com dois. Compara as duas versões a 1280 píxeis e explica no `respostas.md` a diferença. No fim, volta a pôr os sete músicos e o `auto-fill`.
2. Nas definições do browser, aumenta o tamanho da letra para "Muito grande" e abre a página dos músicos a 1280 píxeis. Explica no `respostas.md` o que mudou na arrumação, e porque é que um ponto de mudança em `rem` ajuda quem precisa de letra maior. No fim, volta a pôr o tamanho da letra que tinhas.

## Critérios de conclusão

- O `respostas.md` tem as respostas aos exercícios 1 a 3, com o número do exercício e a letra da alínea.
- A página dos músicos não tem barra horizontal a 320, a 768 nem a 1280 píxeis.
- A imagem mantém a proporção e, a 1280, tem 600 por 450.
- Os comentários do exercício 4 dizem que causa cada correção resolve.
- Os cartões dos músicos estão numa grelha com colunas iguais, e o comentário mostra a conta da largura mínima.
- A caixa de quem quer entrar na banda fica à direita nos ecrãs largos e por baixo nos estreitos.
- Um comentário explica o ponto de mudança.

![Rodapé](../../imagens/rodape.png)
