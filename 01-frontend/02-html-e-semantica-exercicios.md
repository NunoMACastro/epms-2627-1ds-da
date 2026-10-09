![Cabeçalho](../imagens/cabecalho.png)

# Ficha de exercícios: HTML e semântica

UC: UC02833, Conceber aplicações para a web na vertente frontend

Bloco: F02

Requisitos: UC02833.K03, UC02833.K04, UC02833.K09, UC02833.A04, UC02833.A05, UC02833.A06, UC02833.A11, UC02833.C01

| Identificação | Valor |
| --- | --- |
| Material | Ficha do bloco F02, acompanha o [guia](02-html-e-semantica.md) e o [laboratório](02-html-e-semantica-laboratorio.md) |
| Tempo total | 80 minutos dos 300 do bloco, nos exercícios 1 a 7. O desafio e a secção "Para ires mais longe" são opcionais e ficam fora destes 80 minutos |
| Entrega | As respostas escritas dos sete exercícios, no caderno ou num ficheiro, com o HTML do exercício 7 escrito à mão ou num ficheiro `.html`; o desafio e os exercícios de "Para ires mais longe", se os fizeres |

## Objetivos e conceitos necessários

Vais praticar, um de cada vez, os assuntos do bloco: o vocabulário do HTML, a hierarquia dos títulos, a escolha entre listas, os caminhos relativos, o texto alternativo, os elementos semânticos e as tabelas de dados.

Antes de começares, deves ter lido a teoria e o exemplo explicado do [guia](02-html-e-semantica.md) e feito pelo menos a parte A do [laboratório](02-html-e-semantica-laboratorio.md). Cada exercício diz em que secção do guia está a matéria. Se encravares, volta a essa secção antes de olhares para o apoio, no fim da ficha.

Todos os exercícios, menos o desafio, usam o mesmo site imaginário, o da Banda da Escola. Não é o teu site nem o da Estante Digital: é um terceiro site, para treinares as mesmas ideias num caso novo.

## Como está organizada a ficha

Resolve os exercícios pela ordem. Cada exercício treina uma só coisa, e em cada um há uma pequena decisão que o exemplo do guia não tomou.

| Exercício | O que treina | Tempo |
| --- | --- | ---: |
| 1 | Reconhecer elementos, etiquetas e atributos | 10 min |
| 2 | Dar a cada título o nível certo | 10 min |
| 3 | Escolher entre lista ordenada e não ordenada | 5 min |
| 4 | Escrever caminhos relativos, incluindo para a pasta de cima | 15 min |
| 5 | Escrever o texto alternativo conforme o contexto | 10 min |
| 6 | Escolher os elementos semânticos das zonas de uma página | 15 min |
| 7 | Construir uma tabela de dados | 15 min |
| Total da parte obrigatória | Exercícios 1 a 7 | 80 min |
| Desafio opcional | Acrescentar uma terceira página ao teu site | 30 min |
| Para ires mais longe | Opcional: erros que o browser esconde e uma tabela usada para arrumar a página | fora dos 80 min |

## Exercício 1: Elementos, etiquetas e atributos (10 min)

A matéria está na secção "Elementos, etiquetas e atributos" do guia.

Estas duas linhas são da página inicial da Banda da Escola:

```html
<p>Os bilhetes não são reembolsados: <strong>confirma a data no <a href="concertos.html">calendário de concertos</a> antes de comprares bilhete</strong>.</p>
<img src="imagens/palco.jpg" alt="A banda a tocar no palco do auditório, com o público de pé." width="800" height="500">
```

**a)** Quantos elementos há nas duas linhas? Escreve o nome de cada um.

**b)** Escreve a etiqueta de abertura e a etiqueta de fecho do elemento `a`.

**c)** Faz a lista dos atributos do `img`, com o valor de cada um.

**d)** Porque é que o `img` não tem etiqueta de fecho?

**e)** Qual é o elemento pai do `a`?

## Exercício 2: Os títulos de uma página (10 min)

A matéria está na secção "Títulos: de h1 a h6" do guia.

A página "Como entrar na banda" tem estes títulos, pela ordem em que aparecem, ainda sem nível nenhum:

```text
Como entrar na banda
Quem pode entrar
Instrumentos que procuramos
Sopros
Percussão
Como é a audição
```

As partes "Sopros" e "Percussão" pertencem a "Instrumentos que procuramos".

**a)** Dá a cada título um nível, de `h1` a `h6`, e escreve o índice da página com a indentação a mostrar os níveis, como no passo 7 do exemplo explicado.

**b)** O título principal da página inicial do site é "Bem-vindos à Banda da Escola". Mais abaixo, a página inicial tem uma parte curta com o título "Como entrar na banda", uma frase e uma ligação para a página da alínea a). Que nível dás a este título na página inicial? Justifica numa frase.

## Exercício 3: Ordenada ou não ordenada (5 min)

A matéria está na secção "Listas" do guia.

Para cada conteúdo, escolhe `ul` ou `ol` e justifica numa frase com o teste da troca de itens.

**a)** Os instrumentos que a banda tem: guitarra, baixo, bateria, teclado e saxofone.

**b)** Os passos para montar a bateria antes de um ensaio.

**c)** A classificação das três bandas no concurso regional.

**d)** Os nomes dos cinco músicos da banda, escritos por ordem alfabética.

## Exercício 4: Caminhos relativos (15 min)

A matéria está na secção "Caminhos relativos" do guia.

A pasta do site da Banda da Escola é esta:

```text
banda-da-escola/
├── index.html
├── concertos.html
├── imagens/
│   ├── logotipo.png
│   └── palco.jpg
└── musicos/
    ├── baterista.html
    └── vocalista.html
```

Escreve o valor do `href` ou do `src` em cada caso.

**a)** No `index.html`, uma ligação para a página dos concertos.

**b)** No `musicos/baterista.html`, uma ligação para a página da vocalista.

**c)** No `musicos/baterista.html`, uma ligação de volta para a página inicial.

**d)** No `musicos/baterista.html`, a imagem do logótipo.

**e)** Um colega escreveu, no `concertos.html`, `src="C:\Users\Rui\Desktop\banda-da-escola\imagens\palco.jpg"`. A imagem aparece no computador dele? E no teu, se lhe copiares a pasta? Explica porquê numa frase.

## Exercício 5: O texto alternativo (10 min)

A matéria está nas secções "O texto alternativo" e "Imagem com legenda: figure e figcaption" do guia.

Escreve o valor do `alt` de cada imagem. Se achares que deve ficar vazio, escreve `alt=""` e diz porquê.

**a)** No cabeçalho de todas as páginas, o logótipo da banda, uma clave de sol desenhada a dourado, está mesmo ao lado do texto "Banda da Escola" e tem `alt=""`, como o logótipo da Estante Digital. Nas páginas dos músicos, no fim do texto, o mesmo logótipo aparece outra vez, sozinho e sem nenhum texto ao lado, e quem carrega nele volta à página inicial. Que `alt` leva o logótipo neste segundo sítio?

**b)** Na página dos concertos, dentro de um `figure`, uma fotografia da banda a tocar. A legenda, no `figcaption`, diz "Concerto de Natal de 2025, no auditório da escola". A fotografia mostra os cinco músicos no palco, com o vocalista à frente, e o público de pé.

**c)** Na página "Como entrar na banda", um mapa com o caminho da entrada principal da escola até à sala de ensaios. O texto da página não explica o caminho: só o mapa o mostra. No mapa vê-se que, da entrada principal, se segue em frente até ao pavilhão B, e que a sala de ensaios é a segunda porta à esquerda.

## Exercício 6: As zonas de uma página (15 min)

A matéria está na secção "Os elementos semânticos" do guia.

Este é o wireframe da página dos concertos, descrito por palavras, zona a zona, de cima para baixo:

1. Uma faixa no topo, com o logótipo, o nome "Banda da Escola" e o menu com as ligações Início, Concertos e Músicos.
2. O título "Próximos concertos".
3. Três blocos iguais, um por concerto, cada um com o nome do concerto, a data, o local e uma frase de descrição.
4. Um bloco com o título "Como tudo começou" e duas frases: a banda nasceu em 1998, com três alunos do 10.º ano, e tocou pela primeira vez na festa de fim de ano, no pavilhão da escola.
5. Uma faixa no fundo, com o contacto do professor responsável e o ano letivo.

**a)** Para cada zona, diz que elemento ou elementos usavas: `header`, `nav`, `main`, `section`, `article`, `aside`, `footer`, ou um título, de `h1` a `h6`. Uma das zonas precisa de dois elementos, um dentro do outro.

**b)** Diz quais das cinco zonas ficam dentro do `main`.

**c)** Justifica, com o teste da secção do guia, o elemento que escolheste para a zona 3.

## Exercício 7: Uma tabela de dados (15 min)

A matéria está na secção "Tabelas de dados" do guia e no passo 11 do exemplo explicado.

Os bilhetes do concerto de primavera têm estes preços (inventados): um aluno da escola paga 2 euros se comprar antes e 3 euros no dia; um adulto paga 5 euros antes e 7 euros no dia; uma criança até aos 12 anos não paga, antes nem no dia.

**a)** Escreve o HTML de uma tabela com estes preços, com uma legenda. Decide o que fica nas linhas e o que fica nas colunas, e justifica a escolha numa frase. Usa `caption`, `thead`, `tbody`, `th` com `scope` e `td`.

**b)** Um leitor de ecrã chega à célula com o preço do adulto no dia. Que duas informações é que os teus cabeçalhos lhe permitem anunciar, além do preço?

## Apoio

Usa estas pistas pela ordem em que aparecem, e só a seguinte se a anterior não tiver chegado. Nenhuma dá a resposta: indicam onde olhar.

**Exercício 1.** Conta as etiquetas de abertura: cada uma começa um elemento. Um atributo tem sempre a forma `nome="valor"` e está dentro da etiqueta de abertura. Para o pai, desenha a árvore da primeira linha, como a da secção "Elementos dentro de elementos".

**Exercício 2.** Começa por perguntar qual é o assunto da página inteira: é esse o `h1`. Depois, para cada título, pergunta se é uma parte nova da página ou uma parte dentro da anterior. Duas partes pertencem a uma terceira, e isso quer dizer que ficam um nível abaixo dela. Na alínea b), faz a mesma primeira pergunta, mas sobre a página inicial.

**Exercício 3.** Para cada lista, imagina que trocas o primeiro item com o último. Pergunta se a informação passa a estar errada, e não se passa a ser estranha.

**Exercício 4.** Põe o dedo na pasta onde está o ficheiro que tem a ligação: é daí que o caminho parte. Para descer a uma pasta, escreves o nome dela e uma barra. Para subir à pasta de cima, escreves `../`. Nas alíneas b), c) e d), o ficheiro com a ligação está dentro da pasta `musicos`.

**Exercício 5.** Faz a pergunta do telefone para cada imagem. Na alínea a), a imagem é a mesma do cabeçalho, mas o que está à volta dela não é: procura na secção "O texto alternativo" a situação que corresponde a este segundo sítio. Na alínea b), lê o que a legenda já diz, para não o repetires. Na alínea c), pensa no que perde quem não vê o mapa, sabendo que o texto da página não o substitui.

**Exercício 6.** Segue as perguntas da lista do guia, pela ordem, para cada zona. Na zona 1, repara que há duas coisas: a faixa inteira e o menu dentro dela. Nas zonas 3 e 4, faz as perguntas uma de cada vez e para na primeira a que respondes que sim. Na zona 3, faz as perguntas sobre um só bloco, e não sobre os três juntos.

**Exercício 7.** Começa por desenhar a tabela à mão, com os cabeçalhos no topo e à esquerda, antes de escreveres o HTML. Para decidir o que fica nas linhas, desenha as duas arrumações possíveis e vê qual se lê melhor; o que conta é a justificação que dás. Na primeira linha, a do `thead`, a célula do canto também é um `th`.

## Desafio opcional (30 min)

Acrescenta ao teu site uma terceira página do teu mapa, com o mesmo esqueleto, o mesmo cabeçalho e o mesmo rodapé das outras duas.

**a)** Antes de escreveres, decide onde entra a nova página na navegação, e altera o `nav` das três páginas para que todas tenham o mesmo menu. Explica numa frase porque é que o menu tem de ser igual nas três.

**b)** Na nova página, se o conteúdo o justificar, usa um elemento semântico que ainda não tenhas usado no teu site, como um `article` ou um `aside`, e justifica a escolha com o teste da secção do guia. Se nenhum se justificar, não o inventes: explica numa frase porquê.

**c)** Refaz a verificação da parte 8 do laboratório para as três páginas: ligações, ordem de leitura, teclado e árvore.

## Para ires mais longe

Esta secção é opcional e fica fora dos 80 minutos da ficha. Não precisas de fazer nada daqui para concluíres a ficha. Serve para quem terminou a parte obrigatória e quer mais prática, ou para estudar em casa.

### Mais longe 1: Erros que o browser esconde (15 min)

Esta página da Banda da Escola aparece no browser sem nenhum aviso, e parece quase normal. Tem cinco erros. Encontra-os, diz para cada um quem é prejudicado e como, e escreve a página corrigida.

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Músicos | Banda da Escola</title>
  </head>
  <body>
    <main>
      <h1>Os músicos</h1>
      <p>Conhece alguns dos músicos da banda:
        <ul>
          <li>Vocalista</li>
          <li>Baterista</li>
        </ul>
      </p>
      <h4>Ensaios</h4>
      <p>Ensaiamos à quinta-feira. Vê o <a href="www.escola.example/horarios">horário das salas</a>.</p>
      <img src="imagens/ensaio.jpg" width="600" height="400">
    </main>
  </body>
</html>
```

Pista: um dos erros não muda nada do que se vê na página, e só aparece no separador Elements. Outro só se nota quando a página é lida em voz alta.

### Mais longe 2: Uma tabela para arrumar a página (10 min)

A matéria está na secção "Tabelas não servem para arrumar a página" do guia.

Um colega fez a página dos concertos com uma tabela de uma linha e duas colunas: o menu na coluna da esquerda e os concertos na da direita. Dá-lhe duas razões para não o fazer, e diz com que elementos a devia escrever.

![Rodapé](../imagens/rodape.png)
