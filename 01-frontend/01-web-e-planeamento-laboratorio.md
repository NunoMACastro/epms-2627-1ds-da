![Cabeçalho](../imagens/cabecalho.png)

# Laboratório: A Web vista por dentro

UC: UC02833, Conceber aplicações para a web na vertente frontend

Bloco: F01

Requisitos: UC02833.K01, UC02833.K02, UC02833.A01

| Identificação | Valor |
| --- | --- |
| Material | Laboratório do bloco F01, acompanha o [guia](01-web-e-planeamento.md) |
| Duração | 45 minutos dos 240 do bloco |
| Material de apoio | O site de exemplo [Estante Digital](../exemplos/frontend/estante-digital/index.html), do repositório da disciplina, e ligação à Internet para as partes 4 e 5 |
| Evidência a guardar | A tabela de registo da parte 6, preenchida |

## O que vais fazer

Neste laboratório vais abrir as ferramentas do programador pela primeira vez e usá-las para ver por dentro o que o guia explicou por palavras. No fim deves conseguir:

- abrir as ferramentas do programador e encontrar, no separador Elements, o ramo da árvore que corresponde a uma parte da página;
- mostrar, com uma experiência, que mudar o DOM não muda o ficheiro;
- mostrar, numa página antiga, que o DOM tem elementos que o ficheiro não tem;
- ver, no separador Network, os pedidos de uma página, com o endereço, o método e o código de resposta, e provocar um 404.

Não vais aprender teoria nova. Tudo o que vês aqui está explicado no [guia](01-web-e-planeamento.md), e cada parte diz-te que secção deves ter aberta ao lado. E não vais escrever código: vais só observar e experimentar.

## O que precisas antes

- Do guia deste bloco, as secções "O browser" (com "O ficheiro e o DOM"), "Cliente e servidor", "O endereço de uma página", "O que se diz num pedido e numa resposta" e "As ferramentas do programador".
- Um computador com o Chrome ou o Edge. Os passos são iguais nos dois. No Firefox as ferramentas existem e funcionam da mesma maneira, mas alguns nomes mudam: o separador Elements chama-se Inspetor, por exemplo.
- A pasta do repositório da disciplina no computador, com a pasta `exemplos`. Se ainda não a tens, o professor diz-te como a obter. Uma forma é abrir a página do repositório no GitHub, carregar no botão verde Code, escolher Download ZIP e descompactar o ficheiro numa pasta tua.

## Os atalhos de que vais precisar

| O que fazer | Windows | Mac |
| --- | --- | --- |
| Abrir e fechar as ferramentas do programador | F12 ou Ctrl+Shift+I | Cmd+Option+I |
| Ver o código-fonte da página, tal como chegou do ficheiro | Ctrl+U | Cmd+Option+U |
| Recarregar a página | F5 | Cmd+R |
| Abrir um ficheiro do computador no browser | Ctrl+O | Cmd+O |

## Parte 1: Uma página do teu computador (5 min)

Tem aberta a secção "Cliente e servidor" do guia.

**1.** No browser, carrega em Ctrl+O (Cmd+O no Mac), vai à pasta do repositório da disciplina e abre o ficheiro `exemplos/frontend/estante-digital/index.html`. Também podes fazer duplo clique no ficheiro, no explorador de ficheiros.

**2.** Carrega uma vez na barra de endereço, para veres o endereço completo: alguns browsers, como o Chrome, escondem o início até carregares lá. O endereço começa por `file://`, e a seguir vem o caminho do ficheiro no teu disco. Não há servidor nenhum: o browser leu o ficheiro diretamente do disco.

**3.** Carrega na ligação "Sobre" e depois em "Início", no menu. As páginas mudam, e o endereço muda com elas: continua a ser `file://`, e só muda o nome do ficheiro no fim.

**Confirma:** consegues dizer, olhando para a barra de endereço, que esta página vem do teu disco e não de um servidor, e em que pasta está o ficheiro.

## Parte 2: O separador Elements (10 min)

Tem aberta a secção "As ferramentas do programador" do guia.

**1.** Com a página inicial da Estante Digital aberta, carrega em F12 (Cmd+Option+I no Mac). As ferramentas do programador abrem-se, normalmente do lado direito ou em baixo da janela. Se se abrirem noutro separador que não o Elements, carrega em Elements, na fila de separadores do topo das ferramentas. Em português pode aparecer como Elementos.

**2.** O que vês é a árvore do DOM: `html` em cima e, lá dentro, `head` e `body`. Os pequenos triângulos à esquerda de cada linha abrem e fecham cada ramo. Abre o `body` e, lá dentro, o `main`.

**3.** Passa o rato devagar por cima das linhas da árvore, sem carregar. Repara que, na página, a parte correspondente a cada linha fica pintada de azul. É assim que se descobre que ramo da árvore desenha que parte da página.

**4.** Agora faz o caminho contrário. Na página, carrega com o botão direito do rato no título grande, "Recursos de estudo recomendados pela turma", e escolhe Inspecionar. As ferramentas saltam para a linha desse título na árvore, e deixam-na selecionada. É um `h1`.

**5.** Há ainda uma terceira forma. No canto superior esquerdo das ferramentas há um ícone com uma seta a apontar para um quadrado. Carrega nele e depois passa o rato pela página: cada parte fica pintada, com o nome do elemento numa etiqueta. Carrega numa das ligações do menu e vê que linha da árvore fica selecionada.

**Confirma:** consegues encontrar, na árvore, a linha de qualquer parte da página, e a parte da página de qualquer linha da árvore.

## Parte 3: Mudar o DOM sem mudar o ficheiro (5 min)

Tem aberta a secção "O ficheiro e o DOM" do guia.

**1.** Na árvore, seleciona outra vez o `h1`. Faz duplo clique no texto do título, que está entre `<h1>` e `</h1>`. O texto passa a poder ser editado.

**2.** Apaga o texto, escreve `Olá, sou o DOM` e carrega em Enter. Olha para a página: o título mudou.

**3.** Carrega em Ctrl+U (Cmd+Option+U no Mac). Abre-se um separador novo com o código-fonte da página, tal como está no ficheiro. Procura o `h1`. O texto continua a ser "Recursos de estudo recomendados pela turma". Fecha esse separador.

**4.** Volta à página e recarrega-a com F5 (Cmd+R no Mac). O título volta a ser o original.

**5.** Escreve no caderno, por palavras tuas, o que esta experiência mostrou. A frase deve usar as palavras "ficheiro" e "DOM".

**Confirma:** lê a tua frase a um colega. Ele percebe, só com ela, porque é que o título voltou ao original? Não estragaste nada: o que mudas nas ferramentas do programador fica só na tua cópia da página, até recarregares.

## Parte 4: O primeiro site da história (10 min)

Tem aberta a secção "Uma história curta da Web" do guia.

**1.** Num separador novo, escreve este endereço e carrega em Enter:

```text
https://info.cern.ch/hypertext/WWW/TheProject.html
```

É uma das primeiras páginas da Web, guardada pelo CERN tal como era. O ficheiro foi alterado pela última vez em 1992. Está em inglês e não tem imagens nem cores: é só texto e ligações azuis, sublinhadas.

**2.** Parte o endereço nas suas partes, como na secção "O endereço de uma página" do guia, e escreve-as no caderno: o protocolo, o domínio e o caminho.

**3.** Carrega em Ctrl+U (Cmd+Option+U no Mac) para ver o código-fonte. Repara em três coisas:

- as etiquetas estão escritas em maiúsculas, como `<TITLE>` e `<H1>`. Nos anos 90 escrevia-se assim; hoje usa-se minúsculas;
- não há `<!doctype html>` no início;
- no lugar onde hoje se escreveria `<head>` está uma etiqueta `<HEADER>`.

Não feches o separador do código-fonte: vais compará-lo com a árvore no passo seguinte.

**4.** Volta ao separador da página, abre as ferramentas do programador no separador Elements e compara o topo da árvore com o código-fonte. Abre também o `body` e, lá dentro, o `header`, e procura o `title` da página.

**5.** Escreve no caderno os dois elementos que estão na árvore do DOM desta página e não estão no ficheiro, e dentro de que elemento foi parar o `title`.

**Confirma:** consegues explicar, com esta página, as duas primeiras razões da secção "O ficheiro e o DOM": o browser acrescenta à árvore elementos que o ficheiro não tem, porque as regras do HTML os põem sempre lá, e arruma à sua maneira o que não percebe. Aqui, não percebeu que o `HEADER` de 1992 queria dizer a cabeça da página, e fez o melhor que pôde com um ficheiro escrito com regras antigas.

## Parte 5: Os pedidos no separador Network (10 min)

Tem aberta a secção "O que se diz num pedido e numa resposta" do guia.

**1.** Ainda na página do primeiro site, com as ferramentas abertas, carrega no separador Network (em português, Rede). A lista está vazia, porque as ferramentas só registam os pedidos feitos enquanto estão abertas. Na fila de cima do separador, marca a caixa Disable cache (em português, Desativar cache). Assim, ao recarregar, o browser pede a página inteira ao servidor, em vez de usar a cópia que guardou na primeira visita.

**2.** Recarrega a página com F5. Aparece uma linha na lista, com o nome `TheProject.html`. É o pedido que o browser fez ao servidor. Na coluna Status aparece o código de resposta, e na barra de baixo das ferramentas aparece o número total de pedidos. Esta página precisou de um só pedido, porque é só texto: não tem imagens, estilos nem JavaScript.

**3.** Carrega na linha `TheProject.html`. Abre-se um painel com vários separadores; no separador Headers procura três informações e escreve-as no caderno: o endereço do pedido (Request URL), o método (Request Method) e o código de resposta (Status Code).

**4.** Agora provoca um erro de propósito. Na barra de endereço, muda o fim do endereço de `TheProject.html` para `NaoExiste.html` e carrega em Enter. A página mostra "Not Found", e no separador Network a nova linha tem outro código de resposta. Escreve-o no caderno. É o que acontece quando alguém carrega numa ligação sem destino.

**5.** Para comparar com um site atual, abre um separador novo. As ferramentas do programador abrem-se em cada separador à parte: carrega em F12, escolhe o separador Network e só depois escreve, na barra de endereço, o endereço da página do repositório da disciplina no GitHub, que o professor te dá. Olha para o número de pedidos na barra de baixo das ferramentas. Escreve-o no caderno, ao lado do número de pedidos do primeiro site.

**Confirma:** tens escritos o método e os dois códigos de resposta, e consegues explicar porque é que uma página moderna faz muitos mais pedidos do que a página de 1992.

## Parte 6: Registar (5 min)

Copia esta tabela para o caderno, ou para um ficheiro, e preenche-a com o que observaste. É a evidência deste laboratório.

| Observação | O que viste |
| --- | --- |
| O início do endereço da Estante Digital aberta do teu disco | |
| O elemento que ficou selecionado quando inspecionaste o título grande | |
| O que aconteceu ao título depois de recarregares a página | |
| O protocolo, o domínio e o caminho do endereço do primeiro site | |
| Os dois elementos que estão no DOM do primeiro site e não estão no ficheiro, e onde foi parar o `title` | |
| O método e o código de resposta do pedido de `TheProject.html` | |
| O código de resposta de `NaoExiste.html` | |
| O número de pedidos do primeiro site e o da página do repositório no GitHub | |

## Quando alguma coisa corre mal

| O que vês | Porque acontece | O que fazer |
| --- | --- | --- |
| F12 não abre nada, ou muda o volume do som | Em alguns portáteis, as teclas F só funcionam com a tecla Fn carregada | Usa Fn+F12, ou Ctrl+Shift+I, ou o botão direito do rato e Inspecionar |
| No Edge, o F12 abre uma janela a perguntar se queres mesmo abrir as ferramentas do programador | O Edge pede confirmação da primeira vez | Escolhe a opção de abrir as ferramentas |
| As ferramentas do programador não abrem de maneira nenhuma | Podem estar desativadas nos computadores da escola | Avisa o professor |
| As ferramentas abriram num sítio incómodo, a tapar a página | Podem ficar à direita, em baixo ou numa janela à parte | No canto superior direito das ferramentas há um botão com três pontos; em Dock side escolhe outra posição |
| As ferramentas estão em português e os nomes não batem com os deste laboratório | O browser mostra as ferramentas na língua do sistema | Os separadores estão pela mesma ordem; Elementos, Consola e Rede são Elements, Console e Network |
| O separador Network está vazio | As ferramentas só registam os pedidos feitos com elas abertas | Recarrega a página com as ferramentas abertas |
| Na coluna Status aparece 304, e não 200 | O browser já tinha guardado uma cópia da página e só perguntou ao servidor se ela tinha mudado. O 304 quer dizer "não mudou, usa a cópia que tens" | Marca a caixa Disable cache, na fila de cima do separador Network, e recarrega |
| A página do primeiro site não abre | Não há ligação à Internet, ou a rede da escola bloqueia o endereço | Avisa o professor e faz a parte 4 a partir das imagens que ele projetar |
| O Ctrl+U não mostra nada | Em alguns browsers o atalho é outro | Carrega com o botão direito numa zona vazia da página e escolhe Ver código-fonte da página |

## O que entregar

A tabela da parte 6, preenchida, e a frase da parte 3 que explica a diferença entre o ficheiro e o DOM.

![Rodapé](../imagens/rodape.png)
