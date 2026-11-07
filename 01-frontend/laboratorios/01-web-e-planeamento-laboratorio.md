![Cabeçalho](../../imagens/cabecalho.png)

# Laboratório: A Web, os utilizadores e o planeamento

## O que vais construir

Neste laboratório não escreves código: vês as páginas por dentro, com as ferramentas do programador, e fazes experiências com elas. O que constróis é um ficheiro `registo.md`, com uma observação no fim de cada fase.

1. [Fase 1: Uma página do teu disco não vem de um servidor](#fase-1-uma-página-do-teu-disco-não-vem-de-um-servidor)
2. [Fase 2: O browser constrói uma árvore, o DOM](#fase-2-o-browser-constrói-uma-árvore-o-dom)
3. [Fase 3: Mudar o DOM não muda o ficheiro](#fase-3-mudar-o-dom-não-muda-o-ficheiro)
4. [Fase 4: O browser acrescenta o que falta no ficheiro](#fase-4-o-browser-acrescenta-o-que-falta-no-ficheiro)
5. [Fase 5: O endereço de uma página](#fase-5-o-endereço-de-uma-página)
6. [Fase 6: O pedido diz o que o browser quer](#fase-6-o-pedido-diz-o-que-o-browser-quer)
7. [Fase 7: A resposta diz como correu o pedido](#fase-7-a-resposta-diz-como-correu-o-pedido)
8. [Fase 8: Uma página de hoje faz muitos pedidos](#fase-8-uma-página-de-hoje-faz-muitos-pedidos)

## O que precisas

- O Chrome ou o Edge: confirma que o tens abrindo-o. Deve aparecer uma janela com a barra de endereço no topo. Os passos são iguais nos dois.
- O VS Code, o editor das aulas: confirma que o tens abrindo-o. Deve aparecer a janela do editor, com uma coluna de ícones à esquerda.
- A pasta do repositório da disciplina, com a Estante Digital, o site de exemplo dos guias. Se ainda não a tens, "Preparar o projeto" diz como a obter.
- Ligação à Internet, a partir da fase 4: confirma que a tens abrindo um site qualquer.

## Preparar o projeto

1. Arranja a pasta do repositório da disciplina, se ainda não a tens, para teres a Estante Digital no teu disco. Se o professor não te disser outra forma, abre no browser o endereço `https://github.com/NunoMACastro/epms-2627-1ds-da`. Carrega no botão verde Code e escolhe Download ZIP. O browser descarrega um ficheiro ZIP, que guarda várias pastas num só ficheiro.

2. Descompacta o ZIP numa pasta tua, antes de abrires qualquer página lá de dentro, porque dentro do ZIP as ligações entre as páginas podem falhar. No Windows, carrega com o botão direito no ficheiro e escolhe a opção de extrair. No Mac, faz duplo clique no ficheiro. O que deves ver: uma pasta `epms-2627-1ds-da-main`, com as pastas `01-frontend`, `exemplos`, `imagens` e `projeto` lá dentro. No Windows, pode aparecer outra pasta com o mesmo nome dentro da primeira: abre-a até veres `01-frontend`. Se aparecer outra coisa, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

3. Abre no VS Code a pasta `epms-2627-1ds-da-main`, a que tem `01-frontend` lá dentro, porque é lá que vai ficar o teu registo. No menu File, escolhe Open Folder... e depois a pasta. Se o VS Code perguntar se confias nos autores dos ficheiros, carrega em "Yes, I trust the authors", porque são os ficheiros da disciplina. O que deves ver: à esquerda, o painel Explorer, com as pastas `01-frontend` e `exemplos`.

4. Cria o `registo.md`, o ficheiro onde escreves o que observas no fim de cada fase, a não ser que o professor te indique outro sítio. No painel Explorer, carrega numa zona vazia. Depois carrega no ícone de ficheiro novo, New File..., no topo do painel, ao lado do nome da pasta. Escreve `registo.md` e carrega em Enter.

   O que deves ver: o `registo.md` no painel Explorer, ao lado das pastas, e aberto, vazio, no meio da janela. Sempre que escreveres nele, guarda com Ctrl+S, ou Cmd+S no Mac.

## Fase 1: Uma página do teu disco não vem de um servidor

Abres a Estante Digital a partir do teu disco e vês, pelo endereço, que nenhum servidor a enviou. Rever: [Uma página do teu disco não vem de um servidor](../01-web-e-planeamento.md#uma-página-do-teu-disco-não-vem-de-um-servidor).

1. Abre a página inicial da Estante Digital. No browser, carrega em Ctrl+O (Cmd+O no Mac), vai à pasta do repositório e abre `exemplos/frontend/estante-digital/index.html`. O que deves ver: uma página com o título "Recursos de estudo recomendados pela turma" e listas de livros, vídeos e sítios. É texto preto sobre fundo branco, sem estilos. Se aparecer outra coisa, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

2. Antes de olhares para a barra de endereço, prevê: o endereço desta página começa por `https://` ou por outra coisa? Depois, carrega uma vez na barra de endereço, porque o Chrome esconde o início até carregares lá. O que deves ver: o endereço começa por `file:///`, seguido do caminho do ficheiro no teu disco, com `index.html` no fim. Isto quer dizer que o browser leu o ficheiro diretamente do disco, sem servidor nenhum.

3. Carrega na ligação "Sobre" e depois em "Início", no menu. O que deves ver: o endereço continua a começar por `file:///`. Só muda o nome do ficheiro no fim, de `index.html` para `sobre.html` e outra vez para `index.html`.

### Paragem 1

Tens a Estante Digital aberta a partir do teu disco. Escreve no `registo.md` a observação 1: o início do endereço, `file:///`, seguido do caminho da tua pasta.

Pensa antes de continuares: se enviasses este endereço a um colega, por mensagem, ele via a página no computador dele? A resposta: não. O endereço aponta para um ficheiro no teu disco, e no computador do colega esse ficheiro não está nesse sítio.

## Fase 2: O browser constrói uma árvore, o DOM

Abres as ferramentas do programador e encontras, na árvore do DOM, cada parte da página. Rever: [O browser constrói uma árvore, o DOM](../01-web-e-planeamento.md#o-browser-constrói-uma-árvore-o-dom) e [As ferramentas do programador](../01-web-e-planeamento.md#as-ferramentas-do-programador).

1. Abre as ferramentas do programador, as ferramentas do browser que mostram a página por dentro. Com a Estante Digital aberta, carrega em F12 (Cmd+Option+I no Mac). O que deves ver: as ferramentas abrem-se à direita ou em baixo da janela, com uma fila de separadores no topo, como Elements e Console. Se não estiverem em Elements, carrega em Elements, que em português pode aparecer como Elementos. Se aparecer outra coisa, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

2. Olha para a árvore. O que deves ver: `html` em cima e, lá dentro, `head` e `body`. Antes do `html` aparecem o `<!doctype html>` e, a verde, comentários: notas para quem lê o código, que o browser não mostra na página. Os pequenos triângulos à esquerda de cada linha abrem e fecham cada ramo. Abre o `body` e, lá dentro, o `main`.

3. Passa o rato devagar pelas linhas da árvore, sem carregar. O que deves ver: na página, a parte que corresponde a cada linha fica pintada de azul. Isto quer dizer que cada ramo da árvore desenha uma parte da página.

4. Agora faz o caminho contrário, da página para a árvore. Na página, carrega com o botão direito no título grande e escolhe Inspecionar, ou Inspect, com o browser em inglês. O que deves ver: as ferramentas saltam para a linha desse título e deixam-na selecionada. A linha começa por `<h1>`: o título grande é um elemento `h1`.

5. Há ainda uma terceira forma. No canto superior esquerdo das ferramentas, carrega no ícone com uma seta a apontar para um quadrado e depois carrega na ligação "Sobre" do menu. O que deves ver: fica selecionada uma linha que começa por `<a`, que é como o HTML marca uma ligação.

### Paragem 2

Encontras na árvore a linha de qualquer parte da página, e na página a parte de qualquer linha. Escreve no `registo.md` a observação 2: o elemento do título grande, `h1`.

Pensa antes de continuares: das três formas de ligar a página à árvore, qual usavas para descobrir que elemento é o logótipo, e porquê? A resposta: a segunda ou a terceira, porque partem da página: já vês o logótipo e queres a sua linha na árvore. A primeira serve para o caminho contrário. A linha do logótipo começa por `<img`, que é como o HTML marca uma imagem.

## Fase 3: Mudar o DOM não muda o ficheiro

Mudas o título da página no DOM e confirmas que o ficheiro fica igual. Rever: [Mudar o DOM não muda o ficheiro](../01-web-e-planeamento.md#mudar-o-dom-não-muda-o-ficheiro).

1. Na árvore, seleciona outra vez a linha do `h1` e faz duplo clique no texto do título, entre `<h1>` e `</h1>`. O que deves ver: o texto passa a poder ser editado, como numa caixa de texto.

2. Apaga o texto, escreve `Olá, sou o DOM` e carrega em Enter. O que deves ver: na página, o título passou a dizer "Olá, sou o DOM".

3. Antes do passo seguinte, prevê: no código-fonte da página, que é o texto do ficheiro, o que diz agora o título? Depois carrega em Ctrl+U (Cmd+Option+U no Mac), que abre o código-fonte num separador novo do browser. O que deves ver: o `h1` continua a dizer "Recursos de estudo recomendados pela turma", porque o ficheiro não mudou. Fecha esse separador. Se aparecer outra coisa, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

4. Volta à página e recarrega-a com F5 (Cmd+R no Mac). O que deves ver: o título volta a ser "Recursos de estudo recomendados pela turma". Isto quer dizer que o browser construiu um DOM novo a partir do ficheiro, e a tua mudança desapareceu.

5. Escreve no `registo.md`, como observação 3, por palavras tuas e com as palavras "ficheiro" e "DOM", o que esta experiência mostrou. Uma resposta completa diz o que mudou, o que ficou igual e porque é que a mudança desapareceu. Por exemplo: "Mudei o DOM, e por isso a página mudou. O ficheiro no disco não mudou. Quando recarreguei, o browser construiu um DOM novo a partir do ficheiro, e a mudança desapareceu."

### Paragem 3

Mostraste com uma experiência que mudar o DOM não muda o ficheiro, e não estragaste nada. A tua observação 3 diz o que mudou, o que ficou igual e porque é que a mudança desapareceu.

Pensa antes de continuares: se o professor mudasse o título da Estante Digital nas ferramentas do programador do computador dele, o teu título mudava? A resposta: não. Ele mudava só o DOM da cópia que o browser dele tem aberta, e os ficheiros ficavam iguais.

## Fase 4: O browser acrescenta o que falta no ficheiro

Visitas uma cópia do primeiro site da Web, de 1992, e encontras no DOM elementos que o ficheiro não tem. Rever: [O browser acrescenta o que falta no ficheiro](../01-web-e-planeamento.md#o-browser-acrescenta-o-que-falta-no-ficheiro).

1. Num separador novo, escreve este endereço e carrega em Enter:

   ```text
   https://info.cern.ch/hypertext/WWW/TheProject.html
   ```

   O que deves ver: uma página em inglês, com o título "World Wide Web", só com texto e ligações azuis e sublinhadas. É uma das primeiras páginas da Web, guardada pelo CERN tal como era. Se a página não abrir, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

2. Carrega em Ctrl+U (Cmd+Option+U no Mac) para ver o código-fonte. O que deves ver, em três pormenores:

   - os nomes entre `<` e `>` estão em maiúsculas, como `<TITLE>` e `<H1>`, como se escrevia nos anos 90;
   - não há `<!doctype html>` no início;
   - no lugar onde hoje se escreveria `<head>` está `<HEADER>`, com o `<TITLE>` lá dentro.

   Não feches o separador do código-fonte: vais compará-lo com a árvore no passo seguinte.

3. Antes de abrires a árvore, prevê: vais encontrar lá elementos que o ficheiro não tem? Depois volta ao separador da página, abre as ferramentas do programador no separador Elements e compara o topo da árvore com o código-fonte. Abre também o `body`, e lá dentro o `header`. O que deves ver: a árvore começa por `html`, com um `head` vazio e um `body`, e o `header` está dentro do `body`.

4. Descobre os dois elementos que estão no DOM e não estão no ficheiro, e dentro de que elemento foi parar o `title`. A resposta: o `html` e o `head`, e o `title` foi parar dentro do `header`. O `body` não conta, porque o ficheiro tem `<BODY>` na linha 5. A seguir ao `title`, no mesmo `header`, está um elemento `nextid`, de 1992, que hoje não quer dizer nada.

### Paragem 4

Viste numa página verdadeira que o DOM tem elementos que o ficheiro não tem. Escreve no `registo.md` a observação 4: os dois elementos acrescentados, e onde foi parar o `title`.

Pensa antes de continuares: porque é que o `title` foi parar dentro de um `header`, no `body`? A resposta: para as regras de hoje, um `header` é um cabeçalho que se vê, e fica no `body`. O browser não percebeu que o `HEADER` de 1992 queria dizer a cabeça da página. Pô-lo no `body`, com o `title` dentro, e deixou o `head` vazio.

## Fase 5: O endereço de uma página

Partes o endereço do primeiro site nas suas partes. Rever: [O endereço de uma página](../01-web-e-planeamento.md#o-endereço-de-uma-página).

1. Volta ao separador do primeiro site e carrega uma vez na barra de endereço, como na fase 1, para veres o endereço completo. Separa o protocolo, que vem antes de `://`, o domínio, que vai daí até à barra seguinte, e o caminho, que é o resto. A resposta: o protocolo é `https`, o domínio é `info.cern.ch` e o caminho é `/hypertext/WWW/TheProject.html`.

2. Compara com o endereço da Estante Digital, da fase 1. O que deves ver: o da Estante começa por `file:///` e não tem domínio, porque não veio de nenhum servidor.

### Paragem 5

Sabes dizer as partes de um endereço. Escreve no `registo.md` a observação 5: o protocolo, o domínio e o caminho do endereço do primeiro site.

Pensa antes de continuares: no caminho `/hypertext/WWW/TheProject.html`, o que é a parte `TheProject.html`? A resposta: o nome do ficheiro, dentro das pastas `hypertext` e `WWW` do servidor.

## Fase 6: O pedido diz o que o browser quer

Segues, no separador Network, o pedido que o browser fez para mostrar o primeiro site. Rever: [O pedido diz o que o browser quer](../01-web-e-planeamento.md#o-pedido-diz-o-que-o-browser-quer).

1. Ainda na página do primeiro site, com as ferramentas abertas, carrega no separador Network (em português, Rede). O que deves ver: a lista está vazia, porque as ferramentas só registam os pedidos feitos enquanto estão abertas.

2. Na fila de cima do separador, marca a caixa Disable cache (em português, Desativar cache). A cache é a cópia que o browser guardou da página na primeira visita. Sem a caixa marcada, ele podia usá-la em vez de pedir a página ao servidor.

3. Recarrega a página com F5 (Cmd+R no Mac). O que deves ver: aparece uma linha com o nome `TheProject.html`. É o pedido que o browser fez ao servidor. Na barra de baixo das ferramentas, o total de pedidos é 1, porque esta página é só texto. Se aparecer outra coisa, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

4. Carrega na linha `TheProject.html`. No painel que se abre, carrega no separador Headers, em português Cabeçalhos, que mostra o que foi no pedido e veio na resposta. Procura o endereço do pedido, Request URL, e o método, Request Method. O que deves ver: o endereço é o da barra de endereço, e o método é `GET`. Isto quer dizer que o browser pediu ao servidor "dá-me este ficheiro".

### Paragem 6

Seguiste um pedido, com o endereço e o método. Escreve no `registo.md` a observação 6: o método do pedido de `TheProject.html`, que é `GET`.

Pensa antes de continuares: quando carregas numa ligação, que método usa o browser? A resposta: também o `GET`, porque está a pedir outro ficheiro ao servidor.

## Fase 7: A resposta diz como correu o pedido

Lês o código da resposta a um pedido que correu bem, e provocas um pedido que corre mal. Rever: [A resposta diz como correu o pedido](../01-web-e-planeamento.md#a-resposta-diz-como-correu-o-pedido).

1. No separador Headers, que ainda tens aberto, procura o código de resposta, Status Code. O que deves ver: `200 OK`. Isto quer dizer que o servidor encontrou a página e a enviou. Fecha o painel do pedido, no X do canto, e o mesmo 200 aparece na coluna Status da lista. Se aparecer outra coisa, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

2. Agora provoca um erro de propósito. Antes de o fazeres, prevê: que código de resposta vai dar uma página que não existe? Na barra de endereço, muda o fim do endereço de `TheProject.html` para `NaoExiste.html` e carrega em Enter. O que deves ver: a página mostra "Not Found", e no separador Network a linha `NaoExiste.html` tem o código 404. O servidor respondeu, mas a dizer que o que pediste não existe.

### Paragem 7

Leste o código de uma resposta certa e o de uma resposta a um pedido que falhou. Escreve no `registo.md` a observação 7: o código de `TheProject.html`, 200, e o de `NaoExiste.html`, 404.

Pensa antes de continuares: o 404 começa por 4, e o 500, que quer dizer que o servidor avariou, começa por 5. O que diz o primeiro algarismo? A resposta: a família do código. Um código começado por 4 quer dizer que o problema está no pedido, aqui uma página que não existe. Um começado por 5 quer dizer que o problema é do servidor.

## Fase 8: Uma página de hoje faz muitos pedidos

Contas os pedidos de uma página de hoje e comparas com os do primeiro site. Rever: [Uma página de hoje faz muitos pedidos](../01-web-e-planeamento.md#uma-página-de-hoje-faz-muitos-pedidos).

1. Abre um separador novo e, nele, as ferramentas do programador no separador Network. Abre-as antes de escrever o endereço, porque só registam os pedidos feitos com elas abertas. Depois escreve este endereço, o da página do repositório da disciplina, e carrega em Enter:

   ```text
   https://github.com/NunoMACastro/epms-2627-1ds-da
   ```

2. Antes de olhares para a barra de baixo das ferramentas, prevê: esta página vai fazer mais ou menos pedidos do que o primeiro site? Depois olha para o total de pedidos. O que deves ver: mais de cem. O número exato muda de visita para visita.

### Paragem 8

Viste que uma página de hoje faz muitos pedidos. Escreve no `registo.md` a observação 8: o número de pedidos do primeiro site, 1, e o da página do GitHub.

Pensa antes de terminares: porque é que a página do GitHub faz tantos mais pedidos do que a de 1992? A resposta: a de 1992 é um só ficheiro, só com texto. A do GitHub precisa também de imagens, ícones, folhas de estilos, JavaScript e tipos de letra, e cada ficheiro é um pedido.

O teu `registo.md` tem as oito observações. É o resultado deste laboratório.

## Se alguma coisa falhar

1. As ferramentas do programador abriram? Se o F12 não abre nada, experimenta Fn+F12 ou Ctrl+Shift+I (Cmd+Option+I no Mac). Também podes usar o botão direito do rato e Inspecionar.
2. Os nomes estão em português? Elementos, Consola e Rede são Elements, Console e Network, pela mesma ordem.
3. As ferramentas estão abertas no separador certo do browser? Cada separador tem as suas. Se mudaste de separador, abre-as outra vez.
4. Tens Internet? As fases 4 a 8 precisam dela.

### O F12 não abre nada, ou muda o volume do som

Em alguns portáteis, as teclas F só funcionam com a tecla Fn carregada. Usa Fn+F12, Ctrl+Shift+I, ou o botão direito do rato e Inspecionar.

### No Edge, o F12 abre uma janela a perguntar se queres abrir as ferramentas do programador

O Edge pede confirmação da primeira vez. Escolhe a opção de abrir as ferramentas.

### As ferramentas do programador não abrem de maneira nenhuma

Podem estar desativadas nos computadores da escola. Avisa o professor.

### As ferramentas abriram num sítio incómodo, a tapar a página

No canto superior direito das ferramentas há um botão com três pontos. Em Dock side, escolhe outra posição.

### Não encontro a pasta `01-frontend` dentro da pasta descompactada

No Windows, a pasta descompactada pode ter outra pasta com o mesmo nome lá dentro. Abre-a até veres `01-frontend` e `exemplos`.

### As ligações da Estante Digital não abrem, ou o logótipo não aparece

Abriste a página dentro do ZIP, sem o descompactar. Descompacta-o, como diz o passo 2 de "Preparar o projeto", e abre a página a partir da pasta descompactada.

### Não consigo mudar o título no código-fonte

O código-fonte, que se abre com Ctrl+U, mostra o ficheiro e não deixa editar. O título muda-se no separador Elements, com duplo clique no texto do `h1`.

### O Ctrl+U não mostra nada

Em alguns browsers o atalho é outro. Carrega com o botão direito numa zona vazia da página e escolhe Ver código-fonte da página, ou View page source, com o browser em inglês.

### A página do primeiro site não abre

Não há ligação à Internet, ou a rede da escola bloqueia o endereço. Avisa o professor, que pode projetar o que se vê nas fases 4 a 8.

### O separador Network está vazio

As ferramentas só registam os pedidos feitos com elas abertas. Recarrega a página com as ferramentas abertas.

### Na coluna Status aparece 304, e não 200

O browser já tinha guardado uma cópia da página e só perguntou ao servidor se ela tinha mudado. O 304 quer dizer "não mudou, usa a cópia que tens". Marca a caixa Disable cache, na fila de cima do separador Network, e recarrega.

## Desafios

Escreve as explicações dos desafios no fim do teu `registo.md`.

1. Na Estante Digital, muda no DOM o texto da ligação "Sobre", do menu, para "Quem somos", e depois carrega nela. A ligação leva à mesma página que antes? Na página a que chegas, o menu diz "Sobre" ou "Quem somos"? Explica o que viste com as palavras "ficheiro" e "DOM". Pista: pensa no que o browser faz sempre que abre uma página.

2. Na Estante Digital, o browser acrescenta à árvore algum elemento, como fez com o primeiro site? Confirma, comparando o código-fonte com o topo da árvore, e explica o que viste. Pista: procura no código-fonte da Estante as partes que faltavam ao ficheiro de 1992.

3. Na barra de endereço da Estante Digital, muda `index.html` para `naoexiste.html` e carrega em Enter. O que aparece? Porque é que não é um 404, como no primeiro site? Pista: pensa em quem responde ao pedido quando a página vem do teu disco.

## Antes de terminares

- [ ] O teu `registo.md` tem as oito observações e as frases da fase 3, e está guardado.
- [ ] Sabes abrir as ferramentas do programador e encontrar na árvore qualquer parte de uma página.
- [ ] Sabes seguir um pedido no separador Network e ler o método e o código de resposta.

![Rodapé](../../imagens/rodape.png)
