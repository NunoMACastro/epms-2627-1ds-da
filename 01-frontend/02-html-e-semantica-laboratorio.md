![Cabeçalho](../imagens/cabecalho.png)

# Laboratório: HTML e semântica

Laboratório do tema HTML e semântica, do módulo Conceber aplicações para a web na vertente frontend. Vais escrever as duas primeiras páginas do teu site, ligá-las uma à outra e verificá-las. Cada passo diz o que fazer, porquê e o que deves ver, e avanças ao teu ritmo. O que não acabares na aula, acabas na aula seguinte. Tudo o que precisas está aqui; o [guia do tema](02-html-e-semantica.md) tem a teoria completa, para quem quiser saber mais. A lista "Palavras que vais usar" é para consultar quando precisares, e não para ler de seguida antes de começar.

## O que vais construir

Vais transformar o plano do teu site em páginas de verdade, escritas em HTML. No fim, tens uma pasta com o nome do teu site, com duas páginas e uma pasta de imagens. As duas páginas têm o mesmo cabeçalho, a mesma navegação e o mesmo rodapé, e cada uma tem o seu conteúdo principal. Estão ligadas nos dois sentidos, e a segunda tem uma imagem com o texto alternativo certo.

Pelo caminho, ficas a saber escrever o esqueleto de uma página de memória e escolher cada elemento pelo que o conteúdo é. Ficas também a saber verificar uma página, e a reconhecer os erros mais comuns pelo que eles fazem.

O tema é o do teu site. Os exemplos deste laboratório usam o site de um clube de xadrez da escola, inventado, só para mostrar a forma. Não copies os textos do exemplo: escreve os teus. No fim, a pasta do exemplo fica assim:

```text
clube-de-xadrez/
├── index.html
├── torneios.html
└── imagens/
    └── imagem-provisoria.svg
```

| Fase | O que muda | O que funciona no fim |
| --- | --- | --- |
| 1 | O ficheiro `index.html`, com o esqueleto | A página abre em branco, com o título no separador do browser |
| 2 | O cabeçalho e a navegação, no `index.html` | O nome do site e o menu com duas ligações |
| 3 | O conteúdo principal, no `index.html` | O título da página, as secções e uma lista |
| 4 | O rodapé, no `index.html` | A primeira página completa, com as três zonas |
| 5 | O ficheiro `torneios.html` e a imagem | A segunda página, com a imagem e a ligação de volta |
| 6 | Nada: experimentas as ligações | Vais de uma página à outra e voltas |
| 7 | Nada: verificas as duas páginas | A tabela de verificação preenchida, com três justificações |
| 8 | Erros provocados de propósito, um de cada vez, e desfeitos | Reconheces cada erro pelo que ele faz |
| 9 | Uma tabela de dados, se o teu site tiver dados em linhas e colunas | A tabela, com legenda e cabeçalhos |

## Palavras que vais usar

Consulta esta lista quando um passo usar uma palavra que não conheces.

- HTML: a linguagem que diz ao browser o que cada pedaço de conteúdo de uma página é. Para saber mais, vê a secção "O que é o HTML" do [guia](02-html-e-semantica.md).
- Etiqueta: uma palavra entre `<` e `>`, como `<h1>`. A etiqueta de fecho leva uma barra antes do nome, como `</h1>`.
- Elemento: a etiqueta de abertura, o conteúdo e a etiqueta de fecho, juntos. É o que representa uma coisa na página.
- Atributo: uma informação extra sobre um elemento, escrita na etiqueta de abertura com a forma `nome="valor"`, como `href="torneios.html"`.
- Elemento vazio: um elemento sem conteúdo e sem etiqueta de fecho, como `img` e `meta`.
- Comentário: um texto entre `<!--` e `-->`, para quem lê o código. O browser não o mostra.
- Esqueleto: a estrutura com que todas as páginas começam, do `<!doctype html>` ao `body`. Para saber mais, vê a secção "O esqueleto de uma página" do [guia](02-html-e-semantica.md).
- Leitor de ecrã: um programa que lê a página em voz alta a pessoas cegas ou com pouca visão.
- Cabeçalho, `header`: a zona de introdução do topo da página, com o nome do site e o menu. Repete-se em todas as páginas.
- Navegação, `nav`: o bloco de ligações que leva às partes principais do site, o menu.
- Conteúdo principal, `main`: o que é próprio de cada página e não se repete nas outras. Há um só por página.
- Secção, `section`: uma parte do conteúdo com o seu próprio título.
- Rodapé, `footer`: a zona de informação final, no fundo da página. Também se repete em todas as páginas.
- Título, de `h1` a `h6`: os seis níveis de título, do mais importante para o menos importante. O `h1` é o assunto da página. Para saber mais, vê a secção "Títulos: de h1 a h6" do [guia](02-html-e-semantica.md).
- Índice da página: a lista dos títulos de uma página, com a indentação a mostrar os níveis.
- Lista não ordenada, `ul`, e lista ordenada, `ol`: listas em que a ordem dos itens não importa, ou importa. Cada item é um `li`.
- Ligação, `a`: o elemento que leva a outro sítio. O destino fica no atributo `href`.
- Caminho relativo: o caminho de um ficheiro a partir do ficheiro onde estás, como `torneios.html` ou `imagens/imagem-provisoria.svg`. Para saber mais, vê a secção "Caminhos relativos" do [guia](02-html-e-semantica.md).
- Texto alternativo: o valor do atributo `alt` de uma imagem, que ocupa o lugar dela quando ela não pode ser vista. Para saber mais, vê a secção "O texto alternativo" do [guia](02-html-e-semantica.md).
- `figure` e `figcaption`: uma imagem com a sua legenda, e a legenda.
- Indentação: os espaços no início das linhas, que mostram quem está dentro de quem. O browser ignora-os.
- DOM: a árvore que o browser constrói em memória a partir do teu ficheiro, e a partir da qual desenha a página.
- Ferramentas do programador: o painel do browser que mostra a página por dentro. O separador Elements mostra o DOM, e o separador Console mostra as mensagens de erro.
- Árvore de acessibilidade: uma segunda árvore, construída a partir do DOM, que os leitores de ecrã recebem. Cada coisa aparece nela com um papel, o que ela é, e um nome, o texto que a identifica.
- Foco: a moldura que mostra em que ligação estás quando percorres a página com o teclado.
- Tabela de dados: uma tabela em que cada valor responde a uma pergunta que junta uma linha e uma coluna. Para saber mais, vê a secção "Tabelas de dados" do [guia](02-html-e-semantica.md).

## O que precisas

- Um computador com o VS Code, o editor de código que usamos na escola. Mostra cada parte do HTML com uma cor diferente, o que ajuda a encontrar erros, e guarda os ficheiros no formato certo. Para confirmar que o tens, abre-o: deve aparecer a janela do editor, com uma coluna de ícones do lado esquerdo.
- O Chrome ou o Edge, para abrir as páginas. Os passos são iguais nos dois. No Firefox as ideias são as mesmas, mas alguns nomes mudam. Para confirmar, abre o browser: deve aparecer uma janela com a barra de endereço no topo.
- O plano do teu site, feito no tema 01: o mapa com pelo menos duas páginas e as ligações entre elas. Os wireframes ajudam, mas não são obrigatórios para começar. Se ainda não tens o plano, faz primeiro a secção "Se ainda não tens o plano do teu site", mais abaixo.
- Uma imagem para a segunda página, sobre o tema do teu site. Se ainda não tens nenhuma, usas a [imagem provisória](../laboratorios/frontend/primeiras-paginas/README.md), que está no repositório da disciplina.
- Um caderno, ou um ficheiro de texto, para o índice dos títulos, a tabela de verificação e as notas dos erros.

Vais precisar destes atalhos de teclado:

| O que fazer | Windows | Mac |
| --- | --- | --- |
| Guardar o ficheiro no VS Code | Ctrl+S | Cmd+S |
| Desfazer a última alteração no VS Code | Ctrl+Z | Cmd+Z |
| Indentar o ficheiro inteiro no VS Code | Shift+Alt+F | Shift+Option+F |
| Abrir um ficheiro do computador no browser | Ctrl+O | Cmd+O |
| Recarregar a página no browser | F5 | Cmd+R |
| Abrir as ferramentas do programador | F12 ou Ctrl+Shift+I | Cmd+Option+I |
| Andar para a ligação seguinte, e para a anterior | Tab e Shift+Tab | Tab e Shift+Tab |

O ciclo de trabalho deste laboratório é sempre o mesmo. Escreves no VS Code e guardas. Depois passas para o browser e recarregas a página.

O texto das tuas páginas pode ser inventado, e deve ser curto. Duas ou três frases por secção chegam, porque o que se treina aqui é a estrutura, e não a escrita. Nunca ponhas nas páginas dados pessoais verdadeiros, teus ou de outras pessoas: moradas, números de telefone, fotografias de colegas.

## Se alguma coisa falhar

1. Guardaste o ficheiro? No VS Code, um ficheiro por guardar tem uma bolinha no separador, no lugar da cruz de fechar. Guarda com Ctrl+S, ou Cmd+S no Mac.
2. Recarregaste a página no browser? O browser não vê as alterações sozinho. Carrega em F5, ou Cmd+R no Mac.
3. O browser tem aberta a página que estás a editar? Lê o endereço na barra do browser e compara-o com o nome e a pasta do ficheiro no VS Code.
4. O nome do ficheiro acaba em `.html`? No canto inferior direito do VS Code deve aparecer a palavra HTML.

Se o problema for outro, procura-o em [problemas frequentes](#problemas-frequentes).

## Se ainda não tens o plano do teu site

O laboratório parte do mapa do teu site. Se o tema 01 ainda não foi dado, ou se não tens o teu plano, faz esta versão curta. Chega para começar, e o plano completo fica para quando deres o tema 01.

1. Escolhe o tema do teu site, do menu de temas que o professor te dá, e dá um nome provisório ao site.
2. No caderno, desenha duas caixas. Uma é a página inicial. A outra é uma segunda página do teu site, como a página dos horários, dos jogadores ou das receitas.
3. Dentro de cada caixa, escreve numa frase o que essa página mostra.
4. Desenha uma seta da página inicial para a segunda página, e outra da segunda para a página inicial. Cada seta é uma ligação.

O que deves ver: no caderno, um mapa com duas caixas e duas setas, uma em cada sentido. É este o plano de que as fases seguintes partem. A secção "O plano do teu site" do [guia do tema 01](01-web-e-planeamento.md) explica o plano completo.

## Preparar o projeto

O teu site vive numa pasta. Os nomes das pastas e dos ficheiros de um site seguem três regras: minúsculas, sem espaços e sem acentos, com hífenes entre as palavras. A razão é esta. No teu computador, `Torneios.html` e `torneios.html` são o mesmo ficheiro. Num servidor, quando publicares o site, são dois ficheiros diferentes. Os espaços e os acentos causam problemas parecidos.

1. Escolhe o nome da pasta, a partir do tema do teu site, com as três regras. Por exemplo: `clube-de-xadrez`, `receitas-da-avo` ou `guia-de-sintra`. Um nome como `O Meu Site` ou `receitas_avó` vai dar problemas mais tarde.

2. Cria a pasta onde o professor indicar. Se já criaste a pasta do teu site no tema 01, com as fotografias do plano, usa essa. Para criar pastas, abre o programa que mostra as pastas do computador. No Windows, é o Explorador de Ficheiros, que se abre com as teclas Windows+E. No Mac, é o Finder, o ícone com uma cara sorridente na barra de baixo do ecrã. Vai até ao sítio onde a pasta deve ficar.

   No Windows, carrega com o botão direito do rato num sítio vazio, escolhe Novo e depois Pasta, e escreve o nome. No Mac, carrega com o botão direito num sítio vazio, escolhe Nova pasta e escreve o nome. No trackpad de um Mac, o botão direito é um clique com dois dedos, ou um clique com a tecla Ctrl carregada.

3. Entra na pasta do teu site, com um duplo clique nela. Lá dentro, cria da mesma maneira uma pasta chamada `imagens`. É lá que vão ficar as imagens do site.

4. Abre a pasta no VS Code. No menu File, escolhe Open Folder... e depois a pasta do teu site. Os nomes foram confirmados no VS Code 1.142, a 16 de outubro de 2026. Com o VS Code em português, os nomes são Arquivo e Abrir Pasta. É o português do Brasil, porque é o único pacote de português do VS Code. O VS Code pode perguntar se confias nos autores dos ficheiros da pasta: "Do you trust the authors of the files in this folder?". Carrega no botão "Yes, I trust the authors", que quer dizer "sim, confio nos autores", porque a pasta é tua.

   O que deves ver: do lado esquerdo, o painel Explorer, em português Explorador. Mostra o nome da pasta do teu site em maiúsculas e a pasta `imagens` lá dentro, vazia. As maiúsculas são só a forma como o VS Code mostra o nome da pasta aberta: o nome verdadeiro continua em minúsculas.

## Fase 1: O esqueleto da primeira página

Todas as páginas começam com a mesma estrutura, a que se chama o esqueleto. Cada linha do esqueleto está lá por uma razão, e quase nenhuma aparece na janela do browser. Nesta fase, escreves o esqueleto da página inicial, à mão, e confirmas que o browser o lê. Para saber mais, lê a secção "O esqueleto de uma página" do [guia](02-html-e-semantica.md).

1. Cria o ficheiro da página inicial. Antes, carrega numa zona vazia do painel Explorer, para o ficheiro novo ficar na pasta do site, e não dentro da pasta `imagens`. Depois, passa o rato por cima do nome da pasta e carrega no ícone de ficheiro novo, New File.... Escreve o nome `index.html` e carrega em Enter. O ficheiro abre-se, vazio, no meio da janela.

   O nome `index.html` não é uma escolha tua. Quando alguém escreve o endereço de um site sem dizer a página, a maior parte dos servidores procura um ficheiro com este nome e envia-o. Chamar `index.html` à tua página inicial garante que ela aparece quando o site for publicado.

2. Escreve o esqueleto à mão, linha a linha. Não copies e não uses atalhos do editor que o escrevam por ti. O atalho mais conhecido, escrever `!` e carregar em Enter, põe a página em inglês, com `lang="en"`. Escrever o esqueleto é também a melhor forma de o saberes de cor. Escreve no `index.html` este conteúdo. Põe o nome do teu site no lugar de "Clube de Xadrez", e o teu comentário no lugar do do exemplo:

   ```html
   <!doctype html>
   <!-- Página inicial do Clube de Xadrez: apresenta o clube e leva às outras páginas. -->
   <html lang="pt-PT">
     <head>
       <meta charset="utf-8">
       <meta name="viewport" content="width=device-width, initial-scale=1">
       <title>Início | Clube de Xadrez</title>
     </head>
     <body>
     </body>
   </html>
   ```

   Leitura guiada: lê de cima para baixo. A primeira linha, `<!doctype html>`, diz ao browser que a página segue as regras modernas do HTML. A segunda é um comentário, que diz para que serve o ficheiro. O elemento `html` contém todo o resto, e o atributo `lang="pt-PT"` diz que a página está em português de Portugal. Um leitor de ecrã usa-o para escolher a pronúncia. Lá dentro há dois filhos. O `head` guarda informação sobre a página, que não aparece na janela. O `body` vai guardar tudo o que aparece, e por agora está vazio. No `head`, o `meta charset` diz ao browser como ler as letras acentuadas, e por isso vem em primeiro lugar. O `meta name="viewport"` diz a um telemóvel que use a largura verdadeira do ecrã, em vez de encolher a página. O `title` é o título que aparece no separador do browser. Tem a forma `Página | Site`: primeiro o nome desta página, depois o do site. Quando há muitos separadores abertos, o browser corta os títulos compridos, e fica visível o princípio, que é o que muda de página para página. Repara que o `meta` não tem etiqueta de fecho: é um elemento vazio, porque toda a sua informação está nos atributos.

   Enquanto escreves, o VS Code acrescenta sozinho a etiqueta de fecho quando acabas de escrever uma etiqueta de abertura. Isso ajuda, mas confirma sempre que o fecho ficou no sítio certo.

3. Guarda o ficheiro, com Ctrl+S, ou Cmd+S no Mac.

4. Abre a página no browser. No painel Explorer do VS Code, carrega com o botão direito no `index.html`. Escolhe Reveal in File Explorer, que quer dizer "mostrar no Explorador de Ficheiros". No Mac, a opção chama-se Reveal in Finder, "mostrar no Finder". Abre-se a pasta do teu site: faz duplo clique no `index.html`. Se a página abrir noutro browser, abre o Chrome ou o Edge, carrega em Ctrl+O, ou Cmd+O no Mac, e escolhe o ficheiro. Deixa a página aberta num separador, porque vais recarregá-la muitas vezes.

   Antes de olhares, prevê: o que aparece na janela, e o que aparece no separador?

   O que deves ver: a janela em branco, porque o `body` está vazio. No separador aparece "Início | Clube de Xadrez", com o nome do teu site. Isto quer dizer que o browser leu o ficheiro. A barra de endereço começa por `file://`, porque o ficheiro está a ser lido do teu computador, e não de um servidor. Se o separador mostrar `index.html` em vez do teu título, o `title` tem um erro. Confirma que abre com `<title>` e fecha com `</title>`, dentro do `head`.

### Paragem 1

A página abre em branco, e o separador do browser mostra o título que escreveste.

Pensa antes de continuares: escreveste onze linhas, e nenhuma aparece na janela. Porquê? A resposta: o `body`, onde fica o que se vê, ainda está vazio. Tudo o resto é informação sobre a página, no `head`, e o comentário, que o browser não mostra. O `title` também está no `head`, e por isso aparece no separador, e não na janela.

## Fase 2: O cabeçalho e a navegação

Uma página divide-se em zonas, como as que desenhaste no wireframe. O HTML tem um elemento para cada zona, que diz o que ela é. Nesta fase escreves a primeira zona, o cabeçalho, com o nome do site e o menu. Para saber mais, lê a secção "Os elementos semânticos" do [guia](02-html-e-semantica.md).

O cabeçalho é o elemento `header`. Repete-se igual em todas as páginas, para quem muda de página encontrar o menu sempre no mesmo sítio. O menu é o elemento `nav`, o bloco de ligações que leva às partes principais do site. Lá dentro, as ligações ficam numa lista, porque são várias opções do mesmo tipo. Um leitor de ecrã anuncia quantas são antes de as ler.

Uma ligação é o elemento `a`. O texto entre `<a>` e `</a>` é o que aparece na página, e o atributo `href` diz o destino. Quando o destino está na mesma pasta, basta o nome do ficheiro: é um caminho relativo.

1. Olha para o teu mapa e escolhe já o nome do ficheiro da segunda página, com as três regras dos nomes. Por exemplo, `horario.html` ou `torneios.html`. Escreve-o no mapa, ao lado da caixa dessa página.

2. Em `index.html`, entre `<body>` e `</body>`, escreve o cabeçalho, com os nomes das tuas páginas nas ligações:

   ```html
   <header>
     <p>Clube de Xadrez</p>
     <nav>
       <ul>
         <li><a href="index.html">Início</a></li>
         <li><a href="torneios.html">Torneios</a></li>
       </ul>
     </nav>
   </header>
   ```

   Leitura guiada: o `header` tem dois filhos, o parágrafo com o nome do site e o `nav`. O nome do site está num `p`, e não num título `h1`. O `h1` vai ser o assunto desta página, na fase seguinte, e o assunto da página inicial não é o nome do site. Dentro do `nav` está uma lista `ul` com dois itens `li`, e cada item tem uma ligação. A primeira leva à própria página inicial. Não faz mal: o menu vai ser igual em todas as páginas, e nas outras é a forma de voltar ao princípio. A segunda leva a uma página que ainda não existe. Vais criá-la na fase 5.

3. Guarda e recarrega a página no browser.

   O que deves ver: o nome do site e, por baixo, uma lista com duas ligações. Estão sublinhadas, normalmente a azul, e cada uma tem uma bolinha à frente. A bolinha é da lista. No tema do CSS vais aprender a tirá-la.

### Paragem 2

A página mostra o nome do site e o menu com duas ligações.

Pensa antes de continuares: se carregares agora na segunda ligação do menu, o que acontece? A resposta: o browser mostra uma página de erro. No Chrome em português, diz "Não foi possível aceder ao seu ficheiro", com o código `ERR_FILE_NOT_FOUND`. O `href` aponta para um ficheiro que ainda não existe na pasta. É normal, e deixa de acontecer na fase 5, quando criares essa página.

## Fase 3: O conteúdo principal, com títulos, secções e uma lista

Depois do cabeçalho vem o conteúdo principal, o elemento `main`. É o que é próprio desta página e não se repete nas outras. Há um só `main` em cada página. Para saber mais, lê as secções "Títulos: de h1 a h6" e "Listas" do [guia](02-html-e-semantica.md).

Os títulos de uma página formam o seu índice, como os capítulos de um livro. O `h1` é o assunto da página inteira, e há um só. Cada `h2` é o título de uma parte da página, e um `h3` seria o de uma parte dentro de um `h2`. A regra que mais importa: a descer, não se saltam níveis. Depois de um `h1` vem um `h2`, e não um `h3`. O nível de um título escolhe-se pelo lugar que ele ocupa no índice, e nunca pelo tamanho da letra.

Cada parte do conteúdo com o seu próprio título é uma secção, o elemento `section`. Para saber se uma lista é ordenada ou não, faz o teste da troca: se trocares dois itens de lugar, a informação fica errada? Se fica, é uma lista ordenada, `ol`, e o browser numera os itens. Se não fica, é uma lista não ordenada, `ul`, e o browser põe uma bolinha à frente de cada um.

1. Por baixo do `</header>`, ainda dentro do `body`, abre o `main`. Lá dentro, escreve o `h1` com o assunto desta página. Para o encontrar, pergunta a ti próprio o que alguém encontra nesta página. No clube de xadrez podia ser "Aprende a jogar xadrez connosco".

2. Escreve um ou dois parágrafos curtos de apresentação, cada um num elemento `p`.

3. Escreve pelo menos duas secções, cada uma com o seu `h2` e o seu conteúdo. Segue as zonas do teu wireframe ou, se ainda não o tens, as frases do teu mapa. Pelo menos uma das secções tem de ter uma lista. Antes de a escreveres, faz o teste da troca, e escolhe `ul` ou `ol` pela resposta. No exemplo, o conteúdo principal fica assim:

   ```html
   <main>
     <h1>Aprende a jogar xadrez connosco</h1>
     <p>O clube reúne-se todas as semanas para jogar, aprender aberturas e preparar torneios.</p>

     <section>
       <h2>Quando nos encontramos</h2>
       <p>Às quartas-feiras à tarde, na sala 12.</p>
     </section>

     <section>
       <h2>O que precisas de trazer</h2>
       <ul>
         <li>Vontade de aprender.</li>
         <li>Um caderno para anotar as partidas.</li>
       </ul>
     </section>
   </main>
   ```

   Leitura guiada: o `main` começa pelo `h1`, o assunto da página. A seguir vem o parágrafo de apresentação, e depois as duas secções. Cada secção começa pelo seu `h2` e tem o conteúdo dessa parte. A lista do que trazer é um `ul`: trocar os dois itens de lugar não torna a informação errada. Repara na indentação. Cada elemento que está dentro de outro começa dois espaços mais à direita, e é isso que mostra, de relance, quem está dentro de quem.

4. Guarda e recarrega.

   O que deves ver: por baixo do menu, o título da página, em letra grande e a negrito, e o parágrafo. A seguir, os dois títulos das secções, um pouco mais pequenos, cada um com o seu conteúdo. A lista do que trazer tem uma bolinha à frente de cada item.

5. No caderno, escreve o índice dos títulos da página, com a indentação a mostrar os níveis. No exemplo, fica assim:

   ```text
   h1  Aprende a jogar xadrez connosco
       h2  Quando nos encontramos
       h2  O que precisas de trazer
   ```

### Paragem 3

O índice da tua página tem um só `h1`, e os `h2` vêm a seguir, sem saltos. Se tiveres um `h3`, está dentro de uma parte com `h2`.

Pensa antes de continuares: o clube quer acrescentar os passos para alguém se inscrever. Primeiro fala com o professor responsável, depois preenche a ficha de inscrição e por fim vem ao primeiro treino. É uma lista `ul` ou `ol`? A resposta: `ol`. Se trocares o primeiro passo com o último, a informação fica errada, porque ninguém vem ao primeiro treino antes de se inscrever.

## Fase 4: O rodapé e as três zonas da página

A última zona da página é o rodapé, o elemento `footer`. Tem a informação final: quem fez o site, a turma, o ano, ou um aviso. Como o cabeçalho, repete-se igual em todas as páginas. Com ele, o `body` fica com três filhos, pela ordem em que aparecem no wireframe: `header`, `main` e `footer`. Para saber mais, lê a secção "Elementos dentro de elementos" do [guia](02-html-e-semantica.md).

1. Por baixo do `</main>`, ainda dentro do `body`, escreve o rodapé, com um parágrafo de informação final:

   ```html
   <footer>
     <p>Site do Clube de Xadrez, feito na disciplina de Desenvolvimento de Aplicações. Conteúdo fictício.</p>
   </footer>
   ```

   Leitura guiada: o `footer` fica a seguir ao `main`, ao mesmo nível do `header`, e não dentro do `main`. O `main` é só o que é próprio desta página, e o rodapé repete-se em todas.

2. Guarda e recarrega. O que deves ver: no fundo da página, o parágrafo do rodapé.

3. Indenta o ficheiro inteiro com o comando do VS Code Format Document, que quer dizer "formatar o documento": Shift+Alt+F no Windows, Shift+Option+F no Mac. O VS Code muda só os espaços, as linhas em branco e as linhas muito compridas, e não mexe nas etiquetas nem no texto.

   O que deves ver: o `header`, o `main` e o `footer` à mesma distância da margem, dentro do `body`. Por omissão, o VS Code deixa o `head` e o `body` à mesma margem do `html` e acrescenta algumas linhas em branco. É só a forma como o VS Code arruma o ficheiro. A página fica igual, porque o browser ignora os espaços do início das linhas. Se uma etiqueta de fecho ficar desalinhada da sua etiqueta de abertura, há um erro de aninhamento perto dela.

### Paragem 4

A primeira página está completa. O `body` tem três filhos diretos, `header`, `main` e `footer`, por esta ordem. O ficheiro do exemplo, como deve estar agora, antes do comando de indentar:

```html
<!doctype html>
<!-- Página inicial do Clube de Xadrez: apresenta o clube e leva às outras páginas. -->
<html lang="pt-PT">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Início | Clube de Xadrez</title>
  </head>
  <body>
    <header>
      <p>Clube de Xadrez</p>
      <nav>
        <ul>
          <li><a href="index.html">Início</a></li>
          <li><a href="torneios.html">Torneios</a></li>
        </ul>
      </nav>
    </header>
    <main>
      <h1>Aprende a jogar xadrez connosco</h1>
      <p>O clube reúne-se todas as semanas para jogar, aprender aberturas e preparar torneios.</p>

      <section>
        <h2>Quando nos encontramos</h2>
        <p>Às quartas-feiras à tarde, na sala 12.</p>
      </section>

      <section>
        <h2>O que precisas de trazer</h2>
        <ul>
          <li>Vontade de aprender.</li>
          <li>Um caderno para anotar as partidas.</li>
        </ul>
      </section>
    </main>
    <footer>
      <p>Site do Clube de Xadrez, feito na disciplina de Desenvolvimento de Aplicações. Conteúdo fictício.</p>
    </footer>
  </body>
</html>
```

Pensa antes de continuares: um colega pôs o `header` e o `footer` dentro do `main`. Que pergunta lhe fazes para ele perceber o erro? A resposta: "o que muda de página para página?". O cabeçalho e o rodapé repetem-se em todas as páginas, e o que muda é o conteúdo principal. Por isso o `main` tem só o que é desta página.

## Fase 5: A segunda página, com uma imagem

A segunda página tem o mesmo esqueleto, o mesmo cabeçalho e o mesmo rodapé da primeira. Por isso não se começa do zero: copia-se a primeira e muda-se só o título do separador e o conteúdo principal. Nesta página entra também uma imagem.

Uma imagem é o elemento `img`, que é vazio, como o `meta`. O atributo `src` diz onde está o ficheiro da imagem, com um caminho relativo. A imagem vai estar na pasta `imagens`, e por isso o caminho é o nome da pasta, uma barra e o nome do ficheiro. Os atributos `width` e `height` dizem a largura e a altura, em píxeis, sem escrever a unidade.

O atributo `alt` é o texto alternativo: ocupa o lugar da imagem quando ela não pode ser vista. Um leitor de ecrã lê-o em voz alta, e o browser mostra-o se a imagem não carregar. Para o escrever, faz a pergunta do telefone. Se estivesses ao telefone a descrever esta página a alguém, o que dirias no sítio da imagem? Se a imagem só repete o texto que está ao lado, o `alt` fica vazio, `alt=""`, e o leitor de ecrã salta-a. O atributo nunca falta. Para saber mais, lê as secções "Imagens" e "O texto alternativo" do [guia](02-html-e-semantica.md).

1. Arranja a imagem e põe-na na pasta `imagens` do teu site. Pode ser uma fotografia ou um desenho teus. Pode também ser uma imagem de outra pessoa cuja licença permita o uso. Uma imagem encontrada numa pesquisa não é livre só por estar na Internet. Se a imagem não for tua, anota de onde veio e qual é a licença, porque mais tarde vais dizê-lo no README do teu site. O README é um ficheiro que fica na pasta do site e o apresenta a quem o abre; o modelo está em [readme-do-projeto](../projeto/modelos/readme-do-projeto.md). Dá-lhe um nome com as três regras dos nomes, como `tabuleiro.jpg`.

   Se for uma fotografia tirada com o telemóvel, reduz-lhe primeiro a largura para 600 a 800 píxeis. Usa um programa de edição de imagem, como o Paint no Windows ou a Pré-visualização no Mac. As tuas páginas ainda não têm CSS, e por isso a imagem aparece com as medidas que escreveres. Uma fotografia de 4000 píxeis aparecia enorme, e demorava a carregar.

   Se ainda não tens nenhuma imagem, usa a imagem provisória. Na pasta do repositório da disciplina, o ficheiro está em `laboratorios/frontend/primeiras-paginas/imagem-provisoria.svg`. Copia-o para a pasta `imagens` do teu site, sem lhe mudar o nome, e troca-o mais tarde. Se não tens o repositório no computador, pede a imagem ao professor, ou descarrega-a do repositório da turma no GitHub, onde está na mesma pasta.

2. Cria a segunda página a partir da primeira. No painel Explorer do VS Code, carrega com o botão direito do rato no `index.html` e escolhe Copy, que quer dizer copiar. Depois, carrega com o botão direito numa zona vazia do painel e escolhe Paste, colar. Aparece uma cópia, com um nome como `index copy.html`. Carrega com o botão direito nela, escolhe Rename..., mudar o nome, e dá-lhe o nome que escreveste no mapa, como `torneios.html`. Os nomes foram confirmados no VS Code 1.142, a 16 de outubro de 2026. O nome tem de ser igual, letra a letra, ao do `href` do menu.

3. Na cópia, muda o comentário do topo para dizer o que esta página é. Muda também o `title`, para o nome desta página e o nome do site, como `Torneios | Clube de Xadrez`.

4. Apaga todo o conteúdo do `main` desta cópia, deixando o `<main>` e o `</main>`. O `header` e o `footer` não se mexem: ficam iguais aos da página inicial. Dentro do `main`, escreve o conteúdo desta página: o `h1` com o assunto dela, um parágrafo e pelo menos uma secção com `h2`.

5. Põe a imagem numa das secções. No exemplo, com a imagem provisória, o conteúdo principal fica assim:

   ```html
   <main>
     <h1>Torneios do clube</h1>
     <p>Todos os anos o clube organiza torneios abertos a toda a escola.</p>

     <section>
       <h2>O torneio do ano passado</h2>
       <p>A fotografia da final do torneio do ano passado vai entrar aqui.</p>
       <!-- Imagem provisória: troca o ficheiro, as medidas e o alt quando tiveres a fotografia. -->
       <img src="imagens/imagem-provisoria.svg" alt="Imagem provisória" width="400" height="300">
     </section>
   </main>
   ```

   Leitura guiada: a página tem o seu `h1`, diferente do da página inicial, e uma secção com `h2`. A imagem está dentro da secção de que faz parte. O `src` desce da pasta da página para a pasta `imagens`. A imagem provisória é um retângulo cinzento com o desenho de uma montanha e as palavras "Imagem provisória", e mede 400 por 300 píxeis. O `alt` diz o que ela mostra. O comentário lembra o que trocar mais tarde.

   Com a tua própria imagem, usa as medidas verdadeiras dela, depois de reduzida. No Windows, vês as medidas nas propriedades do ficheiro, no separador Detalhes. No Mac, na janela Obter informações.

   A tua imagem pode ter uma legenda que acrescente alguma coisa, como de onde vem ou quem a fez. Nesse caso, junta a imagem e a legenda num `figure`. A legenda vai num `figcaption`, que é o primeiro ou o último filho do `figure`. O `alt` e a legenda não se repetem. O `alt` diz o que a imagem mostra, e a legenda acrescenta o que toda a gente deve saber. Por exemplo, com uma fotografia `tabuleiro.jpg` na pasta `imagens`:

   ```html
   <figure>
     <img src="imagens/tabuleiro.jpg"
          alt="Tabuleiro de xadrez a meio de uma partida, com as peças brancas em ataque."
          width="600" height="400">
     <figcaption>Final do torneio da escola do ano passado. Fotografia do clube.</figcaption>
   </figure>
   ```

   Se a imagem não tiver uma legenda que acrescente alguma coisa, basta o `img`, como no exemplo com a imagem provisória.

6. No fim do `main`, depois da última secção, acrescenta um parágrafo com uma ligação de volta à página inicial. O texto da ligação diz o destino:

   ```html
   <p><a href="index.html">Voltar à página inicial</a></p>
   ```

   Esta ligação não vai num `nav`, porque não é a navegação principal do site: é uma ligação solta no fim do conteúdo.

7. Guarda e abre esta página no browser, com Ctrl+O, ou Cmd+O no Mac.

   O que deves ver: o separador mostra o título novo, e a imagem aparece por baixo do parágrafo da secção. O cabeçalho e o rodapé são iguais aos da página inicial.

### Paragem 5

A segunda página abre, com a imagem. O ficheiro `torneios.html` do exemplo, como deve estar agora:

```html
<!doctype html>
<!-- Página dos torneios do Clube de Xadrez: o torneio do ano passado e os próximos. -->
<html lang="pt-PT">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Torneios | Clube de Xadrez</title>
  </head>
  <body>
    <header>
      <p>Clube de Xadrez</p>
      <nav>
        <ul>
          <li><a href="index.html">Início</a></li>
          <li><a href="torneios.html">Torneios</a></li>
        </ul>
      </nav>
    </header>
    <main>
      <h1>Torneios do clube</h1>
      <p>Todos os anos o clube organiza torneios abertos a toda a escola.</p>

      <section>
        <h2>O torneio do ano passado</h2>
        <p>A fotografia da final do torneio do ano passado vai entrar aqui.</p>
        <!-- Imagem provisória: troca o ficheiro, as medidas e o alt quando tiveres a fotografia. -->
        <img src="imagens/imagem-provisoria.svg" alt="Imagem provisória" width="400" height="300">
      </section>

      <p><a href="index.html">Voltar à página inicial</a></p>
    </main>
    <footer>
      <p>Site do Clube de Xadrez, feito na disciplina de Desenvolvimento de Aplicações. Conteúdo fictício.</p>
    </footer>
  </body>
</html>
```

Pensa antes de continuares: quando trocares a imagem provisória por uma fotografia do torneio, o que tens de mudar no `img`? A resposta: mudas três coisas. O `src` passa a ter o nome do ficheiro novo. O `width` e o `height` passam a ter as medidas da fotografia. E o `alt` passa a descrever o que a fotografia mostra. Se a fotografia tiver uma legenda que acrescente alguma coisa, passa também a estar num `figure`, com o `figcaption`.

## Fase 6: As duas páginas ligadas nos dois sentidos

Uma ligação só funciona se o `href` for igual, letra a letra, ao nome do ficheiro de destino. Agora que a segunda página existe, já podes experimentar as ligações nos dois sentidos: de cada página tem de se chegar à outra e voltar.

1. Volta à página inicial no browser e carrega na segunda ligação do menu. O que deves ver: a segunda página. Na fase 2, a mesma ligação dava erro, porque o ficheiro ainda não existia.

2. Na segunda página, carrega em "Início", no menu, e depois volta e carrega na ligação de volta, no fim do conteúdo. O que deves ver: as duas levam à página inicial.

3. Se alguma ligação der a página de erro "Não foi possível aceder ao seu ficheiro", lê o endereço na barra do browser. Compara-o letra a letra com o nome do ficheiro no painel Explorer. As diferenças mais comuns são uma letra trocada, a mais ou a menos, um acento ou a extensão esquecida. Corrige o `href`, guarda e recarrega.

   Uma diferença só de maiúsculas e minúsculas, como `Torneios.html` no `href` e `torneios.html` no disco, não dá erro no teu computador. O Windows e o macOS tratam os dois nomes como o mesmo ficheiro. Só falha quando o site for publicado num servidor. Por isso, corrige-a na mesma.

### Paragem 6

Consegues ir de uma página à outra e voltar, pelo menu e pela ligação de volta.

Pensa antes de continuares: porque é que um `href` com `Torneios.html`, para o ficheiro `torneios.html`, se corrige, se no teu computador funciona? A resposta: os servidores onde os sites se publicam usam quase sempre Linux, que distingue maiúsculas de minúsculas. Lá, `Torneios.html` e `torneios.html` são dois ficheiros diferentes, e a ligação dava erro no site publicado, com uma página a dizer que não a encontrou.

## Fase 7: Verificar as duas páginas

Uma página só está pronta depois de verificada. Verificar quer dizer seguir as ligações e ler a página pela ordem do HTML. Quer dizer também percorrê-la só com o teclado e ver a estrutura nas ferramentas do programador. Há pessoas que não veem o ecrã e usam um leitor de ecrã. Há também quem não use o rato e navegue sempre com o teclado. As verificações confirmam que a página serve a toda a gente. Para saber mais, lê a secção "Verificar uma página" do [guia](02-html-e-semantica.md).

Copia esta tabela para o caderno, ou para um ficheiro, e preenche-a à medida que fazes cada verificação:

| Verificação | O que fiz | Passou? | Se não passou, o que corrigi |
| --- | --- | --- | --- |
| Ligações | Carreguei em todas as ligações das duas páginas | | |
| Ordem de leitura | Li as duas páginas de cima a baixo e escrevi o índice dos títulos | | |
| Teclado | Percorri as duas páginas só com Tab, Shift+Tab e Enter | | |
| Árvore do DOM | Comparei a árvore do separador Elements com o meu ficheiro | | |
| Árvore de acessibilidade | Encontrei as zonas da página e o nome da imagem | | |

1. Ligações. Carrega em cada ligação das duas páginas, uma de cada vez, e volta atrás depois de cada uma. O que deves ver: cada ligação leva ao sítio certo.

2. Ordem de leitura. As tuas páginas não têm CSS. Por isso, o que vês é a página com o aspeto que o browser lhe dá por omissão. Aparece pela ordem em que o HTML está escrito. É também por essa ordem que um leitor de ecrã a lê. Lê cada página de cima a baixo como se fosses outra pessoa, e pergunta: a ordem faz sentido? Os títulos dizem de que trata cada parte? O assunto da página aparece logo a seguir ao menu? Escreve o índice dos títulos da segunda página, como fizeste na fase 3.

3. Teclado. Carrega uma vez no nome do site, no topo da página, fora das ligações. A partir daí, não toques no rato. O Tab começa a seguir ao sítio onde carregaste, e por isso carregas no topo. Carrega em Tab várias vezes. Uma moldura, a que se chama foco, salta de ligação em ligação. Com Shift+Tab, o foco anda para trás, e com Enter segues a ligação onde ele está.

   O que deves ver: o foco passa por todas as ligações, pela ordem em que estão escritas no ficheiro. No exemplo, passa na página inicial por "Início" e por "Torneios". Na segunda página, passa por "Início", "Torneios" e "Voltar à página inicial". Consegues ir à segunda página e voltar só com o teclado.

4. Árvore do DOM. Quando abre um ficheiro, o browser constrói em memória uma árvore com os elementos da página. Chama-se DOM, e é a partir dela que o browser desenha a página. Abre as ferramentas do programador com F12, ou Cmd+Option+I no Mac. Escolhe o separador Elements, que em português pode aparecer como Elementos. Abre os pequenos triângulos do `body`, do `header`, do `main` e do `footer`, e compara a árvore com o teu ficheiro no VS Code.

   O que deves ver: os mesmos elementos, pela mesma ordem. Isto quer dizer que o browser não teve de corrigir nenhum erro teu. Se a árvore tiver um parágrafo vazio que não escreveste, ou um elemento noutro sítio, o browser corrigiu um erro. Procura-o no ficheiro, perto desse sítio.

5. Árvore de acessibilidade. A partir do DOM, o browser constrói uma segunda árvore, mais simples, que é a que os leitores de ecrã recebem. Nela, cada coisa tem um papel, que diz o que ela é, e um nome, o texto que a identifica. Ainda no separador Elements, carrega no elemento `main` da árvore para o selecionar. No painel ao lado, onde está o separador Styles, procura o separador Accessibility, em português Acessibilidade. Se não o vires, pode estar escondido atrás de um botão com duas setas, `»`.

   O que deves ver: o papel do elemento selecionado, que é *main*. Seleciona agora o `nav`, o `header` e o `footer`, um de cada vez. Os papéis são *navigation*, *banner* e *contentinfo*, os nomes em inglês do menu, do cabeçalho e do rodapé. Por fim, seleciona o `img` da segunda página: o nome que aparece é o texto que escreveste no `alt`.

6. Escreve, no fim da tabela, a justificação de três elementos que escolheste nas tuas páginas, numa ou duas frases cada. Cada justificação diz o que o conteúdo é, e não o aspeto que tem. Por exemplo: "A lista do que trazer é um `ul`, porque trocar a ordem dos itens não muda nada". Outro exemplo: "O nome do clube está num `p`, e não num `h1`, porque o assunto da página inicial é aprender xadrez no clube".

7. Se já preencheste no tema 01 o [modelo do brief](../projeto/modelos/brief-e-wireframe.md) do teu site, completa agora os dois campos que ficaram para este tema. Em "Relação entre zonas desenhadas e elementos HTML", escreve o elemento que escolheste para cada zona do teu wireframe. Em "Percurso por teclado e foco", escreve a ordem pela qual o Tab passou pelas ligações no ponto 3. Se ainda não tens o brief, escreve as duas coisas no caderno, para as passares para o brief quando o fizeres.

### Paragem 7

As cinco linhas da tabela dizem que passou, ou dizem o que corrigiste até passar. No fim da tabela estão as três justificações.

Pensa antes de continuares: porque é que o foco do Tab segue a ordem em que escreveste as ligações no ficheiro? A resposta: o foco segue a ordem do HTML, que é também a ordem em que um leitor de ecrã lê a página. Nos próximos temas, o CSS vai mudar o aspeto e a posição das coisas, mas esta ordem fica. É por isso que a ordem do HTML tem de fazer sentido sozinha.

## Fase 8: Provocar erros e corrigi-los

O HTML não dá mensagens de erro. Quando o browser encontra uma coisa mal escrita, tenta adivinhar o que querias dizer. Corrige a árvore à sua maneira e desenha a página na mesma. Por isso, um erro pode passar despercebido. Nesta fase vais estragar as tuas páginas de propósito, um erro de cada vez, para aprenderes a reconhecer cada um pelo que ele faz. Para saber mais, lê a secção "Como o browser lida com os erros" do [guia](02-html-e-semantica.md).

Depois de cada erro, escreve no caderno o que viste, numa linha, e desfaz a alteração antes de passares ao seguinte. No VS Code, Ctrl+Z, ou Cmd+Z no Mac, desfaz a última alteração. Guarda e recarrega depois de desfazeres.

1. A imagem que falta. No painel Explorer, muda o nome da tua imagem, acrescentando uma letra no fim do nome, antes da extensão. Recarrega a segunda página.

   O que deves ver: no sítio da imagem, um pequeno ícone de imagem partida, com o texto do `alt` ao lado. O browser foi procurar o ficheiro com o nome do `src`, e esse ficheiro já não existe. Abre agora as ferramentas do programador no separador Console, em português Consola. Recarrega a página com a Console aberta. Deve aparecer uma mensagem a vermelho a dizer que não foi possível carregar um ficheiro. Repõe o nome original da imagem e recarrega.

2. O caminho sem a pasta. No `src` da imagem, apaga `imagens/`, deixando só o nome do ficheiro. Guarda e recarrega.

   O que deves ver: a imagem desaparece outra vez, com o ícone e o `alt`. Agora o browser procura o ficheiro na pasta da página, e não na pasta `imagens`. Repõe o caminho.

3. O título que salta um nível. Numa das tuas secções, muda o `h2` para `h4`, na abertura e no fecho. Guarda e recarrega.

   O que deves ver: só muda o aspeto. A letra do título fica mais pequena, e o espaço à volta dele muda um pouco. É isso que torna este erro perigoso: parece só uma questão de aspeto. Escreve o índice dos títulos da página e vês o salto de `h1` para `h4`, com um nível vazio pelo meio. Repõe o `h2`.

4. A lista dentro de um parágrafo. Escolhe uma das tuas listas e põe-na dentro de um parágrafo: escreve `<p>` antes do `<ul>` e `</p>` depois do `</ul>`. Guarda e recarrega.

   O que deves ver: na página quase não se nota nada. Abre agora o separador Elements e procura esse sítio da árvore. O parágrafo que abriste fecha logo antes da lista e fica vazio. Depois da lista aparece outro parágrafo, também vazio, que não escreveste. Um parágrafo não pode conter uma lista, e por isso o browser fechou-o antes dela. O `</p>` que sobrou depois da lista virou um parágrafo novo. É a diferença entre o teu ficheiro e o DOM. Repõe a lista como estava.

5. O negrito que ficou aberto. Vais usar o parágrafo de apresentação da página inicial, o que está logo a seguir ao `h1`. Marca uma palavra dele com `<strong>`, que é o elemento do texto importante. Não escrevas o `</strong>`. Guarda e recarrega.

   Antes de olhares, prevê: até onde vai o negrito?

   O que deves ver: o negrito começa na palavra marcada e vai até ao fim da página, com o rodapé incluído. Abre o separador Elements: vês três `strong`, e só escreveste um. O browser fechou o `strong` no fim do parágrafo e abriu outro em cada zona seguinte. Abriu um à volta do resto do `main` e mais um à volta do rodapé. Escreve agora o `</strong>` no sítio certo, guarda e recarrega.

6. Depois de desfazeres os cinco erros, faz outra vez, rapidamente, a verificação das ligações e da árvore do DOM da fase 7.

### Paragem 8

Tens no caderno cinco linhas, uma por erro, com o que viste. As páginas voltaram a passar as verificações da fase 7.

Pensa antes de continuares: qual dos cinco erros quase não mudou nada na página, e onde o descobriste? A resposta: a lista dentro do parágrafo. Na página quase não se nota nada, e o erro só aparece no separador Elements, nos parágrafos vazios. O título que salta um nível também parece só uma mudança de aspeto, e descobre-se no índice dos títulos.

## Fase 9: Uma tabela de dados, se o teu site a tiver

Uma tabela serve para dados que se leem em linhas e colunas, como um horário, uma tabela de preços ou uma classificação. O teste é este: cada valor responde a uma pergunta que junta uma linha e uma coluna? Num horário, "a que horas fecha à quarta-feira?" responde-se cruzando a linha da quarta-feira com a coluna "Fecha". Uma tabela nunca serve para pôr coisas lado a lado: isso é trabalho do CSS. Para saber mais, lê a secção "Tabelas de dados" do [guia](02-html-e-semantica.md).

Uma tabela usa vários elementos, uns dentro dos outros. O `table` é a tabela inteira, e o `caption` é a legenda, o nome da tabela, logo a seguir à abertura do `table`. O `thead` agrupa a linha de cabeçalhos do topo, e o `tbody` as linhas de dados. Cada linha é um `tr`. Uma célula de cabeçalho é um `th`, e uma célula de dados é um `td`. O atributo `scope` diz a que se aplica cada cabeçalho: `scope="col"` à coluna, e `scope="row"` à linha. É por ele que um leitor de ecrã diz, em cada célula, a que linha e a que coluna ela pertence.

1. Pergunta a ti próprio se o teu site tem informação que se lê em linhas e colunas. Aplica o teste: cada valor responde a uma pergunta que junta uma linha e uma coluna?

2. Se tiver, acrescenta essa tabela a uma das tuas páginas, dentro da secção onde faz sentido. Começa pelo `caption`, depois o `thead`, com os cabeçalhos das colunas, e depois o `tbody`, com uma linha por registo. Se a primeira célula de cada linha disser de que é a linha, é um `th` com `scope="row"`. No exemplo, em `torneios.html`, acrescenta-se esta secção entre a secção do torneio do ano passado e a ligação de volta:

   ```html
   <section>
     <h2>Próximos torneios</h2>
     <table>
       <caption>Próximos torneios do clube (datas fictícias)</caption>
       <thead>
         <tr>
           <th scope="col">Torneio</th>
           <th scope="col">Data</th>
           <th scope="col">Ritmo de jogo</th>
         </tr>
       </thead>
       <tbody>
         <tr>
           <th scope="row">Torneio de outono</th>
           <td>14 de novembro</td>
           <td>Partidas de 15 minutos</td>
         </tr>
         <tr>
           <th scope="row">Torneio de primavera</th>
           <td>20 de março</td>
           <td>Partidas de 10 minutos</td>
         </tr>
       </tbody>
     </table>
   </section>
   ```

   Leitura guiada: lê a tabela linha a linha. A linha do `thead` só tem cabeçalhos, que dizem o que é cada coluna. Em cada linha do `tbody`, a primeira célula é o nome do torneio, num `th` de linha, e as outras duas são dados, em `td`. A legenda diz de que trata a tabela, e "(datas fictícias)" avisa que as datas foram inventadas.

3. Se o teu site não tiver dados em linhas e colunas, não inventes uma tabela só para ter uma. Escreve no caderno, numa frase, porque é que o teu site não precisa de tabela. A tabela treina-se no exercício 7 da [ficha](02-html-e-semantica-exercicios.md).

4. Guarda e recarrega.

   O que deves ver: a legenda centrada por cima da tabela, e os valores arrumados em colunas. Sem CSS, o browser não desenha linhas entre as células. Os cabeçalhos aparecem a negrito e centrados, e os dados em letra normal. Na árvore de acessibilidade, seleciona o `table`: o nome dele é o texto da legenda.

### Paragem 9

A tabela tem legenda, cabeçalhos com `scope`, e só mostra dados. Ou tens no caderno a frase que explica porque é que o teu site não precisa de tabela. O ficheiro `torneios.html` do exemplo, completo:

```html
<!doctype html>
<!-- Página dos torneios do Clube de Xadrez: o torneio do ano passado e os próximos. -->
<html lang="pt-PT">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Torneios | Clube de Xadrez</title>
  </head>
  <body>
    <header>
      <p>Clube de Xadrez</p>
      <nav>
        <ul>
          <li><a href="index.html">Início</a></li>
          <li><a href="torneios.html">Torneios</a></li>
        </ul>
      </nav>
    </header>
    <main>
      <h1>Torneios do clube</h1>
      <p>Todos os anos o clube organiza torneios abertos a toda a escola.</p>

      <section>
        <h2>O torneio do ano passado</h2>
        <p>A fotografia da final do torneio do ano passado vai entrar aqui.</p>
        <!-- Imagem provisória: troca o ficheiro, as medidas e o alt quando tiveres a fotografia. -->
        <img src="imagens/imagem-provisoria.svg" alt="Imagem provisória" width="400" height="300">
      </section>

      <section>
        <h2>Próximos torneios</h2>
        <table>
          <caption>Próximos torneios do clube (datas fictícias)</caption>
          <thead>
            <tr>
              <th scope="col">Torneio</th>
              <th scope="col">Data</th>
              <th scope="col">Ritmo de jogo</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th scope="row">Torneio de outono</th>
              <td>14 de novembro</td>
              <td>Partidas de 15 minutos</td>
            </tr>
            <tr>
              <th scope="row">Torneio de primavera</th>
              <td>20 de março</td>
              <td>Partidas de 10 minutos</td>
            </tr>
          </tbody>
        </table>
      </section>

      <p><a href="index.html">Voltar à página inicial</a></p>
    </main>
    <footer>
      <p>Site do Clube de Xadrez, feito na disciplina de Desenvolvimento de Aplicações. Conteúdo fictício.</p>
    </footer>
  </body>
</html>
```

Pensa antes de terminares: um leitor de ecrã chega à célula "20 de março". Que duas informações dos cabeçalhos pode dizer, além da data? A resposta: o torneio, "Torneio de primavera", que é o cabeçalho da linha, e "Data", que é o cabeçalho da coluna.

## Problemas frequentes

### A página não mudou depois de alterares o ficheiro

Ou não guardaste, ou não recarregaste, ou o browser tem aberta outra cópia do ficheiro. Olha para o separador do ficheiro no VS Code: uma bolinha no lugar da cruz quer dizer que não está guardado. Guarda e recarrega. Se continuar igual, confirma na barra de endereço do browser que o ficheiro aberto é o que estás a editar.

### O separador mostra o nome do ficheiro em vez do título

O `title` tem um erro, ou não está dentro do `head`. Confirma que abre com `<title>`, que fecha com `</title>` e que está entre `<head>` e `</head>`.

### As letras acentuadas aparecem trocadas por símbolos estranhos

Aparece, por exemplo, `Ã§` no lugar de `ç`. Confirma que `<meta charset="utf-8">` é a primeira linha dentro do `head`. Olha também para a barra de baixo do VS Code, que deve dizer UTF-8. Se disser outra coisa, carrega nela, escolhe Save with Encoding, que quer dizer "guardar com a codificação", e depois UTF-8. A codificação é a tabela que transforma os bytes do ficheiro em letras.

### O esqueleto tem `lang="en"`

O esqueleto foi escrito pelo atalho `!` do VS Code, que põe a página em inglês. No ecrã não muda nada, mas um leitor de ecrã lê o teu português com pronúncia inglesa. Muda para `lang="pt-PT"`.

### Uma ligação dá "Não foi possível aceder ao seu ficheiro"

O `href` não é igual ao nome do ficheiro de destino, ou a página ainda não existe. Lê o endereço na barra do browser e compara-o, letra a letra, com o nome do ficheiro no painel Explorer. Corrige o `href`.

### A imagem não aparece

No sítio dela aparece o ícone de imagem partida, ou só o texto do `alt`. O `src` não corresponde ao sítio onde a imagem está. Compara o `src` com o nome e a pasta da imagem. Procura uma letra trocada, a extensão diferente (`.jpeg` no disco e `.jpg` no código) ou a pasta `imagens/` esquecida. Abre também o separador Console, que diz que ficheiro o browser não encontrou.

### O separador Console não mostra nenhuma mensagem

A Console só mostra o que acontece enquanto está aberta. Com ela aberta, recarrega a página. Se continuar vazia, confirma que o filtro dos níveis, por cima das mensagens, deixa ver os erros.

### A imagem aparece enorme

A fotografia tem as medidas originais, com milhares de píxeis de largura, e as tuas páginas ainda não têm CSS para a encolher. Reduz a largura da fotografia para 600 a 800 píxeis. Usa um programa de edição de imagem, como o Paint no Windows ou a Pré-visualização no Mac. Depois, escreve as medidas novas no `width` e no `height`.

### A página aparece em texto simples, com as etiquetas à mostra

O nome do ficheiro acaba em `.txt`, e não em `.html`. Acontece quando o ficheiro foi guardado num editor de texto simples, e o Windows esconde muitas vezes a extensão. Cria os ficheiros no VS Code. Se o problema já aconteceu, renomeia o ficheiro no painel Explorer do VS Code, que mostra o nome completo.

### Metade da página ficou a negrito, ou com letra de título

Falta uma etiqueta de fecho, ou falta a barra nela, como `<strong>` onde devia estar `</strong>`. Procura o último sítio onde a página estava certa e a etiqueta que abre logo antes. Escreve a etiqueta de fecho, com a barra.

### O VS Code não mostra cores no código

O VS Code não sabe que o ficheiro é HTML. Olha para o canto inferior direito, que deve dizer HTML, e confirma que o nome do ficheiro acaba em `.html`.

### A cópia da página ficou com o nome `index copy.html`

Faltou mudar-lhe o nome. No painel Explorer, carrega com o botão direito na cópia, escolhe Rename... e dá-lhe o nome que está no `href` do menu.

### O F12 não abre as ferramentas do programador

Em muitos portáteis, as teclas de cima fazem outras coisas, como mudar o volume. Experimenta Fn+F12, ou Ctrl+Shift+I. No Mac, usa Cmd+Option+I. Também podes carregar com o botão direito do rato na página e escolher Inspecionar.

### Não encontro o separador Accessibility

O painel ao lado da árvore do DOM está estreito, e o separador ficou escondido. Carrega no botão com duas setas, `»`, ao lado dos separadores Styles e Computed, e escolhe Accessibility na lista. Também podes alargar o painel das ferramentas do programador, arrastando a margem dele.

## Desafios

1. Na página inicial, acrescenta uma ligação, logo a seguir ao parágrafo de apresentação, que salte para uma das secções da mesma página. Pista: o elemento de destino precisa de um nome que nenhum outro elemento da página tenha.
2. O teu site pode ter um logótipo, ou um pequeno desenho que o represente. Põe-no no cabeçalho das duas páginas, ao lado do nome do site. Decide o `alt` e justifica-o numa frase. Pista: faz a pergunta do telefone, sabendo o que está escrito logo ao lado.
3. Numa das tuas páginas, acrescenta uma ligação para outro site, onde a pessoa encontre mais informação sobre o teu tema. Pista: o destino não está na pasta do teu site, e o texto da ligação tem de dizer o que a pessoa lá encontra.

## Antes de terminares

- [ ] A pasta do teu site tem as duas páginas e a pasta `imagens`, com nomes em minúsculas, sem espaços e sem acentos.
- [ ] As duas páginas têm o esqueleto completo, com `lang="pt-PT"` e um `title` diferente em cada uma.
- [ ] O cabeçalho, a navegação e o rodapé são iguais nas duas páginas.
- [ ] Cada página tem um só `h1`, e os títulos não saltam níveis a descer.
- [ ] A imagem tem o atributo `alt`, escrito com a pergunta do telefone.
- [ ] As ligações funcionam nos dois sentidos, também só com o teclado.
- [ ] A tabela de verificação da fase 7 está preenchida, com as três justificações no fim.
- [ ] Tens no caderno as cinco linhas da fase 8, uma por erro.
- [ ] Tens a tabela da fase 9, ou a frase que explica porque é que o teu site não precisa de tabela.
- [ ] Entregaste a pasta do teu site da forma que o professor indicar.
- [ ] Consegues explicar, por palavras tuas, porque escolheste o elemento de cada zona pelo que o conteúdo é, e não pelo aspeto.

![Rodapé](../imagens/rodape.png)
