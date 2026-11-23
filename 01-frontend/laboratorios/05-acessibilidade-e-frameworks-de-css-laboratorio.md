![Cabeçalho](../../imagens/cabecalho.png)

# Laboratório: Acessibilidade e frameworks de CSS

## O que vais construir

Corriges os erros de acessibilidade de uma página de treino, com o Lighthouse e à mão, e fazes a mesma auditoria ao teu site. Depois, comparas três dos teus cartões com os mesmos feitos com o Bootstrap. Os exemplos são do clube de xadrez, e tu usas os teus textos.

No fim, a página de comparação do exemplo fica assim, a 1280 píxeis de largura:

```text
┌────────────────────────────────────────────────────┐
│ Clube de Xadrez                   Início  Torneios │
├────────────────────────────────────────────────────┤
│ As peças com o meu CSS e com o Bootstrap           │
│ Com o meu CSS                                      │
│ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ │
│ │ Rei: anda    │ │ Dama: anda   │ │ Torre: anda  │ │
│ └──────────────┘ └──────────────┘ └──────────────┘ │
│ Com o Bootstrap                                    │
│ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ │
│ │ Rei: anda    │ │ Dama: anda   │ │ Torre: anda  │ │
│ └──────────────┘ └──────────────┘ └──────────────┘ │
└────────────────────────────────────────────────────┘
```

1. [Fase 1: As ferramentas automáticas só ajudam](#fase-1-as-ferramentas-automáticas-só-ajudam)
2. [Fase 2: A auditoria faz-se à mão, com uma lista](#fase-2-a-auditoria-faz-se-à-mão-com-uma-lista)
3. [Fase 3: Cada ligação e cada imagem têm um nome](#fase-3-cada-ligação-e-cada-imagem-têm-um-nome)
4. [Fase 4: Um problema regista-se pelo efeito em quem usa a página](#fase-4-um-problema-regista-se-pelo-efeito-em-quem-usa-a-página)
5. [Fase 5: O ARIA só entra quando o HTML não chega](#fase-5-o-aria-só-entra-quando-o-html-não-chega)
6. [Fase 6: Um framework de CSS traz regras já escritas](#fase-6-um-framework-de-css-traz-regras-já-escritas)
7. [Fase 7: A ordem das folhas de estilos decide os conflitos](#fase-7-a-ordem-das-folhas-de-estilos-decide-os-conflitos)
8. [Fase 8: Um framework tem vantagens e custos](#fase-8-um-framework-tem-vantagens-e-custos)

## O que precisas

- O VS Code, e o Chrome ou o Edge com as ferramentas do programador.
- O Python 3, de Fundamentos de Programação: a resposta de `python --version`, ou `py --version` no Windows e `python3 --version` no macOS, começa por `Python 3.`.
- A pasta do teu site, no GitHub, com a lista da classe `cartoes`, e o `registo.md` ao lado dela. Se não acabaste o laboratório 04, faz este na mesma: só precisas da lista do laboratório 03.
- Internet, nas fases 6 a 8.

## Preparar o projeto

1. No VS Code, abre a pasta do teu site e um terminal. Corre primeiro o `git pull`, com a tua frase-passe, como em todas as aulas. O que deves ver: `Already up to date.`, ou os commits que vieram do GitHub.

2. Corre o `git status`. A última linha da resposta deve ser `nothing to commit, working tree clean`.

3. No menu File, em Open Recent, abre o teu `registo.md`. Confirma o caminho, porque o portátil pode ter o de outro colega. Escreve no fim o título `## Laboratório da acessibilidade` e guarda.

4. Ao lado da pasta do teu site, e não dentro dela, cria a pasta `pagina-de-treino`. Copia para lá os três ficheiros do [código de partida](05-acessibilidade-e-frameworks-de-css-laboratorio/README.md), como diz o README dele: `index.html`, `estilos.css` e `logotipo.svg`.

5. Abre a página de treino numa janela nova do VS Code. No menu File, escolhe New Window, e na janela nova, Open Folder, com a pasta `pagina-de-treino`. O que deves ver: duas janelas do VS Code, uma do site e outra da página de treino.

## Fase 1: As ferramentas automáticas só ajudam

Ligas um servidor local na pasta da página de treino e analisas a página com o Lighthouse. Rever: [As ferramentas automáticas só ajudam](../05-acessibilidade-e-frameworks-de-css.md#as-ferramentas-automáticas-só-ajudam) e [Um servidor local serve uma pasta por HTTP](../05-acessibilidade-e-frameworks-de-css.md#um-servidor-local-serve-uma-pasta-por-http).

1. Na janela da página de treino, abre um terminal, no menu Terminal, com New Terminal. Liga o servidor local:

   ```bash
   python -m http.server 8000 --bind 127.0.0.1
   ```

   No Windows, se o terminal não conhecer o `python`, escreve `py` no lugar dele; no macOS, `python3`. O que deves ver: `Serving HTTP on 127.0.0.1 port 8000 (http://127.0.0.1:8000/) ...`. O terminal fica ocupado com o servidor: deixa-o assim até ao fim da fase 3. Se aparecer outra coisa, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

2. No browser, abre o endereço `http://127.0.0.1:8000`. O que deves ver: a página de um clube de xadrez, com o logótipo, o menu "Encontros", "Torneio" e "Regras", e três secções. No terminal aparece uma linha com `GET` para cada ficheiro que o browser pediu. Uma delas, a do `favicon.ico`, tem o código 404: é o ícone do separador, que esta página não tem, e não faz mal.

3. Abre as ferramentas do programador, com F12, ou Cmd+Option+I no Mac. No separador Network, marca a caixa Disable cache e deixa as ferramentas abertas até ao fim da fase 3. Assim, quando mudares um ficheiro e recarregares, o browser vai buscá-lo outra vez ao servidor, em vez de usar a cópia que guardou.

4. Antes de analisares a página, prevê: ela tem cinco erros de acessibilidade, e quantos vai o Lighthouse encontrar? Abre o separador Lighthouse, que pode estar escondido atrás do botão `»`. Nas categorias, deixa marcada só a Accessibility e carrega em Analyze page load. O que deves ver: ao fim de uns segundos, um relatório com uma pontuação num círculo, abaixo de 100. Por baixo, a lista dos problemas, com os nomes em inglês. São três:

   - `Background and foreground colors do not have a sufficient contrast ratio.`: o contraste de um texto com o fundo;
   - `Links do not have a discernible name`: uma ligação sem nome;
   - `Heading elements are not in a sequentially-descending order`: um salto nos títulos.

   Carrega em cada problema, para veres o elemento da página que o tem. A resposta à previsão: o Lighthouse encontrou três dos cinco erros.

5. No `registo.md`, que está aberto na janela do teu site, escreve o título `### Página de treino` e, por baixo, o que o Lighthouse encontrou. No exemplo:

   ```text
   Lighthouse: a frase de destaque não tem contraste suficiente.
   Lighthouse: a ligação do logótipo não tem nome.
   Lighthouse: os títulos saltam do h1 para o h4.
   ```

### Paragem 1

A página de treino está a ser servida pelo servidor local, e o Lighthouse encontrou três dos cinco erros.

Pensa antes de continuares: porque é que foi preciso ligar o servidor local? A resposta: o Lighthouse só analisa páginas que chegam por HTTP. Com duplo clique, o browser lê a página do disco, e o endereço começa por `file://`.

## Fase 2: A auditoria faz-se à mão, com uma lista

Fazes a lista das oito verificações na página de treino, encontras os dois erros que faltam e corriges os três que já sabes corrigir. Rever: [A auditoria faz-se à mão, com uma lista](../05-acessibilidade-e-frameworks-de-css.md#a-auditoria-faz-se-à-mão-com-uma-lista).

1. Teclado e foco. No browser, carrega numa zona vazia do cabeçalho verde, para o Tab começar daí. Depois carrega duas vezes em Tab e uma vez em Enter. O que deves ver: nenhuma ligação ganhou uma moldura, mas o endereço passou a acabar em `#encontros`. O foco andou até à ligação "Encontros", e quem usa o teclado não o viu.

2. Encontra a causa. No VS Code, em `estilos.css`, procura a palavra `outline`, com Ctrl+F, ou Cmd+F no Mac. O que deves ver: a regra `a:focus` com `outline: none;` e o comentário "A moldura do foco parecia feia, e por isso tirou-se.".

3. Nomes. Em `index.html`, lê o texto de cada ligação como se estivesse sozinho, fora da frase. O que deves ver: "Encontros", "Torneio" e "Regras" dizem para onde levam, mas "clica aqui" não diz nada. O logótipo tem `alt=""`, e a ligação dele fica sem texto: é o erro que o Lighthouse já encontrou.

4. Títulos, contraste e cor. No separador Elements, vê os títulos: a seguir ao `h1` vêm três `h4`. Depois, carrega no parágrafo da frase de destaque, por baixo do `h1`. No separador Styles, carrega no quadrado colorido ao lado de `color: #a8a8a8`. O que deves ver: na linha Contrast ratio da janela de escolher cores, o número 2.11, com um sinal de que não chega. Os títulos e o contraste são erros que o Lighthouse já encontrou. As ligações estão sublinhadas, e a cor passa.

5. Idioma e localização, e zoom. Em `index.html`, confirma que o `html` tem `lang="pt-PT"` e que há um `title`. O menu leva a partes da mesma página, e por isso não tem página atual. Carrega cinco vezes em Ctrl e na tecla +, ou Cmd e + no Mac, até o browser mostrar 200%. Volta com Ctrl e 0, ou Cmd e 0. O que deves ver: estas duas verificações passam.

6. No `registo.md`, por baixo das linhas do Lighthouse, escreve os dois erros que encontraste à mão:

   ```text
   À mão: o foco não se vê, porque a regra a:focus tem outline: none.
   À mão: a ligação "clica aqui" não diz para onde leva.
   ```

7. Corrige o foco, com as regras do tema 03. Em `estilos.css`, substitui a regra `a:focus` e o comentário dela por:

   ```css
   /* O foco do teclado bem visível, afastado da ligação. */
   a:focus-visible {
     outline: 3px solid var(--cor-principal);
     outline-offset: 2px;
   }

   /* No cabeçalho, o fundo é da cor principal: a moldura passa a branca. */
   header a:focus-visible {
     outline-color: #ffffff;
   }
   ```

8. Corrige os títulos. Em `index.html`, troca os três `h4` por `h2`, na etiqueta de abertura e na de fecho. Em `estilos.css`, na regra dos títulos, troca o seletor `h1, h4` por `h1, h2`.

9. Corrige o contraste. Em `estilos.css`, na regra `.destaque`, troca a cor e o comentário:

   ```css
   /* A frase de destaque, em cinzento-escuro: 6,61 de contraste com o fundo. */
   .destaque {
     color: #555555;
     font-size: 1.25rem;
   }
   ```

   Guarda os dois ficheiros e recarrega a página, com F5, ou Cmd+R no Mac. O que deves ver: com o Tab, a moldura branca no logótipo e no menu, e verde no "clica aqui". Os títulos das secções ficam maiores e verdes, e a frase de destaque mais escura. Na janela de escolher cores, o contraste dela passa a 6.61.

### Paragem 2

A página de treino tem o foco visível, os títulos sem saltos e a frase de destaque com contraste. Faltam o logótipo e o "clica aqui".

Pensa antes de continuares: dos cinco erros, qual impede mais quem só usa o teclado? A resposta: o foco invisível. Os outros dificultam a leitura, mas sem a moldura essa pessoa não sabe onde está, nem onde vai carregar no Enter.

## Fase 3: Cada ligação e cada imagem têm um nome

Vês o nome acessível do logótipo e da ligação "clica aqui", no separador Accessibility, e corriges os dois. Rever: [Cada ligação e cada imagem têm um nome](../05-acessibilidade-e-frameworks-de-css.md#cada-ligação-e-cada-imagem-têm-um-nome).

1. No separador Elements, abre o `header` e carrega no `a` do logótipo. Ao lado do Styles, abre o separador Accessibility, que pode estar atrás do botão `»`. O que deves ver: na secção Computed Properties, a linha Role diz `link`, e a linha Name não tem nenhum nome.

2. Em `index.html`, no `img` do logótipo, troca o `alt` vazio por um que diga para onde a ligação leva. O `alt` vazio diz que a imagem é decorativa, mas aqui ela é a única coisa dentro da ligação:

   ```html
   <a href="index.html"><img src="logotipo.svg" alt="Clube de Xadrez, página inicial" width="48" height="48"></a>
   ```

   Guarda, recarrega e volta a carregar no `a` do logótipo. O que deves ver: na linha Name, "Clube de Xadrez, página inicial".

3. Carrega no `a` do "clica aqui". O que deves ver: o nome é "clica aqui". Tem nome, mas não diz para onde leva. Em `index.html`, substitui o parágrafo do torneio por este, em que o texto da ligação é o destino:

   ```html
   <p>As inscrições estão abertas até ao fim do mês. Antes de te inscreveres, lê <a href="#regras">as regras do torneio</a>.</p>
   ```

   Guarda e recarrega. O que deves ver: o nome da ligação passa a "as regras do torneio".

4. Analisa outra vez a página com o Lighthouse. No separador Lighthouse, carrega no botão com o sinal +, no canto de cima, e depois em Analyze page load. O que deves ver: os três problemas da fase 1 já não aparecem na lista.

5. No terminal da página de treino, para o servidor com Ctrl+C. O que deves ver: `Keyboard interrupt received, exiting.`, e o terminal volta a aceitar comandos.

6. No `registo.md`, acrescenta uma linha com o resultado:

   ```text
   Corrigi os cinco erros. O Lighthouse encontrou três, e eu encontrei mais dois à mão: o foco e o "clica aqui".
   ```

### Paragem 3

A página de treino não tem nenhum dos cinco erros, e o servidor está parado. Podes fechar a janela do VS Code da página de treino.

Pensa antes de continuares: porque é que o Lighthouse não encontrou o "clica aqui"? A resposta: a ligação tinha nome, e o Lighthouse só verifica se há um nome. Só uma pessoa consegue julgar se o nome diz para onde a ligação leva.

## Fase 4: Um problema regista-se pelo efeito em quem usa a página

Fazes a mesma auditoria a todas as páginas do teu site, registas cada problema com as quatro coisas e corriges o que encontraste. Rever: [Um problema regista-se pelo efeito em quem usa a página](../05-acessibilidade-e-frameworks-de-css.md#um-problema-regista-se-pelo-efeito-em-quem-usa-a-página).

1. Volta à janela do VS Code do teu site. Abre a página inicial no browser, com duplo clique no `index.html`, no Explorador de Ficheiros, ou no Finder do Mac. Para as verificações à mão, não precisas de servidor.

2. No `registo.md`, escreve o título `### O meu site`. Faz as oito verificações da fase 2 em todas as páginas do teu site e escreve uma linha por verificação. No exemplo do clube de xadrez:

   ```text
   Teclado: passou, nas duas páginas.
   Foco: passou. A moldura é branca no cabeçalho e verde no resto.
   Nomes: passou. A imagem dos torneios tem alt, e as ligações dizem para onde levam.
   Títulos: passou. Um h1 por página, e as secções com h2.
   Contraste: passou. O mais baixo são os títulos verdes, com 8,09.
   Cor: passou. A ligação de volta, no texto, está sublinhada.
   Idioma e localização: falhou uma parte. O menu não diz em que página estou.
   Zoom: passou.
   ```

   Os teus resultados podem ser diferentes, porque o teu site tem os teus textos, as tuas cores e as tuas imagens.

3. Por baixo, regista cada problema que encontraste com quatro linhas. São "O que falha e onde", "Quem fica sem conseguir o quê", "A causa" e "A correção e como se confirmou". Escreve já as três primeiras, e a quarta depois de corrigires. No exemplo, o problema do menu:

   ```text
   O que falha e onde: no menu das duas páginas, a ligação da página onde estou é igual à outra.
   Quem fica sem conseguir o quê: quem usa um leitor de ecrã ouve "Início, ligação" e não sabe se já está nessa página.
   A causa: o HTML não tem nenhum elemento para dizer qual é a página atual.
   ```

4. Corrige cada problema que encontraste, menos o do menu, que corriges na fase 5, com o ARIA. Usa o que fizeste na página de treino e nos temas 02 e 03. Depois de cada correção, volta a fazer a verificação que falhou e escreve a quarta linha do problema. No exemplo do clube de xadrez, o menu é o único problema.

5. Se corrigiste algum problema, guarda as correções num commit. No `git add`, escreve os nomes dos ficheiros que mudaste:

   ```bash
   git add index.html estilos.css
   git diff --staged
   git commit -m "Corrige os problemas da auditoria de acessibilidade"
   ```

   O que deves ver: no `git diff --staged`, as tuas correções com `+`. Se a resposta aparecer aos bocados, sai com a tecla `q`. No commit, o número de ficheiros que mudaste.

### Paragem 4

O `registo.md` tem as oito verificações do teu site e cada problema que encontraste, com as quatro linhas. Só o problema do menu ficou por corrigir.

Pensa antes de continuares: porque é que a segunda linha diz quem fica sem conseguir o quê, e não só a regra que falhou? A resposta: é ela que mostra o efeito na pessoa que usa a página, e o que essa pessoa ganha com a correção.

## Fase 5: O ARIA só entra quando o HTML não chega

O menu do teu site passa a dizer em que página estás, para quem ouve e para quem vê. Rever: [O ARIA só entra quando o HTML não chega](../05-acessibilidade-e-frameworks-de-css.md#o-aria-só-entra-quando-o-html-não-chega) e [O seletor de atributo escolhe pelo valor de um atributo](../05-acessibilidade-e-frameworks-de-css.md#o-seletor-de-atributo-escolhe-pelo-valor-de-um-atributo).

1. Em cada página do teu site, acrescenta o `aria-current="page"` à ligação do menu que leva a essa mesma página. No exemplo, em `index.html`, é a ligação "Início":

   ```html
   <!-- O aria-current diz ao leitor de ecrã que esta é a página onde se está. -->
   <li><a href="index.html" aria-current="page">Início</a></li>
   ```

   Em `torneios.html`, é a ligação "Torneios". Numa página que não esteja no menu, nenhuma ligação leva o atributo.

2. Guarda e recarrega a página inicial. O que deves ver: nada muda no ecrã. No separador Elements, carrega na ligação "Início" e abre o separador Accessibility. Na secção ARIA Attributes aparece `aria-current: page`. Isto quer dizer que o leitor de ecrã já sabe qual é a página atual, mas quem vê ainda não tem nenhum sinal.

3. Em `estilos.css`, a seguir à regra `header a`, acrescenta a regra que mostra a página atual a quem vê:

   ```css
   /* A ligação da página onde se está, a negrito. O seletor de atributo
      escolhe só as ligações do menu com aria-current="page". */
   nav a[aria-current="page"] {
     font-weight: bold;
   }
   ```

   Guarda e recarrega. O que deves ver: "Início" a negrito na página inicial. Vai à outra página pelo menu: lá, é a outra ligação que fica a negrito.

4. No `registo.md`, escreve a quarta linha do problema do menu. No exemplo:

   ```text
   A correção e como se confirmou: aria-current="page" na ligação da página atual e uma regra que a põe a negrito. No separador Accessibility aparece aria-current: page.
   ```

5. Guarda o passo num commit, com os nomes das tuas páginas:

   ```bash
   git add index.html torneios.html estilos.css
   git diff --staged
   git commit -m "Mostra no menu a página atual"
   ```

   O que deves ver: no exemplo, `3 files changed`, no fim da resposta do commit. Do `git diff --staged` sais com a tecla `q`, se for preciso.

### Paragem 5

Em cada página, o menu mostra a página atual a negrito, e o separador Accessibility mostra `aria-current: page` na ligação dela.

Pensa antes de continuares: porque é que a regra de CSS escolhe o atributo `aria-current`, e não uma classe nova? A resposta: assim, o sinal para quem vê e o sinal para quem ouve vêm do mesmo atributo. Se mudares a página atual, mudam os dois, e nunca ficam diferentes.

## Fase 6: Um framework de CSS traz regras já escritas

Crias no teu site uma página de comparação, com três dos teus cartões feitos com o teu CSS e com o Bootstrap. Rever: [Um framework de CSS traz regras já escritas](../05-acessibilidade-e-frameworks-de-css.md#um-framework-de-css-traz-regras-já-escritas) e [As classes do framework vêm da documentação](../05-acessibilidade-e-frameworks-de-css.md#as-classes-do-framework-vêm-da-documentação).

1. Na pasta do teu site, cria `comparacao-bootstrap.html` com esta primeira versão. Troca o nome do site, as ligações do menu e os três cartões pelos teus, copiados do teu `index.html`. Tira o `aria-current`, porque esta página não está no menu.

   ```html
   <!doctype html>
   <!-- Página de comparação: três peças com o meu CSS e com o Bootstrap.
        Não está no menu, porque não faz parte do site: serve só para comparar. -->
   <html lang="pt-PT">
     <head>
       <meta charset="utf-8">
       <meta name="viewport" content="width=device-width, initial-scale=1">
       <title>Comparação com o Bootstrap | Clube de Xadrez</title>
       <link rel="stylesheet" href="estilos.css">
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
         <h1>As peças com o meu CSS e com o Bootstrap</h1>

         <section>
           <h2>Com o meu CSS</h2>
           <ul class="cartoes">
             <li>Rei: anda uma casa, em qualquer direção.</li>
             <li>Dama: anda as casas que quiser, em qualquer direção.</li>
             <li>Torre: anda em linha reta, na horizontal ou na vertical.</li>
           </ul>
         </section>
       </main>
       <footer>
         <p>Site do Clube de Xadrez, feito na disciplina de Desenvolvimento de Aplicações. Conteúdo fictício.</p>
       </footer>
     </body>
   </html>
   ```

   Abre a página no browser, com duplo clique. O que deves ver: o cabeçalho e o rodapé do teu site, e três cartões, como na página inicial.

2. No `head`, antes da linha do `estilos.css`, cola a linha do CSS do Bootstrap. É a mesma da documentação oficial, na página Introduction, no passo 2 do Quick start:

   ```html
   <!-- O CSS do Bootstrap 5.3.9, do jsDelivr. O integrity é a impressão digital do ficheiro. -->
   <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.9/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-yEPZ7jP9S0QKiUQ0m3jjsO4ProIW7wvR9gXkI7JOGa2XVsw53Yke2bsdkBbjmmiX" crossorigin="anonymous">
   ```

   Guarda e recarrega. O que deves ver: os títulos ficam menos grossos e mudam de tamanho, e alguns espaços entre os elementos mudam. O fundo e as cores continuam os do teu site. Isto quer dizer que o CSS do Bootstrap chegou à página.

3. No `main`, a seguir à secção "Com o meu CSS", acrescenta a secção com os mesmos três cartões, com as classes do Bootstrap:

   ```html
   <section>
     <h2>Com o Bootstrap</h2>
     <!-- row e g-3: uma linha da grelha do Bootstrap, com 1rem entre os cartões.
          list-unstyled: a lista sem bolinhas nem recuo. Continua a ser uma lista. -->
     <ul class="row g-3 list-unstyled">
       <!-- col-sm-6: meia linha a partir de 576 píxeis. col-lg-4: um terço a partir de 992.
            card e card-body: a caixa do cartão e o espaço por dentro.
            h-100: o cartão ocupa a altura toda da coluna. -->
       <li class="col-sm-6 col-lg-4">
         <div class="card h-100">
           <div class="card-body">Rei: anda uma casa, em qualquer direção.</div>
         </div>
       </li>
       <li class="col-sm-6 col-lg-4">
         <div class="card h-100">
           <div class="card-body">Dama: anda as casas que quiser, em qualquer direção.</div>
         </div>
       </li>
       <li class="col-sm-6 col-lg-4">
         <div class="card h-100">
           <div class="card-body">Torre: anda em linha reta, na horizontal ou na vertical.</div>
         </div>
       </li>
     </ul>
   </section>
   ```

   Guarda e recarrega. Abre a barra de dispositivos, com Ctrl+Shift+M, ou Cmd+Shift+M no Mac, e põe a largura em 1280. O que deves ver: os cartões do Bootstrap quase iguais aos teus, três lado a lado, com a mesma largura.

4. Põe a largura em 320. O que deves ver: nas duas secções, um cartão por linha. Antes de passares para 900, prevê: quantas colunas tem cada grelha? Depois, põe a largura em 900. O que deves ver, no exemplo: os teus cartões em três colunas, e os do Bootstrap em duas. A tua grelha muda quando cabe mais um cartão de 15rem, e a do Bootstrap nos pontos dele, 576 e 992 píxeis.

5. Guarda o passo num commit:

   ```bash
   git add comparacao-bootstrap.html
   git commit -m "Acrescenta a página de comparação com o Bootstrap"
   ```

   O que deves ver: `1 file changed`, no fim da resposta do commit.

### Paragem 6

A página de comparação mostra três cartões com o teu CSS e os mesmos três com o Bootstrap. O ficheiro `comparacao-bootstrap.html` do exemplo, como deve estar agora:

```html
<!doctype html>
<!-- Página de comparação: três peças com o meu CSS e com o Bootstrap.
     Não está no menu, porque não faz parte do site: serve só para comparar. -->
<html lang="pt-PT">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Comparação com o Bootstrap | Clube de Xadrez</title>
    <!-- O CSS do Bootstrap 5.3.9, do jsDelivr. O integrity é a impressão digital do ficheiro. -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.9/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-yEPZ7jP9S0QKiUQ0m3jjsO4ProIW7wvR9gXkI7JOGa2XVsw53Yke2bsdkBbjmmiX" crossorigin="anonymous">
    <link rel="stylesheet" href="estilos.css">
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
      <h1>As peças com o meu CSS e com o Bootstrap</h1>

      <section>
        <h2>Com o meu CSS</h2>
        <ul class="cartoes">
          <li>Rei: anda uma casa, em qualquer direção.</li>
          <li>Dama: anda as casas que quiser, em qualquer direção.</li>
          <li>Torre: anda em linha reta, na horizontal ou na vertical.</li>
        </ul>
      </section>

      <section>
        <h2>Com o Bootstrap</h2>
        <!-- row e g-3: uma linha da grelha do Bootstrap, com 1rem entre os cartões.
             list-unstyled: a lista sem bolinhas nem recuo. Continua a ser uma lista. -->
        <ul class="row g-3 list-unstyled">
          <!-- col-sm-6: meia linha a partir de 576 píxeis. col-lg-4: um terço a partir de 992.
               card e card-body: a caixa do cartão e o espaço por dentro.
               h-100: o cartão ocupa a altura toda da coluna. -->
          <li class="col-sm-6 col-lg-4">
            <div class="card h-100">
              <div class="card-body">Rei: anda uma casa, em qualquer direção.</div>
            </div>
          </li>
          <li class="col-sm-6 col-lg-4">
            <div class="card h-100">
              <div class="card-body">Dama: anda as casas que quiser, em qualquer direção.</div>
            </div>
          </li>
          <li class="col-sm-6 col-lg-4">
            <div class="card h-100">
              <div class="card-body">Torre: anda em linha reta, na horizontal ou na vertical.</div>
            </div>
          </li>
        </ul>
      </section>
    </main>
    <footer>
      <p>Site do Clube de Xadrez, feito na disciplina de Desenvolvimento de Aplicações. Conteúdo fictício.</p>
    </footer>
  </body>
</html>
```

O `head` liga primeiro o Bootstrap e depois a tua folha. As duas secções do `main` têm o mesmo conteúdo: a primeira com a tua classe `cartoes`, a segunda com as classes do Bootstrap.

Pensa antes de continuares: porque é que a secção do Bootstrap usa `ul` e `li`, e não `div`? A resposta: os cartões são uma lista. Com o `ul`, o leitor de ecrã anuncia uma lista de três itens, no Chrome e no Edge, e o framework só muda o aspeto.

## Fase 7: A ordem das folhas de estilos decide os conflitos

Provocas um conflito de propósito, com o Bootstrap depois da tua folha, e encontras no separador Styles a regra que ganhou. Rever: [A ordem das folhas de estilos decide os conflitos](../05-acessibilidade-e-frameworks-de-css.md#a-ordem-das-folhas-de-estilos-decide-os-conflitos).

1. Provoca o conflito. No `head` de `comparacao-bootstrap.html`, corta a linha do Bootstrap, com o comentário, e cola-a depois da linha do `estilos.css`. Guarda e recarrega. O que deves ver, no exemplo: o fundo da página fica branco, e os títulos perdem a cor do site.

2. No separador Elements, carrega no `body`. No separador Styles, procura a tua regra `body`. O que deves ver: a tua `background-color` riscada. Mais acima está a regra `body` que ganhou, com `background-color: var(--bs-body-bg)`. À direita dela, está o nome de um ficheiro do Bootstrap, como `_reboot.scss` ou `bootstrap.min.css`. As duas regras têm a mesma especificidade, e ganha a que vem depois.

3. Carrega no `h1`. O que deves ver: a tua `color` riscada, e por cima uma regra do Bootstrap para os seis níveis de títulos, de `h1` a `h6`.

4. Desfaz o conflito: volta a pôr a linha do Bootstrap, com o comentário, antes da do `estilos.css`. Guarda e recarrega. O que deves ver: o fundo e a cor dos títulos do teu site outra vez.

5. Corre o `git status`. O que deves ver: `nothing to commit, working tree clean`, porque o ficheiro voltou a ser igual ao do último commit. Se aparecer `modified: comparacao-bootstrap.html`, a linha não voltou ao sítio exato. Corre `git restore comparacao-bootstrap.html`, que devolve o ficheiro ao último commit.

### Paragem 7

A tua folha de estilos vem depois do Bootstrap, e nos conflitos com seletores iguais ganham as tuas regras.

Pensa antes de continuares: com o Bootstrap depois da tua folha, as ligações do cabeçalho continuaram brancas. Porquê? A resposta: a tua regra `header a` tem dois elementos no seletor, e a regra `a` do Bootstrap tem só um. Com especificidades diferentes, ganha a mais específica, venha antes ou depois.

## Fase 8: Um framework tem vantagens e custos

Vês o tamanho e a dependência das duas versões, personalizas os cartões do Bootstrap e registas a comparação. Rever: [Um framework tem vantagens e custos](../05-acessibilidade-e-frameworks-de-css.md#um-framework-tem-vantagens-e-custos).

1. Tamanho. Na página de comparação, abre o separador Network, marca a caixa Disable cache, se não estiver marcada, e recarrega. Sem a cache, o browser volta a pedir todos os ficheiros. O que deves ver: uma linha para cada ficheiro, com o tamanho na coluna Size. O `bootstrap.min.css` tem cerca de 23 kB, porque o jsDelivr o envia comprimido, e o teu `estilos.css` poucos kB. Na barra de baixo, o valor de "resources" passa dos 230 kB, quase todo do Bootstrap descomprimido.

2. Dependência. Com o Disable cache ainda marcado, escolhe Offline no menu que diz No throttling, e recarrega a página. O que deves ver: a linha do `bootstrap.min.css` a vermelho, com o pedido falhado. Os cartões do Bootstrap ficam uma lista simples, com bolinhas e sem bordas, e os teus não mudam. Volta a pôr No throttling, tira a marca do Disable cache e recarrega.

3. Personalização. Em `estilos.css`, a seguir à regra `.cartoes li`, acrescenta:

   ```css
   /* Na página de comparação, os cartões do Bootstrap com a borda dos meus cartões.
      A --bs-card-border-color é a variável do Bootstrap para a cor da borda. */
   .card {
     --bs-card-border-color: var(--cor-borda);
   }
   ```

   Guarda e recarrega. O que deves ver: a borda dos cartões do Bootstrap com a cor da borda dos teus. No separador Styles, com um `.card` escolhido, a tua regra aparece por cima da do Bootstrap.

4. No `registo.md`, escreve o título `### O meu CSS e o Bootstrap` e quatro linhas: a dependência, o tamanho, a personalização e quando usarias um framework. No exemplo:

   ```text
   Dependência: o Bootstrap vem do jsDelivr. Sem Internet, os cartões dele ficam uma lista simples, e os meus não mudam.
   Tamanho: o Bootstrap tem cerca de 23 kB pela rede e mais de 230 kB descomprimido. O meu estilos.css tem poucos kB.
   Personalização: mudei a borda dos cartões do Bootstrap com a variável --bs-card-border-color, da documentação do Bootstrap.
   Quando usar: num site grande, feito por uma equipa com pouco tempo. No meu site, o meu CSS chega e funciona sem Internet.
   ```

5. Guarda o passo num commit e envia o trabalho para o GitHub:

   ```bash
   git add estilos.css
   git commit -m "Personaliza a borda dos cartões do Bootstrap"
   git status
   git log --oneline -4
   git push
   ```

   O que deves ver: o `git status` diz que estás à frente do `origin/main`, com um commit por cada fase em que guardaste alterações. No exemplo, são 3. O `git log` mostra os commits deste laboratório. O `git push` pede a frase-passe, e a última linha tem `main -> main`.

### Paragem 8

O teu site tem o menu com a página atual e a página de comparação, e está no GitHub. O `registo.md` tem a auditoria da página de treino, a do teu site e a comparação com o Bootstrap.

Pensa antes de continuares: que limitação do Bootstrap viste neste laboratório, que o teu CSS não tem? A resposta: sem Internet, os cartões do Bootstrap perdem o aspeto, porque o CSS dele vem de outro servidor. O teu `estilos.css` vai com o site.

## Se alguma coisa falhar

Primeiro, três verificações rápidas:

1. Estás na janela certa do VS Code? As fases 1 a 3 são na janela da página de treino, menos o `registo.md`, que fica na janela do teu site. As fases 4 a 8 são na do teu site.
2. Guardaste o ficheiro? No VS Code, o separador de um ficheiro por guardar mostra uma bolinha.
3. Recarregaste a página? Depois de guardar, carrega em F5, ou Cmd+R no Mac. Se continuar igual, carrega em Ctrl+F5, ou Cmd+Shift+R no Mac, que obriga o browser a ler os ficheiros outra vez.

### O terminal não conhece o python, ou abre a Microsoft Store

No Windows, fecha a loja e experimenta o mesmo comando com `py` no lugar de `python`. No macOS, usa `python3`. Usa o comando que funciona em Fundamentos de Programação.

### O servidor diz Address already in use

A porta 8000 está ocupada por outro programa. No Windows, a mensagem fala de `WinError 10048`. Liga o servidor noutra porta, como 8001, e abre `http://127.0.0.1:8001`.

### A página não abre em http://127.0.0.1:8000

O servidor não está a correr. Confirma no terminal da página de treino que a última linha é a do `Serving HTTP`. Se o terminal estiver a aceitar comandos, liga o servidor outra vez, na pasta `pagina-de-treino`.

### Os títulos ficaram maiores, mas pretos, e a frase continua clara

O browser usou a cópia antiga do `estilos.css`, que tinha guardado, e só o `index.html` veio novo. Com as ferramentas do programador abertas, confirma que a caixa Disable cache, do separador Network, está marcada. Depois, recarrega com Ctrl+F5, ou Cmd+Shift+R no Mac.

### O git diff fica parado, com dois pontos ou com (END) no fim

A resposta é comprida e aparece aos bocados. Carrega na tecla `q` para sair.

### O separador Lighthouse não deixa analisar a página

A página foi aberta com duplo clique, e o endereço começa por `file://`. Abre-a pelo endereço do servidor local, `http://127.0.0.1:8000`.

### O separador Accessibility não aparece

Fica ao lado do Styles, no separador Elements, e pode estar escondido atrás do botão `»`. Se as ferramentas estiverem estreitas, alarga-as, arrastando a margem delas.

### Os cartões do Bootstrap aparecem como uma lista simples

O CSS do Bootstrap não chegou à página. Confirma que tens Internet e que o Offline não ficou escolhido no separador Network. Se a consola mostrar `Failed to find a valid digest in the 'integrity' attribute`, a linha do Bootstrap não foi copiada inteira: copia-a outra vez.

### O git pull ou o git push pedem a frase-passe e falham

É a frase-passe da chave SSH que criaste no tema 02 do Git. As soluções estão no "Se alguma coisa falhar" do [laboratório desse tema](../../02-git/laboratorios/02-partilhar-versoes-com-o-github-laboratorio.md#se-alguma-coisa-falhar).

## Desafios

1. Na página de comparação, acrescenta uma ligação para a página inicial com o aspeto de um botão do Bootstrap, com as classes `btn` e `btn-primary`. Faz-lhe as verificações do foco e do contraste, e escreve no `registo.md` o que encontraste. Pista: compara a moldura do foco desta ligação com a das outras ligações do teu site.
2. Na barra de dispositivos, encontra a largura a partir da qual cada grelha da página de comparação passa de uma para duas colunas. Escreve as duas larguras no `registo.md` e explica porque são diferentes.

## Antes de terminares

- [ ] A página de treino tem o foco visível, os títulos sem saltos, o contraste certo, o `alt` no logótipo e nenhum "clica aqui".
- [ ] O `registo.md` tem o que o Lighthouse encontrou na página de treino e os dois erros que encontraste à mão.
- [ ] O `registo.md` tem as oito verificações do teu site, e cada problema com as quatro linhas.
- [ ] Em cada página do teu site, o menu mostra a página atual, com `aria-current="page"` e a negrito.
- [ ] A página de comparação tem três cartões com o teu CSS e os mesmos três com o Bootstrap.
- [ ] No `head` da página de comparação, a tua folha vem depois da do Bootstrap.
- [ ] O `registo.md` tem a comparação: a dependência, o tamanho, a personalização e quando usarias um framework.
- [ ] O site está no GitHub, com os commits deste laboratório.

![Rodapé](../../imagens/rodape.png)
