![Cabeçalho](../imagens/cabecalho.png)

# HTML e semântica

Módulo Conceber aplicações para a web na vertente frontend. Neste guia aprendes a escrever páginas web com HTML, escolhendo cada elemento pelo que o conteúdo é, e não pelo aspeto que tem. Vês as páginas da Estante Digital construídas passo a passo e aprendes a verificar uma página. Lê-se ao teu ritmo, de preferência em mais do que uma vez. A teoria é longa, e não precisas de a decorar: vais voltar a ela muitas vezes, sempre que te surgir uma dúvida. Para praticar, há o [laboratório](02-html-e-semantica-laboratorio.md) e a [ficha de exercícios](02-html-e-semantica-exercicios.md) deste tema.

Este guia continua o guia [A Web, os utilizadores e o planeamento](01-web-e-planeamento.md), o primeiro desta área. Se já tiveste as primeiras aulas sobre HTML, vais reconhecer as primeiras secções. O guia retoma tudo desde o princípio, porque o vocabulário tem de ficar muito seguro antes de avançar. Depois acrescenta o que ainda falta. Falta o esqueleto completo, os títulos com hierarquia e as imagens com texto alternativo. Faltam também os elementos semânticos, as tabelas e a verificação de uma página. As páginas deste tema ainda não têm CSS, e por isso têm o aspeto que o browser lhes dá por omissão. Este tema também não usa Git. Se já fizeste o primeiro tema de Git, guarda uma versão da pasta do teu site depois de cada página. Se ainda não, é esta a pasta que vais pôr sob controlo de versões nesse tema. A partir daí, cada página nova fica registada no histórico.

## Neste guia

1. O que vais aprender
2. O que já sabes e vais usar
3. O que é o HTML
4. Elementos, etiquetas e atributos
5. Elementos dentro de elementos
6. Espaços e mudanças de linha
7. O esqueleto de uma página
8. O que vai no head
9. Títulos: de h1 a h6
10. Parágrafos e texto com significado
11. Listas
12. Ligações
13. Caminhos relativos
14. Imagens
15. O texto alternativo
16. Imagem com legenda: figure e figcaption
17. Comentários
18. Os elementos semânticos
19. Tabelas de dados
20. Como o browser lida com os erros
21. Verificar uma página
22. Exemplo guiado: as páginas da Estante Digital
23. Erros frequentes
24. Palavras novas deste guia
25. Verificar o que aprendeste
26. O que vem a seguir
27. Para saber mais

## O que vais aprender

No fim deste guia, consegues:

- explicar o que é um elemento, uma etiqueta e um atributo, e apontar cada um deles num pedaço de HTML;
- escrever de memória o esqueleto completo de uma página, do `<!doctype html>` ao `body`, com a língua, o `charset`, o `viewport` e o `title`;
- organizar o texto de uma página com parágrafos, listas e títulos de `h1` a `h6` que formam uma hierarquia coerente;
- ligar as páginas do teu site com caminhos relativos, e ligar a outros sites com endereços completos;
- pôr imagens numa página com o texto alternativo certo para o sítio onde estão, e usar `figure` e `figcaption` quando a imagem tem legenda;
- dividir uma página nas zonas `header`, `nav`, `main`, `section`, `article`, `aside` e `footer`, e justificar cada escolha pelo significado do conteúdo;
- construir uma tabela de dados com legenda e cabeçalhos, e explicar porque é que uma tabela não serve para arrumar uma página;
- verificar uma página: seguir as ligações, lê-la pela ordem do HTML, percorrê-la com o teclado e comparar a árvore do browser com o ficheiro.

## O que já sabes e vais usar

- A divisão de trabalho entre as três linguagens da Web. O HTML diz o que cada pedaço de conteúdo é, o CSS diz como se apresenta e o JavaScript diz como se comporta. Este guia é todo sobre a primeira. Está no guia [01 A Web, os utilizadores e o planeamento](01-web-e-planeamento.md), secção "Três linguagens, três trabalhos".
- O que faz o browser com um ficheiro HTML. Lê o texto, constrói uma árvore em memória chamada DOM e desenha a página a partir dessa árvore. Guia [01](01-web-e-planeamento.md), secção "O browser".
- A diferença entre abrir um ficheiro do teu computador e abrir uma página que veio de um servidor. O endereço do primeiro começa por `file://`, e o do segundo por `https://`. Guia [01](01-web-e-planeamento.md), secções "Cliente e servidor" e "O endereço de uma página".
- Ler um mapa do site e um wireframe. Guia [01](01-web-e-planeamento.md), secções "O mapa do site" e "O wireframe".
- O plano do teu site, com o mapa de pelo menos duas páginas e, se já os fizeste, os wireframes. Fizeste-o no tema 01, e é o ponto de partida do laboratório deste tema.
- Abrir as ferramentas do programador e usar o separador Elements. Guia [01](01-web-e-planeamento.md), secção "As ferramentas do programador", e o [laboratório do tema 01](01-web-e-planeamento-laboratorio.md). Se ainda não fizeste esse laboratório, o laboratório deste tema explica o mínimo no momento em que for preciso.

## O que é o HTML

HTML são as iniciais de *HyperText Markup Language*, que em português quer dizer linguagem de marcação de hipertexto. Vale a pena perceber as duas palavras difíceis, porque dizem o que o HTML faz.

**Hipertexto** é texto que tem ligações para outros textos. Um livro normal lê-se de uma ponta à outra. Um hipertexto lê-se saltando. Estás a ler uma página, encontras uma palavra sublinhada, carregas nela e passas para outra página, que por sua vez tem ligações para outras. A Web inteira é um enorme hipertexto. Foi para isso que o HTML foi inventado, como viste na história curta da Web no guia 01.

**Marcação** é o ato de pôr marcas num texto para dizer o que cada pedaço é. Imagina que o professor te dá um texto impresso e três marcadores de cores diferentes. Pede-te para pintar de amarelo os títulos, de verde as listas e de azul os nomes de livros. Depois de marcado, o texto não mudou uma única palavra, mas agora qualquer pessoa sabe o papel de cada pedaço. O HTML faz o mesmo, só que em vez de cores usa etiquetas escritas no próprio texto.

Vê a diferença com um exemplo. Este é um pedaço de texto sem marcação nenhuma:

```text
Estante Digital
Recursos de estudo recomendados pela turma
Livros
Primeiros passos na Web
Pequeno dicionário de HTML
```

Tu percebes que "Estante Digital" é o nome de um site e que "Livros" é o título de uma parte. Percebes também que as duas últimas linhas são uma lista. Percebes porque és uma pessoa e adivinhas pela experiência. O browser não adivinha.

Antes de continuares, tenta prever: se pusesses este texto, tal como está, num ficheiro `.html` e o abrisses no browser, aparecia em cinco linhas?

Não aparece. O browser junta tudo seguido, como se fosse uma só frase, com um espaço no sítio de cada mudança de linha. Aparece assim:

```text
Estante Digital Recursos de estudo recomendados pela turma Livros Primeiros passos na Web Pequeno dicionário de HTML
```

Ninguém lhe disse que eram coisas diferentes. A secção "Espaços e mudanças de linha", mais à frente, explica porquê.

Com marcação, o mesmo texto fica assim:

```html
<p>Estante Digital</p>
<h1>Recursos de estudo recomendados pela turma</h1>
<h2>Livros</h2>
<ul>
  <li>Primeiros passos na Web</li>
  <li>Pequeno dicionário de HTML</li>
</ul>
```

Agora o browser mostra um parágrafo, um título grande e um título um pouco mais pequeno. Por baixo, mostra uma lista com dois itens, cada um com uma bolinha à frente. As palavras são as mesmas. O que mudou foi que cada pedaço passou a dizer o que é.

Leitura guiada: lê o código linha a linha, de cima para baixo. Cada linha começa com uma marca entre `<` e `>`, que diz o que vem a seguir. O `p` é um parágrafo, o `h1` e o `h2` são títulos, o `ul` é uma lista e cada `li` é um item dela. A marca com a barra, como `</p>`, diz onde esse pedaço acaba. As duas linhas dos `li` estão mais à direita porque estão dentro da lista. A secção seguinte dá o nome a cada uma destas peças.

O HTML não é uma linguagem de programação. Uma linguagem de programação, como as que estás a aprender em Fundamentos de Programação, dá ordens ao computador. Faz esta conta, se isto acontecer faz aquilo, repete dez vezes. O HTML não dá ordens nem toma decisões. Descreve o conteúdo, e o browser lê essa descrição e mostra-a. Isto tem uma consequência prática que vais encontrar muitas vezes: quando te enganas a escrever HTML, não aparece nenhuma mensagem de erro. O browser tenta adivinhar o que querias dizer e continua. A secção "Como o browser lida com os erros", mais à frente, explica o que isso quer dizer e como se descobrem esses erros escondidos.

## Elementos, etiquetas e atributos

Estes três nomes vão aparecer em todas as aulas de HTML, e convém não os confundir.

Uma **etiqueta** (em inglês, *tag*) é uma palavra entre os sinais `<` e `>`. Há etiquetas de abertura, como `<h1>`, e etiquetas de fecho, que são iguais mas levam uma barra antes do nome, como `</h1>`. A etiqueta de abertura diz "começa aqui um título". A de fecho diz "acaba aqui o título".

Um **elemento** é o conjunto formado pela etiqueta de abertura, pelo conteúdo e pela etiqueta de fecho. É o elemento, e não a etiqueta, que representa uma coisa na página.

```html
<h1>Recursos de estudo recomendados pela turma</h1>
```

| Parte | Neste exemplo | O que é |
| --- | --- | --- |
| Etiqueta de abertura | `<h1>` | Marca o início do elemento |
| Conteúdo | `Recursos de estudo recomendados pela turma` | O texto que o elemento marca |
| Etiqueta de fecho | `</h1>` | Marca o fim do elemento; tem a barra antes do nome |
| Elemento | tudo junto, do `<h1>` ao `</h1>` | Um título de primeiro nível |

Uma forma de fixar a diferença: a etiqueta é a marca que escreves, e o elemento é a coisa marcada. Quando dizes "esta página tem três parágrafos", estás a contar elementos `p`. Quando dizes "esqueci-me de fechar a etiqueta", estás a falar da marca que falta escrever.

Um **atributo** é uma informação extra sobre um elemento. Escreve-se dentro da etiqueta de abertura, com a forma `nome="valor"`. Os atributos dizem coisas que não fazem parte do conteúdo visível. Numa ligação, por exemplo, o texto em que o utilizador carrega é o conteúdo, mas o destino da ligação é um atributo:

```html
<a href="sobre.html">Sobre</a>
```

Aqui, `a` é o nome do elemento (uma ligação) e `href` é o nome do atributo (o destino). `"sobre.html"` é o valor do atributo, e `Sobre` é o conteúdo, o texto que aparece na página. Quatro regras sobre atributos:

- escrevem-se sempre na etiqueta de abertura, nunca na de fecho;
- se houver mais do que um, separam-se com espaços, como em `<img src="imagens/logotipo.svg" alt="" width="48" height="48">`, que tem quatro atributos;
- o valor escreve-se entre aspas. Há casos em que o browser aceita sem aspas, mas basta um espaço dentro do valor para deixar de funcionar. Por isso, nas aulas usamos sempre aspas duplas;
- cada elemento aceita os seus atributos. `href` faz sentido numa ligação e não faz sentido num título.

Há elementos que não têm conteúdo e por isso não têm etiqueta de fecho. Chamam-se **elementos vazios**. O exemplo mais comum é a imagem. Uma imagem não tem texto lá dentro, e toda a informação de que precisa (o ficheiro, a descrição, o tamanho) está nos atributos.

```html
<img src="imagens/logotipo.svg" alt="" width="48" height="48">
```

Não existe `</img>`. Os elementos vazios que vais usar neste tema são `img`, `meta` e `br`. Em código escrito por outras pessoas vais encontrar às vezes `<img ... />`, com uma barra antes do `>`. O HTML aceita essa barra, mas ela não faz nada, e nos materiais da disciplina não a usamos.

Por último, o HTML não distingue maiúsculas de minúsculas nos nomes das etiquetas: `<H1>` e `<h1>` são a mesma coisa. A convenção de hoje é escrever tudo em minúsculas, e é essa que seguimos.

## Elementos dentro de elementos

Um elemento pode ter outros elementos dentro do seu conteúdo. A isto chama-se **aninhar** (ou encaixar) elementos:

```html
<p>Entrega o trabalho <strong>até sexta-feira</strong>, na sala 12.</p>
```

O elemento `strong` está dentro do elemento `p`. Diz-se que o `p` é o **pai** do `strong`, e que o `strong` é **filho** do `p`. Dois elementos com o mesmo pai são **irmãos**. Este vocabulário de família vai servir-te durante o ano inteiro, no CSS e no JavaScript.

A regra de ouro do aninhamento é esta: fecha-se primeiro o que se abriu por último. Pensa em caixas dentro de caixas. Se puseres uma caixa pequena dentro de uma grande, tens de fechar a pequena antes de fechar a grande. É a mesma regra dos parênteses em Matemática: em `[ ( 2 + 3 ) × 4 ]`, o parêntese curvo abre depois do reto e fecha antes dele.

No exemplo seguinte, as linhas entre `<!--` e `-->` são comentários: notas para quem lê o código, que o browser ignora. A secção "Comentários", mais à frente, explica-os melhor.

```html
<!-- Certo: o strong abriu dentro do p e fecha dentro do p. -->
<p>Isto é <strong>muito</strong> importante.</p>

<!-- Errado: o p fecha antes do strong, que abriu depois dele. -->
<p>Isto é <strong>muito importante.</p></strong>
```

Uma página inteira é uma grande estrutura de elementos dentro de elementos. No topo está o elemento `html`, que tem dois filhos, `head` e `body`. Cada um tem os seus filhos, e assim por diante. Esta estrutura desenha-se como uma árvore virada ao contrário, com a raiz em cima:

```text
html
├── head
│   ├── meta
│   └── title
└── body
    ├── header
    ├── main
    │   ├── h1
    │   └── p
    └── footer
```

É esta árvore que o browser constrói em memória quando lê o teu ficheiro. É a ela que se chama DOM, como viste no guia 01. No separador Elements das ferramentas do programador, a árvore aparece com pequenos triângulos, que abrem e fecham cada ramo.

### A indentação

Repara que, nos exemplos deste guia, cada elemento que está dentro de outro começa um pouco mais à direita. Esses espaços no início das linhas chamam-se **indentação**. O browser ignora-os por completo: a página fica igual com ou sem eles. Servem para as pessoas, porque mostram de relance quem está dentro de quem. Nos materiais usamos dois espaços por nível.

Sem indentação, um ficheiro de cinquenta linhas torna-se quase impossível de ler, e um erro de aninhamento fica escondido. Com indentação, uma etiqueta de fecho fora do sítio salta à vista, porque fica desalinhada da sua etiqueta de abertura. O VS Code tem um comando que indenta o ficheiro inteiro sozinho, chamado Format Document. O atalho é Shift+Alt+F no Windows e Shift+Option+F no Mac. Mesmo assim, habitua-te a indentar à medida que escreves.

## Espaços e mudanças de linha

O browser trata todos os espaços seguidos, tabulações e mudanças de linha como se fossem um único espaço.

Antes de continuares, tenta prever: estas duas versões dão o mesmo resultado no ecrã?

```html
<p>A Estante Digital reúne livros, vídeos e sítios.</p>

<p>
  A Estante Digital
  reúne livros,      vídeos e sítios.
</p>
```

Dão. As duas mostram o mesmo parágrafo, "A Estante Digital reúne livros, vídeos e sítios.", com um só espaço entre cada palavra.

Leitura guiada: o primeiro `p` tem o texto numa linha. O segundo tem o mesmo texto partido por três linhas, com espaços a mais no princípio e entre "livros," e "vídeos". O browser troca cada grupo de espaços e de mudanças de linha por um só espaço. Os que ficam no início e no fim do parágrafo, tira-os.

Há duas consequências. A primeira é boa: podes partir um parágrafo comprido por várias linhas no ficheiro, para ser mais fácil de ler, e o browser junta-as. A segunda apanha muitos principiantes. Carregar em Enter no ficheiro não muda de linha na página, e carregar várias vezes na barra de espaços não afasta palavras. Se queres um parágrafo novo, precisas de um elemento `p` novo.

Existe um elemento para mudar de linha dentro do mesmo parágrafo, o `br` (de *break*, quebra). É um elemento vazio. Usa-se quando a mudança de linha faz parte do próprio conteúdo, como nas linhas de uma morada ou nos versos de um poema:

```html
<p>
  Biblioteca da escola<br>
  Piso 1, junto ao pavilhão B
</p>
```

O browser mostra este parágrafo em duas linhas: "Biblioteca da escola" numa e "Piso 1, junto ao pavilhão B" na de baixo. A mudança de linha vem do `br`, e não do Enter que está no ficheiro depois dele.

O `br` nunca se usa para afastar blocos de texto, nem se empilham vários `br` para criar espaço. Afastar coisas é trabalho do CSS, no próximo tema. Se usares `br` para fazer espaço, estás a pôr aspeto no HTML. É isso que a divisão de trabalho entre as três linguagens tenta evitar.

## O esqueleto de uma página

Todas as páginas HTML começam com a mesma estrutura, a que chamamos o **esqueleto**. É isto:

```html
<!doctype html>
<html lang="pt-PT">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Início | Estante Digital</title>
  </head>
  <body>
    <!-- Aqui vai tudo o que aparece na página. -->
  </body>
</html>
```

São onze linhas. Uma delas, entre `<!--` e `-->`, é um comentário: só marca o sítio onde vai o conteúdo, e o browser ignora-a. As outras dez estão lá, cada uma, por uma razão.

**`<!doctype html>`** não é um elemento. É uma declaração, e diz ao browser que o documento está escrito em HTML moderno. Esta linha existe por causa da história dos browsers. Nos anos 90, cada browser desenhava as páginas à sua maneira, e os sites foram feitos a contar com esses defeitos. Quando os browsers passaram a seguir as regras oficiais, os sites antigos ficariam desarrumados. A solução foi esta: se a página começa com o doctype, o browser segue as regras modernas. Se não começa, entra num **modo de compatibilidade** que imita os browsers antigos. Mais tarde, o teu CSS vai comportar-se nesse modo de maneiras estranhas, que nada no teu código explica. Por isso o doctype é sempre a primeira linha do ficheiro, sem nada antes.

**`<html lang="pt-PT">`** é o **elemento raiz**: contém todos os outros. O atributo `lang` diz em que língua está escrito o conteúdo. `pt-PT` quer dizer português de Portugal; `pt-BR` seria português do Brasil e `en` seria inglês. Este atributo faz muita diferença a quem não vê o ecrã. Um **leitor de ecrã** é um programa que lê a página em voz alta a pessoas cegas ou com pouca visão. Esse programa usa o `lang` para escolher a voz e a pronúncia. Se a tua página em português disser que está em inglês, o leitor de ecrã lê as palavras portuguesas com pronúncia inglesa. O texto fica impossível de perceber. O `lang` serve também ao browser para oferecer tradução e ao corretor ortográfico para saber que dicionário usar.

**`<head>`** é a cabeça da página: guarda informação sobre a página que não aparece dentro dela. Pensa numa pasta de arquivo. O que está escrito na etiqueta da lombada, como o assunto e o ano, não faz parte dos documentos lá dentro. Mas é o que permite encontrá-la na estante. O `head` é essa etiqueta.

**`<body>`** é o corpo da página: tudo o que aparece na janela do browser está dentro do `body`. Títulos, parágrafos, imagens, ligações, tabelas: tudo aqui.

## O que vai no head

Neste tema, o `head` leva sempre três elementos. No tema do CSS vais acrescentar um quarto, a ligação à folha de estilos.

**`<meta charset="utf-8">`** diz ao browser como transformar os bytes do ficheiro em letras. Um computador não guarda letras: guarda números, e usa uma tabela para saber que número corresponde a que letra. Houve muitas tabelas diferentes ao longo da história, e a maioria não tinha as letras portuguesas. A **UTF-8** é a tabela usada hoje em quase toda a Web. Tem as letras de todas as línguas, incluindo o ç, o ã e o é. Se o browser ler o teu ficheiro com a tabela errada, as letras acentuadas aparecem trocadas por símbolos estranhos, como `Ã§` no lugar de `ç`.

Esta linha vai sempre em primeiro lugar dentro do `head`. O browser precisa de saber a tabela antes de ler o texto, incluindo o título, e só procura esta linha no princípio do ficheiro. Se ela ficar mais abaixo, pode já não a encontrar a tempo. Há uma segunda condição: o ficheiro tem de estar mesmo guardado em UTF-8. O VS Code guarda assim por omissão, e mostra `UTF-8` na barra de baixo da janela.

**`<meta name="viewport" content="width=device-width, initial-scale=1">`** é para os telemóveis. Quando apareceram os telemóveis com ecrã tátil e um browser completo, quase todos os sites tinham sido feitos para ecrãs de computador. Para não os estragar, os telemóveis passaram a fingir que tinham um ecrã largo, de cerca de 980 píxeis, e encolhiam a página até caber. Esta linha diz ao telemóvel: não finjas; usa a largura verdadeira do teu ecrã (`width=device-width`) e não encolhas nada (`initial-scale=1`). Sem ela, a tua página aparece encolhida num telemóvel, e a pessoa pode ter de fazer zoom para ler. No computador não vais notar diferença nenhuma. No tema da responsividade, sem ela, nada do que fizeres para ecrãs pequenos vai funcionar num telemóvel. Por isso pomo-la desde o primeiro dia.

**`<title>`** é o título da página. Não aparece dentro da página: aparece no separador do browser, e é usado em muitos outros sítios. É o nome que fica gravado quando alguém guarda a página nos favoritos, e é o que aparece no histórico. É o título azul do resultado num motor de pesquisa, e é a primeira coisa que um leitor de ecrã diz quando a página abre. Por isso cada página tem de ter um título diferente, que diga o que ela é.

Nos materiais usamos a forma `Página | Site`, como em `Início | Estante Digital` ou `Sobre | Estante Digital`. A parte que muda de página para página vem primeiro. Quando há muitos separadores abertos, o browser corta os títulos compridos, e fica só visível o princípio. Se o título começasse por "Estante Digital", todos os separadores do teu site pareceriam iguais. O traço vertical `|` é só um separador; também se usa muito o hífen.

## Títulos: de h1 a h6

O HTML tem seis níveis de título: `h1`, `h2`, `h3`, `h4`, `h5` e `h6`, do mais importante para o menos importante. O `h` vem de *heading*, título em inglês.

Os títulos de uma página formam o seu **índice**. São como os capítulos e as secções de um livro, ou as partes de um relatório que entregas na escola. Um trabalho tem um título geral, está dividido em capítulos, e cada capítulo pode ter secções. Numa página é igual:

- o `h1` é o título da página inteira, o assunto do conteúdo principal. Há um só `h1` por página;
- cada `h2` é o título de uma grande parte da página;
- cada `h3` é o título de uma parte dentro de um `h2`;
- e assim por diante, embora numa página pequena raramente se passe do `h3`.

A regra que mais importa é esta: a descer, não se saltam níveis. Depois de um `h2`, o título seguinte pode ser outro `h2`, uma parte nova ao mesmo nível, ou um `h3`, uma parte dentro desta. Não pode ser um `h4`, porque um `h4` a seguir a um `h2` quer dizer "uma subsecção de uma subsecção que não existe". A subir já se pode saltar. Depois de um `h4`, podes voltar a um `h2`, porque isso só quer dizer que a parte anterior acabou e começa uma parte nova.

Vê o índice da página de um recurso da Estante Digital, desenhado com a indentação a mostrar os níveis:

```text
h1  Primeiros passos na Web
    h2  Para quem é
    h2  O que vais aprender
    h2  Como o usar
    h2  Onde o encontrar
    h2  Dica de quem já o leu
```

E agora um índice com dois problemas:

```text
h1  Estante Digital
h1  Primeiros passos na Web
    h3  Para quem é
    h3  O que vais aprender
```

O primeiro problema é haver dois `h1`: a página parece ter dois assuntos principais. O nome do site não é o assunto desta página; o assunto é o livro. O segundo problema é o salto de `h1` para `h3`, que deixa um nível vazio pelo meio.

Porque é que isto importa tanto? Pensa em como tu lês uma página nova. Antes de ler, passas os olhos pelos títulos grandes para ver se a página tem o que procuras. Uma pessoa que usa um leitor de ecrã não pode passar os olhos, mas faz uma coisa equivalente. Pede ao programa a lista dos títulos da página, ou salta de título em título com uma tecla. Para essa pessoa, os títulos são o mapa da página. Se a hierarquia estiver errada, o mapa está errado. Os motores de pesquisa também usam os títulos para perceber de que trata a página. E tu próprio, quando voltares ao teu código daqui a três meses, vais agradecer ter uma estrutura clara.

Há um erro muito comum, que é escolher o título pelo tamanho da letra. O browser mostra o `h1` com letra grande e o `h4` com letra pequena. Há quem use um `h4` só porque "fica com o tamanho certo". Esse tamanho é só o aspeto por omissão do browser, e no tema do CSS vais aprender a mudá-lo como quiseres. O nível de um título escolhe-se pelo lugar que o título ocupa na estrutura, nunca pelo tamanho com que aparece. O erro ao contrário também existe: pôr um texto a negrito para parecer um título. Fica com ar de título para quem vê. Para o leitor de ecrã e para o motor de pesquisa, é só um texto a negrito.

Os erros dos títulos reconhecem-se no índice da página. Há um `h1` seguido de um `h3`, há dois `h1`, ou há um título escolhido "porque fica mais pequeno". Para os apanhar, escreve o índice da página à mão, com a indentação a mostrar os níveis, como os índices acima. O índice tem de fazer sentido sozinho. O tamanho resolve-se no CSS.

## Parágrafos e texto com significado

O elemento `p` marca um **parágrafo**: um bloco de texto corrido, com uma ideia. O browser deixa um espaço antes e depois de cada parágrafo. É o elemento que mais vais escrever.

Dentro de um parágrafo, há dois elementos que dão significado a palavras soltas:

- `strong` marca texto de importância forte, algo que o leitor não pode deixar escapar, como um prazo ou um aviso. O browser mostra-o a negrito;
- `em` marca ênfase: a palavra onde se põe a força quando se diz a frase em voz alta. Por vezes, essa força muda o sentido da frase. O browser mostra o `em` em itálico.

```html
<p>A requisição é por uma semana. <strong>Livros entregues com atraso bloqueiam novas requisições.</strong></p>
<p>Não disse que o livro era difícil. Disse que era <em>comprido</em>.</p>
```

No browser, a segunda frase do primeiro parágrafo aparece a negrito, e a palavra "comprido" aparece em itálico. Experimenta dizer a segunda frase em voz alta com a força em "comprido": é isso que o `em` marca.

Existem também os elementos `b` e `i`, que põem o texto a negrito e em itálico com um significado muito fraco. O `b` só chama a atenção para umas palavras, e o `i` marca um tom diferente do resto do texto, como uma palavra estrangeira. Não os vamos usar. Se queres importância, usa `strong`; se queres ênfase, usa `em`; se só queres mudar o aspeto, isso é trabalho do CSS.

## Listas

Há dois tipos de lista em HTML:

- a **lista não ordenada**, `ul` (de *unordered list*), para itens cuja ordem não importa;
- a **lista ordenada**, `ol` (de *ordered list*), para itens cuja ordem importa.

Nos dois casos, cada item é um elemento `li` (de *list item*).

Antes de continuares, tenta prever: o que é que o browser põe à frente de cada item de cada uma destas listas?

```html
<ul>
  <li>O que fazem o browser e o servidor quando abres uma página.</li>
  <li>Como se escreve a estrutura de uma página com HTML.</li>
</ul>

<ol>
  <li>Lê os capítulos pela ordem.</li>
  <li>No fim de cada capítulo, faz o exercício no computador.</li>
</ol>
```

Na lista `ul`, o browser põe uma bolinha antes de cada item. Na lista `ol`, numera os itens sozinho: 1. e 2. Nas duas, os itens aparecem um pouco afastados da margem esquerda.

Leitura guiada: cada lista abre e fecha com a sua etiqueta, `ul` ou `ol`, e lá dentro só há elementos `li`, um por item. Os números da `ol` não estão escritos no ficheiro: é o browser que os põe, pela ordem dos `li`.

Para decidir entre as duas, faz este teste: se trocar dois itens de lugar, a informação fica errada? Nos passos de uma receita, trocar "bater os ovos" com "pôr no forno" estraga o bolo: é uma lista ordenada. Na lista dos ingredientes, a ordem é indiferente: é uma lista não ordenada. Um top 10 também é ordenado, porque a posição é a própria informação.

Há duas regras de aninhamento que o browser não te avisa se falhares. Dentro de um `ul` ou de um `ol` só podem estar elementos `li`. E um `li` só pode estar dentro de um `ul` ou de um `ol`. Se precisares de uma lista dentro de outra, a lista de dentro vai dentro de um `li`, e não entre dois `li`:

```html
<ul>
  <li>
    Livros
    <ul>
      <li>Primeiros passos na Web</li>
      <li>Pequeno dicionário de HTML</li>
    </ul>
  </li>
  <li>Vídeos</li>
</ul>
```

No browser, os dois livros aparecem por baixo de "Livros", mais afastados da margem, e com uma bolinha vazia em vez de cheia. É assim que o browser mostra uma lista dentro de outra.

Porquê usar uma lista em vez de escrever os itens em parágrafos com um hífen ou um número à frente? Porque o browser passa a saber que é uma lista. Um leitor de ecrã anuncia "lista, 4 itens" antes de ler, e a pessoa fica logo a saber quanto vai ouvir. No CSS vais poder mudar o aspeto de todas as listas de uma vez. E se acrescentares um passo a meio de uma lista ordenada, o browser renumera tudo sozinho.

É também por isto que os menus de navegação dos sites são escritos como listas de ligações, como vais ver no exemplo guiado.

## Ligações

Uma **ligação** (em inglês, *link*) escreve-se com o elemento `a` (de *anchor*, âncora) e o atributo `href` (de *hypertext reference*), que diz o destino:

```html
<a href="sobre.html">Sobre a Estante Digital</a>
```

No browser aparece "Sobre a Estante Digital", sublinhado e de outra cor, normalmente azul, que é o aspeto por omissão de uma ligação. O `sobre.html` não aparece: diz só para onde a ligação leva.

O conteúdo do `a` é o **texto da ligação**: o que aparece na página, sublinhado, e em que o utilizador carrega. Esse texto tem de dizer para onde a ligação leva. Evita "clica aqui", "aqui" ou "ver mais". Há duas razões. A primeira é que muita gente não lê a página toda. Passa os olhos e procura o sítio onde carregar, e um "clica aqui" obriga a ler a frase à volta para perceber para onde vai. A segunda é que os leitores de ecrã conseguem mostrar a lista de todas as ligações da página, fora do texto à volta. Uma lista com dez "clica aqui" não serve para nada. Uma lista com "Horário da biblioteca", "Primeiros passos na Web" e "Sobre a Estante Digital" diz tudo.

Para corrigir um "clica aqui", põe a ligação nas palavras que dizem o destino. Em vez de "Para ver o horário, clica aqui", escreve "Consulta o horário da biblioteca", com a ligação em "horário da biblioteca".

O valor do `href` pode ter várias formas, conforme o sítio para onde queres ir:

| Destino | Exemplo de `href` | Quando se usa |
| --- | --- | --- |
| Outra página do teu site | `sobre.html` | Para navegar entre as tuas páginas. É um **caminho relativo**, explicado na secção seguinte |
| Uma página de outro site | `https://developer.mozilla.org/pt-BR/docs/Web/HTML/Reference/Elements` | Para levar a pessoa para fora do teu site. É um **endereço absoluto**: tem de começar por `https://` |
| Uma parte da mesma página | `#horario` | Para saltar para um elemento da página que tenha o atributo `id="horario"` |
| Um endereço de correio eletrónico | `mailto:biblioteca@escola.example` | Para abrir o programa de correio com o destinatário preenchido |

Num endereço absoluto, o `https://` é obrigatório. Se escreveres `href="developer.mozilla.org"`, sem ele, o browser pensa que é o nome de um ficheiro na pasta do teu site. Procura-o, não o encontra, e a ligação dá erro. É um dos enganos mais frequentes, e reconhece-se assim. Carregas numa ligação para outro site e aparece "ficheiro não encontrado". Na barra do browser, o endereço mostra que ele foi procurar um ficheiro dentro da pasta do teu site. Para corrigir, abre a página de destino, copia o endereço completo da barra do browser e cola-o no `href`.

Numa ligação para uma parte da mesma página, o elemento de destino precisa de um atributo `id` com um nome. A ligação usa esse nome com um cardinal à frente:

```html
<a href="#horario">Ver o horário da biblioteca</a>
...
<section id="horario">
  <h2>Onde o encontrar</h2>
  ...
</section>
```

O valor de um `id` tem de ser único na página: não pode haver dois elementos com o mesmo `id`. Segue também as regras dos nomes de ficheiros que vais ver já a seguir: minúsculas, sem espaços e sem acentos.

Vais encontrar ligações com o atributo `target="_blank"`, que as abre num separador novo. Não o uses por hábito. Quem decide se quer um separador novo é quem está a ler, e pode fazê-lo sozinho, com o botão do meio do rato, por exemplo. Um separador novo aberto sem aviso desorienta quem usa leitor de ecrã, e faz com que o botão de voltar atrás deixe de funcionar. Se um dia tiveres uma razão forte para o usar, diz no próprio texto da ligação que ela abre noutro separador.

### Ligação ou botão

Na Web há duas coisas em que se carrega, as ligações e os botões, e no ecrã podem ter o mesmo aspeto. Uma ligação leva-te a outro sítio: outra página, outra parte da mesma página, um ficheiro. Um **botão** faz uma ação aqui mesmo, sem sair do sítio: enviar um formulário, abrir um menu, acrescentar um item a uma lista. As ligações são o elemento `a`. Os botões são o elemento `button`, que vais usar nos temas dos formulários e do JavaScript.

Ligações e botões também se comportam de maneira diferente para quem usa o teclado ou um leitor de ecrã. Pelo teclado, uma ligação ativa-se com Enter, e um botão com Enter ou com a barra de espaços. Um leitor de ecrã anuncia "ligação" ou "botão", e a pessoa espera coisas diferentes de cada um. De uma ligação espera mudar de sítio, e de um botão espera que aconteça alguma coisa. Por isso não se faz uma ligação com ar de botão para executar uma ação, nem um botão para navegar. Neste tema não há ações, só navegação, e por isso tudo em que se carrega é uma ligação.

## Caminhos relativos

Um **caminho relativo** diz onde está um ficheiro a partir do ficheiro onde estás. É como dar direções a partir de onde a pessoa está: "segue em frente e é a segunda porta". Não se dá a morada completa.

Considera a pasta da Estante Digital:

```text
estante-digital/
├── index.html
├── primeiros-passos-na-web.html
├── sobre.html
└── imagens/
    ├── capa-primeiros-passos-na-web.svg
    └── logotipo.svg
```

A partir do `index.html`:

- para ligar ao `sobre.html`, que está na mesma pasta, basta o nome: `href="sobre.html"`;
- para mostrar o logótipo, que está dentro da pasta `imagens`, escreve-se o nome da pasta, uma barra e o nome do ficheiro: `src="imagens/logotipo.svg"`.

E se um ficheiro estiver numa pasta de cima? Imagina que o site tivesse uma pasta `recursos`, com as páginas dos recursos lá dentro:

```text
estante-digital/
├── index.html
├── imagens/
│   └── logotipo.svg
└── recursos/
    └── primeiros-passos-na-web.html
```

A partir de `recursos/primeiros-passos-na-web.html`, para voltar ao `index.html` é preciso subir uma pasta primeiro. Isso escreve-se com dois pontos seguidos, `..`, que querem dizer "a pasta de cima": `href="../index.html"`. Para chegar ao logótipo, sobe-se uma pasta e desce-se para `imagens`: `src="../imagens/logotipo.svg"`. Cada `../` sobe um nível. Neste tema, as tuas páginas vão ficar todas na mesma pasta, e só vais precisar de nomes simples e de `imagens/`. Mas convém perceberes o `../` desde já, porque o vais encontrar.

Três regras evitam quase todos os problemas com caminhos.

- Nunca uses o caminho completo do teu disco, como `C:\Users\Ana\Desktop\site\imagens\foto.jpg` ou um endereço começado por `file:///`. Pode funcionar no teu computador, porque o ficheiro está lá. Mas deixa de funcionar em qualquer outro computador e no servidor, quando publicares o site. Acontece muitas vezes quando se arrasta um ficheiro para o editor. Reconhece-se assim: a página funciona no teu computador e não funciona no do colega. A correção é trocar o caminho do disco por um caminho relativo, a partir da pasta da página.
- Nos caminhos da Web usa-se a barra `/`, mesmo no Windows, onde o explorador de ficheiros mostra a barra ao contrário, `\`.
- Os nomes dos ficheiros e das pastas escrevem-se em minúsculas, sem espaços e sem acentos, com hífenes entre as palavras, como `primeiros-passos-na-web.html`. No teu computador com Windows, `Foto.JPG` e `foto.jpg` são o mesmo ficheiro. Num servidor, que quase sempre usa Linux, são dois ficheiros diferentes. Uma página que funciona na escola deixa de mostrar a imagem quando é publicada, e ninguém percebe porquê. Os espaços e os acentos causam problemas parecidos. São as mesmas regras que os ficheiros dos materiais da disciplina seguem, como deves ter reparado nos nomes dos guias.

## Imagens

Uma imagem põe-se na página com o elemento `img`, que é vazio:

```html
<img src="imagens/capa-primeiros-passos-na-web.svg"
     alt="Capa azul com o título Primeiros passos na Web em letras brancas e o desenho de um globo terrestre."
     width="240" height="320">
```

Quando uma etiqueta tem muitos atributos, podes parti-la por várias linhas, como aqui, para se ler melhor. Os atributos são:

- `src` (de *source*, origem): o caminho para o ficheiro da imagem, com as regras da secção anterior;
- `alt` (de *alternative*, alternativo): o texto que substitui a imagem quando ela não pode ser vista. Tem uma secção só para ele, a seguir;
- `width` e `height`: a largura e a altura da imagem, em píxeis, sem escrever a unidade. Não são obrigatórios, mas ajudam. O browser fica a saber o espaço que a imagem vai ocupar antes de a descarregar, e a página não "salta" quando ela chega. Usa as medidas verdadeiras da imagem, ou medidas com a mesma proporção.

Os formatos de imagem mais usados na Web são quatro. O **JPG** serve para fotografias. O **PNG** serve para desenhos, capturas de ecrã e imagens com fundo transparente. O **SVG** serve para desenhos feitos de formas geométricas, como logótipos e ícones, e pode ser aumentado sem perder qualidade. As imagens da Estante Digital são SVG. O **WebP** é um formato mais recente, que faz ficheiros mais pequenos com a mesma qualidade.

Cuidado com o tamanho dos ficheiros. Uma fotografia tirada com um telemóvel pode ter 4000 píxeis de largura e vários megabytes. Numa página, isso quer dizer uma espera longa para quem tem dados móveis. Antes de usares uma fotografia, reduz-lhe o tamanho para a largura de que precisas, com qualquer programa de edição de imagem. No tema da responsividade vais voltar a este assunto.

Sobre a origem das imagens: usa fotografias e desenhos feitos por ti, ou imagens cuja licença permita o uso. Uma imagem encontrada numa pesquisa não é livre só por estar na Internet. Quando uma imagem não é tua, guarda de onde veio e qual é a licença. No README do teu site vais dizer a origem e a licença de cada imagem que não fizeste. E não publiques fotografias de outras pessoas sem autorização delas.

## O texto alternativo

Há pelo menos três situações em que a imagem não é vista, e em cada uma delas é o `alt` que ocupa o lugar dela:

- a pessoa é cega ou tem pouca visão e usa um leitor de ecrã, que lê o `alt` em voz alta no sítio da imagem;
- a imagem não carregou, porque a rede está lenta ou porque o caminho está errado, e o browser mostra o `alt` no sítio dela;
- um motor de pesquisa quer saber o que a imagem mostra, e lê o `alt`.

Para escrever um bom **texto alternativo**, faz esta pergunta. Se eu estivesse ao telefone a descrever esta página a alguém, o que diria no sítio da imagem? A página tem de continuar a fazer sentido. A resposta é o `alt`. Não é uma descrição de todos os pormenores. É o que a imagem transmite naquele sítio da página. Há duas regras práticas. Não comeces por "Imagem de" ou "Fotografia de", porque o leitor de ecrã já anuncia que é uma imagem. E escreve uma frase curta, raramente mais do que uma.

Há três situações, e cada uma pede uma resposta diferente.

**A imagem transmite informação.** O `alt` descreve essa informação. Na página do livro, a capa mostra a cara do livro que a pessoa vai procurar na biblioteca. O `alt` descreve o que se vê: `alt="Capa azul com o título Primeiros passos na Web em letras brancas e o desenho de um globo terrestre."`. Quem não vê a capa fica a saber como a reconhecer na estante.

**A imagem é decorativa ou repete o que já está escrito.** O `alt` fica vazio: `alt=""`. É o caso do logótipo da Estante Digital, que está mesmo ao lado do texto "Estante Digital". Se lhe puséssemos `alt="Logótipo da Estante Digital"`, quem usa leitor de ecrã ouviria "Logótipo da Estante Digital, Estante Digital", com o nome repetido. Com o `alt` vazio, o leitor de ecrã salta a imagem, e a pessoa ouve o nome uma só vez.

Atenção: `alt` vazio não é o mesmo que não ter `alt`. Um `alt=""` diz "esta imagem não tem nada a acrescentar, podes saltá-la". Uma imagem sem atributo `alt` não diz nada. Na dúvida, muitos leitores de ecrã leem o nome do ficheiro, como "logotipo ponto svg", o que é pior do que tudo. Toda a imagem tem o atributo `alt`: às vezes com texto, às vezes vazio, nunca ausente.

**A imagem é o único conteúdo de uma ligação.** Quando uma imagem sozinha serve de ligação, o `alt` é o texto dessa ligação. Deve dizer para onde ela leva, e não o que a imagem mostra. Vais precisar disto mais tarde; por agora, basta saberes que existe.

Repara que a mesma imagem pode precisar de textos alternativos diferentes em sítios diferentes. A capa do livro, na página do livro, tem um `alt` descritivo. Imagina a mesma capa pequenina numa lista de livros, ao lado do título escrito. Aí o `alt` podia ficar vazio, porque o título já está ali. O `alt` depende do contexto, e não só da imagem.

Um teste simples para uma página inteira: lê-a de cima a baixo substituindo cada imagem pelo seu `alt`. Se a página continuar a fazer sentido, sem faltar nada e sem repetições, os textos alternativos estão bem.

Há três erros frequentes com o `alt`, e todos se corrigem com a pergunta do telefone. O primeiro é uma imagem sem o atributo. O segundo é um `alt` que só diz "imagem", ou que começa por "Imagem de". O terceiro é um `alt` que repete a legenda, como vais ver na secção seguinte. Uma imagem com informação tem um `alt` que descreve essa informação. Uma imagem decorativa, ou que repete o texto ao lado, tem `alt=""`. Nenhuma imagem fica sem o atributo.

## Imagem com legenda: figure e figcaption

Às vezes, uma imagem é um conteúdo com direito próprio, de que o texto fala, e tem uma legenda. Nesse caso, junta-se a imagem e a legenda num elemento `figure`. A legenda vai num `figcaption`:

```html
<figure>
  <img src="imagens/capa-primeiros-passos-na-web.svg"
       alt="Capa azul com o título Primeiros passos na Web em letras brancas e o desenho de um globo terrestre."
       width="240" height="320">
  <figcaption>
    Capa da edição que está na biblioteca da escola.
    Livro fictício, criado para este exemplo.
  </figcaption>
</figure>
```

No browser, a capa aparece com a legenda logo por baixo. As duas ficam um pouco afastadas da margem esquerda, que é o aspeto por omissão de um `figure`.

O `figure` diz ao browser que a imagem e a legenda formam uma unidade: a legenda pertence àquela imagem, e não ao parágrafo seguinte. O `figcaption` é o primeiro ou o último filho do `figure`.

O `alt` e a legenda não fazem o mesmo trabalho, e por isso não devem repetir-se. A legenda é vista por toda a gente e acrescenta contexto: de onde vem a imagem, quando foi tirada, o que se deve notar nela. O `alt` só é lido por quem não vê a imagem, e diz o que a imagem mostra. No exemplo, a legenda diz de que edição é a capa e avisa que o livro é fictício. O `alt` diz o que a capa tem desenhado.

Nem todas as imagens precisam de `figure`. O logótipo no cabeçalho, por exemplo, não é um conteúdo de que o texto fale e não tem legenda; é só uma imagem.

## Comentários

Um **comentário** é um texto escrito no ficheiro para as pessoas que leem o código, e que o browser ignora. Escreve-se entre `<!--` e `-->`:

```html
<!-- O alt fica vazio porque o nome do site está escrito ao lado. -->
<img src="imagens/logotipo.svg" alt="" width="48" height="48">
```

Os comentários servem para explicar decisões que o código sozinho não explica, como o porquê de um `alt` vazio. Os ficheiros da Estante Digital estão cheios de comentários deste tipo, para que os possas ler e perceber. Um aviso: os comentários não aparecem na página, mas qualquer pessoa os pode ler, abrindo o código da página no browser. Nunca escrevas num comentário nada que não escreverias na própria página.

## Os elementos semânticos

**Semântica** quer dizer significado. Escrever HTML semântico é escolher cada elemento pelo que o conteúdo é, e não pelo aspeto que queres que tenha. Já o fizeste com os títulos, as listas e o `strong`. Agora vais fazê-lo com as grandes zonas da página.

No guia 01 viste wireframes: esboços em que a página está dividida em zonas, como o cabeçalho, a navegação, o conteúdo principal e o rodapé. O HTML tem um elemento para cada uma dessas zonas:

| Elemento | O que marca | Na Estante Digital |
| --- | --- | --- |
| `header` | O cabeçalho: o conteúdo de introdução, como o nome do site, o logótipo e a navegação principal | O logótipo, o nome "Estante Digital" e o menu |
| `nav` | Um grupo de ligações de navegação principal, que leva às várias partes do site | A lista com Início e Sobre |
| `main` | O conteúdo principal: o que é próprio desta página e não se repete nas outras | Tudo o que está entre o cabeçalho e o rodapé |
| `section` | Uma parte temática do conteúdo, com o seu próprio título | "Livros", "Vídeos", "Sítios e aplicações" |
| `article` | Um conteúdo completo em si mesmo, que faria sentido sozinho noutro sítio | A ficha do livro Primeiros passos na Web |
| `aside` | Um conteúdo relacionado mas secundário, que se pode saltar sem perder o essencial | A caixa "Dica de quem já o leu" |
| `footer` | O rodapé: informação final, como autoria, contactos ou avisos | A nota que diz que o site é um exemplo e o conteúdo é fictício |

Estas são as regras e os testes para escolheres bem:

- **`main`**: há um só por página. Não pode estar dentro do `header`, do `footer`, do `nav`, do `article`, do `aside` nem de uma `section`. O teste é perguntar o que muda de página para página: o cabeçalho e o rodapé repetem-se, e o que muda é o conteúdo principal.
- **`nav`**: não é para qualquer grupo de ligações. É para os blocos de navegação principais, como o menu do site. A ligação "Voltar à lista de recursos" no fim de uma página não precisa de estar num `nav`.
- **`section`**: tem sempre um título. O teste é perguntar se consegues dar-lhe um título que faça sentido. Se não consegues, provavelmente não é uma secção.
- **`article`**: o teste é imaginar que o copias sozinho para outro site. Uma notícia, uma publicação de um blogue, a ficha de um produto ou de um livro continuam a fazer sentido. Um parágrafo solto a meio de uma explicação não.
- **`aside`**: o teste é perguntar se, ao saltares esse bloco, perdes alguma coisa essencial. Uma dica, uma caixa de "sabias que", ligações para assuntos parecidos: saltam-se, e o conteúdo principal continua completo.
- **`header` e `footer`**: além do cabeçalho e do rodapé da página inteira, também podem ser o cabeçalho e o rodapé de um `article`. Não se põe um `header` nem um `footer` dentro de outro `header` ou de outro `footer`.

E quando nenhum destes elementos serve? Existe o elemento `div`, que é uma caixa genérica, sem significado nenhum. Não é proibido: vais usá-lo no CSS para agrupar coisas por razões de arrumação. Mas é o último recurso, e não o primeiro. Uma página feita só de `div` funciona para quem a vê, e não diz nada a mais ninguém.

Quando estiveres indeciso, faz as perguntas por esta ordem:

1. É o conteúdo principal desta página, o que não se repete nas outras? Então é o `main`.
2. É o bloco de ligações que leva às partes principais do site? Então é um `nav`.
3. É a zona de introdução do topo, ou a zona de informação final do fundo? Então é o `header` ou o `footer`.
4. É secundário, e pode saltar-se sem perder nada? Então é um `aside`.
5. Faria sentido sozinho, copiado para outro sítio? Então é um `article`.
6. É uma parte do conteúdo a que consegues dar um título? Então é uma `section`.
7. Nenhuma das anteriores? Então é talvez um `div`, ou talvez não precise de caixa nenhuma, e basta um parágrafo ou uma lista.

A ordem das perguntas conta. Quase tudo se pode pôr debaixo de um título, e por isso a pergunta da `section` fica para o fim. Se viesse antes, uma caixa secundária com título, como a dica da Estante Digital, ficava classificada como secção sem chegar à pergunta do `aside`.

### Os quatro leitores de uma página

Uma página não é lida só por pessoas que olham para o ecrã. É lida por, pelo menos, quatro tipos de leitores, e a semântica serve a todos.

O primeiro são as pessoas que usam tecnologias de apoio, como os leitores de ecrã. Para elas, os elementos semânticos são pontos de referência. O programa permite saltar diretamente para o conteúdo principal, para a navegação ou para o rodapé, sem ter de ouvir tudo o que está antes. Uma pessoa que visite dez páginas do teu site não quer ouvir o menu dez vezes: salta para o `main`. Numa página feita só de `div`, esse salto não existe.

O segundo são os motores de pesquisa. Usam os elementos para perceber que parte da página é o conteúdo e que parte se repete em todas as páginas.

O terceiro são as pessoas que leem o código: os teus colegas, o teu professor e tu próprio daqui a uns meses. Um `nav` diz o que é logo à primeira. Um `div` obriga a ler o que está lá dentro para perceber.

O quarto são as outras linguagens. No tema do CSS vais dar aspeto aos elementos escolhendo-os pelo nome, por exemplo todos os `nav` ou todos os `article`. No tema do JavaScript vais procurar elementos na página para lhes mudar o conteúdo. Uma estrutura com significado torna os dois trabalhos mais simples.

### A árvore de acessibilidade

Já sabes que o browser constrói uma árvore em memória a partir do teu ficheiro, o DOM. A partir do DOM constrói ainda uma segunda árvore, mais simples, chamada **árvore de acessibilidade**. É essa árvore que os leitores de ecrã e outras tecnologias de apoio recebem.

Na árvore de acessibilidade, cada coisa aparece com duas informações principais. O **papel** diz o que a coisa é: título, ligação, lista, imagem, navegação, conteúdo principal. O **nome** é o texto que a identifica: o texto de uma ligação, o `alt` de uma imagem. Um `div` tem só um papel genérico (em inglês, *generic*), que não diz nada sobre o conteúdo. Uma imagem com `alt=""` nem sequer aparece, porque foi marcada como decorativa. É por isto que a semântica importa tanto. O que não está no HTML não chega à árvore. E o que não chega à árvore não existe para quem usa um leitor de ecrã.

Os elementos `header`, `nav`, `main`, `aside` e `footer` da página inteira aparecem nesta árvore como **pontos de referência** (em inglês, *landmarks*). Os papéis deles são, pela mesma ordem, *banner*, *navigation*, *main*, *complementary* e *contentinfo*. São esses nomes que vais encontrar se abrires a árvore nas ferramentas do programador, como vais fazer no laboratório.

## Tabelas de dados

Uma **tabela de dados** serve para mostrar dados que estão naturalmente organizados em linhas e colunas. Pode ser um horário, as notas de uma turma por disciplina, os preços de um produto por tamanho ou os resultados de um campeonato. O teste é este: cada valor da tabela responde a uma pergunta que junta uma linha e uma coluna? No horário da biblioteca, "a que horas fecha à quarta-feira?" responde-se cruzando a linha "Quarta-feira" com a coluna "Fecha". Se a informação se lê assim, é uma tabela.

Uma tabela usa vários elementos, que se encaixam uns nos outros:

| Elemento | O que marca |
| --- | --- |
| `table` | A tabela inteira |
| `caption` | A legenda: o nome da tabela. Vai logo a seguir à etiqueta de abertura do `table` |
| `thead` | O grupo de linhas de cabeçalho, no topo |
| `tbody` | O grupo de linhas de dados, o corpo da tabela |
| `tr` | Uma linha (de *table row*) |
| `th` | Uma célula de cabeçalho (de *table header*): diz o que é uma coluna ou uma linha |
| `td` | Uma célula de dados (de *table data*): um valor |

Vê como se constrói o horário da biblioteca, com as três primeiras linhas de dados. Antes de leres a explicação, tenta prever: no browser, as células aparecem separadas por linhas, como numa folha de cálculo?

```html
<table>
  <caption>Horário da biblioteca da escola (fictício)</caption>
  <thead>
    <tr>
      <th scope="col">Dia</th>
      <th scope="col">Abre</th>
      <th scope="col">Fecha</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Segunda-feira</th>
      <td>08:30</td>
      <td>17:30</td>
    </tr>
    <tr>
      <th scope="row">Terça-feira</th>
      <td>08:30</td>
      <td>17:30</td>
    </tr>
    <tr>
      <th scope="row">Quarta-feira</th>
      <td>08:30</td>
      <td>13:00</td>
    </tr>
  </tbody>
</table>
```

Não aparecem. Sem CSS, o browser não desenha linhas entre as células: os valores aparecem arrumados em colunas, só com um pequeno espaço entre eles. A legenda aparece centrada por cima da tabela. As células `th` aparecem a negrito e centradas, e as `td` em letra normal.

Leitura guiada: lê o código com calma. A tabela é feita linha a linha: cada `tr` é uma linha, e as células dessa linha estão lá dentro, da esquerda para a direita. A primeira linha, no `thead`, só tem cabeçalhos, que dizem o que é cada coluna. Nas linhas do `tbody`, a primeira célula também é um cabeçalho, porque diz de que dia é aquela linha, e as outras duas são dados.

O atributo `scope` diz a que se aplica cada cabeçalho. `scope="col"` quer dizer "sou o cabeçalho desta coluna", e `scope="row"` quer dizer "sou o cabeçalho desta linha". É isto que permite a um leitor de ecrã dizer a que linha e a que coluna pertence cada célula. Quando a pessoa chega à célula `13:00`, ouve algo como "Quarta-feira, Fecha, 13:00". Sem cabeçalhos, a pessoa ouviria "13:00" e não saberia de que dia nem se é a hora de abrir ou de fechar.

O `caption` é o nome da tabela, e é o que um leitor de ecrã anuncia quando a pessoa chega à tabela. É também útil a quem vê, porque diz de que trata a tabela antes de começar a ler números.

Se te esqueceres do `tbody`, o browser acrescenta-o sozinho quando constrói o DOM. Não aparece no teu ficheiro, mas aparece no separador Elements. É um bom exemplo de que o DOM não é uma cópia exata do ficheiro, como viste no guia 01.

### Tabelas não servem para arrumar a página

Nos anos 90, o CSS ainda não conseguia pôr coisas lado a lado em colunas. Para fazer páginas com um menu à esquerda e o conteúdo à direita, os sites usavam uma tabela enorme e invisível. A página inteira ficava lá dentro, célula a célula. Ainda vais encontrar código assim em sites antigos e em alguns tutoriais velhos. Parece-se com isto:

```html
<table>
  <tr>
    <td>
      <a href="index.html">Início</a><br>
      <a href="sobre.html">Sobre</a>
    </td>
    <td>
      <h1>Recursos de estudo</h1>
      <p>A Estante Digital reúne livros, vídeos e sítios.</p>
    </td>
  </tr>
</table>
```

Para quem olha, fica um menu à esquerda e o texto à direita. Mas repara no que isto diz ao browser: "aqui há uma tabela de dados com uma linha e duas colunas". Os browsers tentam adivinhar quando uma tabela só serve para arrumar e, nesse caso, escondem-na do leitor de ecrã. Mas é um palpite. Quando falham, o leitor de ecrã anuncia uma tabela, lê-a célula a célula, e a pessoa fica à espera de dados que não existem. Mesmo quando acertam, não há navegação nem conteúdo principal na árvore de acessibilidade, porque não há `nav` nem `main`. Num telemóvel, para pôr as duas colunas uma debaixo da outra, é preciso desfazer a tabela com CSS. Ela foi feita para ser uma grelha de linhas e colunas. E para mudar o menu de sítio é preciso reescrever a tabela toda.

A forma certa de escrever o mesmo é com os elementos semânticos. A arrumação em colunas fica para o CSS, nos temas do Flexbox e da Grid. Antes de leres, tenta prever: sem CSS, o menu desta versão aparece à esquerda do texto ou por cima dele?

```html
<nav>
  <ul>
    <li><a href="index.html">Início</a></li>
    <li><a href="sobre.html">Sobre</a></li>
  </ul>
</nav>
<main>
  <h1>Recursos de estudo</h1>
  <p>A Estante Digital reúne livros, vídeos e sítios.</p>
</main>
```

Aparece por cima. Sem CSS, cada zona ocupa a largura toda e fica debaixo da anterior, pela ordem do ficheiro. Pôr o menu ao lado do texto é trabalho do CSS, e o HTML não precisa de mudar para isso.

Leitura guiada: o `nav` diz que as ligações são a navegação, e a lista diz que são opções do mesmo tipo. O `main` diz onde está o conteúdo principal, que começa pelo seu `h1`. Nenhuma linha fala de colunas nem de posições.

A regra é simples: uma tabela é para dados em linhas e colunas, e nunca para pôr coisas lado a lado. Se não há dados em linhas e colunas, não é uma tabela. Usa os elementos semânticos e deixa a arrumação para o CSS.

## Como o browser lida com os erros

Já sabes que o HTML não dá mensagens de erro. Quando o browser encontra uma coisa mal escrita, não para. Segue regras próprias para adivinhar o que querias dizer, corrige o DOM à sua maneira e desenha a página. Isto tem um lado bom: uma página com um erro continua a aparecer. Tem também um lado mau: não sabes que erraste, e o browser nem sempre adivinha bem.

Estes são quatro casos reais, experimentados no browser, com o que o browser faz a cada um:

| O que escreveste | O que o browser faz no DOM | O que vês na página |
| --- | --- | --- |
| Um `strong` que nunca fechaste, a meio de um parágrafo | Fecha-o no fim do parágrafo e abre logo outro a seguir, à volta de tudo o que vem depois | Tudo o que vem a seguir fica a negrito |
| Uma lista `ul` dentro de um `p` | Fecha o `p` antes da lista e cria um parágrafo vazio a seguir, com o `</p>` que sobrou | A lista aparece, mas o DOM tem um parágrafo vazio a mais |
| Um `h2` fechado com `</h3>` | Aceita o `</h3>` como fecho do `h2`, porque qualquer etiqueta de fecho de título fecha o título que estiver aberto | Nada de estranho: o erro fica escondido até ao dia em que deixar de dar certo |
| Uma ligação `a` dentro de outra `a` | Fecha a primeira ligação logo antes de abrir a segunda. O texto que vinha depois da segunda já não pertence a nenhuma ligação | Duas ligações seguidas, em vez de uma, e o fim do texto sem ligação |

Os dois primeiros casos são os mais frequentes nas primeiras páginas, e corrigem-se assim.

Quando tudo fica a negrito a partir de certo ponto, a causa é um `strong` sem etiqueta de fecho. Pode também ser a barra esquecida: `<strong>` onde devia estar `</strong>`. Procura o último sítio onde o negrito estava certo e confirma que cada `<strong>` tem o seu `</strong>`.

Às vezes aparece, no separador Elements, um parágrafo vazio a seguir a uma lista. A causa é um `ul` ou um `ol` escrito dentro de um `p`. Na página parece estar tudo bem. Um parágrafo não pode conter listas, títulos, tabelas nem outros parágrafos. Fecha o parágrafo antes da lista. Se a frase introduz a lista, como "Os recursos são:", fica num parágrafo sozinha, e a lista vem a seguir.

A forma de apanhar estes erros é comparar o que escreveste com o que o browser construiu. Abre as ferramentas do programador, vai ao separador Elements e percorre a árvore. Se a árvore for diferente do teu ficheiro, o browser corrigiu um erro teu. Pode ser um parágrafo vazio que não escreveste, ou um elemento dentro de outro onde não o puseste. O laboratório tem uma fase só para isto.

Existe também um serviço público do W3C, a organização que escreve muitas das regras da Web. Lê um ficheiro HTML e faz a lista de todos os erros, com o número da linha. É o **validador**, em `validator.w3.org`. Podes enviar-lhe o teu ficheiro e ver o que ele encontra. As mensagens estão em inglês, e algumas são difíceis de ler no início. Nesse caso, leva-as à aula.

## Verificar uma página

Uma página só está pronta depois de verificada. Neste tema, verificar quer dizer quatro coisas, que vais fazer no laboratório.

**Seguir todas as ligações.** Abre a página no browser e carrega em cada ligação, uma de cada vez. Cada uma tem de levar ao sítio certo, e cada página de destino tem de ter uma forma de voltar. Uma ligação que dá "ficheiro não encontrado" é uma ligação sem destino, o erro que aprendeste a procurar no mapa do site, no guia 01.

**Ler a página pela ordem do HTML.** Uma página sem CSS mostra o conteúdo pela ordem em que está escrito no ficheiro. Tem o aspeto por omissão do browser. As tuas páginas ainda não têm CSS, por isso o que vês é já essa leitura. Lê de cima a baixo e pergunta: a ordem faz sentido? O mais importante vem primeiro? Os títulos dizem de que trata cada parte? É assim que um leitor de ecrã percorre a página. É essa ordem que tem de continuar a fazer sentido quando, nos próximos temas, o CSS mudar o aspeto e a posição das coisas.

**Percorrer a página só com o teclado.** Carrega na tecla Tab, várias vezes. O **foco**, a moldura que mostra onde estás, salta de ligação em ligação, pela ordem do HTML. Com Shift+Tab andas para trás, e com Enter segues a ligação onde estás. Há pessoas que não podem usar o rato e navegam sempre assim. Se consegues chegar a todas as ligações e perceber onde estás, a página passa este teste.

**Ver a estrutura com as ferramentas do programador.** No separador Elements, confirma que a árvore é igual ao teu ficheiro. Depois abre a árvore de acessibilidade e confirma três coisas:

- aparecem o cabeçalho, a navegação, o conteúdo principal e o rodapé;
- os títulos estão na ordem certa;
- cada imagem tem o nome que lhe deste no `alt`.

## Exemplo guiado: as páginas da Estante Digital

Neste exemplo vês construir, passo a passo, duas páginas do site da Estante Digital: a página inicial e a página de um recurso. A terceira página, "Sobre", é curta e aparece no fim. Os ficheiros completos estão na pasta [estante-digital](../exemplos/frontend/estante-digital/index.html), dos exemplos da disciplina. Podes abri-los no browser e no editor para comparar com o que vais lendo. Se ainda não tens o repositório da disciplina no computador, o professor diz-te como o obter. Uma forma é abrir a página do repositório no GitHub, carregar no botão verde Code e escolher Download ZIP. Depois descompactas o ficheiro numa pasta tua.

### Passo 1: Partir do plano

No guia 01 fizemos o plano deste site. Fizemos o mapa do site, com as páginas e as ligações, e os wireframes da página inicial e da página de um recurso. O HTML não se inventa ao escrever: traduz o plano. Por isso, antes de abrir o editor, olha para o wireframe e dá nome a cada zona. Os wireframes destas páginas estão no exemplo do [guia 01](01-web-e-planeamento.md).

| Zona desenhada no wireframe | Elemento | Porquê |
| --- | --- | --- |
| Faixa de cima, com o logótipo, o nome e o menu | `header` com um `nav` lá dentro | É a introdução do site e repete-se em todas as páginas; o menu é a navegação principal |
| Título grande da página | `h1` | É o assunto desta página |
| Blocos "Livros", "Vídeos" e "Sítios e aplicações" | Três `section`, cada uma com o seu `h2` e uma lista | Cada bloco é uma parte com título próprio |
| Faixa de baixo, com a nota sobre o site | `footer` | É a informação final, e repete-se em todas as páginas |
| Tudo o que fica entre o cabeçalho e o rodapé | `main` | É o conteúdo próprio desta página |

Esta tabela é a decisão mais importante do exemplo. Tudo o que vem a seguir é escrever o que ela diz.

### Passo 2: A pasta e os nomes dos ficheiros

O site vive numa pasta chamada `estante-digital`, com os ficheiros HTML diretamente lá dentro e as imagens numa subpasta `imagens`. Todos os nomes seguem as regras da secção "Caminhos relativos": minúsculas, sem espaços, sem acentos e com hífenes.

A página inicial chama-se `index.html`. Este nome não é uma escolha nossa: é uma convenção da Web. Imagina que alguém escreve o endereço de um site sem indicar a página, como `https://www.exemplo.pt/`. A maior parte dos servidores procura então na pasta um ficheiro chamado `index.html` e envia-o. Chamar `index.html` à tua página inicial garante que ela aparece quando o site for publicado, no tema da publicação.

### Passo 3: O esqueleto da página inicial

Começamos pelo esqueleto, com o título certo para esta página. Antes de abrires este ficheiro no browser, tenta prever: o que aparece na janela? E no separador?

```html
<!doctype html>
<html lang="pt-PT">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Início | Estante Digital</title>
  </head>
  <body>
  </body>
</html>
```

A janela fica em branco, porque o `body` está vazio. Mas não está tudo vazio: no separador aparece "Início | Estante Digital". É a primeira confirmação de que o ficheiro foi lido.

Leitura guiada: o doctype abre o ficheiro. Lá dentro do `html` estão os dois filhos, `head` e `body`. Tudo o que está no `head` é informação sobre a página, e por isso nada dele aparece na janela; o `title` aparece no separador. O `body` ainda não tem nada.

### Passo 4: O cabeçalho e a navegação

Dentro do `body`, a primeira zona é o `header`:

```html
<header>
  <p>
    <img src="imagens/logotipo.svg" alt="" width="48" height="48">
    Estante Digital
  </p>
  <nav>
    <ul>
      <li><a href="index.html">Início</a></li>
      <li><a href="sobre.html">Sobre</a></li>
    </ul>
  </nav>
</header>
```

No browser, aparecem o logótipo e o nome do site na mesma linha e, por baixo, uma lista com duas ligações, "Início" e "Sobre".

Há três decisões a explicar.

A primeira é o nome do site estar num `p`, e não num `h1`. O `h1` é o assunto da página. O assunto da página inicial é "recursos de estudo recomendados pela turma", e não o nome do site. Se o nome do site fosse o `h1` em todas as páginas, todas teriam o mesmo assunto principal. E a página do livro teria dois `h1`. Por isso o nome do site é um parágrafo, e cada página tem o seu `h1` dentro do `main`.

A segunda é o `alt` vazio do logótipo. O desenho está mesmo ao lado do nome "Estante Digital". Um `alt` com texto faria o leitor de ecrã dizer o nome duas vezes. O `alt` vazio diz-lhe que salte a imagem. Repara que o atributo está lá, vazio: não foi esquecido.

A terceira é a navegação ser uma lista de ligações dentro de um `nav`. É uma lista porque são várias opções do mesmo tipo, e um leitor de ecrã anuncia quantas são. Está num `nav` porque é a navegação principal do site. A página inicial tem uma ligação para si própria, "Início". Não faz mal, porque o menu é igual em todas as páginas, e numa página interior essa ligação é a forma de voltar ao princípio.

### Passo 5: O conteúdo principal

A seguir ao `header` vem o `main`, com o `h1`, dois parágrafos de introdução e as três secções:

```html
<main>
  <h1>Recursos de estudo recomendados pela turma</h1>
  <p>
    A Estante Digital reúne livros, vídeos e sítios que ajudaram alunos
    de Desenvolvimento de Aplicações a estudar. Cada recurso tem uma
    descrição curta. Os que já têm página própria têm uma ligação para ela.
  </p>
  <p>
    Todos os recursos deste site são fictícios: foram inventados para
    servir de exemplo nos guias da disciplina.
  </p>

  <section>
    <h2>Livros</h2>
    <ul>
      <li>
        <a href="primeiros-passos-na-web.html">Primeiros passos na Web</a>:
        livro para quem nunca escreveu uma página, disponível na biblioteca da escola.
      </li>
      <li>
        Pequeno dicionário de HTML: consulta rápida das etiquetas mais usadas,
        com um exemplo curto para cada uma.
      </li>
    </ul>
  </section>

  <!-- As secções "Vídeos" e "Sítios e aplicações" seguem a mesma forma. -->
</main>
```

Cada secção começa pelo seu `h2`, e o conteúdo é uma lista não ordenada, porque a ordem dos recursos não importa. Aplica o teste: trocar dois livros de lugar não torna a informação errada.

Repara que só o primeiro livro tem ligação. É o único que já tem página própria. Pôr uma ligação no segundo livro seria criar uma ligação sem destino, que dá erro quando alguém carrega nela. Um site pode estar em construção, desde que não tenha ligações para páginas que ainda não existem. Quando a página do dicionário existir, acrescenta-se a ligação.

O texto da ligação é o título do livro, "Primeiros passos na Web", e não "ver mais" nem "clica aqui". Numa lista de ligações lida fora do contexto, continua a dizer para onde vai.

### Passo 6: O rodapé e a página completa

Depois do `main` vem o `footer`, com a nota final:

```html
<footer>
  <p>
    Estante Digital, site de exemplo dos materiais de Desenvolvimento de
    Aplicações do 10.º ano. Conteúdo fictício.
  </p>
</footer>
```

Com as três zonas escritas, o `body` fica com três filhos, `header`, `main` e `footer`, pela ordem em que aparecem no wireframe. O ficheiro completo é o [index.html](../exemplos/frontend/estante-digital/index.html) da pasta de exemplo. Abre-o no editor e confirma que reconheces cada parte. Vais encontrar comentários a explicar as decisões, que são as mesmas que acabaste de ler.

### Passo 7: Abrir e ler de cima a baixo

Antes de abrires o `index.html` no browser, tenta prever o que vais ver, de cima para baixo, e com que aspeto.

Vais ver o logótipo e o nome do site, a lista do menu com as bolinhas da lista, o título grande e os parágrafos. A seguir vêm os três títulos de secção, com as suas listas, e, no fundo, o rodapé. Não há cores nem colunas: é o aspeto por omissão do browser, e está certo que seja assim nesta fase.

Faz agora a leitura pela ordem do HTML. Primeiro aparecem o nome do site e o menu. A seguir vêm o assunto da página e as três partes, e no fim a nota. É a ordem em que uma pessoa precisa das coisas. O índice dos títulos é este:

```text
h1  Recursos de estudo recomendados pela turma
    h2  Livros
    h2  Vídeos
    h2  Sítios e aplicações
```

Um `h1`, três `h2` ao mesmo nível e nenhum salto.

### Passo 8: A segunda página parte do mesmo esqueleto

A página do livro chama-se `primeiros-passos-na-web.html`, com o nome derivado do título do livro. Não se começa do zero. Copia-se o `index.html`, porque o esqueleto, o cabeçalho e o rodapé são iguais, e muda-se só o que é próprio desta página:

- o `title`, que passa a `Primeiros passos na Web | Estante Digital`;
- todo o conteúdo do `main`.

O cabeçalho e o rodapé ficam iguais em todas as páginas, por uma regra de navegação. Quem muda de página deve encontrar o menu no mesmo sítio, com as mesmas opções, para não ter de reaprender o site em cada página.

### Passo 9: Um article com uma figura

O conteúdo principal desta página é a ficha de um livro. Aplica o teste do `article`: se copiasses a ficha para o site da biblioteca, fazia sentido sozinha? Faz: tem título, descrição, capa e informações. Por isso fica num `article`, dentro do `main`:

```html
<main>
  <article>
    <h1>Primeiros passos na Web</h1>
    <p>
      Um livro curto, com capítulos de poucas páginas, para quem quer
      perceber como se faz uma página web sem saber nada de programação.
    </p>

    <figure>
      <img src="imagens/capa-primeiros-passos-na-web.svg"
           alt="Capa azul com o título Primeiros passos na Web em letras brancas e o desenho de um globo terrestre."
           width="240" height="320">
      <figcaption>
        Capa da edição que está na biblioteca da escola.
        Livro fictício, criado para este exemplo.
      </figcaption>
    </figure>
    <!-- As secções do livro vêm a seguir. -->
  </article>
</main>
```

O raciocínio do `alt` foi o da secção "O texto alternativo". Nesta página, a capa serve para reconhecer o livro na estante da biblioteca. Por isso o `alt` descreve o que se vê na capa: a cor, o título e o desenho. Não começa por "Imagem de", e não repete a legenda.

A legenda acrescenta o que o `alt` não diz: de que edição é a capa e o aviso de que o livro é fictício. Como a imagem e a legenda formam uma unidade, ficam juntas num `figure`.

Os valores de `width` e `height` são 240 e 320, as medidas do desenho da capa. Como o desenho é SVG, podia ser mostrado maior sem perder qualidade, mas estas medidas dizem ao browser que espaço reservar.

### Passo 10: Duas listas, duas decisões

A ficha tem uma secção "O que vais aprender" e uma secção "Como o usar". As duas são listas, mas de tipos diferentes:

```html
<section>
  <h2>O que vais aprender</h2>
  <ul>
    <li>O que fazem o browser e o servidor quando abres uma página.</li>
    <li>Como se escreve a estrutura de uma página com HTML.</li>
    <li>Como se ligam várias páginas umas às outras.</li>
    <li>Como se descreve uma imagem a quem não a pode ver.</li>
  </ul>
</section>

<section>
  <h2>Como o usar</h2>
  <ol>
    <li>Lê os capítulos pela ordem, porque cada um usa o anterior.</li>
    <li>No fim de cada capítulo, faz o exercício no computador antes de avançar.</li>
    <li>Anota as dúvidas e leva-as à aula seguinte.</li>
  </ol>
</section>
```

Aplica o teste das listas a cada uma. Trocar dois assuntos de "O que vais aprender" não torna a informação errada: é um `ul`. Trocar o primeiro e o último passo de "Como o usar" torna a informação errada. Não faz sentido levar as dúvidas à aula antes de ler: é um `ol`.

### Passo 11: A tabela do horário

A secção "Onde o encontrar" diz em que estante está o livro e mostra o horário da biblioteca. Um horário é informação em linhas e colunas, e cada valor responde a uma pergunta do tipo "a que horas fecha à quarta-feira?". Passa o teste da tabela de dados. A tabela completa tem uma linha por dia, de segunda a sexta-feira, com a forma que viste na secção "Tabelas de dados". Tem um `caption` com o nome da tabela, um `thead` com os três cabeçalhos de coluna e um `tbody` com uma linha por dia. Cada linha tem o dia num `th` de linha e as duas horas em `td`.

O `caption` diz "(fictício)" porque o horário foi inventado para o exemplo. Uma tabela de dados verdadeiros deve dizer, sempre que possível, de onde vêm os dados.

### Passo 12: O aside e o caminho de volta

Depois do `article`, ainda dentro do `main`, há uma caixa com uma dica e uma ligação de regresso:

```html
<aside>
  <h2>Dica de quem já o leu</h2>
  <p>
    Não saltes o capítulo sobre ligações: é o que mais vais usar
    quando fizeres o teu próprio site.
  </p>
</aside>

<p><a href="index.html">Voltar à lista de recursos</a></p>
```

A dica é um `aside`: está relacionada com o livro, mas quem a saltar não perde nada da ficha. Fica fora do `article` porque não faz parte da ficha do livro. É um comentário ao lado dela.

A ligação "Voltar à lista de recursos" dá a esta página um caminho de volta à página de onde se veio, além do menu. Não está num `nav`, porque não é a navegação principal do site: é uma ligação solta no fim do conteúdo.

O índice dos títulos desta página é o que viste na secção "Títulos: de h1 a h6". Tem um `h1` com o nome do livro e cinco `h2`, um por secção e um para a dica.

### Passo 13: A página Sobre e uma ligação para fora

A terceira página, [sobre.html](../exemplos/frontend/estante-digital/sobre.html), segue o mesmo esqueleto, o mesmo cabeçalho e o mesmo rodapé. Tem um `h1`, "Sobre a Estante Digital", e três secções. A secção "Saber mais" tem a única ligação para outro site:

```html
<p>
  Para consultares o significado de cada etiqueta, usa também a
  <a href="https://developer.mozilla.org/pt-BR/docs/Web/HTML/Reference/Elements">lista de elementos HTML da MDN</a>,
  em português do Brasil.
</p>
```

O endereço é absoluto e começa por `https://`, porque o destino não está na pasta do site. O texto da ligação diz o que se vai encontrar. A frase avisa que a página está em português do Brasil, para que a pessoa não se surpreenda.

### Passo 14: Verificar

Com as três páginas escritas, faz-se a verificação da secção "Verificar uma página".

As ligações. Na página inicial, "Início" leva à própria página inicial e "Sobre" leva à página Sobre. "Primeiros passos na Web" leva à página do livro. Na página do livro, "Início" e "Voltar à lista de recursos" levam à página inicial, e "Sobre" leva à página Sobre. Na página Sobre, as duas ligações do menu funcionam, e a ligação para a MDN abre a página da MDN. Nenhuma ligação fica sem destino, e de todas as páginas se volta ao princípio.

O teclado. Na página inicial, a primeira tecla Tab leva o foco a "Início", a segunda a "Sobre" e a terceira a "Primeiros passos na Web". Com o foco nessa ligação, Enter abre a página do livro. A ordem do foco é a ordem do HTML, e é a ordem de leitura.

A árvore. No separador Elements, a árvore de cada página tem os elementos do ficheiro, pela mesma ordem, sem parágrafos vazios nem elementos mudados de sítio. Isto quer dizer que o browser não teve de corrigir nenhum erro. Na árvore de acessibilidade da página do livro aparecem cinco pontos de referência. São o cabeçalho (*banner*), a navegação (*navigation*), o conteúdo principal (*main*), a caixa da dica (*complementary*) e o rodapé (*contentinfo*). A capa aparece como imagem, com o nome que lhe demos no `alt`. O logótipo não aparece, porque tem o `alt` vazio.

A página passou as quatro verificações. Está pronta, por agora. No próximo tema vai ganhar aspeto com CSS, e a verificação volta a fazer-se.

## Erros frequentes

Estes são os erros que mais aparecem nas primeiras páginas e que não ficaram nas secções da matéria. Para cada um tens o que se vê, porque acontece e como se corrige. Alguns erros estão explicados na secção da ideia a que pertencem. O "clica aqui" e o endereço sem `https://` estão em "Ligações". O caminho do disco que só funciona no teu computador está em "Caminhos relativos". Os títulos que saltam níveis estão em "Títulos: de h1 a h6", e o `alt` em falta em "O texto alternativo". A tabela para arrumar a página está em "Tabelas não servem para arrumar a página". O negrito que não acaba e a lista dentro de um parágrafo estão em "Como o browser lida com os erros".

### A imagem não aparece

O que se vê: no sítio da imagem aparece um pequeno ícone de imagem partida, ou só o texto do `alt`, ou nada.

Porque acontece: quase sempre, o caminho do `src` não corresponde ao sítio onde a imagem está. As razões mais frequentes são quatro. A imagem pode estar noutra pasta, por exemplo ainda nas Transferências. O nome pode ter uma letra trocada, a mais ou a menos, como `fotografia.jpg` no disco e `fotogafia.jpg` no código. A extensão pode estar trocada, como `.jpeg` no disco e `.jpg` no código. Ou pode faltar a pasta no caminho, como `capa.svg` em vez de `imagens/capa.svg`. Uma diferença só de maiúsculas e minúsculas, como `Foto.jpg` no disco e `foto.jpg` no código, não faz falhar a imagem no teu computador. O Windows e o macOS tratam os dois nomes como o mesmo ficheiro. Faz falhar quando o site for publicado, como explica a secção "Caminhos relativos", e por isso também se corrige.

Como se corrige: compara letra a letra o caminho do `src` com o que vês no explorador de ficheiros. Começa na pasta onde está a página.

### A ligação dá "ficheiro não encontrado"

O que se vê: carregas na ligação e o browser mostra uma página de erro a dizer que o ficheiro não existe.

Porque acontece: a mesma razão dos caminhos das imagens, ou uma ligação para uma página que ainda não escreveste.

Como se corrige: confirma o nome do ficheiro de destino e a pasta onde está. Se a página ainda não existe, retira a ligação até ela existir.

### Mudei o ficheiro e a página não mudou

O que se vê: alteraste o ficheiro no editor, mas o browser mostra a página como estava.

Porque acontece: há três causas possíveis. Não guardaste o ficheiro, ou não recarregaste a página no browser, ou estás a editar uma cópia diferente da que está aberta no browser. No VS Code, um ficheiro por guardar tem uma bolinha no separador, no lugar da cruz de fechar.

Como se corrige: guarda (Ctrl+S no Windows, Cmd+S no Mac) e recarrega a página (F5 no Windows, Cmd+R no Mac). Se continuar igual, confirma na barra de endereço do browser qual é o ficheiro aberto.

### O ficheiro abre como texto, ou chama-se `index.html.txt`

O que se vê: o browser mostra as etiquetas como texto, em vez da página, ou o ficheiro abre noutro programa.

Porque acontece: o ficheiro foi guardado num editor de texto simples, que acrescentou `.txt` ao nome. O Windows esconde muitas vezes as extensões, e por isso o nome parece certo.

Como se corrige: usa o VS Code para criar os ficheiros. Se o problema já aconteceu, ativa no explorador de ficheiros a opção de mostrar as extensões dos nomes, e renomeia o ficheiro.

### Aparece um título onde devia estar texto normal

O que se vê: o texto que vem depois de um título aparece também com letra de título, grande e a negrito. No separador Elements vês dois `h2` onde só escreveste um.

Porque acontece: a barra esquecida numa etiqueta de fecho de um título. Sem a barra, o segundo `<h2>` de `<h2>Livros<h2>` é uma etiqueta de abertura. O browser fecha ali o primeiro título, abre outro, e o que vem a seguir fica dentro desse segundo título.

Como se corrige: a etiqueta de fecho tem sempre a barra: `</h2>`.

### A língua da página está errada

O que se vê: no ficheiro, o `html` tem `lang="en"`. No ecrã não muda nada, mas um leitor de ecrã lê o teu português com pronúncia inglesa.

Porque acontece: o esqueleto foi gerado automaticamente pelo editor. O VS Code tem um atalho que escreve o esqueleto sozinho, mas põe `lang="en"`.

Como se corrige: muda para `lang="pt-PT"`. Enquanto estás a aprender, escreve o esqueleto à mão, que é a melhor forma de o saber de cor.

## Palavras novas deste guia

- HTML: a linguagem de marcação que diz ao browser o que cada pedaço de conteúdo de uma página é.
- Hipertexto: texto com ligações para outros textos, que se lê saltando de um para outro.
- Marcação: as marcas escritas num texto para dizer o que cada pedaço é.
- Etiqueta: uma palavra entre `<` e `>`, como `<h1>`. A de fecho leva uma barra, como `</h1>`.
- Elemento: a etiqueta de abertura, o conteúdo e a etiqueta de fecho, juntos. É o que representa uma coisa na página.
- Atributo: uma informação extra sobre um elemento, escrita na etiqueta de abertura com a forma `nome="valor"`.
- Elemento vazio: um elemento sem conteúdo e sem etiqueta de fecho, como `img`, `meta` e `br`.
- Aninhar: pôr um elemento dentro de outro. Fecha-se primeiro o que se abriu por último.
- Pai, filho e irmãos: o elemento que contém outro diretamente é o pai dele, e o de dentro é o filho. Dois filhos do mesmo pai são irmãos.
- Indentação: os espaços no início das linhas, que mostram quem está dentro de quem. O browser ignora-os.
- Comentário: um texto entre `<!--` e `-->`, para quem lê o código, que o browser ignora.
- Esqueleto: a estrutura com que todas as páginas começam: o doctype, o `html`, o `head` e o `body`.
- Doctype: a primeira linha, `<!doctype html>`, que diz ao browser para seguir as regras modernas.
- Modo de compatibilidade: o modo em que o browser entra quando falta o doctype, e que imita os browsers antigos.
- Elemento raiz: o elemento `html`, que contém todos os outros.
- Leitor de ecrã: um programa que lê a página em voz alta a pessoas cegas ou com pouca visão.
- UTF-8: a tabela que transforma os bytes do ficheiro em letras, com as letras de todas as línguas.
- Índice da página: a lista dos títulos, com a indentação a mostrar os níveis.
- Parágrafo: um bloco de texto corrido, com uma ideia, marcado com `p`.
- Lista não ordenada: uma lista em que a ordem dos itens não importa, marcada com `ul`.
- Lista ordenada: uma lista em que a ordem dos itens importa, marcada com `ol`.
- Ligação: um elemento `a` que leva a outro sítio, com o destino no atributo `href`.
- Texto da ligação: o conteúdo do `a`, em que se carrega, e que diz para onde a ligação leva.
- Caminho relativo: o caminho de um ficheiro a partir do ficheiro onde estás, como `sobre.html` ou `imagens/logotipo.svg`.
- Endereço absoluto: um endereço completo, começado por `https://`, para levar a outro site.
- Botão: um elemento `button`, que faz uma ação sem sair do sítio.
- Texto alternativo: o valor do `alt`, que substitui a imagem quando ela não pode ser vista.
- Semântica: o significado. Escrever HTML semântico é escolher cada elemento pelo que o conteúdo é.
- Árvore de acessibilidade: a árvore que o browser constrói a partir do DOM, e que os leitores de ecrã recebem.
- Papel: o que uma coisa é, na árvore de acessibilidade, como título, ligação ou navegação.
- Nome: o texto que identifica uma coisa na árvore de acessibilidade, como o texto de uma ligação ou o `alt` de uma imagem.
- Ponto de referência: uma zona da página a que um leitor de ecrã salta diretamente, como a navegação ou o conteúdo principal.
- Tabela de dados: uma tabela em que cada valor responde a uma pergunta que junta uma linha e uma coluna.
- Validador: o serviço do W3C que lê um ficheiro HTML e faz a lista dos erros, com o número da linha.
- Foco: a moldura que mostra em que ligação estás quando percorres a página com o teclado.

Os elementos deste guia, e o que cada um marca:

- `p`: um parágrafo. `br`: uma mudança de linha que faz parte do conteúdo.
- `h1` a `h6`: os títulos, do mais importante para o menos importante.
- `strong`: texto de importância forte. `em`: a palavra com ênfase.
- `ul`, `ol` e `li`: a lista não ordenada, a lista ordenada e cada item.
- `a`: uma ligação. `img`: uma imagem.
- `figure` e `figcaption`: uma imagem com a sua legenda, e a legenda.
- `header`: o cabeçalho. `nav`: a navegação principal. `main`: o conteúdo principal. `footer`: o rodapé.
- `section`: uma parte do conteúdo com título próprio. `article`: um conteúdo que faria sentido sozinho noutro sítio. `aside`: um conteúdo secundário, que se pode saltar.
- `div`: uma caixa genérica, sem significado.
- `table` e `caption`: a tabela e a legenda dela.
- `thead` e `tbody`: o grupo das linhas de cabeçalho e o grupo das linhas de dados.
- `tr`, `th` e `td`: uma linha, uma célula de cabeçalho e uma célula de dados.

Os atributos deste guia:

- `lang`: a língua da página. `charset`: a tabela das letras.
- `href`: o destino de uma ligação. `id`: o nome único de um elemento.
- `src`: o ficheiro de uma imagem. `alt`: o texto alternativo.
- `width` e `height`: a largura e a altura de uma imagem.
- `scope`: a que se aplica um cabeçalho de tabela.

## Verificar o que aprendeste

Usa estas perguntas para te testares. Responde a cada uma sem olhar para o guia. Se não conseguires, volta à secção que explica a ideia.

1. Na linha `<a href="sobre.html">Sobre a Estante Digital</a>`, aponta o elemento, a etiqueta de abertura e a etiqueta de fecho. Aponta também o atributo e o valor dele. O que aparece na página?
2. Porque é que `<img>` não tem `</img>`?
3. Escreve de memória o esqueleto completo de uma página. Diz, para cada linha, para que serve.
4. Uma página em português tem `lang="en"`. Quem é prejudicado, e como?
5. Uma página tem estes títulos, por esta ordem: `h1` Torneios, `h3` Regras, `h2` Inscrições, `h4` Prémios. Onde estão os saltos de nível? Há algum que não seja um erro?
6. Os passos para criar um ficheiro no VS Code vão numa lista ordenada ou não ordenada? E as cores do logótipo de um clube? Justifica cada uma com o teste da troca.
7. Na pasta da Estante Digital, que `href` escreves no `index.html` para ligar ao `sobre.html`? Que `src` escreves para o logótipo? E se a página estivesse dentro de uma pasta `recursos`?
8. Porque é que o nome do site da Estante Digital está num `p` e não num `h1`?
9. Porque é que o logótipo da Estante Digital tem `alt=""` e a capa do livro tem um `alt` com texto? Que `alt` levaria a capa se aparecesse pequenina numa lista, ao lado do título do livro?
10. Qual é a diferença entre uma ligação e um botão? Com que teclas se ativa cada um?
11. Que elemento usas para cada uma destas zonas?
    - O menu do site.
    - Uma notícia que faria sentido sozinha noutro site.
    - Uma caixa "Sabias que?" ao lado de uma explicação.
    - A nota final com o ano letivo e o contacto.
12. Numa tabela de horário, o que é que o `scope` permite a um leitor de ecrã dizer quando chega à célula `13:00`?
13. Quais são as quatro verificações de uma página? O que procuras em cada uma?
14. Este pedaço de uma página tem quatro erros. Encontra-os, diz para cada um o que o browser faz ou o que corre mal a quem usa a página, e escreve a versão corrigida.

    ```html
    <main>
      <h1>Clube de fotografia da escola</h1>
      <h3>As saídas deste período</h3>
      <p>Às terças-feiras à tarde, saímos pela vila com a máquina. Este período vamos fotografar:
        <ul>
          <li>as árvores do jardim municipal</li>
          <li>as fachadas de azulejo da rua principal</li>
        </ul>
      </p>
      <img src="imagens/azulejos.jpg">
      <p>Para veres as fotografias da última saída, <a href="ultima-saida.html">clica aqui</a>.</p>
    </main>
    ```

15. O que te custou mais neste tema: o aninhamento, os caminhos, o texto alternativo, escolher entre os elementos semânticos ou as tabelas? Escreve duas ou três linhas e guarda-as junto do plano do teu site.

## O que vem a seguir

Para praticar este tema, faz o [laboratório](02-html-e-semantica-laboratorio.md) e depois a [ficha de exercícios](02-html-e-semantica-exercicios.md). No laboratório vais construir no computador duas páginas do teu site, a partir do mapa e dos wireframes que fizeste no tema 01. Vais ligá-las nos dois sentidos e verificá-las com as quatro verificações do passo 14. Depois vais provocar de propósito os erros mais comuns, para aprenderes a reconhecê-los e a corrigi-los. A ficha treina as mesmas ideias, uma de cada vez, num site que não é o teu.

O tema seguinte é CSS explicado e Flexbox. As tuas páginas têm agora estrutura e significado, mas têm o aspeto por omissão do browser: letra preta, fundo branco, tudo empilhado. No tema do CSS vais dar-lhes aspeto, com cores, tipos de letra, espaços e menus lado a lado, sem mudar uma única etiqueta do HTML. É aí que se vê o valor da divisão de trabalho: como a estrutura está certa, o CSS só tem de tratar do aspeto. No tema do Git aprendes a guardar versões da pasta do teu site, para que nenhuma alteração se perca.

## Para saber mais

- MDN Web Docs, [lista de elementos HTML](https://developer.mozilla.org/pt-BR/docs/Web/HTML/Reference/Elements), em português do Brasil: cada elemento explicado, com exemplos.
- W3C, Web Accessibility Initiative, [tutorial sobre imagens](https://www.w3.org/WAI/tutorials/images/), em inglês: o texto alternativo, com muitos exemplos de cada situação.
- W3C, Web Accessibility Initiative, [tutorial sobre tabelas](https://www.w3.org/WAI/tutorials/tables/), em inglês: os cabeçalhos das tabelas e o `scope`, com exemplos.
- W3C, [serviço de validação de HTML](https://validator.w3.org/), em inglês: envias o teu ficheiro e recebes a lista dos erros, com o número da linha.

![Rodapé](../imagens/rodape.png)
