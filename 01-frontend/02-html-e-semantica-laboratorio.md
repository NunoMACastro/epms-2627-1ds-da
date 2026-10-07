![Cabeçalho](../imagens/cabecalho.png)

# Laboratório: HTML e semântica

UC: UC02833, Conceber aplicações para a web na vertente frontend

Bloco: F02

Requisitos: UC02833.R01, UC02833.K03, UC02833.K04, UC02833.K09, UC02833.A04, UC02833.A05, UC02833.A06, UC02833.A11, UC02833.C01

| Identificação | Valor |
| --- | --- |
| Material | Laboratório do bloco F02, acompanha o [guia](02-html-e-semantica.md) |
| Duração | 115 minutos dos 300 do bloco, em duas partes. A parte A (partes 1 a 8, 85 minutos) constrói e verifica as duas primeiras páginas do teu site. A parte B (partes 9 e 10, 30 minutos) provoca erros de propósito para os aprenderes a corrigir e acrescenta uma tabela de dados |
| Ponto de partida | O plano do teu site, feito no bloco 01: o mapa com pelo menos duas páginas e, se já os fizeste, os wireframes |
| Material de apoio | A [imagem provisória](../laboratorios/frontend/primeiras-paginas/README.md), para quem ainda não tem uma imagem do seu tema |
| Evidência a guardar | A pasta do teu site com as duas páginas, a tabela de verificação da parte 8 preenchida e a justificação escrita de três elementos |

## O que vais fazer

Neste laboratório vais escrever as duas primeiras páginas do teu site, a partir do plano que fizeste no bloco 01. No fim deves ter:

- uma pasta com o nome do teu site, com duas páginas HTML e uma subpasta de imagens;
- duas páginas com o esqueleto completo, o mesmo cabeçalho, a mesma navegação e o mesmo rodapé, e cada uma com o seu conteúdo principal;
- as duas páginas ligadas nos dois sentidos;
- uma imagem com o texto alternativo certo;
- a verificação das duas páginas feita e registada.

Não vais aprender teoria nova. Tudo o que escreves aqui está explicado no [guia](02-html-e-semantica.md), e cada parte diz-te que secção do guia deves ter aberta ao lado. Se uma instrução não fizer sentido, volta a essa secção antes de continuares.

O tema é o do teu site, escolhido por ti no bloco 01. Os exemplos deste laboratório usam o site de um clube de xadrez da escola, inventado, só para mostrar a forma. Não copies os textos do exemplo: escreve os teus.

## O que precisas antes

- O plano do teu site: o mapa, com pelo menos duas páginas e as ligações entre elas, e, se já os fizeste, os wireframes. Se ainda não tens o mapa, faz primeiro os passos 1 a 4 da prática guiada do [guia do bloco 01](01-web-e-planeamento.md), na secção "Prática guiada: o plano do teu site". Os wireframes ajudam, mas não são obrigatórios para começar: sem eles, decides as zonas de cada página ao escrever, com a tabela do passo 1 do exemplo explicado do guia.
- Do guia deste bloco, as secções "Elementos, etiquetas e atributos", "O esqueleto de uma página", "O que vai no head", "Títulos: de h1 a h6", "Listas", "Ligações", "Caminhos relativos", "O texto alternativo" e "Os elementos semânticos", e o exemplo explicado.
- Um computador com o VS Code e um browser (Chrome ou Edge).

Uma nota sobre conteúdo: o texto das tuas páginas pode ser inventado, e deve ser curto nesta fase. Duas ou três frases por secção chegam. O que se treina aqui é a estrutura, e não a escrita. Nunca ponhas nas páginas dados pessoais verdadeiros, teus ou de outras pessoas: moradas, números de telefone, fotografias de colegas.

## Os atalhos de que vais precisar

| O que fazer | Windows | Mac |
| --- | --- | --- |
| Guardar o ficheiro no VS Code | Ctrl+S | Cmd+S |
| Recarregar a página no browser | F5 | Cmd+R |
| Abrir as ferramentas do programador | F12 ou Ctrl+Shift+I | Cmd+Option+I |
| Indentar o ficheiro inteiro no VS Code | Shift+Alt+F | Shift+Option+F |
| Andar para a ligação seguinte, e para a anterior | Tab e Shift+Tab | Tab e Shift+Tab |

O ciclo de trabalho de todo o laboratório é sempre o mesmo: escreves no VS Code, guardas, passas para o browser e recarregas. Se a página não mudou, é quase sempre porque te esqueceste de guardar ou de recarregar.

## Parte A: As duas páginas

### Parte 1: Criar a pasta do teu site (5 min)

**1.** Escolhe o nome da pasta a partir do tema do teu site, com as regras da secção "Caminhos relativos" do guia: minúsculas, sem espaços, sem acentos e com hífenes entre as palavras. Por exemplo, `clube-de-xadrez`, `receitas-da-avo` ou `guia-de-sintra`. Um nome como `O Meu Site` ou `receitas_avó` vai dar problemas mais tarde.

**2.** Se já criaste a pasta do teu site no fim da prática guiada do guia 01, com as fotografias do plano, usa essa e salta para a criação da pasta `imagens`. Se não, cria a pasta onde o professor indicar. Dentro dela, cria uma pasta chamada `imagens`.

**3.** Abre o VS Code e, no menu File, escolhe Open Folder. Com o VS Code em português, os nomes são Arquivo e Abrir Pasta, porque o único pacote de português do VS Code é o do Brasil. Escolhe a pasta do teu site. Do lado esquerdo aparece o painel Explorer (em português, Explorador), com o nome da pasta em maiúsculas e a pasta `imagens` lá dentro. Se o VS Code perguntar se confias nos autores dos ficheiros da pasta, responde que sim: a pasta é tua.

**Confirma:** o painel Explorer do VS Code mostra a pasta do teu site e a subpasta `imagens`, vazia.

### Parte 2: O esqueleto da primeira página (10 min)

Tem aberta a secção "O esqueleto de uma página" do guia.

**1.** No painel Explorer, passa o rato por cima do nome da pasta e carrega no ícone de ficheiro novo (New File). Escreve o nome `index.html` e carrega em Enter. O ficheiro abre-se, vazio, no meio da janela. O nome `index.html` não é uma escolha tua: é o nome que os servidores procuram para a página inicial, como explica o passo 2 do exemplo explicado.

**2.** Escreve o esqueleto à mão, linha a linha. Não copies e não uses atalhos do editor que o escrevam por ti: escrevê-lo é a melhor forma de o saberes de cor. No `title`, põe o nome da página inicial e o nome do teu site, com a forma `Página | Site`:

```html
<!doctype html>
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

Enquanto escreves, repara que o VS Code acrescenta sozinho a etiqueta de fecho quando acabas de escrever uma etiqueta de abertura. Isso ajuda, mas confirma sempre que o fecho ficou no sítio certo.

**3.** Guarda o ficheiro.

**4.** Abre a página no browser. Há três formas: no explorador de ficheiros do sistema, fazer duplo clique no `index.html`; arrastar o ficheiro para uma janela do browser; ou, no browser, carregar em Ctrl+O (Cmd+O no Mac) e escolher o ficheiro. Deixa a página aberta num separador: vais recarregá-la muitas vezes.

**Confirma:** a página está em branco e o separador do browser mostra o título que escreveste. Olha também para a barra de endereço: começa por `file://`, porque o ficheiro está a ser lido do teu computador, e não de um servidor, como viste no guia 01. Se o separador mostrar `index.html` em vez do teu título, o `title` tem um erro: confirma que abre com `<title>` e fecha com `</title>`.

### Parte 3: O cabeçalho e a navegação (10 min)

Tem aberta a secção "Os elementos semânticos" do guia e o passo 4 do exemplo explicado.

**1.** Olha para o teu mapa do site e escolhe já o nome do ficheiro da segunda página, com as mesmas regras dos nomes: por exemplo, `horario.html` ou `torneios.html`. Escreve-o no mapa, ao lado da caixa dessa página.

**2.** Dentro do `body`, escreve o `header`, com o nome do teu site num parágrafo e a navegação numa lista de ligações:

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

Nas tuas ligações, usa os nomes das tuas páginas. A segunda ligação aponta para uma página que ainda não existe: vais criá-la na parte 6. Até lá, carregar nela dá erro, e é normal.

**3.** Guarda e recarrega.

**Confirma:** aparece o nome do site e, por baixo, uma lista com duas ligações sublinhadas, cada uma com uma bolinha à frente. A bolinha é da lista: no bloco de CSS vais aprender a tirá-la.

### Parte 4: O conteúdo principal da primeira página (15 min)

Tem aberto o teu mapa, o wireframe da página inicial se já o fizeste, e as secções "Títulos: de h1 a h6" e "Listas" do guia.

**1.** Por baixo do `header`, ainda dentro do `body`, abre o `main`. Lá dentro, escreve o `h1` com o assunto desta página, que não é o nome do site. Pergunta a ti próprio o que alguém encontra nesta página. No clube de xadrez podia ser "Bem-vindo ao clube de xadrez da escola" ou "Aprende a jogar xadrez connosco".

**2.** Escreve um ou dois parágrafos curtos de apresentação.

**3.** Escreve pelo menos duas `section`, cada uma com o seu `h2` e o seu conteúdo, pelas zonas que desenhaste no wireframe ou, se ainda não o tens, pelos grupos de conteúdo do teu inventário. Pelo menos uma das secções tem de ter uma lista. Antes de escreveres a lista, faz o teste da secção "Listas": se trocares dois itens de lugar, a informação fica errada? Escolhe `ul` ou `ol` pela resposta.

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

**4.** Guarda e recarrega.

**5.** Numa folha, escreve o índice dos títulos da página, com a indentação a mostrar os níveis, como no passo 7 do exemplo explicado.

**Confirma:** o índice tem um só `h1`, e os `h2` vêm a seguir, sem saltos. Se tiveres um `h3`, está dentro de uma parte com `h2`.

### Parte 5: O rodapé (5 min)

**1.** Por baixo do `main`, ainda dentro do `body`, escreve o `footer`, com um parágrafo de informação final: por exemplo, quem fez o site, a turma e o ano, e um aviso de que o conteúdo é fictício, se for o caso.

**2.** Guarda, recarrega e indenta o ficheiro inteiro com o atalho do VS Code, para confirmares que a indentação mostra a estrutura: `header`, `main` e `footer` à mesma distância da margem, dentro do `body`. Por omissão, o VS Code deixa o `head` e o `body` à mesma margem do `html` e acrescenta algumas linhas em branco. É só a forma como o VS Code arruma o ficheiro, e a página fica igual.

**Confirma:** o `body` tem exatamente três filhos diretos, `header`, `main` e `footer`, por esta ordem.

### Parte 6: A segunda página (20 min)

Tem abertos o passo 8 e o passo 9 do exemplo explicado e a secção "O texto alternativo" do guia.

**1.** Arranja a imagem da segunda página e põe-na na pasta `imagens`. Pode ser uma fotografia ou um desenho teus, ou uma imagem cuja licença permita o uso, como explica a secção "Imagens" do guia. Dá-lhe um nome com as regras dos nomes, como `tabuleiro.jpg`. Se for uma fotografia tirada com o telemóvel, reduz-lhe primeiro a largura para 600 a 800 píxeis, como explica a secção "Imagens" do guia: as tuas páginas ainda não têm CSS, e por isso a imagem aparece no ecrã com as medidas que escreveres no `width` e no `height`. Se ainda não tens nenhuma imagem, copia para a pasta `imagens` a [imagem provisória](../laboratorios/frontend/primeiras-paginas/README.md) do laboratório e troca-a mais tarde. Na pasta do repositório da disciplina, o ficheiro está em `laboratorios/frontend/primeiras-paginas/imagem-provisoria.svg`.

**2.** No painel Explorer do VS Code, carrega com o botão direito do rato no `index.html` e escolhe Copy; depois carrega com o botão direito numa zona vazia do painel e escolhe Paste. Aparece uma cópia com um nome como `index copy.html`. Carrega com o botão direito nela, escolhe Rename e dá-lhe o nome exato que puseste na navegação na parte 3, como `torneios.html`. O nome tem de ser igual letra a letra.

**3.** Na cópia, muda o `title` para o nome desta página e o nome do site, como `Torneios | Clube de Xadrez`.

**4.** Apaga todo o conteúdo do `main` desta cópia, deixando o `main` vazio, e escreve o conteúdo desta página: o `h1` com o assunto da página, um parágrafo e pelo menos uma secção com `h2`. O `header` e o `footer` não se mexem: ficam iguais aos da página inicial.

**5.** Põe a imagem numa das secções. Se a imagem tiver uma legenda que acrescente alguma coisa (de onde vem, quem a fez, o que mostra de especial), usa um `figure` com `figcaption`, como no passo 9 do exemplo. Se não tiver, basta o `img`.

```html
<figure>
  <img src="imagens/tabuleiro.jpg"
       alt="Tabuleiro de xadrez a meio de uma partida, com as peças brancas em ataque."
       width="600" height="400">
  <figcaption>Final do torneio da escola do ano passado. Fotografia do clube.</figcaption>
</figure>
```

Para o `alt`, faz a pergunta do telefone: o que dirias a alguém ao telefone, no sítio desta imagem, para a página continuar a fazer sentido? Se usaste a imagem provisória, o `alt` é `Imagem provisória`, e fica anotado que tens de trocar os dois mais tarde.

Para o `width` e o `height`, usa as medidas verdadeiras da imagem, depois de reduzida. No Windows, vês as medidas nas propriedades do ficheiro, no separador Detalhes; no Mac, na janela Obter informações. A imagem provisória mede 400 por 300.

**6.** No fim do `main`, acrescenta um parágrafo com uma ligação de volta à página inicial, com um texto que diga o destino, como "Voltar à página inicial".

**7.** Guarda e abre esta página no browser.

**Confirma:** o separador mostra o título novo, a imagem aparece, e o cabeçalho e o rodapé são iguais aos da página inicial.

### Parte 7: Ligar as duas páginas nos dois sentidos (5 min)

**1.** Volta à página inicial no browser e carrega na segunda ligação da navegação. Agora que a página existe, a ligação tem de funcionar.

**2.** Na segunda página, carrega em "Início" na navegação e depois na ligação de volta, no fim do conteúdo. As duas levam à página inicial.

**3.** Se alguma ligação der "ficheiro não encontrado", compara letra a letra o `href` com o nome do ficheiro no painel Explorer. As diferenças mais comuns são uma letra maiúscula, um acento ou a extensão esquecida.

**Confirma:** consegues ir de uma página à outra e voltar, pelos dois caminhos.

### Parte 8: Verificar (15 min)

Tem aberta a secção "Verificar uma página" do guia. Copia esta tabela para o teu caderno, ou para um ficheiro, e preenche-a à medida que fazes cada verificação:

| Verificação | O que fiz | Passou? | Se não passou, o que corrigi |
| --- | --- | --- | --- |
| Ligações | Carreguei em todas as ligações das duas páginas | | |
| Ordem de leitura | Li as duas páginas de cima a baixo e escrevi o índice dos títulos | | |
| Teclado | Percorri as duas páginas só com Tab, Shift+Tab e Enter | | |
| Árvore do DOM | Comparei a árvore no separador Elements com o meu ficheiro | | |
| Árvore de acessibilidade | Encontrei as zonas e o nome da imagem | | |

**1. Ligações.** Carrega em cada ligação das duas páginas, uma de cada vez, e volta atrás depois de cada uma. Todas têm de levar ao sítio certo.

**2. Ordem de leitura.** As tuas páginas não têm CSS, por isso o que vês é já a página com o aspeto por omissão do browser e pela ordem em que o HTML está escrito. Lê cada página de cima a baixo como se fosses outra pessoa, e pergunta: a ordem faz sentido? Os títulos dizem de que trata cada parte? O assunto da página aparece logo a seguir ao menu?

**3. Teclado.** Carrega uma vez em qualquer sítio vazio da página e, a partir daí, não toques no rato. Carrega em Tab várias vezes. Uma moldura, a que se chama foco, salta de ligação em ligação. Confirma que chegas a todas as ligações pela ordem em que aparecem, que Shift+Tab anda para trás e que Enter segue a ligação onde está o foco. Consegues ir à segunda página e voltar só com o teclado?

**4. Árvore do DOM.** Abre as ferramentas do programador com o atalho da tabela do início. Se ainda não as conheces, o [laboratório do bloco 01](01-web-e-planeamento-laboratorio.md) explica-as com calma; por agora, basta saberes que o separador Elements (em português pode aparecer como Elementos) mostra a árvore que o browser construiu a partir do teu ficheiro. Abre os triângulos do `body`, do `header`, do `main` e do `footer`, e compara com o teu ficheiro no VS Code. Os elementos têm de ser os mesmos, pela mesma ordem. Um parágrafo vazio que não escreveste, ou um elemento noutro sítio, quer dizer que o browser corrigiu um erro teu: procura-o no ficheiro.

**5. Árvore de acessibilidade.** Ainda no separador Elements, carrega no elemento `main` da árvore para o selecionar. No painel do lado, onde está o separador Styles, procura o separador Accessibility (Acessibilidade). Se não o vires, pode estar escondido atrás de um botão com duas setas, `»`. Aí aparece o papel do elemento selecionado, que deve ser *main*. Seleciona agora o `nav`, o `header` e o `footer`, um de cada vez, e confirma que os papéis são *navigation*, *banner* e *contentinfo*. Por fim, seleciona o `img` da segunda página e confirma que o nome que aparece é o texto que escreveste no `alt`.

**6.** Escreve, no fim da tabela, a justificação de três elementos que escolheste nas tuas páginas, uma ou duas frases cada. Por exemplo: "A lista do que trazer é um `ul` porque trocar a ordem dos itens não muda nada" ou "A imagem do tabuleiro está num `figure` porque tem uma legenda que diz de onde vem a fotografia".

**7.** Se já preencheste no bloco 01 o [modelo do brief](../projeto/modelos/brief-e-wireframe.md) do teu site, completa agora os dois campos que ficaram para este bloco: "Relação entre zonas desenhadas e elementos HTML", com o elemento que escolheste para cada zona do teu wireframe, e "Percurso por teclado e foco", com a ordem pela qual o Tab passou pelas ligações na verificação 3. Se ainda não tens o brief, escreve as duas coisas no caderno e passa-as para o brief quando o fizeres.

**Confirma:** as cinco linhas da tabela dizem que passou, ou dizem o que corrigiste até passar.

Aqui acaba a parte A.

## Parte B: Erros e tabelas

### Parte 9: Provocar erros e corrigi-los (20 min)

Tem aberta a secção "Erros comuns" do guia. Nesta parte vais estragar as tuas páginas de propósito, um erro de cada vez, para aprenderes a reconhecer cada erro pelo que ele faz. Depois de cada erro, desfaz a alteração antes de passares ao seguinte. No VS Code, Ctrl+Z (Cmd+Z no Mac) desfaz a última alteração.

**9.1 A imagem que falta.** No painel Explorer, muda o nome da tua imagem, acrescentando uma letra no fim do nome, antes da extensão. Recarrega a segunda página. No sítio da imagem aparece, normalmente, um pequeno ícone de imagem partida com o texto do `alt` ao lado. Abre as ferramentas do programador no separador Console (em português, Consola) e procura uma mensagem de erro, normalmente a vermelho, sobre um recurso que não foi possível carregar. Se não aparecer nada, recarrega a página com o Console aberto. Escreve no caderno o que viste. Repõe o nome original e recarrega.

**9.2 O caminho sem a pasta.** No `src` da imagem, apaga `imagens/`, deixando só o nome do ficheiro. Guarda e recarrega. A imagem desaparece outra vez, porque agora o browser procura o ficheiro na pasta da página, e não na pasta `imagens`. Repõe o caminho.

**9.3 O título que salta um nível.** Numa das tuas secções, muda o `h2` para `h4`, na abertura e no fecho. Guarda e recarrega. Na página, a única coisa que muda é o tamanho da letra, e é isso que torna este erro perigoso: parece só uma questão de aspeto. Escreve o índice dos títulos da página e vê o salto de `h1` para `h4`. Repõe o `h2`.

**9.4 A lista dentro de um parágrafo.** Escolhe uma das tuas listas e põe-na dentro de um parágrafo: escreve `<p>` antes do `<ul>` e `</p>` depois do `</ul>`. Guarda e recarrega. Na página quase não se nota nada. Agora abre o separador Elements e procura esse sítio da árvore: o browser fechou o parágrafo antes da lista e criou um parágrafo vazio a seguir. É a diferença entre o teu ficheiro e o DOM de que fala a secção "Como o browser lida com os erros". Repõe a lista como estava.

**9.5 O strong que ficou aberto.** Num parágrafo, marca uma palavra com `<strong>`, mas não escrevas o `</strong>`. Guarda e recarrega. Vê até onde vai o negrito. Depois escreve o fecho no sítio certo.

**Confirma:** depois de desfazeres os cinco erros, as páginas voltam a passar as verificações da parte 8. Faz de novo, rapidamente, a verificação das ligações e da árvore.

### Parte 10: Uma tabela de dados (10 min)

Tem aberta a secção "Tabelas de dados" do guia e o passo 11 do exemplo explicado.

**1.** Pergunta a ti próprio se o teu site tem informação que se lê em linhas e colunas: um horário, uma tabela de preços, uma classificação, uma comparação entre coisas. Aplica o teste da secção: cada valor responde a uma pergunta que junta uma linha e uma coluna?

**2.** Se tiver, acrescenta essa tabela a uma das tuas páginas, dentro da secção onde faz sentido. Começa pelo `caption`, depois o `thead` com os cabeçalhos de coluna, cada um com `scope="col"`, e depois o `tbody`, com uma linha por registo. Se a primeira célula de cada linha disser de que é a linha, é um `th` com `scope="row"`.

```html
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
  </tbody>
</table>
```

**3.** Se o teu site não tiver dados em linhas e colunas, não inventes uma tabela só para ter uma: faz a tabela no exercício da [ficha](02-html-e-semantica-exercicios.md) e escreve no caderno porque é que o teu site não precisa de tabela.

**4.** Guarda, recarrega e, na árvore de acessibilidade, seleciona uma célula de dados. Confirma que a tabela aparece com a legenda que escreveste.

**Confirma:** a tabela tem legenda, cabeçalhos com `scope`, e não serve para arrumar nada: só mostra dados.

## Quando alguma coisa corre mal

| O que vês | Como investigar | Como resolver |
| --- | --- | --- |
| A página não mudou depois de alterares o ficheiro | Olha para o separador do ficheiro no VS Code: uma bolinha no lugar da cruz quer dizer que não está guardado | Guarda e recarrega. Se continuar igual, confirma na barra de endereço do browser que o ficheiro aberto é o que estás a editar |
| O separador mostra o nome do ficheiro em vez do título | Procura o `title` no `head` | Confirma que o `title` está dentro do `head` e fecha com `</title>` |
| As letras acentuadas aparecem trocadas por símbolos estranhos | Confirma que `<meta charset="utf-8">` é a primeira linha do `head`, e olha para a barra de baixo do VS Code, que deve dizer UTF-8 | Corrige o `meta`. Se a barra disser outra coisa, carrega nela, escolhe Save with Encoding e depois UTF-8 |
| Uma ligação dá "ficheiro não encontrado" | Lê o endereço na barra do browser e compara-o com o nome do ficheiro no painel Explorer | Corrige o `href`, letra a letra |
| A imagem não aparece | Compara o `src` com o nome e a pasta da imagem; abre o separador Console | Corrige o caminho ou o nome |
| A página aparece em texto simples, com as etiquetas à mostra | Olha para o nome completo do ficheiro: pode ter ficado `.txt` no fim | Renomeia o ficheiro para acabar em `.html` |
| Metade da página ficou a negrito ou com letra de título | Procura o último sítio onde estava certo e a etiqueta que abre logo antes | Escreve a etiqueta de fecho em falta, com a barra |
| O VS Code não mostra cores no código | Olha para o canto inferior direito: deve dizer HTML | Confirma que o nome do ficheiro acaba em `.html` |

## O que entregar

- A pasta do teu site, com as duas páginas e a pasta `imagens`, entregue da forma que o professor indicar.
- A tabela de verificação da parte 8, preenchida, com a justificação dos três elementos no fim.
- As notas da parte 9: o que viste em cada erro, uma linha por erro.
- A tabela da parte 10, ou a frase que explica porque é que o teu site não precisa de tabela.

![Rodapé](../imagens/rodape.png)
