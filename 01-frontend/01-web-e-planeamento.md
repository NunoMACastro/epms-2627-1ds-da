![Cabeçalho](../imagens/cabecalho.png)

# A Web, os utilizadores e o planeamento

UC: UC02833, Conceber aplicações para a web na vertente frontend

Bloco: F01

Requisitos: UC02833.K01, UC02833.K02, UC02833.A01, UC02833.A02, UC02833.A03

| Identificação | Valor |
| --- | --- |
| Material | Guia do bloco F01, o primeiro da área de frontend |
| Competências | web.fundamentals, web.browser, design.sitemap, design.wireframe |
| Duração do bloco | 4 horas, ou seja 240 minutos, repartidas pelas aulas que o professor indicar |
| Documentos do bloco | Este guia, o [laboratório](01-web-e-planeamento-laboratorio.md) e a [ficha de exercícios](01-web-e-planeamento-exercicios.md) |
| Modelo a preencher | O [brief e wireframe](../projeto/modelos/brief-e-wireframe.md) do projeto |
| Evidência a guardar | O plano do teu site: o brief preenchido, o mapa do site e os wireframes estreito e largo, anotados; e a explicação oral do percurso de um utilizador no teu plano |

## Objetivos

No fim deste bloco, serás capaz de:

- explicar a diferença entre a Internet e a Web, e contar em poucas frases como a Web nasceu e mudou;
- distinguir o trabalho do HTML, do CSS e do JavaScript numa página;
- explicar o que faz o browser com os ficheiros de uma página, o que é o DOM e porque é que o DOM pode ser diferente do ficheiro;
- descrever o que acontece entre escreveres um endereço e veres a página: o cliente, o servidor, o pedido e a resposta;
- partir um endereço nas suas partes e ler os códigos de resposta mais comuns;
- descrever, antes de fazer um site, para quem é, para que serve e que conteúdo vai ter;
- desenhar o mapa de um site e os wireframes estreito e largo das suas páginas, e verificar que o mapa e os wireframes concordam;
- escolher o tema do teu site, que vai crescer ao longo do ano, e fazer o seu plano.

## O que precisas de saber antes

Este é o primeiro guia da disciplina, e não dá por sabido nada de programação. Precisas só de saber usar um browser como utilizador: escrever um endereço, abrir um separador novo, voltar à página anterior. E precisas de papel e lápis, porque o planeamento faz-se primeiro à mão.

## Material e preparação

- Papel, lápis e borracha. Folhas A4 lisas são as melhores para desenhar o mapa e os wireframes.
- O [modelo do brief e wireframe](../projeto/modelos/brief-e-wireframe.md), que está na pasta do projeto do repositório da disciplina. Podes copiar as perguntas para uma folha ou preenchê-las numa cópia do ficheiro.
- Para o laboratório, um computador com o Chrome ou o Edge e ligação à Internet.

## Como está organizado o tempo

Este bloco tem 4 horas, ou seja 240 minutos. Não corresponde a uma aula: o professor reparte-o pelas sessões que existirem. Os tempos da tabela são os de quem faz este trabalho pela primeira vez e somam 255 minutos, um quarto de hora a mais: o que não couber nas aulas, normalmente parte da ficha, faz-se em casa.

| Parte | Onde está | Tempo |
| --- | --- | ---: |
| Teoria | Neste guia | 60 min |
| Exemplo explicado | Neste guia | 30 min |
| Prática guiada: o plano do teu site, em papel | Neste guia | 55 min |
| Laboratório: as ferramentas do programador | No [laboratório](01-web-e-planeamento-laboratorio.md) | 45 min |
| Prática autónoma | Na [ficha](01-web-e-planeamento-exercicios.md) | 50 min |
| Consolidação | Neste guia | 15 min |

A ordem recomendada é esta: ler a teoria e o exemplo explicado, fazer o plano do teu site na prática guiada, fazer o laboratório no computador, resolver a ficha e fechar com a consolidação.

A teoria tem duas metades. A primeira explica como funciona a Web, e é a base de tudo o que vais fazer este ano. A segunda explica como se planeia um site antes de o escrever, e é a que vais usar logo a seguir, no plano do teu site. Na aula, o professor apresenta as ideias principais; depois, cada secção fica aqui para a releres ao teu ritmo.

## Teoria (60 min)

### A Internet e a Web não são a mesma coisa

No dia a dia, muita gente diz "a Internet" quando quer dizer "a Web", e ao contrário. Perceber a diferença ajuda a perceber tudo o resto.

A **Internet** é a rede que liga computadores do mundo inteiro. É feita de coisas físicas: cabos, antenas, routers, satélites, cabos no fundo do mar. A única coisa que faz é transportar dados de um computador para outro. Não sabe o que são páginas, mensagens ou vídeos: só leva e traz pedaços de dados.

A **Web** (de *World Wide Web*, teia do tamanho do mundo) é um dos serviços que usam a Internet para funcionar. É o conjunto de páginas, ligadas umas às outras por ligações, que se leem com um browser. Há outros serviços que usam a mesma Internet sem serem a Web: o correio eletrónico, as chamadas de vídeo, os jogos em rede.

Uma comparação ajuda. A Internet é como a rede de estradas de um país: liga todas as terras, mas não transporta nada sozinha. A Web é como uma empresa de autocarros que usa essas estradas. O correio é outra empresa, que usa as mesmas estradas para outro fim. Se as estradas fecharem, nenhuma das empresas funciona; mas as estradas não são nenhuma das empresas.

Nesta disciplina vais fazer páginas para a Web. Como a Internet as transporta é matéria da disciplina de Sistemas e Redes; aqui, vais ficar a saber só o necessário para perceberes o que acontece quando alguém abre uma página tua.

### Uma história curta da Web

A Web é mais nova do que muitos dos teus professores. Conhecer a sua história ajuda a perceber porque é que as páginas são feitas da forma que vais aprender.

Em 1989, Tim Berners-Lee, um investigador que trabalhava no CERN, um grande laboratório europeu de física perto de Genebra, propôs uma forma de os cientistas partilharem documentos entre computadores diferentes, com ligações de uns documentos para os outros. No ano seguinte, em 1990, pôs a ideia a funcionar, com o primeiro browser e o primeiro servidor, e para isso inventou três coisas que ainda hoje usamos: uma linguagem para escrever os documentos, o **HTML**; umas regras para um computador pedir um documento a outro e o receber, o **HTTP**; e uma forma de dar um endereço único a cada documento, o **URL**. Vais aprender as três neste bloco e no guia 02, HTML e semântica.

Em 1991, o primeiro site ficou acessível a qualquer pessoa. Explicava o próprio projeto da Web. O que hoje se visita é uma cópia de 1992, guardada pelo CERN, a partir do endereço `info.cern.ch`. No laboratório deste bloco vais visitá-la e olhar para o seu código.

Em 1993, o CERN tornou a tecnologia da Web livre para toda a gente, sem pagamento. No mesmo ano apareceu o Mosaic, um dos primeiros browsers fáceis de usar e o primeiro a tornar-se popular, que mostrava imagens no meio do texto. A Web deixou de ser uma ferramenta de cientistas.

Em 1994 foi criado o W3C, uma organização que junta empresas e universidades para combinar as regras da Web, para que uma página funcione em todos os browsers. Em 1995 apareceu o **JavaScript**, para dar comportamento às páginas, e em 1996 foi publicada a primeira versão do **CSS**, para separar o aspeto das páginas da sua estrutura.

A partir de 2007, os telemóveis com ecrã tátil e um browser completo começaram a espalhar-se, e hoje uma grande parte das visitas aos sites é feita a partir de telemóveis. As páginas passaram a ter de funcionar em ecrãs pequenos e grandes, que é o assunto do bloco de responsividade.

Hoje o HTML já não tem versões numeradas. É um padrão vivo, que vai sendo atualizado aos poucos, e os browsers continuam a saber mostrar as páginas antigas. Vais encontrar o nome HTML5 em muitos sítios: é o nome que ficou para o HTML moderno.

Desta história ficam três ideias que vais reencontrar:

- uma página é feita de três linguagens, que nasceram em alturas diferentes para trabalhos diferentes;
- os browsers continuam a mostrar páginas escritas há mais de trinta anos, e por isso aceitam muita coisa mal escrita sem se queixarem. No guia 02, HTML e semântica, vais ver porque é que isso é uma vantagem e um perigo;
- as páginas de hoje têm de funcionar em ecrãs de todos os tamanhos.

### Três linguagens, três trabalhos

O HTML, o CSS e o JavaScript repartem entre si o trabalho de fazer uma página web. Vais usar esta divisão em todos os blocos de frontend do ano.

O **HTML** diz o que cada pedaço do conteúdo é: isto é um título, isto é um parágrafo, isto é uma lista, isto é uma imagem, isto é uma ligação para outra página. É a estrutura e o significado.

O **CSS** diz como cada pedaço se apresenta: a cor, o tipo e o tamanho da letra, os espaços, a posição de cada coisa no ecrã, o que muda num ecrã pequeno. É o aspeto.

O **JavaScript** diz como a página se comporta: o que acontece quando carregas num botão, quando escreves num campo, quando escolhes uma opção. É o comportamento.

Pensa numa casa. A estrutura (as paredes, as divisões, as portas, o que é a cozinha e o que é o quarto) é o HTML. Os acabamentos (a cor das paredes, o chão, os móveis) são o CSS. As instalações que fazem coisas (o interruptor que acende a luz, a campainha que toca) são o JavaScript. Podes pintar a casa de outra cor sem mexer nas paredes, e podes mudar a campainha sem pintar nada.

Vê as três linguagens a trabalhar sobre a mesma coisa: um botão "Gostar", com um contador ao lado. Não precisas de perceber o código ainda; olha só para o que cada parte faz.

```html
<!-- HTML: diz que isto é um botão, com o texto "Gostar", e um parágrafo com o contador. -->
<button id="gostar">Gostar</button>
<p id="contador">Gostos: 0</p>
```

```css
/* CSS: diz que o botão tem fundo azul, letra branca e cantos redondos. */
#gostar {
  background: #1f4e8c;
  color: white;
  border-radius: 8px;
}
```

```js
// JavaScript: diz que, quando se carrega no botão, o contador aumenta um.
let total = 0;
document.querySelector("#gostar").addEventListener("click", function () {
  total = total + 1;
  document.querySelector("#contador").textContent = "Gostos: " + total;
});
```

Repara que cada linguagem tem uma forma própria, e que já as consegues reconhecer pela forma. O HTML tem etiquetas entre `<` e `>`. O CSS tem nomes de propriedades seguidos de dois pontos e de um valor, dentro de chavetas. O JavaScript tem instruções que acabam em ponto e vírgula, com parênteses e palavras como `let` e `function`.

Porque é que se separam os três trabalhos? Porque cada um muda por razões diferentes, e separados mudam-se sem estragar os outros. Um site pode mudar de cores sem tocar no conteúdo. Uma pessoa cega que usa um leitor de ecrã, um programa que lê a página em voz alta, recebe o conteúdo e a estrutura do HTML, sem precisar do aspeto. E numa equipa, uma pessoa pode tratar do aspeto enquanto outra trata do comportamento.

Este ano vais aprender as três, por esta ordem: o HTML no guia 02, depois do bloco de Git, o CSS nos guias de frontend a seguir a esse, e o JavaScript depois, quando já tiveres uma página com estrutura e aspeto a que dar comportamento.

### O browser

O **browser** (em português também se diz navegador) é o programa que pede as páginas, lê os ficheiros e desenha a página no ecrã. O Chrome, o Edge, o Firefox e o Safari são browsers.

Para quem faz páginas, o browser é também o sítio onde o nosso trabalho funciona. Muitas linguagens de programação precisam de um programa próprio, instalado no computador, para os programas escritos nelas funcionarem. Uma página web precisa só de um browser, que qualquer computador e qualquer telemóvel já têm. Por isso se diz que o browser é o ambiente de execução da Web. É também por isso que, nesta disciplina, não precisas de instalar mais nada para começar: um editor de texto e um browser chegam.

Quando o browser recebe um ficheiro HTML, faz isto (a descrição está simplificada, mas chega para este ano):

1. **Lê o texto** do ficheiro, de cima a baixo.
2. **Constrói uma árvore** em memória, com um ramo para cada elemento da página: o título, cada parágrafo, cada ligação. A essa árvore chama-se **DOM**, de *Document Object Model*, que quer dizer modelo do documento em objetos.
3. **Calcula o aspeto** de cada ramo, a partir do CSS, e **desenha** a página no ecrã.
4. **Executa o JavaScript**, que pode mudar a árvore enquanto a página está aberta: acrescentar um item a uma lista, mudar um texto, esconder uma parte.

#### O ficheiro e o DOM

Há uma diferença que vai ser muito útil ao longo do ano: o **ficheiro** e o **DOM** não são a mesma coisa.

O ficheiro é o texto que está guardado no disco, que escreveste no editor. O DOM é a árvore que o browser construiu a partir desse texto, e é a partir do DOM, e não do ficheiro, que a página é desenhada. Pensa numa receita e num bolo. A receita é o ficheiro: fica escrita no livro e não muda. O bolo é o DOM: é feito a partir da receita, mas pode sair um pouco diferente, e depois de feito pode ser decorado sem que a receita mude.

Para perceberes as diferenças entre o ficheiro e o DOM, ajuda conhecer os nomes das partes de uma página. As páginas de hoje começam todas pelo mesmo esqueleto. A primeira linha, `<!doctype html>`, diz ao browser que a página segue as regras modernas do HTML. A seguir vem o elemento `html`, que embrulha tudo o resto e tem lá dentro duas partes: o `head`, a cabeça da página, com informação que não aparece no meio dela, como o título que se vê no separador do browser, escrito num elemento `title`; e o `body`, o corpo, com tudo o que se vê. Dentro do `body`, cada pedaço do conteúdo tem também um nome curto: `h1` é o título principal, `p` é um parágrafo, `main` é o conteúdo principal e `header` é o cabeçalho que se vê no topo, com o nome do site e o menu. Repara que `head` e `header` são nomes parecidos para coisas diferentes: o `head` não aparece na página, e o `header` aparece no topo dela. Vais escrever este esqueleto no guia 02; por agora basta reconheceres os nomes, porque vais encontrá-los na árvore do DOM, no laboratório.

O DOM pode ser diferente do ficheiro por três razões:

- **o browser corrige erros**. Se o ficheiro tiver um erro, o browser adivinha o que querias dizer e constrói a árvore à sua maneira. Por exemplo, se escreveres uma lista dentro de um parágrafo, o que as regras do HTML não permitem, o browser fecha o parágrafo antes da lista;
- **o browser acrescenta o que falta**. Há elementos que o browser põe na árvore mesmo que não estejam no ficheiro. No laboratório vais ver uma página de 1992 a que faltam o `html` e o `head` do esqueleto que hoje se escreve, e em que o browser os acrescenta sozinho;
- **o JavaScript muda a árvore**. Quando carregas no botão "Gostar", o JavaScript muda o texto do contador no DOM. O ficheiro continua a dizer "Gostos: 0".

Se recarregares a página, o browser deita fora a árvore antiga e volta a construí-la a partir do ficheiro. Tudo o que tinha sido mudado no DOM desaparece. No laboratório vais experimentar isto: mudas o texto de um título nas ferramentas do programador, a página muda, e quando recarregas volta tudo ao que estava.

#### Browsers diferentes

O Chrome e o Edge usam o mesmo motor para desenhar as páginas; o Firefox e o Safari usam motores diferentes. Graças às regras que os fabricantes de browsers combinam entre si, uma página bem escrita aparece praticamente igual em todos. Mesmo assim, quem faz páginas testa-as em mais do que um browser, porque há sempre pequenas diferenças.

### Cliente e servidor

Quando abres uma página na Internet, há dois computadores a conversar. O teu browser é o **cliente**: é quem pede. Do outro lado está um **servidor**: um computador sempre ligado, que guarda os ficheiros do site e os envia a quem os pede.

A conversa é parecida com o que acontece num restaurante. O cliente escolhe na ementa e faz um **pedido** ao empregado. O empregado leva o pedido à cozinha, que prepara o prato. O empregado traz a **resposta**: o prato, ou a notícia de que esse prato não existe. O cliente não entra na cozinha nem sabe como o prato foi feito: só faz pedidos e recebe respostas.

Uma página raramente se faz com um só pedido. O browser pede primeiro o ficheiro HTML. Quando o lê, descobre que a página também precisa de imagens, de uma folha de estilos e de um ficheiro de JavaScript, e faz um pedido novo para cada um. Uma página de um site grande pode fazer dezenas de pedidos. No laboratório vais ver esses pedidos, um a um, no separador Network das ferramentas do programador.

Nos primeiros blocos deste ano não vais usar servidor nenhum. Vais abrir as tuas páginas diretamente a partir do disco do teu computador, e nesse caso o browser lê os ficheiros sem pedir nada a ninguém. Percebes a diferença pelo endereço: uma página que veio de um servidor começa por `https://`, e um ficheiro aberto do teu disco começa por `file://`. Alguns browsers, como o Chrome, escondem este início até carregares na barra de endereço: carrega uma vez nela para veres o endereço completo. Isto tem uma consequência importante: um endereço `file://` só funciona no teu computador, porque é lá que o ficheiro está. Se o enviares a um colega, não funciona. Para outras pessoas verem o teu site, ele tem de estar num servidor, e isso é o assunto do bloco de publicação, no fim do ano.

### O endereço de uma página

O endereço de uma página chama-se **URL**, de *Uniform Resource Locator*, que quer dizer localizador uniforme de recursos. Um **recurso**, na Web, é qualquer coisa que se pode pedir a um servidor: uma página, uma imagem, uma folha de estilos. O URL é como a morada de uma casa: diz exatamente onde está aquilo que queres. Vê este endereço, partido nas suas partes:

```text
https://www.example.com/cursos/informatica.html
```

| Parte | Neste endereço | O que quer dizer |
| --- | --- | --- |
| Protocolo | `https` | As regras da conversa entre o browser e o servidor. O `s` quer dizer segura: a conversa vai cifrada, e quem estiver pelo meio não a consegue ler |
| Domínio | `www.example.com` | O nome do servidor, como o nome da rua e da terra de uma morada |
| Caminho | `/cursos/informatica.html` | A pasta e o ficheiro, dentro do servidor, como o número da porta e o andar |

O domínio `example.com` foi usado de propósito: é um domínio reservado para exemplos em documentação, e ninguém o pode registar para um site verdadeiro.

Há mais duas partes que podem aparecer no fim de um endereço. Depois de um ponto de interrogação vêm **parâmetros**, como em `?pesquisa=html`, que passam informação ao servidor, por exemplo o que escreveste numa caixa de pesquisa. Depois de um cardinal vem um **fragmento**, como em `#horario`, que indica uma parte da própria página; o browser salta para essa parte. Vais usar o fragmento no guia 02.

Os endereços de ficheiros do teu computador têm a mesma lógica, com o protocolo `file`, sem domínio e com o caminho do disco:

```text
file:///C:/Users/aluno/Documents/o-meu-site/index.html
```

Repara que a pasta se chama `Documents`. É esse o nome verdadeiro da pasta, que o Windows só mostra traduzido, como Documentos, no explorador de ficheiros.

Sobre o `https`: um endereço começado só por `http`, sem o `s`, não é cifrado. Os browsers avisam com a indicação "Não seguro" na barra de endereço. Nunca escrevas uma palavra-passe numa página com esse aviso. O `https` garante só que a conversa vai cifrada. Um site falso também pode usar `https`, e por isso o `s` não prova que o site é de confiança.

### O que se diz num pedido e numa resposta

As regras da conversa entre o browser e o servidor chamam-se **HTTP**, de *HyperText Transfer Protocol*, protocolo de transferência de hipertexto. O `https` é o mesmo HTTP com a conversa cifrada. Não precisas de saber as regras todas; precisas de saber ler duas coisas.

A primeira é o **método** do pedido, que diz o que o browser quer. O mais comum é o **GET**, que quer dizer "dá-me este recurso". É o que o browser usa quando escreves um endereço ou carregas numa ligação.

A segunda é o **código de resposta**, um número de três algarismos que o servidor envia antes do conteúdo, a dizer como correu o pedido. O primeiro algarismo diz a família:

| Família | Quer dizer | Exemplo que vais encontrar |
| --- | --- | --- |
| 2xx | Correu bem | **200**: aqui está o que pediste |
| 3xx | Está noutro sítio | **301**: esta página mudou de endereço para sempre, e o browser vai buscá-la ao endereço novo |
| 4xx | O pedido tem um problema | **404**: o que pediste não existe neste servidor |
| 5xx | O servidor teve um problema | **500**: o servidor avariou ao preparar a resposta |

O 404 é o mais famoso, porque aparece sempre que, num site publicado, uma ligação aponta para uma página que não existe. Nas páginas que abres do teu disco não há servidor, e por isso não há 404: o browser mostra uma mensagem a dizer que não encontrou o ficheiro. O 404 é o sintoma de uma **ligação sem destino**, que vais aprender a evitar no mapa do site. No laboratório vais provocar um 404 de propósito e vê-lo no separador Network.

### As ferramentas do programador

Todos os browsers têm, escondidas, umas ferramentas para quem faz páginas. Chamam-se **ferramentas do programador** (em inglês, *developer tools* ou *DevTools*). Abrem-se com a tecla F12 ou com Ctrl+Shift+I no Windows, com Cmd+Option+I no Mac, ou carregando com o botão direito do rato num ponto da página e escolhendo Inspecionar.

As ferramentas estão organizadas em separadores. Neste bloco vais usar dois:

- o separador **Elements** (em português pode aparecer como Elementos) mostra o DOM, a árvore que o browser construiu, e permite ver que parte da página corresponde a cada ramo;
- o separador **Network** (Rede) mostra todos os pedidos que a página fez, com o endereço, o método e o código de resposta de cada um.

Mais tarde vais usar o separador **Console** (Consola), onde aparecem os erros e onde se experimenta JavaScript. O laboratório deste bloco ensina a usar as ferramentas passo a passo. Não tenhas receio de mexer nelas: tudo o que mudas nas ferramentas do programador muda só o DOM da tua cópia da página, desaparece quando recarregas, e não estraga nada no site verdadeiro.

### Antes do editor: planear

A segunda metade desta teoria trata de planear um site antes de o escrever, um trabalho que se faz sem computador e que poupa muitas horas de correções depois.

Ninguém constrói uma casa sem planta, e ninguém filma um filme sem guião. Mudar uma parede num desenho custa uma borracha; mudar uma parede numa casa construída custa uma obra. Com os sites é igual: mudar a organização de um site no papel demora segundos, e mudar a organização de um site já escrito demora horas, porque obriga a mexer em todas as páginas e em todas as ligações.

Um site feito sem plano tem sintomas que se reconhecem: páginas acrescentadas à medida que alguém se lembra delas, menus diferentes em páginas diferentes, informação repetida em dois sítios e informação que falta, páginas a que só se chega por acaso. Quem visita um site assim perde-se, e desiste.

O planeamento que vais fazer tem três passos, e cada um responde a uma pergunta:

1. **Para quem é e para que serve?** O utilizador e a sua necessidade.
2. **O que vai ter?** O conteúdo.
3. **Como está organizado?** O mapa do site, com as páginas e as ligações, e os wireframes, com a arrumação de cada página.

Faz-se tudo em papel. O papel é rápido, deita-se fora sem pena, e não te distrai com cores e tipos de letra, que são uma decisão para mais tarde. Um plano simples, feito numa aula, chega para evitar a maior parte dos problemas.

### O utilizador e a necessidade

A primeira pergunta de qualquer site é para quem é. A resposta "para toda a gente" não serve, porque um site feito para toda a gente acaba por não servir bem ninguém. Uma boa resposta é concreta: "alunos do 10.º ano que querem estudar HTML sozinhos, em casa, a partir do telemóvel".

A segunda pergunta é o que é que essa pessoa quer fazer no site. A isso chama-se a **tarefa principal**. Num site de receitas, a tarefa principal pode ser encontrar uma receita que se faça com o que há no frigorífico. No site de um clube, pode ser saber quando é o próximo encontro e como participar. A tarefa principal decide o que aparece primeiro, o que fica no menu e o que pode ficar mais escondido.

Ajuda muito imaginar uma pessoa concreta, com nome, e contar a história da sua visita: "A Marta tem teste de HTML na sexta-feira e quer um livro para estudar. Abre o site, vê logo a lista dos livros, escolhe um, e fica a saber onde o encontrar." Se a história não se conseguir contar com o teu plano, o plano tem um problema.

### O conteúdo

Antes de organizar as páginas, é preciso saber o que se vai pôr nelas. Faz-se uma lista de todo o conteúdo, a que se chama **inventário de conteúdos**: os textos, as imagens, as listas, as tabelas, as informações de contacto. Para cada coisa, anota-se também de onde vem: se és tu que a escreves, se vem de uma fonte que tens de citar, ou se é inventada para o exemplo.

Nos sites que vais fazer este ano, o conteúdo pode ser inventado, desde que seja realista. O que nunca podes pôr são dados pessoais verdadeiros: moradas, números de telefone, datas de nascimento, fotografias de colegas ou de outras pessoas sem autorização. Um site na Web pode ser visto por qualquer pessoa, e o que lá se põe pode ser copiado e guardado por quem o vê.

Com o inventário feito, agrupam-se as coisas parecidas. Os grupos que aparecem são, muitas vezes, as páginas do site ou as partes de uma página.

### O mapa do site

O **mapa do site** (em inglês, *sitemap*) é um desenho de todas as páginas de um site e das ligações que levam a cada uma. Cada página é uma caixa, com o nome da página e uma frase a dizer para que serve. As ligações são linhas entre as caixas. A página inicial fica no topo, e as páginas que se abrem a partir dela ficam por baixo, como numa árvore genealógica.

No papel, desenha-se com caixas e linhas. Escrito, pode fazer-se assim, com a indentação a mostrar o que se abre a partir de quê:

```text
Início
├── Página de cada recurso (uma página por recurso, todas com a mesma forma)
└── Sobre
```

Um bom mapa cumpre algumas regras, e cada uma evita um problema concreto:

- todas as páginas se alcançam a partir da página inicial, seguindo ligações. Uma página a que não se chega por nenhuma ligação é uma **página perdida**: existe, mas ninguém a encontra;
- de todas as páginas se volta à página inicial, pelo menos pelo menu;
- o menu, que se repete em todas as páginas, leva às páginas principais, que são as do primeiro nível da árvore. As páginas mais específicas alcançam-se a partir delas;
- não é preciso carregar em muitas ligações para chegar a qualquer página. Num site pequeno, duas ou três chegam. Se precisares de mais, a árvore está funda demais;
- cada página tem um nome claro, que diz o que se lá encontra. É o nome que vai aparecer no menu.

O mapa desenha, para cada página, o caminho principal a partir da página inicial. As ligações do menu e as ligações de regresso, que se repetem em todas as páginas, não se desenham, para o mapa não ficar cheio de linhas. Repara também que o menu mostra só as páginas principais. A página de um recurso, na Estante Digital, não está no menu, porque há muitas: chega-se a ela pela lista de recursos na página inicial.

### O wireframe

O mapa diz que páginas existem. O **wireframe** diz como cada página está arrumada. É um esboço de uma página, feito só com caixas e com a indicação do tipo de conteúdo de cada caixa, sem cores, sem tipos de letra e sem imagens verdadeiras. O nome vem do inglês e quer dizer estrutura de arame, porque mostra só o esqueleto da página.

Há umas convenções simples que toda a gente usa, para que qualquer pessoa leia um wireframe sem explicação:

- uma caixa com um X lá dentro, ou `[X]`, é uma imagem;
- linhas onduladas ou riscos são texto corrido; um texto escrito em maiúsculas é um título;
- uma palavra sublinhada é uma ligação;
- cada zona grande (cabeçalho, menu, conteúdo, rodapé) é uma caixa com o nome escrito ao lado.

Desenham-se duas versões de cada página importante, porque vai ser vista em ecrãs muito diferentes:

- o **wireframe estreito**, para o ecrã de um telemóvel, com uma só coluna: tudo fica empilhado, de cima para baixo;
- o **wireframe largo**, para o ecrã de um computador, onde algumas coisas podem ficar lado a lado.

O estreito é o mais útil dos dois, por uma razão que vais perceber no guia 02: numa só coluna, a ordem das caixas de cima para baixo é a ordem em que o conteúdo vai estar escrito no HTML, e é a ordem em que um leitor de ecrã o vai ler. A ordem de leitura tem de ser a mesma nas duas versões: no largo as coisas podem ficar lado a lado, mas o que vem primeiro no estreito continua a vir primeiro no largo, lido da esquerda para a direita e de cima para baixo.

Ao lado de cada zona do wireframe escreve-se uma **anotação** a dizer o que é: "cabeçalho com o nome do site", "menu", "lista de livros com ligação para cada um". No guia 02 vais acrescentar a cada anotação o nome do elemento HTML que lhe corresponde, e o wireframe passa a ser a planta do teu código.

### O mapa e os wireframes têm de concordar

O mapa e os wireframes descrevem o mesmo site por dois lados, e por isso têm de dizer a mesma coisa. Antes de dares o plano por acabado, faz estas verificações:

- cada ligação desenhada num wireframe tem de levar a uma página que existe no mapa. Se o wireframe da página inicial tem uma ligação "Contactos", o mapa tem de ter uma página Contactos. Se não tiver, é uma **ligação sem destino**, que no site verdadeiro vai dar o erro 404;
- cada linha do mapa tem de aparecer em algum wireframe, como uma ligação desenhada. Se o mapa diz que da página inicial se vai à página Sobre, o wireframe da página inicial tem de mostrar onde está essa ligação;
- os nomes são os mesmos nos dois. Se no mapa a página se chama "Sobre" e no menu do wireframe se chama "Quem somos", uma pessoa que leia os dois não sabe se são a mesma página;
- o menu é igual em todos os wireframes, com as mesmas opções pela mesma ordem.

Estas verificações apanham no papel os erros que, no site verdadeiro, só se descobrem quando um utilizador carrega numa ligação e lhe aparece uma página de erro.

### O tema do teu site

Ao longo deste ano vais construir um site teu, que vai crescendo bloco a bloco: primeiro a estrutura em HTML, depois o aspeto com CSS, depois a adaptação a ecrãs de todos os tamanhos, depois o comportamento com JavaScript, e no fim a publicação. O tema és tu que escolhes. Estes critérios ajudam a escolher bem:

- escolhe uma coisa de que gostes e que conheças. Vais trabalhar nela o ano todo, e é mais fácil escrever conteúdo sobre um assunto que conheces;
- tem de dar para várias páginas. Pensa se consegues imaginar pelo menos três páginas diferentes sobre o tema;
- ajuda se o tema tiver coleções de coisas parecidas: receitas, jogos, livros, jogadores, sítios, eventos, animais. Mais à frente no ano vais mostrar listas destas coisas com JavaScript e fazer um formulário, e um tema com coleções dá-te material para isso;
- o conteúdo pode ser inventado, mas sem dados pessoais verdadeiros e sem nada que não pudesses mostrar numa aula;
- começa pequeno. Um site com três páginas bem feitas vale mais do que um site com vinte páginas vazias. Podes sempre acrescentar.

Algumas ideias, só para te pôr a pensar: o clube de xadrez da escola, as receitas da tua família, os trilhos a pé da tua zona, os jogos de que mais gostas, um clube de leitura, uma banda imaginária, um abrigo de animais imaginário, a modalidade desportiva que praticas. Os exemplos dos guias usam a Estante Digital, um site de recursos de estudo, mas o teu site não tem de ser parecido com ela.

### Preencher o modelo do brief

O plano do teu site fica registado no [modelo do brief e wireframe](../projeto/modelos/brief-e-wireframe.md), que está na pasta do projeto. **Brief** é uma palavra inglesa que se usa em Portugal para o resumo de um trabalho antes de começar: o que é, para quem, e o que tem de ter. O modelo tem campos entre chavetas duplas, que são os sítios onde escreves as tuas respostas. Alguns campos usam palavras que ainda não conheces, porque o mesmo modelo serve para o ano todo. Esta tabela explica cada campo e diz quando se preenche.

| Campo do modelo | O que quer dizer | Quando se preenche |
| --- | --- | --- |
| O título, no topo | O nome provisório do teu site | Agora |
| A linha a seguir ao título: UC, competências, bloco e duração | A identificação do trabalho. Escreve UC02833, o bloco F01, as competências do quadro no início deste guia, e o tempo que demoraste | Agora |
| Utilizador e necessidade | Para quem é o site e o que essa pessoa precisa | Agora |
| Resultado útil para essa pessoa | O que a pessoa consegue fazer depois de usar o site: a tarefa principal | Agora |
| Conteúdo necessário e respetiva origem | O inventário de conteúdos, com a origem de cada coisa | Agora |
| Limites do trabalho | O que o teu site não vai ter, para caber no tempo. Por exemplo: "não tem contas de utilizador" ou "tem só três páginas nesta fase" | Agora |
| Páginas e ligações entre páginas (sitemap) | O mapa do site | Agora |
| Hierarquia de informação | O que é mais importante em cada página, por ordem | Agora |
| Wireframe de largura pequena e larga | Os dois wireframes, desenhados em papel e fotografados ou digitalizados | Agora |
| Relação entre zonas desenhadas e elementos HTML | O elemento HTML de cada zona do wireframe | No bloco de HTML, no guia 02 |
| Ação do utilizador, evento, dados e resposta visível | O que acontece quando a pessoa faz alguma coisa na página | Nos blocos de JavaScript. Por agora escreve "ainda não" |
| Formulários e mensagens | Os campos que a pessoa preenche e as mensagens que recebe | No bloco de formulários. Por agora escreve "ainda não" |
| Percurso por teclado e foco | A ordem em que se chega às ligações só com o teclado | No bloco de HTML |
| Critérios de aceitação | As condições que o site tem de cumprir para estar pronto nesta fase. Por exemplo: "a partir da página inicial chega-se a todas as páginas em duas ligações ou menos" | Agora |
| Verificação com um colega antes de implementar | O que o colega conseguiu ou não conseguiu encontrar no teu plano | No fim da prática guiada |
| Artefacto de planeamento e versão Git | Onde está guardado o plano e em que versão | No bloco de Git |

## Exemplo explicado: o plano da Estante Digital (30 min)

Neste exemplo faz-se, passo a passo, o plano do site que os guias vão construir ao longo do ano: a Estante Digital, um site onde uma turma reúne os recursos de estudo que recomenda. O conteúdo é todo inventado.

### Passo 1: A necessidade

Tudo começa com um problema real de quem vai usar o site. Os alunos que começam a aprender a fazer páginas web encontram centenas de vídeos, livros e sítios, e não sabem por onde começar nem quais valem a pena. A turma já experimentou vários e sabe quais ajudaram. A necessidade é esta: ter num só lugar uma pequena lista de recursos de confiança, escolhidos por quem já os usou.

### Passo 2: O utilizador e a tarefa principal

Para quem é? Para alunos de Desenvolvimento de Aplicações, sobretudo os que estão a começar, que querem estudar sozinhos, muitas vezes a partir do telemóvel.

Qual é a tarefa principal? Encontrar um recurso para estudar um assunto e saber onde o arranjar.

A história de uma visita, que o plano tem de permitir: "A Marta tem teste de HTML na sexta-feira. Abre a Estante Digital no telemóvel, vê logo que há livros, vídeos e sítios, escolhe o livro Primeiros passos na Web, lê para quem é, e fica a saber que está na biblioteca e a que horas a biblioteca abre."

### Passo 3: O inventário de conteúdos

A lista de tudo o que o site vai ter, com a origem de cada coisa:

| Conteúdo | Tipo | Origem |
| --- | --- | --- |
| Apresentação do site: o que é e para quem | Texto curto | Escrito pela turma |
| Seis recursos, cada um com nome, tipo e descrição curta: dois livros, dois vídeos, dois sítios ou aplicações | Lista | Inventado para o exemplo |
| Para cada recurso com página própria: para quem é, o que se aprende, como usar, onde encontrar | Texto e listas | Inventado para o exemplo |
| Capa de cada livro | Imagem | Desenhada para o exemplo |
| Horário da biblioteca | Tabela | Inventado para o exemplo |
| Porque existe o site e como se escolhem os recursos | Texto | Escrito pela turma |

Agrupando as coisas parecidas, aparecem três grupos: a apresentação e a lista dos recursos, que dão uma página de entrada; a informação completa de cada recurso, que dá uma página por recurso; e a explicação sobre o site, que dá uma página própria.

### Passo 4: As páginas

Dos grupos saem as páginas:

- **Início**: a apresentação do site e a lista dos seis recursos, arrumada por tipo. É aqui que a Marta começa.
- **Página de cada recurso**: uma por recurso, todas com a mesma forma. Nesta fase, só o livro Primeiros passos na Web tem página; os outros têm só a descrição curta na lista.
- **Sobre**: porque existe o site e como se escolhem os recursos.

Houve uma alternativa que se pôs de lado: fazer uma página para cada tipo (uma para os livros, uma para os vídeos, uma para os sítios). Com só seis recursos, isso obrigava a Marta a carregar numa ligação a mais só para ver a lista, e as três páginas ficavam quase vazias. Com poucos recursos, a lista inteira cabe na página inicial. Se um dia houver cinquenta, a decisão muda.

### Passo 5: O mapa do site

```text
Início
├── Página de cada recurso (por agora, só Primeiros passos na Web)
└── Sobre
```

Verificam-se as regras do mapa. Todas as páginas se alcançam a partir do Início: a página do livro, pela lista de recursos, e o Sobre, pelo menu. De todas as páginas se volta ao Início, pelo menu. O menu leva às páginas principais, que são duas: Início e Sobre. As páginas dos recursos não estão no menu, porque vão ser muitas; alcançam-se pela lista. Qualquer página fica a uma ligação de distância do Início.

### Passo 6: O wireframe estreito da página inicial

Este é o wireframe da página inicial num telemóvel, com as anotações à direita:

```text
┌──────────────────────────────┐
│ [X] Estante Digital          │   cabeçalho: logótipo e nome
│ Início   Sobre               │   menu
├──────────────────────────────┤
│ TÍTULO DA PÁGINA             │   título da página
│ ~~~~~~~~~~~~~~~~~~~~~~~~~~   │   texto de apresentação
│ ~~~~~~~~~~~~~~~~~~           │
│                              │
│ Livros                       │   grupo 1, com ligação
│ - Primeiros passos na Web    │
│ - Pequeno dicionário         │
│                              │
│ Vídeos                       │   grupo 2
│ - ~~~~~~~~~~~~~~~            │
│ - ~~~~~~~~~~~~~~~            │
│                              │
│ Sítios e aplicações          │   grupo 3
│ - ~~~~~~~~~~~~~~~            │
│ - ~~~~~~~~~~~~~~~            │
├──────────────────────────────┤
│ Nota sobre o site            │   rodapé
└──────────────────────────────┘
```

Repara na ordem, de cima para baixo: primeiro o nome do site e o menu, que dizem onde a pessoa está e para onde pode ir; depois o assunto da página e a apresentação; depois os três grupos de recursos; no fim, a nota sobre o site. É a ordem pela qual a Marta precisa das coisas. Esta ordem, do que a Marta precisa primeiro para o que precisa depois, é a **hierarquia de informação** da página inicial, e é ela que se escreve nesse campo do brief. Só o primeiro livro é uma ligação, porque é o único que já tem página; os outros são só texto. No papel, essa ligação desenhava-se sublinhada; aqui, a anotação diz "com ligação".

### Passo 7: O wireframe largo da página inicial

No ecrã de um computador há espaço para pôr os três grupos lado a lado, e o menu passa para a mesma linha do nome do site:

```text
┌──────────────────────────────────────────────────────────────┐
│ [X] Estante Digital                          Início   Sobre  │
├──────────────────────────────────────────────────────────────┤
│ TÍTULO DA PÁGINA                                             │
│ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     │
│ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                           │
│                                                              │
│ ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│ │Livros        │  │Vídeos        │  │Sítios e      │         │
│ │- Primeiros   │  │- ~~~~~~~~~   │  │aplicações    │         │
│ │- Pequeno     │  │- ~~~~~~~~~   │  │- ~~~~~~~~~   │         │
│ │              │  │              │  │- ~~~~~~~~~   │         │
│ └──────────────┘  └──────────────┘  └──────────────┘         │
├──────────────────────────────────────────────────────────────┤
│ Nota sobre o site                                            │
└──────────────────────────────────────────────────────────────┘
```

A arrumação mudou, mas a ordem de leitura é a mesma: o nome e o menu, o assunto, a apresentação, os livros, os vídeos, os sítios e a nota final. Lendo da esquerda para a direita e de cima para baixo, encontra-se tudo pela mesma ordem do wireframe estreito.

### Passo 8: O wireframe da página de um recurso

A página do livro, no telemóvel:

```text
┌──────────────────────────────┐
│ [X] Estante Digital          │   cabeçalho igual ao da página inicial
│ Início   Sobre               │
├──────────────────────────────┤
│ TÍTULO DO RECURSO            │   título: o nome do recurso
│ ~~~~~~~~~~~~~~~~~~~~~~~~~~   │
│ ┌────────────────────┐       │   capa do livro
│ │         X          │       │
│ └────────────────────┘       │
│ legenda da capa              │
│                              │
│ Para quem é                  │   secções da ficha do recurso
│ ~~~~~~~~~~~~~~~~~~~~~~       │
│ O que vais aprender          │
│ - ~~~~~~~~~~~~~~~            │
│ - ~~~~~~~~~~~~~~~            │
│ Como o usar                  │
│ 1. ~~~~~~~~~~~~~~            │
│ 2. ~~~~~~~~~~~~~~            │
│ Onde o encontrar             │
│ ~~~~~~~~~~~~~~~~~~~~~~       │
│ ┌────────────────────┐       │   horário da biblioteca
│ │  TABELA: horário   │       │
│ └────────────────────┘       │
│                              │
│ ┌──────────────────────┐     │   caixa secundária
│ │Dica de quem já o leu │     │
│ └──────────────────────┘     │
│ Voltar à lista               │   ligação de regresso
├──────────────────────────────┤
│ Nota sobre o site            │   rodapé igual ao da página inicial
└──────────────────────────────┘
```

O cabeçalho e o rodapé são iguais aos da página inicial, para que a Marta reconheça que continua no mesmo site. A seguir ao nome do livro vem a capa, que ajuda a reconhecê-lo na estante, e depois as partes da ficha, pela ordem das perguntas que a Marta faria: é para mim? o que vou aprender? como o uso? onde o encontro? A dica fica numa caixa à parte, porque é um comentário, e não informação essencial. No fim há uma ligação para voltar à lista. Na versão larga, a caixa da dica podia ficar ao lado da ficha, à direita, sem mudar a ordem de leitura.

### Passo 9: Verificar a coerência

Faz-se a verificação da secção "O mapa e os wireframes têm de concordar", ligação a ligação.

| Ligação desenhada | Onde está | Destino no mapa | Resultado |
| --- | --- | --- | --- |
| Início, no menu | Todas as páginas | Início | Existe |
| Sobre, no menu | Todas as páginas | Sobre | Existe |
| Primeiros passos na Web, na lista | Página inicial | Página do livro | Existe |
| Voltar à lista | Página do livro | Início | Existe |

Numa primeira versão do wireframe da página do livro havia uma caixa "Recursos parecidos", com ligações para o outro livro e para os dois vídeos. A verificação apanhou o problema: essas páginas não estão no mapa, porque ainda não existem. Seriam ligações sem destino. A decisão foi trocar essa caixa pela "Dica de quem já o leu", que não tem ligações. Quando as páginas desses recursos existirem, a caixa de recursos parecidos pode voltar, e o mapa e os wireframes mudam os dois ao mesmo tempo.

Os nomes batem certo: "Início" e "Sobre" são iguais no mapa e nos menus, e o menu é o mesmo nos dois wireframes.

Com a verificação feita, escrevem-se no brief os **critérios de aceitação** desta fase, as condições que o site tem de cumprir para estar pronto: a partir do Início chega-se a qualquer página com uma só ligação; o menu é igual em todas as páginas, com Início e Sobre por esta ordem; nenhuma ligação fica sem destino.

### Passo 10: O percurso de um utilizador

Por fim, conta-se a história do passo 2 com o plano na mão, apontando para cada caixa. A Marta abre o site e está no Início. Vê o título e os três grupos, e no grupo Livros vê o nome sublinhado do Primeiros passos na Web. Carrega nele e chega à página do livro. Lê "Para quem é" e confirma que é para ela. Desce até "Onde o encontrar", vê a estante e o horário. Carrega em "Voltar à lista" e volta ao Início.

A história conta-se sem nenhum salto que o plano não mostre. O plano está pronto para ser passado a HTML, que é o que o guia 02 faz.

## Prática guiada: o plano do teu site (55 min)

Agora fazes o plano do teu site, em papel, pelos mesmos passos do exemplo. Tem aberto o [modelo do brief](../projeto/modelos/brief-e-wireframe.md) e escreve as respostas nos campos que a tabela da secção "Preencher o modelo do brief" diz que se preenchem agora.

### Passo 1: Escolhe o tema (5 min)

Lê os critérios da secção "O tema do teu site" e escolhe o teu. Escreve-o no topo da folha, com um nome provisório para o site. Se estiveres indeciso entre dois, escolhe aquele de que consegues imaginar mais páginas.

### Passo 2: O utilizador e a tarefa principal (5 min)

Preenche os campos "Utilizador e necessidade" e "Resultado útil para essa pessoa". Sê concreto: não "toda a gente", mas uma pessoa como a Marta do exemplo. Escreve, em duas ou três frases, a história de uma visita dessa pessoa ao teu site.

### Passo 3: O inventário de conteúdos (10 min)

Preenche o campo "Conteúdo necessário e respetiva origem", como no passo 3 do exemplo: uma linha por conteúdo, com o tipo e a origem. Depois agrupa as coisas parecidas. Preenche também o campo "Limites do trabalho": o que o teu site não vai ter nesta fase.

### Passo 4: O mapa do site (10 min)

Decide as páginas a partir dos grupos do inventário, e desenha o mapa numa folha lisa, com uma caixa por página e linhas para as ligações. Para o laboratório do guia 02 precisas de pelo menos duas páginas ligadas entre si; se conseguires imaginar três, melhor. Escreve dentro de cada caixa o nome da página e uma frase a dizer para que serve. Confirma as regras da secção "O mapa do site": consegues chegar a todas as páginas a partir do Início, e voltar de todas?

### Passo 5: Os wireframes (15 min)

Desenha o wireframe estreito da tua página inicial, com as anotações ao lado de cada zona, e depois o wireframe largo da mesma página. Confirma que a ordem de leitura é a mesma nos dois. Depois preenche o campo "Hierarquia de informação" com a ordem das zonas do teu wireframe estreito, como no passo 6 do exemplo. Se tiveres tempo, desenha também o wireframe estreito da segunda página. Não gastes tempo em pormenores: caixas, riscos para o texto e um X para as imagens chegam.

### Passo 6: Verificar com um colega (10 min)

Faz primeiro, sozinho, a verificação da coerência entre o mapa e os wireframes, como no passo 9 do exemplo, e corrige o que encontrares. Depois troca de plano com um colega. Sem lhe explicares nada, pede-lhe que encontre, no teu plano, uma informação concreta do teu site (por exemplo, "onde vejo quando é o próximo torneio?") e que te diga, apontando, por onde passou. Se ele se perder, o teu plano tem um problema: pergunta-lhe onde hesitou e corrige. Escreve o que aconteceu no campo "Verificação com um colega antes de implementar". Por fim, escreve no campo "Critérios de aceitação" duas ou três condições que o teu site tem de cumprir nesta fase, como as do passo 9 do exemplo.

Guarda a folha do mapa e dos wireframes. Fotografa-a e guarda as fotografias, com a cópia do brief, numa pasta com o nome do teu site, em minúsculas, sem espaços nem acentos e com hífenes entre as palavras, por exemplo `clube-de-xadrez`. É essa a pasta do teu site: no bloco de Git, a seguir a este, vais pô-la sob controlo de versões, e no laboratório do guia 02 vais escrever lá dentro estas páginas em HTML.

## Laboratório (45 min)

O [laboratório](01-web-e-planeamento-laboratorio.md) faz-se no computador. Vais abrir as ferramentas do programador pela primeira vez, ver o DOM de uma página no separador Elements, mudar o DOM e ver que o ficheiro não muda, visitar o primeiro site da história e ver o que o browser acrescenta ao seu código, e seguir no separador Network os pedidos, os endereços e os códigos de resposta, incluindo um 404 provocado de propósito.

## Erros comuns

### "O meu site é para toda a gente"

Um site para toda a gente não ajuda a decidir nada: nem o que aparece primeiro, nem o que fica no menu, nem a forma de escrever. Escolhe uma pessoa concreta e a sua tarefa principal, e deixa-as decidir por ti.

### Um tema grande demais

"Um site sobre futebol" dá para mil páginas, e nenhuma fica feita. "O site da equipa de futebol da escola, com os jogos da época e os jogadores" dá para três páginas bem feitas. Começa pequeno e acrescenta depois.

### Páginas soltas no mapa

Uma caixa no mapa sem nenhuma linha a chegar-lhe é uma página a que ninguém consegue ir. Todas as páginas têm de estar ligadas, direta ou indiretamente, à página inicial.

### Um menu diferente em cada página

Se o menu muda de página para página, a pessoa tem de reaprender o site em cada página. O menu é igual em todos os wireframes, com as mesmas opções pela mesma ordem.

### Ligações para páginas que não estão no mapa

É o erro que o passo 9 do exemplo apanhou. Cada ligação desenhada tem de ter destino no mapa. No site verdadeiro, uma ligação sem destino dá o erro 404.

### Um wireframe com cores, tipos de letra e desenhos bonitos

O wireframe serve para decidir a arrumação, e não o aspeto. Cada minuto gasto a colorir é um minuto a menos a pensar na ordem e nas ligações. O aspeto decide-se no bloco de CSS.

### A ordem muda entre o wireframe estreito e o largo

Se, no largo, a lista aparece antes do título, e no estreito aparece depois, a página vai ser lida numa ordem num ecrã e noutra ordem noutro. A ordem de leitura é uma só: arruma-se lado a lado no largo, mas sem trocar a ordem.

### Confundir a Internet com a Web

A Internet é a rede que transporta os dados; a Web é o serviço de páginas ligadas que usa essa rede. O correio eletrónico usa a Internet e não é a Web.

### Enviar a um colega um endereço `file://`

Um endereço `file://` aponta para um ficheiro no teu disco, e só funciona no teu computador. Para um colega ver o teu site, tens de lhe dar os ficheiros, ou o site tem de estar publicado num servidor.

## Consolidação (15 min)

A Internet é a rede que transporta os dados, e a Web é o serviço de páginas ligadas que a usa, proposto em 1989 no CERN e posto a funcionar em 1990 com o HTML, o HTTP e o URL. Uma página é feita de três linguagens: o HTML diz o que cada coisa é, o CSS diz como se apresenta e o JavaScript diz como se comporta. O browser pede os ficheiros, constrói o DOM a partir do HTML e desenha a página a partir do DOM, que pode ser diferente do ficheiro porque o browser corrige e acrescenta, e porque o JavaScript o muda. O browser é o cliente, que faz pedidos, e o servidor responde, com um código que diz como correu: 200 se correu bem, 404 se não existe. O URL tem protocolo, domínio e caminho. Antes de escrever um site, planeia-se: para quem é e que tarefa principal serve, que conteúdo tem, que páginas e ligações tem, no mapa, e como se arruma cada página, nos wireframes estreito e largo, com a mesma ordem de leitura. O mapa e os wireframes têm de concordar, para que não haja ligações sem destino.

Confirma o que já consegues fazer:

- [ ] Consigo explicar a diferença entre a Internet e a Web, com um exemplo de um serviço que usa a Internet e não é a Web.
- [ ] Consigo dizer, perante um pedaço de código, se é HTML, CSS ou JavaScript, e o trabalho de cada linguagem.
- [ ] Consigo explicar porque é que o DOM pode ser diferente do ficheiro, com um exemplo.
- [ ] Consigo partir um endereço em protocolo, domínio e caminho.
- [ ] Consigo dizer o que querem dizer os códigos 200 e 404.
- [ ] Consigo descrever o utilizador e a tarefa principal de um site.
- [ ] Consigo desenhar o mapa de um site e os wireframes estreito e largo de uma página, com a mesma ordem de leitura.
- [ ] Consigo encontrar ligações sem destino comparando o mapa com os wireframes.

### 1. Conta o percurso de um utilizador (5 min)

Com o plano do teu site na mão, conta a um colega, em voz alta, a história de uma visita, como no passo 10 do exemplo: quem é a pessoa, o que quer, por onde entra, em que carrega e onde encontra o que procurava, apontando para cada caixa do mapa e dos wireframes. É esta explicação que o professor vai querer ouvir como evidência do bloco.

### 2. Encontra no plano de um colega (5 min)

Troca de plano com outro colega, que não seja o do passo 6 da prática guiada. Ele diz-te uma informação que o site dele tem, e tu tens de a encontrar no plano, sem explicações. Depois trocam os papéis.

### 3. Regista as tuas dificuldades (5 min)

Escreve duas ou três linhas sobre o que te custou mais neste bloco: perceber a diferença entre o ficheiro e o DOM, os códigos de resposta, escolher o tema, desenhar o mapa ou manter a mesma ordem nos dois wireframes. Guarda-as junto do plano.

**Evidência a guardar:** o brief preenchido, o mapa do site e os wireframes estreito e largo da página inicial, com as anotações; a nota da verificação com o colega; as respostas do laboratório.

## A seguir

O [laboratório](01-web-e-planeamento-laboratorio.md) ocupa 45 minutos e a [ficha de exercícios](01-web-e-planeamento-exercicios.md) 50.

O plano que fizeste é a planta do teu site. A seguir vem o bloco de Git, onde vais aprender a guardar versões da pasta do teu site, começando pelo plano, para que nenhuma alteração se perca. Depois, no guia [HTML e semântica](02-html-e-semantica.md), vais transformar o plano em páginas de verdade, escritas em HTML, com cada zona do wireframe a dar um elemento.

## Referências

- Unidade de competência UC02833, *Conceber aplicações para a web na vertente frontend*, do referencial de Técnico/a de Desenvolvimento de Software (481RA116), nível 4. A ficha oficial pode ser consultada no [Catálogo Nacional de Qualificações](https://catalogo.snq.gov.pt/ucDetalhe/357824).
- CERN, [o primeiro site da história](https://info.cern.ch/), em inglês.
- MDN Web Docs, [como a Web funciona](https://developer.mozilla.org/pt-BR/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works), [o que são as ferramentas do programador](https://developer.mozilla.org/pt-BR/docs/Learn_web_development/Howto/Tools_and_setup/What_are_browser_developer_tools) e [a lista dos códigos de resposta do HTTP](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Reference/Status), em português do Brasil.

![Rodapé](../imagens/rodape.png)
