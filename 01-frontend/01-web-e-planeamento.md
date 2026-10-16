![Cabeçalho](../imagens/cabecalho.png)

# A Web, os utilizadores e o planeamento

Módulo Conceber aplicações para a web na vertente frontend. Este guia explica como funciona a Web e como se planeia um site antes de o escrever. Lês ao teu ritmo, e não precisas de o ler de uma vez. Para praticar, há o [laboratório](01-web-e-planeamento-laboratorio.md) e a [ficha de exercícios](01-web-e-planeamento-exercicios.md) deste tema.

É o primeiro guia da disciplina, e não precisas de saber programar. O guia tem duas metades. A primeira explica o que acontece entre escreveres um endereço e veres uma página. É a base de tudo o que vais fazer este ano. A segunda explica como se planeia um site antes de o escrever. É a que vais usar logo a seguir, no plano do teu site. Na aula, o professor apresenta as ideias principais, e cada secção fica aqui para a releres. Neste tema ainda não escreves código: isso começa no tema 02, HTML e semântica.

## Neste guia

1. O que vais aprender
2. O que já sabes e vais usar
3. A Internet e a Web não são a mesma coisa
4. Uma história curta da Web
5. Três linguagens, três trabalhos
6. O browser
7. Cliente e servidor
8. O endereço de uma página
9. O que se diz num pedido e numa resposta
10. As ferramentas do programador
11. Antes do editor: planear
12. O utilizador e a necessidade
13. O conteúdo
14. O mapa do site
15. O wireframe
16. O mapa e os wireframes têm de concordar
17. O tema do teu site
18. Preencher o modelo do brief
19. Exemplo guiado: o plano da Estante Digital
20. Erros frequentes
21. Palavras novas deste guia
22. Verificar o que aprendeste
23. O que vem a seguir
24. Para saber mais

## O que vais aprender

No fim deste guia, consegues:

- explicar a diferença entre a Internet e a Web, e contar em poucas frases como a Web nasceu e mudou;
- dizer que trabalho faz cada uma das três linguagens de uma página: o HTML, o CSS e o JavaScript;
- explicar o que o browser faz com os ficheiros de uma página, o que é o DOM e porque pode ser diferente do ficheiro;
- descrever a conversa entre o cliente e o servidor, partir um endereço nas suas partes e ler os códigos de resposta mais comuns;
- planear o teu site, com um tema do menu do professor: para quem é, para que serve e que conteúdo tem;
- desenhar o mapa de um site e os wireframes estreito e largo das suas páginas, e confirmar que concordam.

## O que já sabes e vais usar

Este guia não dá por sabido nada de programação. Precisas só disto:

- Usar um browser como utilizador: escrever um endereço, abrir um separador novo e voltar à página anterior. Vem do dia a dia.
- Encontrar um ficheiro numa pasta do computador. Vem do dia a dia.
- Desenhar caixas e linhas com papel e lápis, porque o planeamento faz-se primeiro à mão.

## A Internet e a Web não são a mesma coisa

No dia a dia, muita gente diz "a Internet" quando quer dizer "a Web", e ao contrário. Perceber a diferença ajuda a perceber tudo o resto.

A **Internet** é a rede que liga computadores do mundo inteiro. É feita de coisas físicas: cabos, antenas, routers, satélites, cabos no fundo do mar. A única coisa que faz é transportar dados de um computador para outro. Não sabe o que são páginas, mensagens ou vídeos: só leva e traz pedaços de dados.

A **Web** (de *World Wide Web*, teia do tamanho do mundo) é um dos serviços que usam a Internet para funcionar. É o conjunto de páginas, ligadas umas às outras por ligações, que se leem com um browser. Há outros serviços que usam a mesma Internet sem serem a Web: o correio eletrónico, as chamadas de vídeo, os jogos em rede.

Uma comparação ajuda. A Internet é como a rede de estradas de um país: liga todas as terras, mas não transporta nada sozinha. A Web é como uma empresa de autocarros que usa essas estradas. O correio é outra empresa, que usa as mesmas estradas para outro fim. Se as estradas fecharem, nenhuma das empresas funciona. Mas as estradas não são nenhuma das empresas.

Nesta disciplina vais fazer páginas para a Web. Como a Internet as transporta é matéria da disciplina de Sistemas e Redes. Aqui, vais ficar a saber só o necessário para perceberes o que acontece quando alguém abre uma página tua.

## Uma história curta da Web

A Web é mais nova do que muitos dos teus professores. Conhecer a sua história ajuda a perceber porque é que as páginas são feitas da forma que vais aprender.

Em 1989, Tim Berners-Lee era investigador no CERN, um grande laboratório europeu de física perto de Genebra. Nesse ano, propôs uma forma de os cientistas partilharem documentos entre computadores diferentes, com ligações de uns documentos para os outros. Em 1990 pôs a ideia a funcionar, com o primeiro browser, o programa que mostra as páginas, e o primeiro servidor. Um servidor é um computador sempre ligado, que guarda as páginas e as envia a quem as pede. Para isso, inventou três coisas que ainda hoje usamos:

- uma linguagem para escrever os documentos, o **HTML**;
- umas regras para um computador pedir um documento a outro e o receber, o **HTTP**;
- uma forma de dar um endereço único a cada documento, o **URL**.

Vais aprender as três neste tema e no tema 02, HTML e semântica.

Em 1991, o primeiro site ficou acessível a qualquer pessoa. Explicava o próprio projeto da Web. O que hoje se visita é uma cópia de 1992, guardada pelo CERN, a partir do endereço `info.cern.ch`. No laboratório deste tema vais visitá-la e olhar para o seu código.

Em 1993, o CERN tornou a tecnologia da Web livre para toda a gente, sem pagamento. No mesmo ano apareceu o Mosaic, um dos primeiros browsers fáceis de usar. Foi o primeiro a tornar-se popular, e mostrava imagens no meio do texto. A Web deixou de ser uma ferramenta de cientistas.

Em 1994 foi criado o W3C, uma organização que junta empresas e universidades para combinar as regras da Web. Com regras combinadas, uma página funciona em todos os browsers. Em 1995 apareceu o **JavaScript**, para dar comportamento às páginas. Em 1996 foi publicada a primeira versão do **CSS**, para separar o aspeto das páginas da sua estrutura.

A partir de 2007, espalharam-se os telemóveis com ecrã tátil e um browser completo. Hoje, uma grande parte das visitas aos sites é feita a partir de telemóveis. As páginas passaram a ter de funcionar em ecrãs pequenos e grandes, e é esse o assunto do tema da responsividade.

Hoje o HTML já não tem versões numeradas. É um padrão vivo, que vai sendo atualizado aos poucos, e os browsers continuam a saber mostrar as páginas antigas. Vais encontrar o nome HTML5 em muitos sítios: é o nome que ficou para o HTML moderno.

Desta história ficam três ideias que vais reencontrar:

- uma página é feita de três linguagens, que nasceram em alturas diferentes para trabalhos diferentes;
- os browsers continuam a mostrar páginas escritas há mais de trinta anos, e por isso aceitam muita coisa mal escrita sem se queixarem. No tema 02 vais ver porque é que isso é uma vantagem e um perigo;
- as páginas de hoje têm de funcionar em ecrãs de todos os tamanhos.

## Três linguagens, três trabalhos

O HTML, o CSS e o JavaScript repartem entre si o trabalho de fazer uma página web. Vais usar esta divisão em todos os temas de frontend do ano.

O **HTML** diz o que cada pedaço do conteúdo é. Isto é um título, isto é um parágrafo, isto é uma lista. Isto é uma imagem, isto é uma ligação para outra página. É a estrutura e o significado.

O **CSS** diz como cada pedaço se apresenta. Decide a cor, o tipo e o tamanho da letra e os espaços. Decide também a posição de cada coisa no ecrã, e o que muda num ecrã pequeno. É o aspeto.

O **JavaScript** diz como a página se comporta: o que acontece quando carregas num botão, quando escreves num campo, quando escolhes uma opção. É o comportamento.

Pensa numa casa. A estrutura é o HTML: as paredes, as divisões, as portas, o que é a cozinha e o que é o quarto. Os acabamentos são o CSS: a cor das paredes, o chão, os móveis. As instalações que fazem coisas são o JavaScript: o interruptor que acende a luz, a campainha que toca. Podes pintar a casa de outra cor sem mexer nas paredes, e podes mudar a campainha sem pintar nada.

Vê as três linguagens a trabalhar sobre a mesma coisa: um botão "Gostar", com um contador ao lado. Não precisas de perceber o código ainda. Olha só para o que cada parte faz.

Antes de leres a explicação, tenta prever: numa página com estes três pedaços, o que aparece depois de carregares três vezes no botão? E qual dos três pedaços faz o número mudar?

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
// A função entre chavetas corre uma vez por cada clique no botão.
document.querySelector("#gostar").addEventListener("click", function () {
  total = total + 1;
  document.querySelector("#contador").textContent = "Gostos: " + total;
});
```

O resultado é um botão azul, com a palavra "Gostar" a branco e os cantos redondos, e por baixo o texto `Gostos: 0`. Depois de três cliques, o texto diz `Gostos: 3`. Quem faz o número mudar é o JavaScript. O HTML só disse que havia um botão e um parágrafo, e o CSS só disse como o botão se apresenta.

Leitura guiada: começa pelo HTML, que cria as duas coisas que se veem, o botão e o parágrafo. Dá a cada uma um nome, `gostar` e `contador`. O CSS usa o nome `gostar` para dizer a que elemento se aplica a cor e a forma. O JavaScript usa os dois nomes. Encontra o botão e fica à espera dos cliques. A cada clique, soma um ao total e escreve-o no parágrafo.

Repara que cada linguagem tem uma forma própria, e que já as consegues reconhecer pela forma. O HTML tem **etiquetas**, os nomes entre `<` e `>`, como `<p>`. A etiqueta `<p>` marca onde começa um parágrafo, e `</p>`, com uma barra, marca onde acaba. A cada pedaço marcado assim, do princípio ao fim, chama-se **elemento**: o botão é um elemento, e o parágrafo é outro. O CSS tem um nome e, dentro de chavetas, propriedades seguidas de dois pontos, de um valor e de ponto e vírgula. O JavaScript tem instruções que acabam em ponto e vírgula, com parênteses e palavras como `let` e `function`.

Porque é que se separam os três trabalhos? Porque cada um muda por razões diferentes, e separados mudam-se sem estragar os outros. Um site pode mudar de cores sem tocar no conteúdo. Uma pessoa cega usa um **leitor de ecrã**, um programa que lê a página em voz alta. Recebe o conteúdo e a estrutura do HTML, sem precisar do aspeto. E numa equipa, uma pessoa pode tratar do aspeto enquanto outra trata do comportamento.

Este ano vais aprender as três, por esta ordem. O HTML vem no tema 02, depois do primeiro tema de Git. O CSS vem nos temas de frontend a seguir a esse. O JavaScript vem depois, quando já tiveres uma página com estrutura e aspeto a que dar comportamento.

## O browser

O **browser** (em português também se diz navegador) é o programa que pede as páginas, lê os ficheiros e desenha a página no ecrã. O Chrome, o Edge, o Firefox e o Safari são browsers.

Para quem faz páginas, o browser é também o sítio onde o nosso trabalho funciona. Muitas linguagens de programação precisam de um programa próprio, instalado no computador, para os programas escritos nelas funcionarem. Uma página web precisa só de um browser, que qualquer computador e qualquer telemóvel já têm. Por isso se diz que o browser é o **ambiente de execução** da Web: o sítio onde as páginas funcionam. É também por isso que, nesta disciplina, não precisas de instalar mais nada para começar. Um editor de texto e um browser chegam.

Quando o browser recebe um ficheiro HTML, faz isto (a descrição está simplificada, mas chega para este ano):

1. **Lê o texto** do ficheiro, de cima a baixo.
2. **Constrói uma árvore** em memória, com um ramo para cada elemento da página: o título, cada parágrafo, cada ligação. A essa árvore chama-se **DOM**, de *Document Object Model*, que quer dizer modelo do documento em objetos.
3. **Calcula o aspeto** de cada ramo, a partir do CSS, e **desenha** a página no ecrã.
4. **Executa o JavaScript**, que pode mudar a árvore enquanto a página está aberta: acrescentar um item a uma lista, mudar um texto, esconder uma parte.

### O ficheiro e o DOM

Há uma diferença que vai ser muito útil ao longo do ano: o **ficheiro** e o **DOM** não são a mesma coisa.

O ficheiro é o texto que está guardado no disco, que escreveste no editor. O DOM é a árvore que o browser construiu a partir desse texto. É a partir do DOM, e não do ficheiro, que a página é desenhada.

Pensa numa receita e num bolo. A receita é o ficheiro: fica escrita no livro e não muda. O bolo é o DOM: é feito a partir da receita, mas pode sair um pouco diferente. E depois de feito pode ser decorado sem que a receita mude.

Para perceberes as diferenças entre o ficheiro e o DOM, ajuda conhecer os nomes das partes de uma página. As páginas de hoje começam todas pelo mesmo esqueleto:

- A primeira linha, `<!doctype html>`, diz ao browser que a página segue as regras modernas do HTML.
- A seguir vem o elemento `html`, que embrulha tudo o resto. Tem lá dentro duas partes, o `head` e o `body`.
- O `head` é a cabeça da página, com informação que não aparece no meio dela. Um exemplo é o título que se vê no separador do browser, escrito num elemento `title`.
- O `body` é o corpo, com tudo o que se vê.

Dentro do `body`, cada pedaço do conteúdo tem também um nome curto. O `h1` é o título principal, o `p` é um parágrafo e o `main` é o conteúdo principal. O `header` é o cabeçalho que se vê no topo, com o nome do site e o menu. Repara que `head` e `header` são nomes parecidos para coisas diferentes: o `head` não aparece na página, e o `header` aparece no topo dela. Vais escrever este esqueleto no tema 02. Por agora basta reconheceres os nomes, porque vais encontrá-los na árvore do DOM, no laboratório.

O DOM pode ser diferente do ficheiro por três razões:

- **O browser corrige erros.** Se o ficheiro tiver um erro, o browser adivinha o que querias dizer e constrói a árvore à sua maneira. Por exemplo, as regras do HTML não permitem uma lista dentro de um parágrafo. Se a escreveres lá, o browser fecha o parágrafo antes da lista.
- **O browser acrescenta o que falta.** Há elementos que o browser põe na árvore mesmo que não estejam no ficheiro. No laboratório vais ver uma página de 1992 a que faltam o `html` e o `head` do esqueleto de hoje. O browser acrescenta-os sozinho.
- **O JavaScript muda a árvore.** Quando carregas no botão "Gostar", o JavaScript muda o texto do contador no DOM. O ficheiro continua a dizer "Gostos: 0".

Se recarregares a página, o browser deita fora a árvore antiga e volta a construí-la a partir do ficheiro. Tudo o que tinha sido mudado no DOM desaparece. No laboratório vais experimentar isto. Mudas o texto de um título nas ferramentas do programador, umas ferramentas escondidas do browser que mostram a página por dentro, e a página muda. Quando recarregas, volta tudo ao que estava.

### Browsers diferentes

O Chrome e o Edge usam o mesmo motor para desenhar as páginas, e o Firefox e o Safari usam motores diferentes. Os fabricantes de browsers combinam regras entre si, e por isso uma página bem escrita aparece praticamente igual em todos. Mesmo assim, quem faz páginas testa-as em mais do que um browser, porque há sempre pequenas diferenças.

## Cliente e servidor

Quando abres uma página na Internet, há dois computadores a conversar. O teu browser é o **cliente**: é quem pede. Do outro lado está um **servidor**: um computador sempre ligado, que guarda os ficheiros do site e os envia a quem os pede.

A conversa é parecida com o que acontece num restaurante. O cliente escolhe na ementa e faz um **pedido** ao empregado. O empregado leva o pedido à cozinha, que prepara o prato. Depois traz a **resposta**: o prato, ou a notícia de que esse prato não existe. O cliente não entra na cozinha nem sabe como o prato foi feito. Só faz pedidos e recebe respostas.

Uma página raramente se faz com um só pedido. O browser pede primeiro o ficheiro HTML. Quando o lê, descobre que a página também precisa de imagens, de um ficheiro de JavaScript e de uma **folha de estilos**. A folha de estilos é o ficheiro com o CSS. Faz um pedido novo para cada um. Uma página de um site grande pode fazer dezenas de pedidos. No laboratório vais ver esses pedidos, um a um, no separador Network das ferramentas do programador.

Nos primeiros temas deste ano não vais usar servidor nenhum. Vais abrir as tuas páginas diretamente a partir do disco do teu computador. Nesse caso, o browser lê os ficheiros sem pedir nada a ninguém. Percebes a diferença pelo endereço. Uma página que veio de um servidor começa por `https://` (ou `http://`), e um ficheiro aberto do teu disco começa por `file://`. Alguns browsers, como o Chrome, escondem este início até carregares na barra de endereço. Carrega uma vez nela para veres o endereço completo.

Isto tem uma consequência importante: um endereço `file://` só funciona no teu computador, porque é lá que o ficheiro está. Se o enviares a um colega, não funciona. Para outras pessoas verem o teu site, ele tem de estar num servidor. É esse o assunto do tema da publicação, no fim do ano.

## O endereço de uma página

O endereço de uma página chama-se **URL**, de *Uniform Resource Locator*, que quer dizer localizador uniforme de recursos. Um **recurso**, na Web, é qualquer coisa que se pode pedir a um servidor: uma página, uma imagem, uma folha de estilos. O URL é como a morada de uma casa: diz exatamente onde está aquilo que queres. Vê este endereço, partido nas suas partes:

```text
https://www.example.com/cursos/informatica.html
```

| Parte | Neste endereço | O que quer dizer |
| --- | --- | --- |
| Protocolo | `https` | As regras da conversa entre o browser e o servidor. O `s` quer dizer segura: a conversa vai cifrada, e quem estiver pelo meio não a consegue ler |
| Domínio | `www.example.com` | O nome do servidor, como o nome da rua e da terra de uma morada |
| Caminho | `/cursos/informatica.html` | A pasta e o ficheiro, dentro do servidor, como o número da porta e o andar |

O domínio `example.com` foi usado de propósito. É um domínio reservado para exemplos em documentação, e ninguém o pode registar para um site verdadeiro.

Há mais duas partes que podem aparecer no fim de um endereço. Depois de um ponto de interrogação vêm **parâmetros**, como em `?pesquisa=html`. Passam informação ao servidor, por exemplo o que escreveste numa caixa de pesquisa. Depois de um cardinal vem um **fragmento**, como em `#horario`, que indica uma parte da própria página. O browser salta para essa parte. Vais usar o fragmento no tema 02.

Os endereços de ficheiros do teu computador têm a mesma lógica, com o protocolo `file`, sem domínio e com o caminho do disco:

```text
file:///C:/Users/aluno/Documents/o-meu-site/index.html
```

Repara que a pasta se chama `Documents`. É esse o nome verdadeiro da pasta, que o Windows só mostra traduzido, como Documentos, no explorador de ficheiros.

Sobre o `https`: um endereço começado só por `http`, sem o `s`, não é cifrado. Os browsers avisam com a indicação "Não seguro" na barra de endereço. Nunca escrevas uma palavra-passe numa página com esse aviso. O `https` garante só que a conversa vai cifrada. Um site falso também pode usar `https`, e por isso o `s` não prova que o site é de confiança.

## O que se diz num pedido e numa resposta

As regras da conversa entre o browser e o servidor chamam-se **HTTP**, de *HyperText Transfer Protocol*, protocolo de transferência de hipertexto. O `https` é o mesmo HTTP com a conversa cifrada. Não precisas de saber as regras todas. Precisas de saber ler duas coisas.

A primeira é o **método** do pedido, que diz o que o browser quer. O mais comum é o **GET**, que quer dizer "dá-me este recurso". É o que o browser usa quando escreves um endereço ou carregas numa ligação.

A segunda é o **código de resposta**, um número de três algarismos que o servidor envia antes do conteúdo, a dizer como correu o pedido. O primeiro algarismo diz a família:

| Família | Quer dizer | Exemplo que vais encontrar |
| --- | --- | --- |
| 2xx | Correu bem | **200**: aqui está o que pediste |
| 3xx | Vai a outro endereço, ou usa a cópia que já tens | **301**: esta página mudou de endereço para sempre, e o browser vai buscá-la ao endereço novo. **304**: a página não mudou desde a última visita, e o browser usa a cópia que guardou |
| 4xx | O pedido tem um problema | **404**: o que pediste não existe neste servidor |
| 5xx | O servidor teve um problema | **500**: o servidor avariou ao preparar a resposta |

O 404 é o mais famoso. É o que o servidor costuma responder quando, num site publicado, uma ligação aponta para uma página que não existe. Nas páginas que abres do teu disco não há servidor, e por isso não há 404. O browser mostra uma mensagem a dizer que não encontrou o ficheiro. O 404 é o sintoma de uma **ligação sem destino**, uma ligação que leva a uma página que não existe. Vais aprender a evitá-la no mapa do site. No laboratório vais provocar um 404 de propósito e vê-lo no separador Network.

## As ferramentas do programador

Todos os browsers têm, escondidas, umas ferramentas para quem faz páginas. Chamam-se **ferramentas do programador** (em inglês, *developer tools* ou *DevTools*). Abrem-se com a tecla F12, ou com Ctrl+Shift+I no Windows e Cmd+Option+I no Mac. Também se abrem com o botão direito do rato num ponto da página, escolhendo Inspecionar.

As ferramentas estão organizadas em separadores. Neste tema vais usar dois:

- o separador **Elements** (em português pode aparecer como Elementos) mostra o DOM, a árvore que o browser construiu. Permite ver que parte da página corresponde a cada ramo;
- o separador **Network** (Rede) mostra todos os pedidos que a página fez, com o endereço, o método e o código de resposta de cada um.

Mais tarde vais usar o separador **Console** (Consola), onde aparecem os erros e onde se experimenta JavaScript. O laboratório deste tema ensina a usar as ferramentas passo a passo. Não tenhas receio de mexer nelas. Tudo o que mudas no separador Elements muda só o DOM da tua cópia da página. Desaparece quando recarregas, e não estraga nada no site verdadeiro.

## Antes do editor: planear

A segunda metade deste guia trata de planear um site antes de o escrever. É um trabalho que se faz sem computador e que poupa muitas horas de correções depois.

Ninguém constrói uma casa sem planta, e ninguém filma um filme sem guião. Mudar uma parede num desenho custa uma borracha. Mudar uma parede numa casa construída custa uma obra. Com os sites é igual. Mudar a organização de um site no papel demora segundos. Mudar a organização de um site já escrito demora horas, porque obriga a mexer em todas as páginas e em todas as ligações.

Um site feito sem plano tem sintomas que se reconhecem:

- páginas acrescentadas à medida que alguém se lembra delas;
- menus diferentes em páginas diferentes;
- informação repetida em dois sítios, e informação que falta;
- páginas a que só se chega por acaso.

Quem visita um site assim perde-se, e desiste.

O planeamento que vais fazer tem três passos, e cada um responde a uma pergunta:

1. **Para quem é e para que serve?** O utilizador e a sua necessidade.
2. **O que vai ter?** O conteúdo.
3. **Como está organizado?** O mapa do site, com as páginas e as ligações, e os wireframes, com a arrumação de cada página.

Faz-se tudo em papel. O papel é rápido, deita-se fora sem pena, e não te distrai com cores e tipos de letra, que são uma decisão para mais tarde. Um plano simples, feito numa aula, chega para evitar a maior parte dos problemas.

## O utilizador e a necessidade

A primeira pergunta de qualquer site é para quem é. A resposta "para toda a gente" não serve, porque um site feito para toda a gente acaba por não servir bem ninguém. Uma boa resposta é concreta: "alunos do 10.º ano que querem estudar HTML sozinhos, em casa, a partir do telemóvel".

A segunda pergunta é o que é que essa pessoa quer fazer no site. A isso chama-se a **tarefa principal**. Num site de receitas, a tarefa principal pode ser encontrar uma receita que se faça com o que há no frigorífico. No site de um clube, pode ser saber quando é o próximo encontro e como participar. A tarefa principal decide o que aparece primeiro, o que fica no menu e o que pode ficar mais escondido.

Ajuda muito imaginar uma pessoa concreta, com nome, e contar a história da sua visita. Por exemplo: "A Marta tem teste de HTML na sexta-feira e quer um livro para estudar. Abre o site, vê logo a lista dos livros, escolhe um, e fica a saber onde o encontrar." Se a história não se conseguir contar com o teu plano, o plano tem um problema.

## O conteúdo

Antes de organizar as páginas, é preciso saber o que se vai pôr nelas. Faz-se uma lista de todo o conteúdo, a que se chama **inventário de conteúdos**. Tem os textos, as imagens, as listas, as tabelas, as informações de contacto. Para cada coisa, anota-se também de onde vem. Pode ser escrita por ti, vir de uma fonte que tens de citar, ou ser inventada para o exemplo.

Nos sites que vais fazer este ano, o conteúdo pode ser inventado, desde que seja realista. O que nunca podes pôr são dados pessoais verdadeiros: moradas, números de telefone, datas de nascimento, fotografias de colegas ou de outras pessoas sem autorização. Um site na Web pode ser visto por qualquer pessoa. O que lá se põe pode ser copiado e guardado por quem o vê.

Com o inventário feito, agrupam-se as coisas parecidas. Os grupos que aparecem são, muitas vezes, as páginas do site ou as partes de uma página.

## O mapa do site

O **mapa do site** (em inglês, *sitemap*) é um desenho de todas as páginas de um site e das ligações que levam a cada uma. Cada página é uma caixa, com o nome da página e uma frase a dizer para que serve. As ligações são linhas entre as caixas. A página inicial fica no topo, e as páginas que se abrem a partir dela ficam por baixo, como numa árvore genealógica.

O exemplo desta secção é a Estante Digital, o site que os guias vão construir ao longo do ano. É um site onde uma turma reúne os recursos de estudo que recomenda, como livros, vídeos e sítios, com uma página para cada recurso.

No papel, o mapa desenha-se com caixas e linhas. Escrito, pode fazer-se assim, com a indentação a mostrar o que se abre a partir de quê:

```text
Início
├── Página de cada recurso (uma página por recurso, todas com a mesma forma)
└── Sobre
```

Um bom mapa cumpre algumas regras, e cada uma evita um problema concreto:

- Todas as páginas se alcançam a partir da página inicial, seguindo ligações. Uma página a que não se chega por nenhuma ligação é uma **página perdida**: existe, mas ninguém a encontra.
- De todas as páginas se volta à página inicial, pelo menos pelo menu.
- O **menu**, a lista de ligações que se repete em todas as páginas, leva às páginas principais. São as do primeiro nível da árvore. As páginas mais específicas alcançam-se a partir delas.
- Não é preciso carregar em muitas ligações para chegar a qualquer página. Num site pequeno, duas ou três chegam. Se precisares de mais, a árvore está funda de mais.
- Cada página tem um nome claro, que diz o que se lá encontra. É o nome que vai aparecer no menu.

O mapa desenha, para cada página, o caminho principal a partir da página inicial. As ligações do menu e as ligações de regresso repetem-se em todas as páginas. Por isso não se desenham, para o mapa não ficar cheio de linhas. Repara também que o menu mostra só as páginas principais. A página de um recurso, na Estante Digital, não está no menu, porque há muitas. Chega-se a ela pela lista de recursos na página inicial.

## O wireframe

O mapa diz que páginas existem. O **wireframe** diz como cada página está arrumada. É um esboço de uma página, feito só com caixas e com a indicação do tipo de conteúdo de cada caixa. Não tem cores, nem tipos de letra, nem imagens verdadeiras. O nome vem do inglês e quer dizer estrutura de arame, porque mostra só o esqueleto da página.

Há umas convenções simples que toda a gente usa, para que qualquer pessoa leia um wireframe sem explicação:

- uma caixa com um X lá dentro, ou `[X]`, é uma imagem;
- linhas onduladas ou riscos são texto corrido; um texto escrito em maiúsculas é um título;
- uma palavra sublinhada é uma ligação;
- cada zona grande (cabeçalho, menu, conteúdo, rodapé) é uma caixa com o nome escrito ao lado.

Desenham-se duas versões de cada página importante, porque vai ser vista em ecrãs muito diferentes:

- o **wireframe estreito**, para o ecrã de um telemóvel, com uma só coluna: tudo fica empilhado, de cima para baixo;
- o **wireframe largo**, para o ecrã de um computador, onde algumas coisas podem ficar lado a lado.

O estreito é o mais útil dos dois, por uma razão que vais perceber no tema 02. Numa só coluna, a ordem das caixas de cima para baixo é a ordem em que o conteúdo vai estar escrito no HTML. É também a ordem em que um leitor de ecrã o vai ler.

A **ordem de leitura** é a ordem em que se encontra o conteúdo, e tem de ser a mesma nas duas versões. No largo, as coisas podem ficar lado a lado. Mas o que vem primeiro no estreito continua a vir primeiro no largo, lido da esquerda para a direita e de cima para baixo.

Ao lado de cada zona do wireframe escreve-se uma **anotação** a dizer o que é. Por exemplo: "cabeçalho com o nome do site", "menu", "lista de livros com ligação para cada um". No tema 02 vais acrescentar a cada anotação o nome do elemento HTML que lhe corresponde. O wireframe passa então a ser a planta do teu código.

## O mapa e os wireframes têm de concordar

O mapa e os wireframes descrevem o mesmo site por dois lados, e por isso têm de dizer a mesma coisa. Antes de dares o plano por acabado, faz estas quatro verificações:

- Cada ligação desenhada num wireframe tem de levar a uma página que existe no mapa. Se o wireframe da página inicial tem uma ligação "Contactos", o mapa tem de ter uma página Contactos. Se não tiver, é uma ligação sem destino, que no site verdadeiro costuma dar o erro 404.
- Cada linha do mapa tem de aparecer em algum wireframe, como uma ligação desenhada. Se o mapa diz que da página inicial se vai à página Sobre, o wireframe da página inicial tem de mostrar onde está essa ligação.
- Os nomes são os mesmos nos dois. Imagina que no mapa a página se chama "Sobre" e no menu do wireframe se chama "Quem somos". Uma pessoa que leia os dois não sabe se são a mesma página.
- O menu é igual em todos os wireframes, com as mesmas opções pela mesma ordem.

Estas verificações apanham no papel os erros que, no site verdadeiro, só se descobrem mais tarde. Aparecem quando alguém carrega numa ligação e vê uma página de erro.

## O tema do teu site

Ao longo deste ano vais construir um site teu, que vai crescendo tema a tema. Primeiro vem a estrutura em HTML, e depois o aspeto com CSS. Segue-se a adaptação a ecrãs de todos os tamanhos, depois o comportamento com JavaScript, e no fim a publicação.

O tema do teu site escolhes do menu de temas que o professor te dá na aula. Todos os temas do menu têm uma pequena coleção de coisas parecidas, como receitas, jogos, livros ou jogadores. Mais à frente no ano, vais mostrar essas coisas em cartões, filtrá-las e acrescentar uma nova por um formulário, com JavaScript. Um tema com uma coleção dá-te material para isso. Se tiveres uma ideia tua, fala com o professor: entra se também tiver uma coleção destas.

Estes critérios ajudam a escolher bem dentro do menu:

- Escolhe uma coisa de que gostes e que conheças. Vais trabalhar nela o ano todo, e é mais fácil escrever conteúdo sobre um assunto que conheces.
- Tem de dar para várias páginas. Pensa se consegues imaginar pelo menos três páginas diferentes sobre o tema.
- O conteúdo pode ser inventado, mas sem dados pessoais verdadeiros e sem nada que não pudesses mostrar numa aula.
- Começa pequeno. Um site com três páginas bem feitas vale mais do que um site com vinte páginas vazias. Podes sempre acrescentar.

Os exemplos dos guias usam a Estante Digital, um site de recursos de estudo, mas o teu site não tem de ser parecido com ela.

## Preencher o modelo do brief

O plano do teu site fica registado no [modelo do brief e wireframe](../projeto/modelos/brief-e-wireframe.md), que está na pasta do projeto. Um **brief** é o resumo de um trabalho antes de começar: o que é, para quem, e o que tem de ter. A palavra é inglesa, e usa-se assim em Portugal. O modelo tem campos entre chavetas duplas, que são os sítios onde escreves as tuas respostas. Podes copiar as perguntas para uma folha, ou preenchê-las numa cópia do ficheiro.

Alguns campos usam palavras que ainda não conheces, porque o mesmo modelo serve para o ano todo. Esta tabela explica cada campo e diz quando se preenche.

| Campo do modelo | O que quer dizer | Quando se preenche |
| --- | --- | --- |
| O título, no topo | O nome provisório do teu site | Neste tema |
| Utilizador e necessidade | Para quem é o site e o que essa pessoa precisa | Neste tema |
| Resultado útil para essa pessoa | O que a pessoa consegue fazer depois de usar o site: a tarefa principal | Neste tema |
| Conteúdo necessário e respetiva origem | O inventário de conteúdos, com a origem de cada coisa | Neste tema |
| Limites do trabalho | O que o teu site não vai ter, para caber no tempo. Por exemplo: "não tem contas de utilizador" ou "tem só três páginas nesta fase" | Neste tema |
| Páginas e ligações entre páginas (sitemap) | O mapa do site | Neste tema |
| Hierarquia de informação | O que é mais importante em cada página, por ordem | Neste tema |
| Wireframe de largura pequena e larga | Os dois wireframes, desenhados em papel e fotografados ou digitalizados | Neste tema |
| Relação entre zonas desenhadas e elementos HTML | O elemento HTML de cada zona do wireframe | No tema 02, HTML e semântica |
| Ação do utilizador, evento, dados/estado e resposta visível | O que acontece quando a pessoa faz alguma coisa na página | Nos temas de JavaScript. Por agora escreve "ainda não" |
| Formulários e mensagens, quando aplicáveis | Os campos que a pessoa preenche e as mensagens que recebe | No tema dos formulários. Por agora escreve "ainda não" |
| Percurso por teclado e foco | A ordem em que se chega às ligações só com o teclado | No tema 02, HTML e semântica |
| Critérios de aceitação | As condições que o site tem de cumprir para estar pronto nesta fase. Por exemplo: "a partir da página inicial chega-se a todas as páginas em duas ligações ou menos" | Neste tema |
| Verificação com um colega antes de implementar | O que o colega conseguiu ou não conseguiu encontrar no teu plano | Neste tema, depois de um colega ver o teu plano |
| Artefacto de planeamento e versão Git | Onde está guardado o plano e em que versão | No tema 01 do Git |

## Exemplo guiado: o plano da Estante Digital

Neste exemplo faz-se, passo a passo, o plano do site que os guias vão construir ao longo do ano: a Estante Digital. É um site onde uma turma reúne os recursos de estudo que recomenda. O conteúdo é todo inventado.

### Passo 1: A necessidade

Tudo começa com um problema real de quem vai usar o site. Os alunos que começam a aprender a fazer páginas web encontram centenas de vídeos, livros e sítios. Não sabem por onde começar nem quais valem a pena. A turma já experimentou vários e sabe quais ajudaram. A necessidade é esta: ter num só lugar uma pequena lista de recursos de confiança, escolhidos por quem já os usou.

### Passo 2: O utilizador e a tarefa principal

Para quem é? Para alunos de Desenvolvimento de Aplicações, sobretudo os que estão a começar, que querem estudar sozinhos, muitas vezes a partir do telemóvel.

Qual é a tarefa principal? Encontrar um recurso para estudar um assunto e saber onde o arranjar.

A história de uma visita, que o plano tem de permitir: "A Marta tem teste de HTML na sexta-feira. Abre a Estante Digital no telemóvel e vê logo que há livros, vídeos e sítios. Escolhe o livro Primeiros passos na Web e lê para quem é. Fica a saber que está na biblioteca e a que horas a biblioteca abre."

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

Agrupando as coisas parecidas, aparecem três grupos:

- a apresentação e a lista dos recursos, que dão uma página de entrada;
- a informação completa de cada recurso, que dá uma página por recurso;
- a explicação sobre o site, que dá uma página própria.

### Passo 4: As páginas

Dos grupos saem as páginas:

- **Início**: a apresentação do site e a lista dos seis recursos, arrumada por tipo. É aqui que a Marta começa.
- **Página de cada recurso**: uma por recurso, todas com a mesma forma. Nesta fase, só o livro Primeiros passos na Web tem página. Os outros têm só a descrição curta na lista.
- **Sobre**: porque existe o site e como se escolhem os recursos.

Houve uma alternativa que se pôs de lado: uma página para cada tipo, com os livros, os vídeos e os sítios em páginas separadas. Com só seis recursos, a Marta tinha de carregar numa ligação a mais só para ver a lista. E as três páginas ficavam quase vazias. Com poucos recursos, a lista inteira cabe na página inicial. Se um dia houver cinquenta, a decisão muda.

### Passo 5: O mapa do site

```text
Início
├── Página de cada recurso (por agora, só Primeiros passos na Web)
└── Sobre
```

Verificam-se as regras do mapa, uma a uma:

- Todas as páginas se alcançam a partir do Início: a página do livro, pela lista de recursos, e o Sobre, pelo menu.
- De todas as páginas se volta ao Início, pelo menu.
- O menu leva às páginas principais, que são duas: Início e Sobre. As páginas dos recursos não estão no menu, porque vão ser muitas. Alcançam-se pela lista.
- Qualquer página fica a uma ligação de distância do Início.

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

Repara na ordem, de cima para baixo:

1. o nome do site e o menu, que dizem onde a pessoa está e para onde pode ir;
2. o assunto da página e a apresentação;
3. os três grupos de recursos;
4. no fim, a nota sobre o site.

É a ordem pela qual a Marta precisa das coisas. Esta ordem, do que a Marta precisa primeiro para o que precisa depois, é a **hierarquia de informação** da página inicial. É ela que se escreve nesse campo do brief.

Só o primeiro livro é uma ligação, porque é o único que já tem página. Os outros são só texto. No papel, essa ligação desenhava-se sublinhada. Aqui, a anotação diz "com ligação".

### Passo 7: O wireframe largo da página inicial

No ecrã de um computador há espaço para pôr os três grupos lado a lado. O menu passa para a mesma linha do nome do site:

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

A arrumação mudou, mas a ordem de leitura é a mesma. Primeiro o nome e o menu, depois o assunto e a apresentação. A seguir, os livros, os vídeos e os sítios, e por fim a nota. Lendo da esquerda para a direita e de cima para baixo, encontra-se tudo pela mesma ordem do wireframe estreito.

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

O cabeçalho e o rodapé são iguais aos da página inicial, para que a Marta reconheça que continua no mesmo site. A seguir ao nome do livro vem a capa, que ajuda a reconhecê-lo na estante. Depois vêm as partes da ficha, pela ordem das perguntas que a Marta faria. É para mim? O que vou aprender? Como o uso? Onde o encontro? A dica fica numa caixa à parte, porque é um comentário, e não informação essencial. No fim há uma ligação para voltar à lista. Na versão larga, a caixa da dica podia ficar ao lado da ficha, à direita, sem mudar a ordem de leitura.

### Passo 9: Verificar a coerência

Faz-se a verificação da secção "O mapa e os wireframes têm de concordar", ligação a ligação.

| Ligação desenhada | Onde está | Destino no mapa | Resultado |
| --- | --- | --- | --- |
| Início, no menu | Todas as páginas | Início | Existe |
| Sobre, no menu | Todas as páginas | Sobre | Existe |
| Primeiros passos na Web, na lista | Página inicial | Página do livro | Existe |
| Voltar à lista | Página do livro | Início | Existe |

Numa primeira versão do wireframe da página do livro havia uma caixa "Recursos parecidos", com ligações para o outro livro e para os dois vídeos. A verificação apanhou o problema: essas páginas não estão no mapa, porque ainda não existem. Seriam ligações sem destino. A decisão foi trocar essa caixa pela "Dica de quem já o leu", que não tem ligações. Quando as páginas desses recursos existirem, a caixa de recursos parecidos pode voltar. Nesse dia, o mapa e os wireframes mudam os dois ao mesmo tempo.

Os nomes batem certo: "Início" e "Sobre" são iguais no mapa e nos menus, e o menu é o mesmo nos dois wireframes.

Com a verificação feita, escrevem-se no brief os **critérios de aceitação** desta fase, as condições que o site tem de cumprir para estar pronto:

- a partir do Início chega-se a qualquer página com uma só ligação;
- o menu é igual em todas as páginas, com Início e Sobre por esta ordem;
- nenhuma ligação fica sem destino.

### Passo 10: O percurso de um utilizador

Por fim, conta-se a história do passo 2 com o plano na mão, apontando para cada caixa. A Marta abre o site e está no Início. Vê o título e os três grupos. No grupo Livros vê o nome sublinhado do Primeiros passos na Web, carrega nele e chega à página do livro. Lê "Para quem é" e confirma que é para ela. Desce até "Onde o encontrar", vê a estante e o horário. Carrega em "Voltar à lista" e volta ao Início.

A história conta-se sem nenhum salto que o plano não mostre. O plano está pronto para ser passado a HTML, que é o que o tema 02 faz.

## Erros frequentes

### "O meu site é para toda a gente"

O que se vê: o campo "Utilizador e necessidade" do brief diz "toda a gente". Depois, não se consegue decidir o que vai para o menu nem o que aparece primeiro. Acontece porque um site para toda a gente não ajuda a decidir nada, nem a forma de escrever. Corrige-se escolhendo uma pessoa concreta e a sua tarefa principal, e deixando-as decidir por ti.

### Um tema grande demais

O que se vê: o mapa não para de crescer, e nenhuma página fica feita. "Um site sobre futebol" dá para mil páginas. "O site de uma equipa de futebol inventada, com os jogos da época e os jogadores" dá para três páginas bem feitas. Corrige-se começando pequeno, e acrescentando depois.

### Páginas soltas no mapa

O que se vê: uma caixa no mapa sem nenhuma linha a chegar-lhe. É uma página perdida, a que ninguém consegue ir. Acontece quando se acrescenta uma página e se esquece de a ligar. Corrige-se ligando-a, direta ou indiretamente, à página inicial.

### Um menu diferente em cada página

O que se vê: os wireframes de duas páginas têm menus com opções diferentes, ou pela ordem diferente. A pessoa tem de reaprender o site em cada página. Corrige-se com o mesmo menu em todos os wireframes, com as mesmas opções pela mesma ordem.

### Ligações para páginas que não estão no mapa

O que se vê: um wireframe com uma ligação cujo destino não aparece no mapa. É o erro que o passo 9 do exemplo guiado apanhou. No site verdadeiro, essa ligação sem destino costuma dar o erro 404. Corrige-se acrescentando a página ao mapa, ou tirando a ligação do wireframe.

### Um wireframe com cores, tipos de letra e desenhos bonitos

O que se vê: o tempo acaba e o wireframe tem cores, mas falta-lhe metade das zonas. O wireframe serve para decidir a arrumação, e não o aspeto. Cada minuto gasto a colorir é um minuto a menos a pensar na ordem e nas ligações. Corrige-se com caixas, riscos e um X para as imagens. O aspeto decide-se nos temas de CSS.

### A ordem muda entre o wireframe estreito e o largo

O que se vê: no largo, a lista aparece antes do título, e no estreito aparece depois. A página vai ser lida numa ordem num ecrã e noutra ordem noutro. Corrige-se mantendo uma só ordem de leitura: arruma-se lado a lado no largo, mas sem trocar a ordem.

### Confundir a Internet com a Web

O que se vê: dizer que uma videochamada ou o correio eletrónico "são a Web". Acontece porque no dia a dia as duas palavras se usam como se fossem a mesma. Corrige-se lembrando que a Internet é a rede que transporta os dados, e a Web é o serviço de páginas ligadas que usa essa rede. O correio eletrónico usa a Internet e não é a Web.

### Enviar a um colega um endereço `file://`

O que se vê: o colega abre o endereço e o browser diz que não encontra o ficheiro. Um endereço `file://` aponta para um ficheiro no teu disco, e só funciona no teu computador. Corrige-se dando ao colega os ficheiros, ou publicando o site num servidor.

## Palavras novas deste guia

- Internet: a rede física que liga computadores do mundo inteiro e transporta dados entre eles.
- Web: o serviço de páginas ligadas umas às outras, que se leem com um browser e usam a Internet para chegar até ti.
- HTML: a linguagem que diz o que cada pedaço do conteúdo é; dá a estrutura e o significado.
- CSS: a linguagem que diz como cada pedaço se apresenta; dá o aspeto.
- JavaScript: a linguagem que diz como a página se comporta quando alguém faz alguma coisa.
- Etiqueta: o nome entre `<` e `>`, como `<p>`, que marca onde começa um elemento; com uma barra, como `</p>`, marca onde ele acaba.
- Elemento: cada pedaço do conteúdo que o HTML marca, do princípio ao fim, como um título, um parágrafo ou um botão.
- Leitor de ecrã: um programa que lê a página em voz alta, usado por pessoas cegas.
- Browser (navegador): o programa que pede as páginas, lê os ficheiros e desenha a página no ecrã.
- Ambiente de execução: o sítio onde um programa funciona; o da Web é o browser.
- DOM: a árvore que o browser constrói em memória a partir do ficheiro HTML, e a partir da qual desenha a página.
- Ficheiro: o texto guardado no disco, que se escreve no editor.
- Esqueleto da página: o `<!doctype html>`, o `html`, o `head`, com o `title`, e o `body`, por que começam todas as páginas de hoje.
- Cliente: quem pede; na Web, o browser.
- Servidor: um computador sempre ligado, que guarda os ficheiros de um site e os envia a quem os pede.
- Pedido: o que o cliente envia ao servidor a dizer o que quer.
- Resposta: o que o servidor devolve, com o código de resposta e o conteúdo.
- URL: o endereço de um recurso na Web.
- Recurso: qualquer coisa que se pode pedir a um servidor, como uma página, uma imagem ou uma folha de estilos.
- Folha de estilos: o ficheiro com o CSS de uma página.
- Protocolo: as regras da conversa entre o browser e o servidor, como o `https`; é a primeira parte do URL.
- Domínio: o nome do servidor, como `www.example.com`.
- Caminho: a pasta e o ficheiro dentro do servidor, como `/cursos/informatica.html`.
- Parâmetros: a parte do endereço depois do ponto de interrogação, que passa informação ao servidor.
- Fragmento: a parte do endereço depois do cardinal, que indica uma parte da própria página.
- HTTP: as regras da conversa entre o browser e o servidor; o `https` é o HTTP cifrado.
- Método: a parte do pedido que diz o que o browser quer; o mais comum é o GET, "dá-me este recurso".
- Código de resposta: o número de três algarismos que diz como correu o pedido, como 200 ou 404.
- Ligação sem destino: uma ligação para uma página que não existe; num site publicado, costuma dar o erro 404.
- Ferramentas do programador: as ferramentas do browser para ver e experimentar uma página por dentro.
- Tarefa principal: o que o utilizador quer fazer no site.
- Inventário de conteúdos: a lista de todo o conteúdo de um site, com a origem de cada coisa.
- Mapa do site: o desenho das páginas de um site e das ligações que levam a cada uma.
- Página perdida: uma página a que não se chega por nenhuma ligação.
- Menu: a lista de ligações para as páginas principais, que se repete em todas as páginas.
- Wireframe: o esboço de uma página só com caixas e com o tipo de conteúdo de cada uma.
- Wireframe estreito e wireframe largo: o esboço da página num telemóvel, numa só coluna, e num computador, com coisas lado a lado.
- Ordem de leitura: a ordem em que se encontra o conteúdo de uma página, a mesma no wireframe estreito e no largo.
- Anotação: o texto ao lado de uma zona do wireframe, a dizer o que ela é.
- Hierarquia de informação: a ordem do que é mais importante numa página, do que o utilizador precisa primeiro para o que precisa depois.
- Brief: o resumo de um trabalho antes de começar: o que é, para quem e o que tem de ter.
- Critérios de aceitação: as condições que o site tem de cumprir para estar pronto numa fase.

## Verificar o que aprendeste

1. Dá um exemplo de um serviço que usa a Internet e não é a Web. Porque não é a Web?
2. Numa página, que linguagem decide a cor de um título? E qual decide o que acontece quando carregas num botão?
3. Mudaste o texto de um título nas ferramentas do programador e depois recarregaste a página. O que aparece no título, e porquê?
4. Dá duas razões para o DOM de uma página poder ser diferente do ficheiro.
5. Parte o endereço `https://www.example.com/escola/horario.html` em protocolo, domínio e caminho.
6. Porque é que um endereço começado por `file://` não serve para um colega ver a tua página?
7. O que quer dizer o código 200? E o 404? De que família é cada um?
8. Porque é que "para toda a gente" não serve como resposta à pergunta sobre para quem é o site?
9. O que é uma página perdida, e como a encontras olhando para o mapa?
10. Porque é que a ordem de leitura tem de ser a mesma no wireframe estreito e no largo?
11. O wireframe de uma página tem uma ligação "Contactos", e o mapa não tem nenhuma página com esse nome. Como se chama este problema, e o que acontece no site verdadeiro?
12. Para que serve contar a história da visita de uma pessoa, com o plano na mão?

## O que vem a seguir

Para praticar este tema, faz o [laboratório](01-web-e-planeamento-laboratorio.md) e depois a [ficha de exercícios](01-web-e-planeamento-exercicios.md). No laboratório, abres as ferramentas do programador pela primeira vez. Vês o DOM de uma página, mudas o DOM e confirmas que o ficheiro não muda. Visitas o primeiro site da história e vês o que o browser acrescenta ao seu código. E segues os pedidos, os endereços e os códigos de resposta, incluindo um 404 provocado de propósito.

### O plano do teu site

Na aula, fazes o plano do teu site em papel, pelos mesmos passos do exemplo guiado. Tem à mão o [modelo do brief](../projeto/modelos/brief-e-wireframe.md). Escreve as respostas nos campos que a tabela da secção "Preencher o modelo do brief" diz que se preenchem neste tema.

1. **Escolhe o tema.** Lê os critérios da secção "O tema do teu site". Depois escolhe o teu tema do menu de temas que o professor te dá na aula. Escreve-o no topo da folha, com um nome provisório para o site. Se estiveres indeciso entre dois, escolhe aquele de que consegues imaginar mais páginas.
2. **O utilizador e a tarefa principal.** Preenche os campos "Utilizador e necessidade" e "Resultado útil para essa pessoa". Sê concreto: não "toda a gente", mas uma pessoa como a Marta do exemplo guiado. Escreve, em duas ou três frases, a história de uma visita dessa pessoa ao teu site.
3. **O inventário de conteúdos.** Preenche o campo "Conteúdo necessário e respetiva origem", como no passo 3 do exemplo guiado. Escreve uma linha por conteúdo, com o tipo e a origem. Depois agrupa as coisas parecidas. Preenche também o campo "Limites do trabalho", com o que o teu site não vai ter nesta fase.
4. **O mapa do site.** Decide as páginas a partir dos grupos do inventário. Desenha o mapa numa folha lisa, com uma caixa por página e linhas para as ligações. Dentro de cada caixa, escreve o nome da página e uma frase a dizer para que serve. Para o laboratório do tema 02 precisas de pelo menos duas páginas ligadas entre si. Se conseguires imaginar três, melhor. Confirma as regras da secção "O mapa do site": consegues chegar a todas as páginas a partir do Início, e voltar de todas?
5. **Os wireframes.** Desenha o wireframe estreito da tua página inicial, com as anotações ao lado de cada zona. Depois desenha o wireframe largo da mesma página, e confirma que a ordem de leitura é a mesma nos dois. Preenche o campo "Hierarquia de informação" com a ordem das zonas do wireframe estreito, como no passo 6 do exemplo guiado. Se te sobrar tempo, desenha também o wireframe estreito da segunda página. Não gastes tempo em pormenores: caixas, riscos para o texto e um X para as imagens chegam.
6. **A verificação.** Primeiro, sozinho, verifica se o mapa e os wireframes concordam, como no passo 9 do exemplo guiado, e corrige o que encontrares. Depois troca de plano com um colega. Sem lhe explicares nada, pede-lhe que encontre no teu plano uma informação concreta do teu site, como "onde vejo quando é o próximo torneio?". Ele diz-te, apontando, por onde passou. Se ele se perder, o teu plano tem um problema: pergunta-lhe onde hesitou e corrige. Escreve o que aconteceu no campo "Verificação com um colega antes de implementar". Por fim, preenche o campo "Critérios de aceitação". Escreve duas ou três condições que o teu site tem de cumprir nesta fase, como as do passo 9 do exemplo guiado.

Guarda a folha do mapa e dos wireframes. Fotografa-a e guarda as fotografias, com a cópia do brief, numa pasta com o nome do teu site. Se não puderes fotografar, guarda as folhas, e o professor diz como as passas para a pasta. O nome da pasta vai em minúsculas, sem espaços nem acentos, com hífenes entre as palavras, como `estante-digital`. É essa a pasta do teu site. No laboratório do tema 02, é lá dentro que vais escrever as páginas em HTML.

Cria a pasta onde o professor indicar. No Windows, carrega com o botão direito num sítio vazio da janela dessa pasta e escolhe Novo e depois Pasta. No Mac, carrega com o botão direito num sítio vazio e escolhe Nova pasta. Depois escreve o nome e carrega em Enter.

O plano que fizeste é a planta do teu site. A seguir vem o tema 01 do Git, onde vais aprender a guardar versões da pasta do teu site, começando pelo plano. Assim, nenhuma alteração se perde. Depois, no guia [HTML e semântica](02-html-e-semantica.md), vais transformar o plano em páginas de verdade, escritas em HTML. Cada zona do wireframe vai dar um elemento.

## Para saber mais

- CERN, [o primeiro site da história](https://info.cern.ch/): a página de entrada da cópia do primeiro site, em inglês.
- MDN Web Docs, [como a Web funciona](https://developer.mozilla.org/pt-BR/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works): o caminho de um pedido, do browser ao servidor, em português do Brasil.
- MDN Web Docs, [o que são as ferramentas do programador](https://developer.mozilla.org/pt-BR/docs/Learn_web_development/Howto/Tools_and_setup/What_are_browser_developer_tools): os separadores das ferramentas, em português do Brasil.
- MDN Web Docs, [a lista dos códigos de resposta do HTTP](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Reference/Status): todos os códigos, com o que quer dizer cada um, em português do Brasil.

![Rodapé](../imagens/rodape.png)
