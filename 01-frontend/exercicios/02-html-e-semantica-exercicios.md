![Cabeçalho](../../imagens/cabecalho.png)

# Ficha de exercícios: HTML e semântica

Praticas as ideias do tema, uma de cada vez, no site da Banda da Escola. Os exercícios 1 a 7 são obrigatórios. Escreve as respostas no VS Code, num ficheiro `respostas.md`, com o número do exercício e a letra da alínea. A tabela do exercício 7 vai numa página `bilhetes.html`. Guarda os dois ficheiros numa pasta para esta ficha, fora da pasta do teu site, e entrega-os onde o professor indicar. Para rever: o [guia do tema](../02-html-e-semantica.md) e o [laboratório](../laboratorios/02-html-e-semantica-laboratorio.md).

## O cenário

A Banda da Escola é um site imaginário. Tem uma página inicial, uma página dos concertos, uma página dos músicos, uma página para cada músico e uma página "Como entrar na banda".

## Exercício 1: Elementos, etiquetas e atributos

Estas duas linhas são da página inicial da Banda da Escola:

```html
<p>Os bilhetes não são reembolsados: <strong>confirma a data no <a href="concertos.html">calendário de concertos</a> antes de comprares bilhete</strong>.</p>
<img src="imagens/logotipo.png" alt="" width="48" height="48">
```

**a)** Quantos elementos há nas duas linhas? Escreve o nome de cada um.

**b)** Escreve a etiqueta de abertura e a etiqueta de fecho do elemento `a`.

**c)** Faz a lista dos atributos do `img`, com o valor de cada um.

**d)** Porque é que o `img` não tem etiqueta de fecho?

**e)** Qual é o elemento pai do `a`?

Rever: [Etiquetas e elementos](../02-html-e-semantica.md#etiquetas-e-elementos), [Atributos](../02-html-e-semantica.md#atributos) e [Elementos dentro de elementos](../02-html-e-semantica.md#elementos-dentro-de-elementos).

<details>
<summary>Pista</summary>

Cada etiqueta de abertura começa um elemento. Um atributo tem sempre a forma `nome="valor"` e está dentro da etiqueta de abertura, mesmo quando o valor está vazio. Para o pai, relê a definição de pai e filho no guia.

</details>

## Exercício 2: Os títulos de uma página

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

**a)** Escreve o índice da página, com o nível de cada título (`h1`, `h2` e os que precisares). A indentação mostra os níveis.

**b)** O título principal da página inicial do site é "Bem-vindos à Banda da Escola". Mais abaixo, tem uma parte curta com o título "Como entrar na banda", com uma frase e uma ligação para a página da alínea a). Que nível dás a este título na página inicial? Justifica numa frase.

Rever: [Títulos: de h1 a h6](../02-html-e-semantica.md#títulos-de-h1-a-h6).

<details>
<summary>Pista</summary>

Começa pelo assunto da página inteira, que é o `h1`. Depois, para cada título, pergunta se é uma parte nova da página ou uma parte dentro da anterior. Na alínea b), faz a mesma primeira pergunta, mas sobre a página inicial.

</details>

## Exercício 3: Ordenada ou não ordenada

Para cada conteúdo, escolhe `ul` ou `ol` e justifica numa frase com o teste da troca de itens.

**a)** Os instrumentos que a banda tem: guitarra, baixo, bateria, teclado e saxofone.

**b)** Os passos para montar a bateria antes de um ensaio.

**c)** A classificação das três bandas no concurso regional.

**d)** Os nomes dos cinco músicos da banda, escritos por ordem alfabética.

Rever: [Listas](../02-html-e-semantica.md#listas).

<details>
<summary>Pista</summary>

Imagina que trocas o primeiro item com o último. Pergunta se a informação passa a estar errada, e não se passa a ser estranha.

</details>

## Exercício 4: Caminhos relativos

Esta é uma parte da pasta do site da Banda da Escola:

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

**e)** Um colega escreveu, no `concertos.html`, `src="C:\Users\Rui\Desktop\banda-da-escola\imagens\palco.jpg"`. A imagem aparece no computador dele? E no teu, se copiares a pasta dele para o teu computador? Explica porquê numa frase.

Rever: [Caminhos relativos](../02-html-e-semantica.md#caminhos-relativos).

<details>
<summary>Pista</summary>

O caminho parte da pasta onde está o ficheiro que tem a ligação. Nas alíneas b), c) e d), esse ficheiro está dentro da pasta `musicos`.

</details>

## Exercício 5: O texto alternativo

Escreve o valor do `alt` de cada imagem. Se achares que deve ficar vazio, escreve `alt=""` e diz porquê.

**a)** O logótipo da banda é uma clave de sol desenhada a dourado. No cabeçalho de todas as páginas, está ao lado do texto "Banda da Escola", e aí tem `alt=""`. Nas páginas dos músicos, no fim do texto, o mesmo logótipo aparece outra vez, sozinho e sem texto ao lado. Quem carrega nele volta à página inicial. Que `alt` leva o logótipo neste segundo sítio?

**b)** Na página dos concertos, dentro de um `figure`, uma fotografia da banda a tocar. A legenda, no `figcaption`, diz "Concerto de Natal de 2025, no auditório da escola". A fotografia mostra os cinco músicos no palco, com a vocalista à frente, e o público de pé.

**c)** Na página "Como entrar na banda", um mapa com o caminho da entrada principal da escola até à sala de ensaios. O texto da página não explica o caminho: só o mapa o mostra. O mapa é um desenho colorido, com os pavilhões a azul, as árvores a verde e o caminho em setas vermelhas. Nele vê-se que, da entrada principal, se segue em frente até ao pavilhão B. A sala de ensaios é a segunda porta à esquerda.

Rever: [O texto alternativo](../02-html-e-semantica.md#o-texto-alternativo) e [Imagem com legenda: figure e figcaption](../02-html-e-semantica.md#imagem-com-legenda-figure-e-figcaption).

<details>
<summary>Pista</summary>

Faz a pergunta do telefone para cada imagem. Na alínea a), a imagem é a mesma do cabeçalho, mas o que está à volta dela não é. Na alínea b), não repitas o que a legenda já diz. Na alínea c), pensa no que perde quem não vê o mapa.

</details>

## Exercício 6: As zonas de uma página

Este é o wireframe da página dos concertos, descrito zona a zona, de cima para baixo:

1. Uma faixa no topo, com o logótipo, o nome "Banda da Escola" e o menu com as ligações Início, Concertos e Músicos.
2. O título "Próximos concertos".
3. Três blocos iguais, um por concerto, cada um com o nome do concerto, a data, o local e uma frase de descrição.
4. Um bloco com o título "Como tudo começou" e duas frases. A banda nasceu em 1998, com três alunos do 10.º ano. Tocou pela primeira vez na festa de fim de ano.
5. Uma faixa no fundo, com o contacto do professor responsável e o ano letivo.

**a)** Para cada zona, diz que elemento ou elementos usavas: `header`, `nav`, `main`, `section`, `article`, `aside`, `footer`, ou um título, de `h1` a `h6`. Quando uma zona precisa de mais do que um elemento, escreve-os todos e diz qual fica dentro de qual.

**b)** Diz quais das cinco zonas ficam dentro do `main`.

**c)** Justifica, com as perguntas do guia, o elemento que escolheste para a zona 3.

Rever: [As zonas da página: header, nav, main e footer](../02-html-e-semantica.md#as-zonas-da-página-header-nav-main-e-footer) e [As partes do conteúdo: section, article e aside](../02-html-e-semantica.md#as-partes-do-conteúdo-section-article-e-aside).

<details>
<summary>Pista</summary>

Um título escolhe-se pelo nível, e não pelo diagrama. Para os blocos, segue as perguntas do diagrama do guia, pela ordem, e para na primeira a que respondes sim. Na zona 1 há duas coisas: a faixa inteira e o menu dentro dela. Na zona 3, faz as perguntas sobre um só bloco, e não sobre os três juntos.

</details>

## Exercício 7: Uma tabela de dados

Os bilhetes do concerto de primavera têm estes preços, inventados:

- um aluno da escola paga 2 euros se comprar antes e 3 euros no dia;
- um adulto paga 5 euros antes e 7 euros no dia;
- uma criança até aos 12 anos não paga, nem antes nem no dia.

**a)** Escreve uma tabela com estes preços, com uma legenda, numa página completa, com o esqueleto, chamada `bilhetes.html`. Decide o que fica nas linhas e o que fica nas colunas, e justifica a escolha numa frase, num comentário logo antes da tabela. Usa `caption`, `thead`, `tbody`, `th` com `scope` e `td`.

**b)** Um leitor de ecrã chega à célula com o preço do adulto no dia. Que duas informações é que os teus cabeçalhos lhe permitem anunciar, além do preço?

Rever: [Uma tabela de dados cruza linhas e colunas](../02-html-e-semantica.md#uma-tabela-de-dados-cruza-linhas-e-colunas) e [Os cabeçalhos e a legenda dizem o que é cada valor](../02-html-e-semantica.md#os-cabeçalhos-e-a-legenda-dizem-o-que-é-cada-valor).

<details>
<summary>Pista</summary>

Antes do HTML, faz um esboço das duas arrumações possíveis e vê qual se lê melhor. O que conta é a justificação. Na primeira linha, a do `thead`, a célula do canto também é um `th`.

</details>

## Desafios

1. No teu site, acrescenta uma terceira página do teu mapa, com o mesmo esqueleto, o mesmo cabeçalho e o mesmo rodapé. O menu fica igual nas três páginas. Se o conteúdo o justificar, usa um elemento que ainda não usaste, como um `article` ou um `aside`. Justifica a escolha num comentário logo antes dele. Depois, verifica as três páginas e regista a verificação no `registo.md` ao lado da pasta do teu site. Rever: [Verificar uma página](../02-html-e-semantica.md#verificar-uma-página).

2. Esta é a página dos músicos da Banda da Escola. No browser, abre sem nenhum aviso e parece quase normal, mas tem cinco erros. Imagina que as outras páginas e a imagem existem. Escreve a página corrigida num ficheiro `musicos.html`, na pasta desta ficha. Junto de cada correção, põe um comentário a dizer quem era prejudicado pelo erro, e como. Rever: [O destino de uma ligação](../02-html-e-semantica.md#o-destino-de-uma-ligação).

   ```html
   <!doctype html>
   <html lang="pt-PT">
     <head>
       <meta charset="utf-8">
       <meta name="viewport" content="width=device-width, initial-scale=1">
       <title>Músicos | Banda da Escola</title>
     </head>
     <body>
       <header>
         <p>Banda da Escola</p>
         <nav>
           <li><a href="index.html">Início</a></li>
           <li><a href="concertos.html">Concertos</a></li>
           <li><a href="musicos.html">Músicos</a></li>
         </nav>
       </header>
       <main>
         <h1>Os músicos</h1>
         <p>A banda tem cinco músicos, todos alunos da escola. Vê os <a href="ensaios">dias de ensaio</a>, mais abaixo.</p>
         <figure>
           <img src="imagens/ensaio.jpg" alt=Os cinco músicos a ensaiar com os seus instrumentos width="600" height="400">
         </figure>
         <figcaption>Ensaio de outubro, na sala de música.</figcaption>
         <h2 id="ensaios">Ensaios</h2>
         <p>Ensaiamos à quinta-feira. Vê o <a>horário das salas</a href="horarios.html">.</p>
       </main>
       <footer>
         <p>Banda da Escola, ano letivo 2026/2027. Conteúdo fictício.</p>
       </footer>
     </body>
   </html>
   ```

3. Um colega fez a página dos concertos com uma tabela de uma linha e duas colunas. O menu ficou numa coluna e os concertos na outra. Diz-te que a página tem mesmo dados: o nome, a data e o local de cada concerto. Que parte da página podia ser uma tabela de dados, e que parte nunca pode? Responde no `respostas.md`. Rever: [Tabelas não servem para arrumar a página](../02-html-e-semantica.md#tabelas-não-servem-para-arrumar-a-página).

## Critérios de conclusão

- Os exercícios 1 a 7 estão respondidos, no `respostas.md` e no `bilhetes.html`, com as justificações que cada um pede.
- No exercício 2, o índice tem um só `h1` e nenhum salto de nível a descer.
- No exercício 4, cada caminho chega ao ficheiro a partir da pasta do ficheiro que tem a ligação.
- No exercício 5, nenhuma imagem ficou sem `alt`, e nenhum `alt` repete a legenda ou o texto ao lado.
- No exercício 7, a tabela tem legenda, cabeçalhos com `scope` e os preços em células de dados.

![Rodapé](../../imagens/rodape.png)
