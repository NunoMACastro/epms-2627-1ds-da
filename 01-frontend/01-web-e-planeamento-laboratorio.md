![Cabeçalho](../imagens/cabecalho.png)

# Laboratório: A Web, os utilizadores e o planeamento

Laboratório do tema A Web, os utilizadores e o planeamento, do módulo Conceber aplicações para a web na vertente frontend. Vais abrir as ferramentas do programador pela primeira vez e usá-las para ver por dentro como uma página chega ao teu ecrã. Cada passo diz o que fazer, porquê e o que deves ver, e avanças ao teu ritmo. O que não acabares na aula, acabas na aula seguinte. Tudo o que precisas está aqui; o [guia do tema](01-web-e-planeamento.md) tem a teoria completa, para quem quiser saber mais.

## O que vais construir

Neste laboratório não vais escrever código. Vais observar páginas por dentro e fazer experiências com elas. O que constróis é uma tabela de registo, no caderno, com oito observações. Cada observação é a prova de uma ideia sobre a Web.

No fim, sabes abrir as ferramentas do programador e encontrar na árvore de uma página qualquer parte dela. Sabes também mostrar que mudar essa árvore não muda o ficheiro, e ver os pedidos que uma página faz.

| Fase | O que fazes | O que fica provado no fim |
| --- | --- | --- |
| 1 | Abres a Estante Digital a partir do teu disco | Uma página do teu disco não vem de um servidor |
| 2 | Abres o separador Elements | Cada parte da página tem um ramo na árvore do DOM |
| 3 | Mudas o título no DOM, vês o ficheiro e recarregas | Mudar o DOM não muda o ficheiro |
| 4 | Visitas o primeiro site da história | O browser acrescenta ao DOM o que falta no ficheiro |
| 5 | Segues um pedido no separador Network e provocas um 404 | Cada pedido tem um método e uma resposta com um código |
| 6 | Contas os pedidos de uma página de hoje | Uma página de hoje faz muitos pedidos |

## Palavras que vais usar

- Browser: o programa que pede as páginas, lê os ficheiros e desenha a página no ecrã. Neste laboratório usas o Chrome ou o Edge. Para saber mais, vê a secção "O browser" do [guia](01-web-e-planeamento.md).
- HTML, CSS e JavaScript: as três linguagens de uma página. O HTML diz o que cada pedaço do conteúdo é, o CSS diz como se apresenta, e o JavaScript diz como se comporta.
- Ficheiro: o texto de uma página, guardado no disco, tal como alguém o escreveu num editor.
- DOM: a árvore que o browser constrói em memória a partir do ficheiro, com um ramo para cada parte da página. É a partir dela que a página é desenhada. Para saber mais, vê a secção "O ficheiro e o DOM" do [guia](01-web-e-planeamento.md).
- Elemento: cada parte de uma página, com um nome curto. O `h1` é o título principal, o `p` é um parágrafo e o `main` é o conteúdo principal. Na árvore, cada elemento é um ramo.
- Etiqueta: o nome de um elemento entre `<` e `>`, como `<h1>`, que marca onde ele começa; `</h1>` marca onde acaba.
- Esqueleto da página: as partes por que começam as páginas de hoje. O `html` embrulha tudo. Lá dentro, o `head` é a cabeça da página, que não aparece no meio dela. Tem o `title`, o título que se vê no separador. O `body` é o corpo, com tudo o que se vê.
- `header`: o cabeçalho que se vê no topo de uma página, com o nome do site e o menu. Tem um nome parecido com o `head`, mas é outra coisa: o `head` não aparece, e o `header` aparece.
- Código-fonte: o texto do ficheiro tal como chegou ao browser, antes de o browser construir a árvore.
- Ferramentas do programador: ferramentas escondidas do browser para ver uma página por dentro. Estão arrumadas em separadores. O separador Elements mostra a árvore do DOM, e o separador Network mostra os pedidos.
- Cliente e servidor: o cliente é quem pede, o teu browser. O servidor é um computador sempre ligado, que guarda os ficheiros de um site e os envia a quem os pede. Para saber mais, vê a secção "Cliente e servidor" do [guia](01-web-e-planeamento.md).
- Pedido e resposta: o browser faz um pedido ao servidor para cada ficheiro de que precisa, e o servidor devolve uma resposta.
- Endereço: o endereço de uma página, a que também se chama URL. Tem três partes principais: o protocolo, o domínio e o caminho. Para saber mais, vê a secção "O endereço de uma página" do [guia](01-web-e-planeamento.md).
- Método: a parte do pedido que diz o que o browser quer. O GET quer dizer "dá-me este ficheiro".
- Código de resposta: o número de três algarismos com que o servidor diz como correu o pedido. O 200 quer dizer que correu bem, e o 404 que o que se pediu não existe. Para saber mais, vê a secção "O que se diz num pedido e numa resposta" do [guia](01-web-e-planeamento.md).
- Cache: a cópia que o browser guarda de uma página já visitada, para não ter de a pedir toda outra vez.

## O que precisas

- Um computador com o Chrome ou o Edge. Para confirmar, abre o browser: deve aparecer uma janela com a barra de endereço no topo. Os passos são iguais nos dois. No Firefox, as ferramentas existem e funcionam da mesma maneira, mas alguns nomes mudam. O separador Elements, por exemplo, chama-se Inspetor.
- A pasta do repositório da disciplina no teu computador, com a pasta `exemplos`. Vais usar a Estante Digital, o site de exemplo dos guias, que está em `exemplos/frontend/estante-digital/`. Se ainda não tens a pasta, a secção "Preparar o projeto" diz como a obter.
- Ligação à Internet, para as fases 4, 5 e 6. Para confirmar, abre um site qualquer.
- Um caderno, ou um ficheiro de texto, para a tabela de registo.

Vais precisar destes atalhos de teclado:

| O que fazer | Windows | Mac |
| --- | --- | --- |
| Abrir e fechar as ferramentas do programador | F12 ou Ctrl+Shift+I | Cmd+Option+I |
| Ver o código-fonte da página, tal como chegou do ficheiro | Ctrl+U | Cmd+Option+U |
| Recarregar a página | F5 | Cmd+R |
| Abrir um ficheiro do computador no browser | Ctrl+O | Cmd+O |

## Se alguma coisa falhar

1. As ferramentas do programador abriram? Se o F12 não abre nada, experimenta Fn+F12, ou Ctrl+Shift+I (Cmd+Option+I no Mac). Também podes carregar com o botão direito do rato na página e escolher Inspecionar.
2. Os nomes estão em português? Elementos, Consola e Rede são Elements, Console e Network, e estão pela mesma ordem.
3. As ferramentas estão abertas no separador certo do browser? Cada separador do browser tem as suas próprias ferramentas. Se mudaste de separador, abre-as outra vez.
4. Tens Internet? As fases 4, 5 e 6 precisam dela. Se uma página da Internet não abre, avisa o professor.

Se o problema for outro, procura-o em [problemas frequentes](#problemas-frequentes).

## Preparar o projeto

1. Arranja a pasta do repositório da disciplina, se ainda não a tens. O professor pode dizer-te outra forma; se não disser, faz assim. Abre no browser o endereço `https://github.com/NunoMACastro/epms-2627-1ds-da`. Carrega no botão verde Code e escolhe Download ZIP (nomes confirmados a 16 de outubro de 2026). O browser descarrega um ficheiro ZIP, que guarda várias pastas num só ficheiro.

2. Descompacta o ficheiro ZIP numa pasta tua, antes de abrires qualquer página lá de dentro. No Windows, carrega com o botão direito no ficheiro e escolhe a opção de extrair. No Mac, faz duplo clique no ficheiro. Descompacta-se primeiro porque, dentro do ZIP, as ligações entre as páginas e as imagens podem falhar. O que deves ver: uma pasta chamada `epms-2627-1ds-da-main`, com as pastas `01-frontend`, `exemplos`, `imagens`, `laboratorios` e `projeto` lá dentro. No Windows, pode aparecer uma pasta com o mesmo nome dentro da primeira: abre-a até veres `01-frontend`.

3. Copia esta tabela para o caderno, ou para um ficheiro, com a segunda coluna vazia. Vais preenchê-la linha a linha, no fim de cada fase.

   | Observação | O que viste |
   | --- | --- |
   | 1. O início do endereço da Estante Digital aberta do teu disco | |
   | 2. O elemento que ficou selecionado quando inspecionaste o título grande | |
   | 3. O que aconteceu ao título depois de recarregares a página | |
   | 4. O protocolo, o domínio e o caminho do endereço do primeiro site | |
   | 5. Os dois elementos que estão no DOM do primeiro site e não estão no ficheiro, e onde foi parar o `title` | |
   | 6. O método e o código de resposta do pedido de `TheProject.html` | |
   | 7. O código de resposta de `NaoExiste.html` | |
   | 8. O número de pedidos do primeiro site e o da página do repositório no GitHub | |

## Fase 1: Uma página aberta do teu disco

Quando abres uma página de um site, o teu browser pede o ficheiro a um servidor, noutro computador. Quando abres um ficheiro que está no teu disco, não há servidor nenhum: o browser lê o ficheiro diretamente. O endereço mostra a diferença. Uma página que veio de um servidor começa por `https://` (ou `http://`), e um ficheiro do teu disco começa por `file://`. Para saber mais, lê a secção "Cliente e servidor" do [guia](01-web-e-planeamento.md).

1. Abre a página inicial da Estante Digital. No browser, carrega em Ctrl+O (Cmd+O no Mac), vai à pasta do repositório e abre o ficheiro `exemplos/frontend/estante-digital/index.html`. Também podes fazer duplo clique no ficheiro, no explorador de ficheiros. O que deves ver: uma página com o título "Recursos de estudo recomendados pela turma" e listas de livros, vídeos e sítios. A página ainda não tem estilos: é texto preto em fundo branco, com as ligações a azul e sublinhadas.

2. Antes de olhares para a barra de endereço, prevê: o endereço desta página começa por `https://` ou por outra coisa? Depois, carrega uma vez na barra de endereço, para veres o endereço completo. Alguns browsers, como o Chrome, escondem o início até carregares lá. O que deves ver: o endereço começa por `file:///`. A seguir vem o caminho do ficheiro no teu disco, com as pastas e o nome `index.html` no fim. Isto quer dizer que não há servidor nenhum: o browser leu o ficheiro diretamente do disco.

3. Carrega na ligação "Sobre" e depois em "Início", no menu. O que deves ver: as páginas mudam, e o endereço muda com elas. Continua a começar por `file:///`, e só muda o nome do ficheiro no fim, de `index.html` para `sobre.html` e outra vez para `index.html`.

### Paragem 1

Tens a Estante Digital aberta a partir do teu disco, e sabes, pela barra de endereço, que não veio de um servidor. Escreve na linha 1 da tabela o início do endereço. O que deve ficar escrito: `file:///`, seguido do caminho da tua pasta.

Pensa antes de continuares: se enviasses este endereço a um colega, por mensagem, ele via a página no computador dele? A resposta: não. O endereço aponta para um ficheiro no teu disco, e no computador do colega esse ficheiro não existe nesse sítio. Para ele ver o site, tinhas de lhe dar os ficheiros, ou o site tinha de estar num servidor.

## Fase 2: A árvore do DOM no separador Elements

Quando o browser abre um ficheiro HTML, lê o texto de cima a baixo. Depois constrói em memória uma árvore, com um ramo para cada parte da página. A essa árvore chama-se DOM. É a partir dela, e não do ficheiro, que a página é desenhada. O separador Elements das ferramentas do programador mostra essa árvore. Para saber mais, lê a secção "O browser" do [guia](01-web-e-planeamento.md).

1. Abre as ferramentas do programador. Com a página inicial da Estante Digital aberta, carrega em F12 (Cmd+Option+I no Mac). O que deves ver: as ferramentas abrem-se, normalmente do lado direito ou em baixo da janela. Se se abrirem noutro separador que não o Elements, carrega em Elements, na fila de separadores do topo das ferramentas. Em português pode aparecer como Elementos.

2. Olha para a árvore. O que deves ver: `html` em cima e, lá dentro, `head` e `body`. Os pequenos triângulos à esquerda de cada linha abrem e fecham cada ramo. Abre o `body` e, lá dentro, o `main`.

3. Passa o rato devagar por cima das linhas da árvore, sem carregar. O que deves ver: na página, a parte que corresponde a cada linha fica pintada de azul. É assim que se descobre que ramo da árvore desenha que parte da página.

4. Agora faz o caminho contrário, da página para a árvore. Na página, carrega com o botão direito do rato no título grande, "Recursos de estudo recomendados pela turma", e escolhe Inspecionar. O que deves ver: as ferramentas saltam para a linha desse título na árvore e deixam-na selecionada. A linha começa por `<h1>`: o título grande é um elemento `h1`, o título principal da página.

5. Há ainda uma terceira forma. No canto superior esquerdo das ferramentas há um ícone com uma seta a apontar para um quadrado. Carrega nele e depois passa o rato pela página: cada parte fica pintada, com o nome do elemento numa etiqueta. Carrega na ligação "Sobre" do menu. O que deves ver: fica selecionada na árvore uma linha que começa por `<a`. É assim que o HTML marca uma ligação, e vais aprendê-lo no tema 02.

### Paragem 2

Encontras na árvore a linha de qualquer parte da página, e na página a parte de qualquer linha da árvore. Escreve na linha 2 da tabela o elemento do título grande. O que deve ficar escrito: `h1`.

Pensa antes de continuares: quais são as três formas de ligar uma parte da página à sua linha na árvore? A resposta: há três formas.

- Passar o rato pelas linhas da árvore e ver a parte pintada na página.
- Carregar com o botão direito numa parte da página e escolher Inspecionar.
- Carregar no ícone da seta e depois na parte da página.

Agora escolhe: qual das três usavas para descobrir que elemento é o desenho do logótipo, no topo da página? Explica a tua escolha numa frase. A resposta: serve a segunda ou a terceira, porque partem da página. Já vês o logótipo e queres encontrar a sua linha na árvore. A primeira serve para o caminho contrário: tens uma linha da árvore e queres saber que parte da página ela desenha. Se experimentares, a linha do logótipo começa por `<img`, que é como o HTML marca uma imagem.

## Fase 3: Mudar o DOM sem mudar o ficheiro

O ficheiro é o texto guardado no disco. O DOM é a árvore que o browser construiu a partir dele, em memória. O que mudas no separador Elements muda só o DOM, e nunca o ficheiro. Quando recarregas a página, o browser deita fora a árvore e volta a construí-la a partir do ficheiro. Para saber mais, lê a secção "O ficheiro e o DOM" do [guia](01-web-e-planeamento.md).

1. Na árvore, seleciona outra vez a linha do `h1`. Faz duplo clique no texto do título, que está entre `<h1>` e `</h1>`. O que deves ver: o texto passa a poder ser editado, como numa caixa de texto.

2. Apaga o texto, escreve `Olá, sou o DOM` e carrega em Enter. O que deves ver: na página, o título passou a dizer "Olá, sou o DOM".

3. Antes do passo seguinte, prevê: no código-fonte, que é o texto do ficheiro, o que diz agora o título? Depois carrega em Ctrl+U (Cmd+Option+U no Mac). O que deves ver: abre-se um separador novo com o código-fonte da página. Procura o `h1`. O texto continua a ser "Recursos de estudo recomendados pela turma", porque o ficheiro não mudou. Fecha esse separador.

4. Volta à página e recarrega-a com F5 (Cmd+R no Mac). O que deves ver: o título volta a ser "Recursos de estudo recomendados pela turma". O browser construiu um DOM novo a partir do ficheiro, e a tua mudança desapareceu.

5. Escreve no caderno, por palavras tuas, o que esta experiência mostrou, em duas ou três frases, com as palavras "ficheiro" e "DOM". Uma resposta completa diz três coisas. Por exemplo: "Mudei o DOM, a árvore que o browser tem em memória, e por isso a página mudou. O ficheiro no disco não mudou. Quando recarreguei, o browser construiu um DOM novo a partir do ficheiro, e a mudança desapareceu." Uma frase como "mudei a página e depois voltou" não chega, porque não diz o que mudou e o que ficou igual.

### Paragem 3

Mostraste com uma experiência que mudar o DOM não muda o ficheiro. Escreve na linha 3 da tabela o que aconteceu ao título. O que deve ficar escrito: voltou ao texto original, "Recursos de estudo recomendados pela turma".

Lê o que escreveste no passo 5 a um colega. Ele percebe, só com isso, porque é que o título voltou ao original? Se não perceber, falta-lhe uma das três coisas da resposta completa.

Não estragaste nada. O que mudas no separador Elements fica só na tua cópia da página, até recarregares.

Pensa antes de continuares: se o professor mudasse o título da Estante Digital nas ferramentas do programador do computador dele, o teu título mudava? A resposta: não. Ele mudava só o DOM da cópia que o browser dele tem em memória. O ficheiro de cada um ficava igual.

## Fase 4: O browser acrescenta o que falta no ficheiro

As páginas de hoje começam todas pelo mesmo esqueleto: o `html`, com o `head` e o `body` lá dentro. Uma página escrita em 1992 não seguia estas regras. Quando o browser de hoje a abre, constrói a árvore pelas regras de hoje e acrescenta o que falta no ficheiro. Para saber mais, lê as secções "Uma história curta da Web" e "O ficheiro e o DOM" do [guia](01-web-e-planeamento.md).

1. Num separador novo, escreve este endereço e carrega em Enter:

   ```text
   https://info.cern.ch/hypertext/WWW/TheProject.html
   ```

   O que deves ver: uma página em inglês, com o título "World Wide Web". Tem só texto e ligações a azul e sublinhadas, sem imagens nem cores. É uma das primeiras páginas da Web, guardada pelo CERN tal como era. O ficheiro foi alterado pela última vez em 1992.

2. Parte o endereço nas suas partes e escreve-as no caderno. O protocolo é o que vem antes de `://`, e diz as regras da conversa com o servidor. O domínio é o nome do servidor, e vai até à primeira barra a seguir. O caminho é o resto: a pasta e o ficheiro dentro do servidor. O que deve ficar escrito: o protocolo é `https`, o domínio é `info.cern.ch` e o caminho é `/hypertext/WWW/TheProject.html`.

3. Carrega em Ctrl+U (Cmd+Option+U no Mac) para ver o código-fonte. O que deves ver, em três pormenores:

   - as etiquetas estão escritas em maiúsculas, como `<TITLE>` e `<H1>`. Nos anos 90 escrevia-se assim; hoje usam-se minúsculas;
   - não há `<!doctype html>` no início;
   - no lugar onde hoje se escreveria `<head>` está uma etiqueta `<HEADER>`, e o `<TITLE>` está lá dentro.

   Não feches o separador do código-fonte: vais compará-lo com a árvore no passo seguinte.

4. Antes de abrires a árvore, prevê: vais encontrar lá elementos que o ficheiro não tem? Depois volta ao separador da página, abre as ferramentas do programador no separador Elements e compara o topo da árvore com o código-fonte. Abre também o `body` e, lá dentro, o `header`, e procura o `title` da página. O que deves ver: a árvore começa por `html`, com um `head` vazio e um `body`. Dentro do `body` está um `header`, e é dentro desse `header` que está o `title`. Ao lado do `title` está um elemento `nextid`, com `n="55"`. É uma etiqueta de 1992 que hoje já não quer dizer nada: o browser guarda-a na árvore, mas não faz nada com ela.

5. Escreve no caderno os dois elementos que estão na árvore do DOM e não estão no ficheiro. Escreve também dentro de que elemento foi parar o `title`. O que deve ficar escrito: o `html` e o `head`; o `title` foi parar dentro do `header`, que está no `body`. O `body` não conta, porque o ficheiro tem `<BODY>` na linha 5.

### Paragem 4

Viste numa página verdadeira que o DOM tem elementos que o ficheiro não tem. Escreve na linha 4 da tabela o protocolo, o domínio e o caminho do passo 2. Escreve na linha 5 o que encontraste no passo 5.

Pensa antes de continuares: porque é que o `title` foi parar dentro de um `header`, no `body`? A resposta: o browser acrescentou o `html` e o `head`, porque as regras de hoje os põem sempre na árvore. Mas não percebeu que o `HEADER` de 1992 queria dizer a cabeça da página. Para as regras de hoje, um `header` é um cabeçalho que se vê, e fica no `body`. O browser pô-lo lá, com o `title` dentro, e deixou o `head` vazio. Fez o melhor que pôde com um ficheiro escrito com regras antigas.

## Fase 5: Um pedido e a sua resposta no separador Network

Para te mostrar o primeiro site, o browser fez um pedido ao servidor do CERN, e o servidor enviou uma resposta. Cada pedido tem um método, que diz o que o browser quer, e cada resposta tem um código, que diz como correu. O separador Network mostra cada pedido numa linha. Para saber mais, lê a secção "O que se diz num pedido e numa resposta" do [guia](01-web-e-planeamento.md).

1. Ainda na página do primeiro site, com as ferramentas abertas, carrega no separador Network (em português, Rede). O que deves ver: a lista está vazia, porque as ferramentas só registam os pedidos feitos enquanto estão abertas. Na fila de cima do separador, marca a caixa Disable cache (em português, Desativar cache). Fazes isto porque o browser guardou uma cópia da página na primeira visita, a cache. Sem a caixa marcada, ao recarregar, o browser podia usar essa cópia em vez de pedir a página inteira ao servidor.

2. Recarrega a página com F5 (Cmd+R no Mac). O que deves ver: aparece uma linha na lista, com o nome `TheProject.html`. É o pedido que o browser fez ao servidor. Na coluna Status aparece o código de resposta, 200. Na barra de baixo das ferramentas aparece o número total de pedidos: 1. Esta página precisou de um só pedido, porque é só texto, sem imagens, estilos nem JavaScript.

3. Carrega na linha `TheProject.html`. Abre-se um painel com vários separadores. No separador Headers, procura três informações e escreve-as no caderno. São o endereço do pedido (Request URL), o método (Request Method) e o código de resposta (Status Code). O que deves ver: o endereço é `https://info.cern.ch/hypertext/WWW/TheProject.html`, o mesmo da barra de endereço. O método é `GET` e o código é `200 OK`. Com as ferramentas em português, os nomes mudam: procura o endereço, o método e o código.

4. Agora provoca um erro de propósito. Antes de o fazeres, prevê: que código de resposta vai dar uma página que não existe? Na barra de endereço, muda o fim do endereço de `TheProject.html` para `NaoExiste.html` e carrega em Enter. O que deves ver: a página mostra "Not Found". No separador Network, a lista passa a ter só a linha `NaoExiste.html`, com o código 404. O servidor respondeu, mas a dizer que o que pediste não existe. É o que acontece quando alguém carrega numa ligação sem destino.

### Paragem 5

Seguiste um pedido do princípio ao fim, com o método, o endereço e o código da resposta. Depois viste o código de um pedido que falhou. Escreve na linha 6 da tabela o método e o código de `TheProject.html`. O que deve ficar escrito: GET e 200. Escreve na linha 7 o código de `NaoExiste.html`. O que deve ficar escrito: 404.

Pensa antes de continuares: o 404 começa por 4, e o 500, que quer dizer que o servidor avariou, começa por 5. O que diz o primeiro algarismo? A resposta: diz a família do código. Um código começado por 4 quer dizer que o pedido tem um problema, aqui uma página que não existe. Um código começado por 5 quer dizer que o problema é do servidor.

## Fase 6: Uma página de hoje faz muitos pedidos

A página de 1992 é um só ficheiro, só com texto. Uma página de hoje precisa também de imagens, ícones, folhas de estilos (os ficheiros com o CSS), ficheiros de JavaScript e tipos de letra. O browser faz um pedido à parte para cada um. Para saber mais, lê a secção "Cliente e servidor" do [guia](01-web-e-planeamento.md).

1. Abre um separador novo. As ferramentas do programador abrem-se em cada separador à parte. Por isso, carrega em F12 neste separador novo e escolhe o separador Network. Só depois escreve, na barra de endereço, o endereço da página do repositório da disciplina no GitHub, e carrega em Enter:

   ```text
   https://github.com/NunoMACastro/epms-2627-1ds-da
   ```

   Abres o Network antes de escrever o endereço porque as ferramentas só registam os pedidos feitos enquanto estão abertas.

2. Antes de olhares para a barra de baixo das ferramentas, prevê: esta página vai fazer mais ou menos pedidos do que o primeiro site? Depois olha para o número de pedidos. O que deves ver: muitos pedidos, mais de cem. Em dois ensaios a 16 de outubro de 2026, foram entre 170 e 190. O número exato muda de visita para visita, e muda se tiveres uma sessão iniciada no GitHub.

### Paragem 6

Escreve na linha 8 da tabela o número de pedidos do primeiro site e o da página do GitHub. O que deve ficar escrito: 1 no primeiro site, e o número que viste no GitHub, mais de cem.

Pensa antes de terminares: porque é que a página do GitHub faz tantos mais pedidos do que a página de 1992? A resposta: a página de 1992 é um só ficheiro, só com texto, e o browser recebe-a com um único pedido. A página do GitHub precisa também de imagens, ícones, folhas de estilos, ficheiros de JavaScript e tipos de letra. Cada um desses ficheiros é um pedido à parte.

A tua tabela de registo está completa. É a evidência deste laboratório.

## Problemas frequentes

### O F12 não abre nada, ou muda o volume do som

Em alguns portáteis, as teclas F só funcionam com a tecla Fn carregada. Usa Fn+F12, ou Ctrl+Shift+I, ou o botão direito do rato e Inspecionar.

### No Edge, o F12 abre uma janela a perguntar se queres mesmo abrir as ferramentas do programador

O Edge pede confirmação da primeira vez. Escolhe a opção de abrir as ferramentas.

### As ferramentas do programador não abrem de maneira nenhuma

Podem estar desativadas nos computadores da escola. Avisa o professor.

### As ferramentas abriram num sítio incómodo, a tapar a página

Podem ficar à direita, em baixo ou numa janela à parte. No canto superior direito das ferramentas há um botão com três pontos. Em Dock side, escolhe outra posição.

### Não encontro a pasta `01-frontend` dentro da pasta descompactada

No Windows, a pasta descompactada pode ter outra pasta com o mesmo nome lá dentro. Abre-a até veres `01-frontend`, `exemplos` e as outras.

### As ligações da Estante Digital não abrem, ou o logótipo não aparece

Abriste a página dentro do ficheiro ZIP, sem o descompactar. Descompacta o ZIP, como diz o passo 2 de "Preparar o projeto", e abre a página a partir da pasta descompactada.

### Não consigo mudar o título no código-fonte

O código-fonte, que se abre com Ctrl+U, mostra o ficheiro e não deixa editar. O título muda-se no separador Elements, com duplo clique no texto do `h1`.

### Escrevi o `body` entre os elementos que faltam no ficheiro do primeiro site

Volta ao código-fonte e procura a linha 5: lá está o `<BODY>`. O ficheiro tem o `body`, e por isso não conta. Os que faltam são o `html` e o `head`.

### O separador Network está vazio

As ferramentas só registam os pedidos feitos com elas abertas. Recarrega a página com as ferramentas abertas.

### Na coluna Status aparece 304, e não 200

O browser já tinha guardado uma cópia da página e só perguntou ao servidor se ela tinha mudado. O 304 quer dizer "não mudou, usa a cópia que tens". Marca a caixa Disable cache, na fila de cima do separador Network, e recarrega.

### A página do primeiro site não abre

Não há ligação à Internet, ou a rede da escola bloqueia o endereço. Avisa o professor. Ele pode projetar o que se vê nas fases 4, 5 e 6.

### O Ctrl+U não mostra nada

Em alguns browsers o atalho é outro. Carrega com o botão direito numa zona vazia da página e escolhe Ver código-fonte da página.

## Desafios

1. Na Estante Digital, muda no DOM o texto da ligação "Sobre", do menu, para "Quem somos", e depois carrega nela. Antes de carregares, prevê: a ligação leva à mesma página que antes? E, na página a que chegas, o menu diz "Sobre" ou "Quem somos"? Explica o que viste com as palavras "ficheiro" e "DOM". Pista: pensa no que o browser faz sempre que abre uma página.

2. Na Estante Digital, antes de abrires o separador Elements, prevê: o browser vai acrescentar à árvore algum elemento, como fez com o primeiro site? Confirma, comparando o código-fonte com o topo da árvore, e explica o que viste. Pista: procura no código-fonte da Estante Digital as partes do esqueleto que faltavam ao ficheiro de 1992.

3. Na barra de endereço da Estante Digital, muda `index.html` para `naoexiste.html` e carrega em Enter. O que aparece? Porque é que não é um 404, como no primeiro site? Pista: pensa em quem responde ao pedido quando a página vem do teu disco.

## Antes de terminares

- [ ] A tabela de registo tem as oito linhas preenchidas.
- [ ] Escreveste na fase 3, em duas ou três frases, o que a experiência mostrou, com as palavras "ficheiro" e "DOM".
- [ ] Explicaste, na paragem 2, a forma que escolheste para encontrar o logótipo na árvore.
- [ ] Sabes abrir as ferramentas do programador e encontrar na árvore qualquer parte de uma página.
- [ ] Sabes seguir um pedido no separador Network e ler o método e o código de resposta.
- [ ] Consegues explicar, por palavras tuas, porque é que o DOM pode ser diferente do ficheiro, e o que quer dizer um 404.

![Rodapé](../imagens/rodape.png)
