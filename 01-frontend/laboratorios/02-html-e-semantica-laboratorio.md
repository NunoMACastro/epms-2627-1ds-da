![Cabeçalho](../../imagens/cabecalho.png)

# Laboratório: HTML e semântica

## O que vais construir

Constróis as duas primeiras páginas do teu site, em HTML, ligadas uma à outra e verificadas. Os exemplos usam o site inventado de um clube de xadrez da escola, só para mostrar a forma: escreve os teus textos. No fim, a pasta do exemplo e o ficheiro de registo ao lado dela ficam assim:

```text
clube-de-xadrez/
├── index.html
├── torneios.html
└── imagens/
    └── imagem-provisoria.svg
registo.md
```

1. [Fase 1: O esqueleto completo de uma página](#fase-1-o-esqueleto-completo-de-uma-página)
2. [Fase 2: As zonas da página: header, nav, main e footer](#fase-2-as-zonas-da-página-header-nav-main-e-footer)
3. [Fase 3: Títulos: de h1 a h6](#fase-3-títulos-de-h1-a-h6)
4. [Fase 4: Listas](#fase-4-listas)
5. [Fase 5: O texto alternativo](#fase-5-o-texto-alternativo)
6. [Fase 6: Caminhos relativos](#fase-6-caminhos-relativos)
7. [Fase 7: Verificar uma página](#fase-7-verificar-uma-página)
8. [Fase 8: Como o browser lida com os erros](#fase-8-como-o-browser-lida-com-os-erros)
9. [Fase 9, opcional: Uma tabela de dados cruza linhas e colunas](#fase-9-opcional-uma-tabela-de-dados-cruza-linhas-e-colunas)

## O que precisas

- O VS Code, o editor das aulas: abre-o, e deve aparecer a janela do editor.
- O Chrome ou o Edge, para abrir as páginas. Os passos são iguais nos dois.
- O plano do teu site e a pasta onde o guardaste, do exercício 7 da [ficha do tema 01](../exercicios/01-web-e-planeamento-exercicios.md). Se não tens a pasta, "Preparar o projeto" diz como a criar.
- Uma imagem para a segunda página, sobre o tema do teu site. Se ainda não tens nenhuma, usas a [imagem provisória](02-html-e-semantica-laboratorio/README.md).

## Preparar o projeto

O texto das tuas páginas pode ser inventado e curto, porque o que se treina aqui é a estrutura. Nunca ponhas nas páginas dados pessoais verdadeiros, teus ou de outras pessoas.

1. As páginas ficam na pasta do teu site, onde guardaste o plano. Se não a tens, cria-a onde o professor indicar, com um nome em minúsculas, sem espaços nem acentos, como `clube-de-xadrez`. Para isso, abre o programa que mostra as pastas do computador. No Windows é o Explorador de Ficheiros, que se abre com as teclas Windows+E. No Mac é o Finder, o ícone com uma cara sorridente na barra de baixo. Vai até ao sítio da pasta e carrega com o botão direito num sítio vazio. Escolhe Novo e depois Pasta, no Windows, ou Nova pasta, no Mac. Escreve o nome e carrega em Enter. No trackpad de um Mac, o botão direito é um clique com dois dedos.

2. Entra na pasta do teu site e cria lá dentro, da mesma maneira, uma pasta chamada `imagens`, onde vão ficar as imagens do site.

3. Abre a pasta do teu site no VS Code: no menu File, escolhe Open Folder... e depois a pasta. Com o VS Code em português, os nomes são Arquivo e Abrir Pasta. Se o VS Code perguntar se confias nos autores dos ficheiros, carrega em "Yes, I trust the authors", porque a pasta é tua. O que deves ver: à esquerda, o painel Explorer, com o nome da pasta do teu site e a pasta `imagens` lá dentro. O VS Code mostra o nome da pasta em maiúsculas, mas o nome verdadeiro continua em minúsculas.

4. Cria o `registo.md`, o ficheiro de texto onde registas o que verificas nas tuas páginas. Fica ao lado da pasta do teu site, e não dentro dela, porque não é uma página do site. No menu File, escolhe New Text File e guarda logo o ficheiro, com Ctrl+S, ou Cmd+S no Mac. Na janela que se abre, sobe para a pasta que tem a pasta do teu site lá dentro. No Windows, carrega no nome dessa pasta na barra de endereço; no Mac, escolhe-a na lista Onde. Escreve o nome `registo.md` e carrega em Guardar.

   O que deves ver: o separador passa a chamar-se `registo.md`, e o ficheiro não aparece no painel Explorer, porque está fora da pasta do site. Para o voltares a abrir noutra aula, no menu File, escolhe Open Recent e depois o `registo.md`.

## Fase 1: O esqueleto completo de uma página

Escreves à mão o esqueleto da página inicial e confirmas que o browser o lê. Rever: [O esqueleto completo de uma página](../02-html-e-semantica.md#o-esqueleto-completo-de-uma-página) e [O que vai no head](../02-html-e-semantica.md#o-que-vai-no-head).

1. Cria o ficheiro da página inicial, que se chama `index.html` porque é o que um servidor envia quando o endereço não diz a página. No painel Explorer, carrega numa zona vazia, para o ficheiro não ficar dentro de `imagens`. Depois carrega no ícone de ficheiro novo, New File..., no topo do painel. Escreve `index.html` e carrega em Enter. O ficheiro abre-se, vazio.

2. Escreve o esqueleto à mão, linha a linha, sem atalhos do editor, porque o atalho mais conhecido põe a página em inglês. Cria `index.html` com este conteúdo. Põe o nome do teu site no lugar de "Clube de Xadrez", e o teu comentário no lugar do do exemplo:

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

   Enquanto escreves, o VS Code acrescenta sozinho a etiqueta de fecho de cada elemento. Confirma sempre que ela ficou no sítio certo.

3. Guarda o ficheiro, com Ctrl+S, ou Cmd+S no Mac.

4. Abre a página no browser. No painel Explorer, carrega com o botão direito no `index.html` e escolhe Reveal in File Explorer, ou Reveal in Finder, no Mac. Na pasta que se abre, faz duplo clique no `index.html`. Se abrir noutro browser, abre o Chrome ou o Edge, carrega em Ctrl+O, ou Cmd+O no Mac, e escolhe o ficheiro. Deixa a página aberta num separador, porque vais recarregá-la muitas vezes.

   Antes de olhares, prevê: o que aparece na janela, e o que aparece no separador? O que deves ver: a janela em branco, porque o `body` está vazio, e no separador o título que escreveste. Isto quer dizer que o browser leu o ficheiro. Se o separador mostrar `index.html`, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

### Paragem 1

A página abre em branco, e o separador mostra o título que escreveste. A partir daqui, trabalhas sempre assim: escreves no VS Code e guardas, e depois recarregas a página, com F5 ou Cmd+R.

Pensa antes de continuares: escreveste onze linhas, e nenhuma aparece na janela. Porquê? A resposta: o `body`, onde fica o que se vê, ainda está vazio. O resto é informação sobre a página, no `head`, e um comentário. O `title` aparece no separador, e não na janela.

## Fase 2: As zonas da página: header, nav, main e footer

Escreves as três zonas da página inicial: o cabeçalho com o menu, o conteúdo principal e o rodapé. Rever: [As zonas da página: header, nav, main e footer](../02-html-e-semantica.md#as-zonas-da-página-header-nav-main-e-footer) e [Uma ligação leva a outro sítio](../02-html-e-semantica.md#uma-ligação-leva-a-outro-sítio).

1. Olha para o teu mapa e escolhe o nome do ficheiro da segunda página, com as regras do nome da pasta, como `torneios.html`. Escreve-o no mapa, ao lado da caixa dessa página, porque o menu vai ligar para ele.

2. Em `index.html`, entre `<body>` e `</body>`, acrescenta o cabeçalho, com os nomes das tuas páginas no menu:

   ```html
   <header>
     <!-- O nome do site fica num p: o h1 vai ser o assunto desta página. -->
     <p>Clube de Xadrez</p>
     <nav>
       <ul>
         <li><a href="index.html">Início</a></li>
         <li><a href="torneios.html">Torneios</a></li>
       </ul>
     </nav>
   </header>
   ```

   Guarda e recarrega. O que deves ver: o nome do site e, por baixo, uma lista com duas ligações, sublinhadas e com uma bolinha à frente.

3. A seguir ao `</header>`, acrescenta o conteúdo principal, com o assunto da página num `h1` e um parágrafo de apresentação. Para encontrar o assunto, pergunta o que alguém encontra nesta página:

   ```html
   <main>
     <h1>Aprende a jogar xadrez connosco</h1>
     <p>O clube reúne-se todas as semanas para jogar, aprender aberturas e preparar torneios.</p>
   </main>
   ```

   Guarda e recarrega. O que deves ver: por baixo do menu, o título em letra grande e a negrito, e o parágrafo.

4. A seguir ao `</main>`, acrescenta o rodapé, com a informação final:

   ```html
   <footer>
     <p>Site do Clube de Xadrez, feito na disciplina de Desenvolvimento de Aplicações. Conteúdo fictício.</p>
   </footer>
   ```

   Guarda e recarrega. O que deves ver: o parágrafo do rodapé no fundo da página. Isto quer dizer que o `body` tem as três zonas, pela ordem do wireframe.

### Paragem 2

A página mostra o cabeçalho com o menu, o conteúdo principal e o rodapé.

Pensa antes de continuares: se carregares agora na segunda ligação do menu, o que acontece? A resposta: o browser mostra uma página de erro, "Não foi possível aceder ao seu ficheiro", porque a segunda página ainda não existe. Deixa de acontecer quando a criares, na fase 5.

## Fase 3: Títulos: de h1 a h6

Divides o conteúdo principal em secções, cada uma com o seu título, e escreves o índice da página. Rever: [Títulos: de h1 a h6](../02-html-e-semantica.md#títulos-de-h1-a-h6) e [As partes do conteúdo: section, article e aside](../02-html-e-semantica.md#as-partes-do-conteúdo-section-article-e-aside).

1. Em `index.html`, a seguir ao parágrafo de apresentação, acrescenta pelo menos duas secções, cada uma com o seu `h2` e um parágrafo curto. Segue as zonas do teu wireframe, e faz com que uma delas enumere coisas, como o que trazer. No exemplo:

   ```html
   <section>
     <h2>Quando nos encontramos</h2>
     <p>Às quartas-feiras à tarde, na sala 12.</p>
   </section>

   <section>
     <h2>O que precisas de trazer</h2>
     <p>Vontade de aprender e um caderno para anotar as partidas.</p>
   </section>
   ```

   Guarda e recarrega. O que deves ver: os dois títulos das secções, um pouco mais pequenos do que o `h1`, cada um com o seu parágrafo.

2. Escreve no `registo.md` o índice dos títulos da página, com a indentação a mostrar os níveis, e guarda. No exemplo:

   ```text
   h1  Aprende a jogar xadrez connosco
       h2  Quando nos encontramos
       h2  O que precisas de trazer
   ```

### Paragem 3

O índice da tua página tem um só `h1`, e os `h2` vêm a seguir, sem saltos.

Pensa antes de continuares: se quisesses uma parte dentro de "Quando nos encontramos", para as férias, que nível de título levava? A resposta: um `h3`, porque é uma parte dentro de uma parte com `h2`.

## Fase 4: Listas

Trocas um parágrafo por uma lista, escolhida com o teste da troca. Rever: [Listas](../02-html-e-semantica.md#listas).

1. Escolhe uma das tuas secções em que o conteúdo seja uma enumeração. Antes de a escreveres, faz o teste da troca: se trocares dois itens de lugar, a informação fica errada? Se fica, é uma lista ordenada, `ol`; se não fica, é uma não ordenada, `ul`.

2. Nessa secção, substitui o parágrafo pela lista. No exemplo, trocar os dois itens do que trazer não torna a informação errada, e por isso é um `ul`:

   ```html
   <section>
     <h2>O que precisas de trazer</h2>
     <ul>
       <li>Vontade de aprender.</li>
       <li>Um caderno para anotar as partidas.</li>
     </ul>
   </section>
   ```

   Guarda e recarrega. O que deves ver: os itens da lista, cada um com uma bolinha à frente, num `ul`, ou com um número, num `ol`.

3. Indenta o ficheiro inteiro com o comando Format Document do VS Code: Shift+Alt+F no Windows, Shift+Option+F no Mac. O VS Code muda só os espaços e as linhas em branco, e a página fica igual. O que deves ver: o `header`, o `main` e o `footer` à mesma distância da margem. O VS Code deixa o `head` e o `body` encostados à margem e acrescenta linhas em branco. É só a forma como arruma o ficheiro. Se uma etiqueta de fecho ficar desalinhada da sua etiqueta de abertura, há um erro de aninhamento perto dela.

### Paragem 4

A primeira página está completa. O ficheiro `index.html` do exemplo, com a indentação dos materiais, antes do Format Document:

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
      <!-- O nome do site fica num p: o h1 vai ser o assunto desta página. -->
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

O `body` tem as três zonas, e só o `main` tem o que é desta página. O cabeçalho e o rodapé vão repetir-se, iguais, na segunda página.

Pensa antes de continuares: o clube quer pôr na página os passos da inscrição. São falar com o professor, preencher a ficha e vir ao primeiro treino. É um `ul` ou um `ol`? A resposta: `ol`, porque ninguém vem ao primeiro treino antes de se inscrever, e trocar os passos torna a informação errada.

## Fase 5: O texto alternativo

Crias a segunda página a partir da primeira e pões nela uma imagem, com o texto alternativo certo. Rever: [Imagens](../02-html-e-semantica.md#imagens), [O texto alternativo](../02-html-e-semantica.md#o-texto-alternativo) e [Imagem com legenda: figure e figcaption](../02-html-e-semantica.md#imagem-com-legenda-figure-e-figcaption).

1. Arranja a imagem e põe-na na pasta `imagens` do teu site, com um nome em minúsculas e sem espaços, como `tabuleiro.jpg`. Pode ser uma fotografia ou um desenho teus, ou de outra pessoa, se a licença o permitir. Se não for tua, anota no `registo.md` de onde veio e qual é a licença. Uma fotografia do telemóvel reduz-se primeiro para 600 a 800 píxeis de largura, no Paint, no Windows, ou na Pré-visualização, no Mac. Se não tens nenhuma imagem, copia a [imagem provisória](02-html-e-semantica-laboratorio/README.md) para a pasta `imagens`, sem lhe mudar o nome.

2. Cria a segunda página a partir da primeira, porque o esqueleto, o cabeçalho e o rodapé são iguais. No painel Explorer, carrega com o botão direito no `index.html` e escolhe Copy. Depois, carrega com o botão direito numa zona vazia do painel e escolhe Paste. Aparece uma cópia, como `index copy.html`. Carrega nela com o botão direito, escolhe Rename... e dá-lhe o nome que escreveste no mapa, igual ao do menu.

3. Abre a cópia, carregando nela no painel Explorer: o separador de cima tem de dizer o nome novo, como `torneios.html`, e não `index.html`. Muda o comentário do topo para dizer o que esta página é, e o `title` para o desta página:

   ```html
   <!-- Página dos torneios do Clube de Xadrez: o torneio do ano passado. -->
   ```

   ```html
   <title>Torneios | Clube de Xadrez</title>
   ```

4. Apaga o conteúdo do `main` da cópia, deixando o `<main>` e o `</main>`. O `header` e o `footer` ficam iguais. Dentro do `main`, escreve o `h1` com o assunto desta página, um parágrafo e uma secção com `h2`, e põe a imagem nessa secção. No exemplo, com a imagem provisória:

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

   O `alt` da imagem provisória diz só "Imagem provisória", porque é isso que ela transmite. Com a tua imagem, escreve no `alt` o que dirias ao telefone no sítio dela. No `width` e no `height`, usa as medidas verdadeiras da imagem. No Windows vês as medidas nas propriedades do ficheiro, no separador Detalhes; no Mac, em Obter informações.

5. Guarda e abre esta página no browser, com Ctrl+O, ou Cmd+O no Mac. O que deves ver: o título novo no separador e a imagem por baixo do parágrafo da secção. O cabeçalho e o rodapé são iguais aos da página inicial. Se a imagem não aparecer, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

### Paragem 5

A segunda página abre, com a imagem e o seu texto alternativo.

Pensa antes de continuares: se a imagem estivesse ao lado de um texto que já dissesse tudo o que ela mostra, que `alt` levava? A resposta: `alt=""`, vazio, porque um `alt` com texto faria o leitor de ecrã repetir o que está escrito ao lado.

## Fase 6: Caminhos relativos

Ligas as duas páginas nos dois sentidos e confirmas que cada caminho chega ao seu ficheiro. Rever: [Caminhos relativos](../02-html-e-semantica.md#caminhos-relativos).

1. Em `torneios.html`, no fim do `main`, depois da última secção, acrescenta uma ligação de volta à página inicial, e guarda. Não vai num `nav`, porque não é a navegação principal:

   ```html
   <p><a href="index.html">Voltar à página inicial</a></p>
   ```

2. Volta à página inicial no browser e carrega na segunda ligação do menu. O que deves ver: a segunda página. Na fase 2, a mesma ligação dava erro, porque o ficheiro ainda não existia.

3. Na segunda página, carrega em "Início", no menu, e depois, de volta à segunda página, carrega em "Voltar à página inicial". O que deves ver: as duas levam à página inicial. Se alguma ligação der "Não foi possível aceder ao seu ficheiro", vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

### Paragem 6

Vais de uma página à outra e voltas, pelo menu e pela ligação de volta. O ficheiro `torneios.html` do exemplo, como deve estar agora:

```html
<!doctype html>
<!-- Página dos torneios do Clube de Xadrez: o torneio do ano passado. -->
<html lang="pt-PT">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Torneios | Clube de Xadrez</title>
  </head>
  <body>
    <header>
      <!-- O nome do site fica num p: o h1 vai ser o assunto desta página. -->
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

O cabeçalho e o rodapé são os da página inicial, e o `main` é o desta página. Os `href` e o `src` são caminhos relativos, a partir da pasta onde está a página.

Pensa antes de continuares: um `href` com `Torneios.html`, para o ficheiro `torneios.html`, funciona no teu computador. Porque é que se corrige na mesma? A resposta: os servidores onde os sites se publicam distinguem quase sempre maiúsculas de minúsculas, e no site publicado a ligação dava erro.

## Fase 7: Verificar uma página

Verificas as duas páginas, como diz o guia, e registas cada verificação no `registo.md`. Rever: [Verificar uma página](../02-html-e-semantica.md#verificar-uma-página).

Para cada verificação, escreve no `registo.md` uma linha com o que fizeste, se passou e, se não passou, o que corrigiste.

1. Ligações. Carrega em cada ligação das duas páginas, uma de cada vez, e volta atrás depois de cada uma. O que deves ver: cada ligação leva ao sítio certo.

2. Ordem de leitura. Lê cada página de cima a baixo, como se fosses outra pessoa: a ordem faz sentido, e o assunto aparece logo a seguir ao menu? Escreve no `registo.md` o índice dos títulos da segunda página, como fizeste na fase 3.

3. Teclado. Carrega uma vez no nome do site, no topo da página, para o Tab começar daí, e depois não toques no rato. Carrega em Tab várias vezes: o foco, a moldura que mostra onde estás, salta de ligação em ligação. Shift+Tab leva o foco para trás, e Enter segue a ligação. O que deves ver: o foco passa por todas as ligações, pela ordem do ficheiro. Consegues ir à segunda página e voltar só com o teclado.

4. Árvore do DOM. Abre as ferramentas do programador com F12, ou Cmd+Option+I no Mac, no separador Elements, em português Elementos. Abre os triângulos do `body`, do `header`, do `main` e do `footer`, e compara a árvore com o teu ficheiro. O que deves ver: os mesmos elementos, pela mesma ordem. Isto quer dizer que o browser não teve de corrigir nenhum erro teu. Se a árvore tiver um parágrafo vazio que não escreveste, o browser corrigiu um erro: procura-o no ficheiro, perto desse sítio.

5. Árvore de acessibilidade. Ainda no Elements, seleciona o `main` na árvore. No painel ao lado, abre o separador Accessibility, em português Acessibilidade, que pode estar escondido atrás do botão `»`. O que deves ver: o papel *main*. Seleciona depois o `nav`, o `header` e o `footer`: os papéis são *navigation*, *banner* e *contentinfo*. Por fim, seleciona o `img` da segunda página: o nome é o texto do teu `alt`.

6. Justifica três elementos que escolheste, numa ou duas frases cada, num comentário logo antes do elemento. Cada justificação diz o que o conteúdo é, e não o aspeto que tem. Por exemplo: "A lista do que trazer é um `ul`, porque trocar a ordem dos itens não muda nada".

7. No brief do teu site, preenche os dois campos deste tema. Em "Relação entre zonas desenhadas e elementos HTML", escreve o elemento de cada zona do teu wireframe. Em "Percurso por teclado e foco", escreve a ordem por que o Tab passou nas ligações.

### Paragem 7

No `registo.md`, as cinco verificações dizem que passou, ou o que corrigiste até passar. As páginas têm os três comentários de justificação, e o brief tem os dois campos.

Pensa antes de continuares: porque é que o foco do Tab segue a ordem em que escreveste as ligações no ficheiro? A resposta: o foco segue a ordem do HTML, que é a mesma em que um leitor de ecrã lê a página. O CSS vai mudar o aspeto e a posição das coisas, mas esta ordem fica.

## Fase 8: Como o browser lida com os erros

Estragas as tuas páginas de propósito, um erro de cada vez, para reconheceres cada um pelo que ele faz. Depois de cada erro, desfazes a alteração com Ctrl+Z, ou Cmd+Z no Mac, guardas, e escreves no `registo.md` o que viste. Rever: [Como o browser lida com os erros](../02-html-e-semantica.md#como-o-browser-lida-com-os-erros).

1. A imagem que falta. No painel Explorer, muda o nome da tua imagem, acrescentando uma letra antes da extensão, e recarrega a segunda página. O que deves ver: no sítio da imagem, um ícone de imagem partida, com o texto do `alt`. Abre as ferramentas do programador no separador Console, em português Consola, e recarrega: aparece uma mensagem a vermelho a dizer que um ficheiro não carregou. Repõe o nome da imagem.

2. O caminho sem a pasta. No `src` da imagem, apaga `imagens/`, guarda e recarrega. O que deves ver: a imagem desaparece outra vez. Isto quer dizer que o browser foi procurar o ficheiro na pasta da página, e não em `imagens`. Repõe o caminho.

3. O título que salta um nível. Numa das tuas secções, muda o `h2` para `h4`, na abertura e no fecho. O que deves ver: só a letra do título fica mais pequena. Por isso este erro é perigoso: parece só aspeto, e no índice dos títulos é um salto de `h1` para `h4`. Repõe o `h2`.

4. A lista dentro de um parágrafo. Escreve `<p>` antes do `<ul>` de uma das tuas listas e apaga o `</p>` que o VS Code acrescenta logo a seguir. Escreve `</p>` depois do `</ul>`. O que deves ver: na página quase não se nota nada. No separador Elements, o parágrafo que abriste fecha logo antes da lista e fica vazio. Depois da lista aparece outro parágrafo vazio, que não escreveste. Repõe a lista.

5. O negrito que ficou aberto. No parágrafo de apresentação da página inicial, marca uma palavra com `<strong>` e apaga o `</strong>` que o VS Code acrescenta sozinho. Antes de olhares, prevê: até onde vai o negrito? O que deves ver: o negrito vai da palavra marcada até ao fim da página, com o rodapé. No separador Elements vês três `strong`, e só escreveste um. Escreve o `</strong>` no sítio certo.

6. Depois de desfazeres os cinco erros, faz outra vez, depressa, a verificação das ligações e da árvore do DOM da fase 7.

### Paragem 8

O `registo.md` tem cinco linhas novas, uma por erro, e as páginas voltaram a passar as verificações.

Pensa antes de continuares: qual dos cinco erros quase não mudou nada na página, e onde o descobriste? A resposta: a lista dentro do parágrafo, que só se vê no separador Elements, nos parágrafos vazios. O título que salta um nível também parece só aspeto, e descobre-se no índice dos títulos.

## Fase 9, opcional: Uma tabela de dados cruza linhas e colunas

Se o teu site tiver informação que se lê em linhas e colunas, escreves-lhe uma tabela de dados. Rever: [Uma tabela de dados cruza linhas e colunas](../02-html-e-semantica.md#uma-tabela-de-dados-cruza-linhas-e-colunas) e [Os cabeçalhos e a legenda dizem o que é cada valor](../02-html-e-semantica.md#os-cabeçalhos-e-a-legenda-dizem-o-que-é-cada-valor).

1. Aplica o teste ao teu site: há informação em que cada valor responde a uma pergunta que junta uma linha e uma coluna? Se não houver, não inventes uma tabela: escreve porquê, numa frase, num comentário no `index.html`, logo antes do `</main>`, e passa ao fim do laboratório.

2. Se houver, acrescenta a tabela à secção onde faz sentido. Escreve o `caption`, o `thead` com os cabeçalhos das colunas, e o `tbody` com uma linha por registo. Se a primeira célula de cada linha disser de que é a linha, é um `th` com `scope="row"`. No exemplo, em `torneios.html`, entre a secção do torneio do ano passado e a ligação de volta:

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

3. Guarda e recarrega. O que deves ver: a legenda por cima da tabela, e os valores arrumados em colunas, sem linhas entre as células. Na árvore de acessibilidade, o `table` tem como nome o texto da legenda.

### Paragem 9

A tabela tem legenda, cabeçalhos com `scope`, e só mostra dados. Ou o teu `index.html` tem o comentário que explica porque é que o teu site não precisa de tabela.

Pensa antes de terminares: um leitor de ecrã chega à célula "20 de março". Que duas informações dos cabeçalhos pode dizer, além da data? A resposta: "Torneio de primavera", o cabeçalho da linha, e "Data", o cabeçalho da coluna.

## Se alguma coisa falhar

1. Guardaste o ficheiro? Uma bolinha no separador do VS Code, no lugar da cruz, quer dizer que não.
2. Recarregaste a página no browser? O browser não vê as alterações sozinho.
3. O browser tem aberta a página que estás a editar? Compara o endereço na barra do browser com o nome e a pasta do ficheiro no VS Code.
4. O nome do ficheiro acaba em `.html`? No canto inferior direito do VS Code deve aparecer HTML.

### O separador mostra o nome do ficheiro em vez do título

O `title` tem um erro, ou não está dentro do `head`. Confirma que abre com `<title>`, fecha com `</title>` e está entre `<head>` e `</head>`.

### As letras acentuadas aparecem trocadas por símbolos estranhos

Aparece, por exemplo, `Ã§` no lugar de `ç`. Confirma que `<meta charset="utf-8">` é a primeira linha dentro do `head`, e que a barra de baixo do VS Code diz UTF-8. Se disser outra coisa, carrega nela, escolhe Save with Encoding e depois UTF-8.

### O esqueleto tem `lang="en"`

O esqueleto foi escrito pelo atalho `!` do VS Code. Muda para `lang="pt-PT"`.

### Uma ligação dá "Não foi possível aceder ao seu ficheiro"

O `href` não é igual ao nome do ficheiro de destino, ou a página ainda não existe. Compara, letra a letra, o endereço na barra do browser com o nome do ficheiro no painel Explorer, e corrige o `href`.

### A imagem não aparece

O `src` não corresponde ao sítio onde a imagem está. Procura uma letra trocada, uma extensão diferente, como `.jpeg` no disco e `.jpg` no código, ou a pasta `imagens/` esquecida. O separador Console diz que ficheiro o browser não encontrou.

### O separador Console não mostra nenhuma mensagem

A Console só mostra o que acontece enquanto está aberta. Com ela aberta, recarrega a página.

### A imagem aparece enorme

A fotografia tem as medidas originais, com milhares de píxeis de largura. Reduz a largura para 600 a 800 píxeis e escreve as medidas novas no `width` e no `height`.

### A página aparece em texto simples, com as etiquetas à mostra

O nome do ficheiro acaba em `.txt`. Cria os ficheiros no VS Code e, se já aconteceu, muda o nome no painel Explorer, que mostra o nome completo.

### Metade da página ficou a negrito, ou com letra de título

Falta uma etiqueta de fecho, ou falta a barra nela, como `<strong>` onde devia estar `</strong>`. Procura o último sítio onde a página estava certa.

### O VS Code não mostra cores no código

O VS Code não sabe que o ficheiro é HTML. Confirma que o nome acaba em `.html`.

### O `registo.md` aparece no painel Explorer

Ficou dentro da pasta do site. Com ele aberto, no menu File, escolhe Save As... e guarda-o na pasta de cima, com o mesmo nome. Depois apaga o que ficou na pasta do site: no painel Explorer, botão direito, Delete.

### Não encontras o `registo.md` no VS Code

O painel Explorer só mostra o que está dentro da pasta do site. No menu File, escolhe Open Recent e depois o `registo.md`, ou Open File... e vai buscá-lo à pasta onde está a pasta do teu site.

### O F12 não abre as ferramentas do programador

Em muitos portáteis, as teclas de cima fazem outras coisas. Experimenta Fn+F12 ou Ctrl+Shift+I, ou Cmd+Option+I no Mac, ou o botão direito do rato e Inspecionar.

### Não encontras o separador Accessibility

O painel ao lado da árvore está estreito. Carrega no botão `»`, ao lado dos separadores Styles e Computed, e escolhe Accessibility.

## Desafios

1. Na página inicial, acrescenta uma ligação, logo a seguir ao parágrafo de apresentação, que salte para uma das secções da mesma página. Pista: o elemento de destino precisa de um nome que nenhum outro elemento da página tenha.
2. Põe no cabeçalho das duas páginas um logótipo, ou um pequeno desenho que represente o teu site, ao lado do nome. Decide o `alt` e justifica-o num comentário logo antes do `img`. Pista: faz a pergunta do telefone, sabendo o que está escrito ao lado.
3. Numa das tuas páginas, acrescenta uma ligação para outro site, onde a pessoa encontre mais informação sobre o teu tema. Pista: o destino não está na pasta do teu site, e o texto da ligação diz o que a pessoa lá encontra.
4. Põe a imagem da segunda página num `figure`, com uma legenda que acrescente alguma coisa, como de onde vem, num `figcaption`. Pista: o `alt` diz o que a imagem mostra, e a legenda acrescenta o que toda a gente deve saber, sem se repetirem.

## Antes de terminares

- [ ] A pasta do teu site tem as duas páginas e a pasta `imagens`, com nomes em minúsculas, sem espaços e sem acentos.
- [ ] O `registo.md` está ao lado da pasta do teu site, e não dentro dela.
- [ ] As duas páginas têm o esqueleto completo, com `lang="pt-PT"` e um `title` diferente em cada uma.
- [ ] O cabeçalho, a navegação e o rodapé são iguais nas duas páginas, e cada página tem um só `h1`, sem saltos de nível a descer.
- [ ] A imagem tem o atributo `alt`, escrito com a pergunta do telefone.
- [ ] As ligações funcionam nos dois sentidos, também só com o teclado.
- [ ] O `registo.md` tem as verificações da fase 7 e as cinco linhas da fase 8, e as páginas têm os três comentários de justificação.
- [ ] Entregaste a pasta do teu site e o `registo.md` como o professor indicou.

![Rodapé](../../imagens/rodape.png)
