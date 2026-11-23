![Cabeçalho](../../imagens/cabecalho.png)

# Ficha de exercícios: Acessibilidade e frameworks de CSS

Praticas a auditoria de acessibilidade, os nomes, o ARIA e a comparação do teu CSS com o Bootstrap. Os exercícios 1 a 6 são obrigatórios. Guarda tudo numa pasta desta ficha, fora do teu site. Lá ficam o `respostas.md` dos exercícios 1, 2, 3 e 6, e as pastas `banda-da-escola-ensaios`, do exercício 4, e `banda-da-escola-bootstrap`, do exercício 5. Entregas a pasta da ficha da forma que o professor disser. Para rever: o [guia do tema](../05-acessibilidade-e-frameworks-de-css.md) e o [laboratório](../laboratorios/05-acessibilidade-e-frameworks-de-css-laboratorio.md).

## O cenário

A Banda da Escola, das fichas anteriores, quer que o site dela possa ser usado por toda a escola. Nos exercícios 1 a 3, lês pedaços do site e registas um problema. No exercício 4, corriges a página dos ensaios abertos. No exercício 5, refazes os cartões dos músicos com o Bootstrap, e no 6 lês a página de um colega que o usa.

## Exercício 1: Os nomes das ligações e das imagens

Para cada pedaço do site da banda, diz o nome acessível da ligação ou, quando não há ligação, da imagem, e se é um problema. Quando for, reescreve o pedaço.

**a)** No cabeçalho, uma ligação para a página dos concertos:

```html
<a href="concertos.html"><img src="imagens/bilhete.svg" alt="Bilhete amarelo com uma estrela" width="40" height="40"></a>
```

**b)** No rodapé, uma ligação para a página dos contactos:

```html
<a href="contactos.html"><img src="imagens/envelope.svg" alt="" width="20" height="20"> Contactos</a>
```

**c)** Na página inicial, entre duas secções, um desenho que só serve para as separar:

```html
<img src="imagens/separador.svg" alt="Linha ondulada dourada" width="600" height="20">
```

Rever: [Cada ligação e cada imagem têm um nome](../05-acessibilidade-e-frameworks-de-css.md#cada-ligação-e-cada-imagem-têm-um-nome) e [O texto alternativo](../02-html-e-semantica.md#o-texto-alternativo).

## Exercício 2: O ARIA certo e o ARIA a mais

Cada pedaço está na página `concertos.html` do site da banda. Diz se o ARIA está certo, se está errado ou se está a mais, e porquê. Quando não estiver certo, escreve a correção.

**a)**

```html
<div role="button">Ouvir a música do concerto</div>
```

**b)**

```html
<li><a href="index.html" aria-current="page">Início</a></li>
<li><a href="concertos.html">Concertos</a></li>
```

**c)**

```html
<nav aria-hidden="true">
  <ul>
    <li><a href="index.html">Início</a></li>
    <li><a href="concertos.html">Concertos</a></li>
  </ul>
</nav>
```

**d)**

```html
<nav role="navigation">
  <ul>
    <li><a href="index.html">Início</a></li>
    <li><a href="concertos.html">Concertos</a></li>
  </ul>
</nav>
```

Rever: [O ARIA só entra quando o HTML não chega](../05-acessibilidade-e-frameworks-de-css.md#o-aria-só-entra-quando-o-html-não-chega), [Ligação ou botão](../02-html-e-semantica.md#ligação-ou-botão) e [Os pontos de referência](../02-html-e-semantica.md#os-pontos-de-referência).

## Exercício 3: O registo de um problema

Uma colega fez a auditoria à página dos concertos e anotou isto: "No calendário, os concertos esgotados estão a vermelho, e os outros a preto. Um parágrafo diz que os concertos a vermelho já não têm bilhetes. O vermelho tem 5,44 de contraste com o fundo branco."

Regista o problema com as quatro linhas do guia. Na quarta, escreve a correção que propões e como a confirmarias.

Rever: [Um problema regista-se pelo efeito em quem usa a página](../05-acessibilidade-e-frameworks-de-css.md#um-problema-regista-se-pelo-efeito-em-quem-usa-a-página) e [A auditoria faz-se à mão, com uma lista](../05-acessibilidade-e-frameworks-de-css.md#a-auditoria-faz-se-à-mão-com-uma-lista).

<details>
<summary>Pista</summary>

Imagina a página a preto e branco. O que deixas de saber, e quem fica sempre assim?

</details>

## Exercício 4: A página dos ensaios sem barreiras

Dentro da pasta da ficha, cria a pasta `banda-da-escola-ensaios`. Põe nela uma cópia da [imagem provisória](../laboratorios/02-html-e-semantica-laboratorio/imagem-provisoria.svg) do laboratório 02, com o mesmo nome, e estes dois ficheiros, sem mudar nada. As páginas `index.html` e `inscricoes.html` não existem: imagina que existem. A página tem cinco problemas de acessibilidade.

O `ensaios.html`:

```html
<!doctype html>
<!-- Página dos ensaios abertos da Banda da Escola. Tem problemas de
     acessibilidade de propósito, para os encontrares. Conteúdo fictício. -->
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Ensaios | Banda da Escola</title>
    <link rel="stylesheet" href="estilos.css">
  </head>
  <body>
    <header>
      <p>Banda da Escola</p>
      <nav>
        <ul>
          <li><a href="index.html">Início</a></li>
          <li><a href="ensaios.html" aria-current="page">Ensaios</a></li>
        </ul>
      </nav>
    </header>
    <main>
      <h1>Os ensaios abertos</h1>
      <p>Num ensaio aberto, experimentas tocar com a banda.</p>
      <!-- Imagem provisória: a fotografia de um ensaio vai entrar aqui. -->
      <img src="imagem-provisoria.svg" alt="imagem-provisoria.svg" width="400" height="300">

      <section>
        <h3>As próximas sessões</h3>
        <ul>
          <li>Sexta-feira, 4 de dezembro, às 17h, na sala de música.</li>
          <li>Sexta-feira, 11 de dezembro, às 17h, na sala de música.</li>
          <li>Sexta-feira, 8 de janeiro, às 17h, no auditório.</li>
        </ul>
      </section>

      <section>
        <h3>A inscrição</h3>
        <p>Cada sessão tem 10 lugares. Vê <a href="inscricoes.html">como te inscreves numa sessão</a>.</p>
      </section>
    </main>
    <footer>
      <p>Site da Banda da Escola. Conteúdo fictício.</p>
    </footer>
  </body>
</html>
```

O `estilos.css`:

```css
/* estilos.css: a folha de estilos da página dos ensaios abertos da Banda da Escola. */

/* A letra e o espaço entre as linhas, para a página toda. */
body {
  margin: 0;
  font-family: system-ui, "Segoe UI", Arial, sans-serif;
  line-height: 1.5;
}

/* Nenhuma imagem passa da largura da caixa onde está. */
img {
  max-width: 100%;
  height: auto;
}

/* O cabeçalho: o nome da banda e o menu, sobre o vermelho-escuro da banda. */
header {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  color: #ffffff;
  background-color: #7a1f1f;
}

/* O nome da banda, sem a margem dos parágrafos. */
header p {
  margin: 0;
  font-weight: bold;
}

/* O menu: os itens lado a lado, sem bolinhas nem recuo. */
nav ul {
  display: flex;
  gap: 1rem;
  margin: 0;
  padding: 0;
  list-style: none;
}

/* As ligações do cabeçalho ficam brancas. */
header a {
  color: #ffffff;
}

/* A ligação da página onde se está, a negrito. */
nav a[aria-current="page"] {
  font-weight: bold;
}

/* O foco do teclado, com uma moldura clara. */
a:focus-visible {
  outline: 3px solid #eeeeee;
  outline-offset: 2px;
}

/* O conteúdo ao centro, sem passar de uma largura confortável para ler. */
main {
  max-width: 60rem;
  margin: 0 auto;
  padding: 1rem;
}

/* O rodapé: letra mais pequena e mais clara, ao centro. */
footer {
  padding: 1rem;
  font-size: 0.875rem;
  color: #999999;
  text-align: center;
}
```

Faz a auditoria da página e corrige os cinco problemas. No fim, a página passa nas oito verificações da lista do guia, em todas as ligações e em todos os fundos. Num comentário no fim do `ensaios.html`, antes de `</body>`, escreve a lista dos cinco problemas que encontraste e, para cada um, a verificação que falhava.

Rever: [A auditoria faz-se à mão, com uma lista](../05-acessibilidade-e-frameworks-de-css.md#a-auditoria-faz-se-à-mão-com-uma-lista).

<details>
<summary>Pista</summary>

Faz as oito verificações por ordem e não saltes nenhuma.

</details>

## Exercício 5: Os músicos numa grelha do Bootstrap

Dentro da pasta da ficha, cria a pasta `banda-da-escola-bootstrap` e, nela, o ficheiro `musicos-bootstrap.html`, copiado tal como está:

```html
<!doctype html>
<!-- Os músicos da Banda da Escola em cartões do Bootstrap. Conteúdo fictício. -->
<html lang="pt-PT">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Músicos com o Bootstrap | Banda da Escola</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.9/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-yEPZ7jP9S0QKiUQ0m3jjsO4ProIW7wvR9gXkI7JOGa2XVsw53Yke2bsdkBbjmmiX" crossorigin="anonymous">
  </head>
  <body>
    <main class="container">
      <h1>Os músicos da banda</h1>
      <ul class="row g-3 list-unstyled">
        <li><div class="card h-100"><div class="card-body">Inês: voz.</div></div></li>
        <li><div class="card h-100"><div class="card-body">Tomás: guitarra.</div></div></li>
        <li><div class="card h-100"><div class="card-body">Leonor: baixo.</div></div></li>
        <li><div class="card h-100"><div class="card-body">Rui: bateria.</div></div></li>
        <li><div class="card h-100"><div class="card-body">Beatriz: teclado.</div></div></li>
        <li><div class="card h-100"><div class="card-body">Gonçalo: saxofone.</div></div></li>
        <li><div class="card h-100"><div class="card-body">Marta: violino.</div></div></li>
      </ul>
    </main>
  </body>
</html>
```

A classe `container` é a caixa do Bootstrap para o conteúdo da página, com espaço dos lados. Só com classes do Bootstrap, nos `li`, e sem CSS teu, os cartões têm de cumprir estes casos:

| Largura do ecrã | Colunas |
| ---: | ---: |
| 320 píxeis | 1 |
| 768 píxeis | 3 |
| 1280 píxeis | 4 |

Em nenhuma largura aparece a barra horizontal. Num comentário por cima do `ul`, escreve que classes escolheste e a partir de que largura vale cada uma.

Rever: [As classes do framework vêm da documentação](../05-acessibilidade-e-frameworks-de-css.md#as-classes-do-framework-vêm-da-documentação).

<details>
<summary>Pista</summary>

Na documentação do Bootstrap, a página Grid system tem uma tabela, Grid options, com o nome e a largura de cada ponto de mudança.

</details>

## Exercício 6: Quem ganha quando o Bootstrap chega

Um colega juntou o Bootstrap à página dos músicos dele. A página tem títulos `h2` dentro do `main` e cartões com a classe `card`. No `head`, as duas folhas estão por esta ordem:

```html
<link rel="stylesheet" href="estilos.css">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.9/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-yEPZ7jP9S0QKiUQ0m3jjsO4ProIW7wvR9gXkI7JOGa2XVsw53Yke2bsdkBbjmmiX" crossorigin="anonymous">
```

E o `estilos.css` dele tem estas três regras:

```css
body {
  background-color: #fdf6e3;
}

main h2 {
  color: #7a1f1f;
}

.card {
  --bs-card-border-color: #b8c4d6;
}
```

No Bootstrap, a regra do fundo apanha o `body`, a da cor dos títulos apanha o `h2`, e a da borda apanha o `.card`.

**a)** Para cada uma das três regras do colega, diz se ela se vê na página ou não, e porquê.

**b)** Escreve a correção que faz as três regras verem-se na página.

Rever: [A ordem das folhas de estilos decide os conflitos](../05-acessibilidade-e-frameworks-de-css.md#a-ordem-das-folhas-de-estilos-decide-os-conflitos), [Um framework tem vantagens e custos](../05-acessibilidade-e-frameworks-de-css.md#um-framework-tem-vantagens-e-custos) e [A especificidade: o seletor mais preciso ganha](../03-css-e-flexbox.md#a-especificidade-o-seletor-mais-preciso-ganha).

## Desafios

1. No Windows, liga o Narrador, o leitor de ecrã do sistema, com Ctrl, a tecla do Windows e Enter, e usa auscultadores. No macOS, o leitor de ecrã é o VoiceOver, que se liga com Cmd e F5. Abre a página dos ensaios do exercício 4, a corrigida, e percorre as ligações com Tab. Escreve no `respostas.md` o que o leitor de ecrã diz na ligação "Início" e na ligação "Ensaios", e a diferença entre as duas. No fim, desliga o leitor de ecrã com o mesmo atalho.
2. Liga o servidor local na pasta `banda-da-escola-ensaios` e analisa com o Lighthouse a página dos ensaios, antes e depois das tuas correções. Para teres a versão de antes, copia outra vez os dois ficheiros do enunciado, com os nomes `ensaios-antes.html` e `estilos-antes.css`. No `ensaios-antes.html`, muda o `href` da folha de estilos para `estilos-antes.css`. Escreve no `respostas.md` quais dos cinco problemas o Lighthouse encontrou e quais não, e porquê.

## Critérios de conclusão

- O `respostas.md` tem as respostas aos exercícios 1, 2, 3 e 6, com o número do exercício e a letra da alínea.
- O problema do exercício 3 está registado com as quatro linhas.
- A página dos ensaios passa nas oito verificações, e o comentário no fim lista os cinco problemas.
- A página dos músicos com o Bootstrap tem 1, 3 e 4 colunas a 320, 768 e 1280 píxeis, sem CSS teu.
- O comentário do exercício 5 diz as classes e a partir de que largura vale cada uma.

![Rodapé](../../imagens/rodape.png)
