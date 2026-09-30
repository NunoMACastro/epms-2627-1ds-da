![Cabeçalho](../imagens/cabecalho.png)

# Ficha de exercícios: A Web, os utilizadores e o planeamento

UC: UC02833, Conceber aplicações para a web na vertente frontend

Bloco: F01

Requisitos: UC02833.K01, UC02833.K02, UC02833.A02, UC02833.A03

| Identificação | Valor |
| --- | --- |
| Material | Ficha do bloco F01, acompanha o [guia](01-web-e-planeamento.md) e o [laboratório](01-web-e-planeamento-laboratorio.md) |
| Tempo total | 45 minutos dos 240 do bloco, nos exercícios 1 a 6. O desafio e a secção "Para ires mais longe" são opcionais e ficam fora destes 45 minutos |
| Entrega | As respostas escritas dos exercícios 1 a 4 e 6, e o mapa do exercício 5, desenhado à mão; o desafio e o exercício de "Para ires mais longe", se os fizeres |

## Objetivos e conceitos necessários

Vais praticar, um de cada vez, os assuntos do bloco: a diferença entre a Internet e a Web, o trabalho de cada uma das três linguagens, as partes de um endereço, os códigos de resposta, o desenho de um mapa do site e a verificação da coerência entre um mapa e um wireframe.

Antes de começares, deves ter lido a teoria e o exemplo explicado do [guia](01-web-e-planeamento.md). Cada exercício diz em que secção do guia está a matéria. Se encravares, volta a essa secção antes de olhares para o apoio, no fim da ficha.

Os sites desta ficha são inventados, e não são o teu site nem a Estante Digital.

## Como está organizada a ficha

Resolve os exercícios pela ordem. Cada exercício treina uma só coisa.

| Exercício | O que treina | Tempo |
| --- | --- | ---: |
| 1 | Distinguir a Internet da Web | 5 min |
| 2 | Atribuir cada trabalho à linguagem certa | 5 min |
| 3 | Partir um endereço nas suas partes | 10 min |
| 4 | Ler os códigos de resposta | 5 min |
| 5 | Desenhar o mapa de um site a partir do seu conteúdo | 10 min |
| 6 | Encontrar ligações sem destino entre um mapa e um wireframe | 10 min |
| Total da parte obrigatória | Exercícios 1 a 6 | 45 min |
| Desafio opcional | Passar um wireframe estreito a largo | 20 min |
| Para ires mais longe | Opcional: um endereço com parâmetros | fora dos 45 min |

## Exercício 1: Internet ou Web? (5 min)

A matéria está na secção "A Internet e a Web não são a mesma coisa" do guia.

Para cada situação, diz se a pessoa está a usar a Web, ou se está a usar a Internet mas não a Web.

**a)** A Rita abre o site da escola no browser para ver a ementa da cantina.

**b)** O Tiago joga um jogo em rede na consola, contra jogadores de outros países.

**c)** A avó faz uma videochamada numa aplicação instalada no telemóvel.

**d)** O Duarte lê, no browser do telemóvel, uma página de um site de notícias.

## Exercício 2: Que linguagem faz este trabalho? (5 min)

A matéria está na secção "Três linguagens, três trabalhos" do guia.

Para cada mudança pedida num site, diz se é trabalho do HTML, do CSS ou do JavaScript.

**a)** Os títulos das páginas passam a ser azuis e maiores.

**b)** Quando se carrega no botão "Só sobremesas", a lista de receitas passa a mostrar só as sobremesas.

**c)** A lista de ingredientes, que estava escrita como um parágrafo corrido, passa a estar marcada como lista.

**d)** Esta linha de código:

```css
nav { background: #1f4e8c; }
```

## Exercício 3: Partir um endereço (10 min)

A matéria está na secção "O endereço de uma página" do guia.

**a)** Parte este endereço em protocolo, domínio, caminho e fragmento:

```text
https://www.example.com/clube/torneios/outono.html#inscricoes
```

**b)** Neste segundo endereço, diz qual é o protocolo e onde está o ficheiro:

```text
file:///C:/Users/aluno/Documentos/clube-de-xadrez/index.html
```

**c)** Se enviares o endereço da alínea b) a um colega, por mensagem, e ele o abrir no computador dele, vê a tua página? Explica numa frase.

## Exercício 4: Códigos de resposta (5 min)

A matéria está na secção "O que se diz num pedido e numa resposta" do guia.

Diz que código de resposta espera o browser em cada situação, e a família a que pertence.

**a)** A página pedida existe, e o servidor envia-a sem problemas.

**b)** Uma ligação aponta para uma página que foi apagada do site.

**c)** O servidor avariou enquanto preparava a página pedida.

## Exercício 5: Desenhar o mapa de um site (10 min)

A matéria está na secção "O mapa do site" do guia e nos passos 3 a 5 do exemplo explicado.

A Carolina quer fazer o site "Receitas da Avó", com este conteúdo, já agrupado:

- uma apresentação do site, a dizer que as receitas são da família e para quem é;
- três receitas de sopas e quatro receitas de doces, cada uma com os ingredientes e os passos;
- uma página com a história do caderno de receitas da família, sem dados pessoais.

**a)** Desenha o mapa do site, com uma caixa por página e linhas para as ligações. Há mais do que um mapa certo; escolhe um e segue as regras do guia.

**b)** Diz que páginas vão para o menu, que se repete em todas as páginas, e justifica numa frase porque é que as outras ficam de fora.

## Exercício 6: O mapa e o wireframe concordam? (10 min)

A matéria está na secção "O mapa e os wireframes têm de concordar" do guia e no passo 9 do exemplo explicado.

O Rafael fez o plano do site do clube de teatro da escola. Este é o mapa dele:

```text
Início
├── Peças
│   ├── A Ilha dos Relógios
│   └── O Último Autocarro
└── Inscrições
```

E este é o wireframe estreito da página inicial, com as anotações dele à direita:

```text
┌────────────────────────────────┐
│ Clube de Teatro                │   cabeçalho
│ Início   Peças   Inscrever-me  │   menu: três ligações
├────────────────────────────────┤
│ SOBE AO PALCO CONNOSCO         │   título da página
│ ~~~~~~~~~~~~~~~~~~~~~~~~~~     │   apresentação
│ ~~~~~~~~~~~~~~~~~~             │
│                                │
│ EM CENA ESTE ANO               │   lista das peças
│ - A Ilha dos Relógios          │   ligação
│ - O Último Autocarro           │   ligação
│                                │
│ Galeria de fotografias         │   ligação
├────────────────────────────────┤
│ Contactos                      │   rodapé: ligação
└────────────────────────────────┘
```

**a)** Faz a tabela de verificação, como no passo 9 do exemplo, com uma linha por ligação desenhada no wireframe: a ligação, o destino que tem no mapa, e se existe ou não.

**b)** Há três problemas no plano do Rafael. Diz quais são.

**c)** Para cada problema, propõe uma correção. Pode haver mais do que uma correção certa: diz qual escolhias e porquê.

## Apoio

Usa estas pistas pela ordem em que aparecem, e só a seguinte se a anterior não tiver chegado. Nenhuma dá a resposta: indicam onde olhar.

**Exercício 1.** Pergunta, em cada caso, se a pessoa está a ler páginas num browser. Se sim, é a Web. Se está a usar outra aplicação que comunica pela rede, é a Internet sem ser a Web.

**Exercício 2.** Pergunta, em cada caso, se a mudança é sobre o que a coisa é, sobre como aparece, ou sobre o que acontece quando alguém faz alguma coisa. Na alínea d), repara na forma do código: há chavetas e um valor depois de dois pontos?

**Exercício 3.** O protocolo acaba antes de `://`. O domínio vai até à primeira barra a seguir. O fragmento começa no cardinal. O resto é o caminho. Na alínea c), relê o fim da secção "Cliente e servidor".

**Exercício 4.** Relê a tabela das quatro famílias de códigos. O primeiro algarismo diz de quem é o problema, se houver problema.

**Exercício 5.** Começa pela página inicial, no topo. Depois pergunta se cada receita merece uma página só dela, ou se todas cabem numa página. Para o menu, relê a nota sobre as páginas dos recursos da Estante Digital, no fim da secção "O mapa do site".

**Exercício 6.** Faz uma linha por cada palavra marcada como ligação nas anotações, incluindo as do menu e a do rodapé. Para cada uma, procura no mapa uma caixa com o mesmo nome. Um dos problemas não é uma página que falta: é um nome.

## Desafio opcional (20 min)

Desenha o wireframe largo da página inicial do clube de teatro do exercício 6, já com os três problemas corrigidos, para o ecrã de um computador. Põe lado a lado o que achares que ganha em ficar lado a lado. Depois confirma, lendo da esquerda para a direita e de cima para baixo, que a ordem de leitura é a mesma do wireframe estreito. Se não for, explica o que mudavas.

## Para ires mais longe

Esta secção é opcional e fica fora dos 45 minutos da ficha.

### Mais longe 1: Um endereço com parâmetros (10 min)

Num site de receitas, escreveste "sopa" na caixa de pesquisa e carregaste em Pesquisar. A barra de endereço passou a mostrar isto:

```text
https://receitas.example.com/pesquisa.html?termo=sopa&pagina=2
```

**a)** Parte o endereço em protocolo, domínio, caminho e parâmetros.

**b)** Quantos parâmetros há, e o que achas que diz cada um?

**c)** O que esperas que aconteça se mudares, na barra de endereço, `sopa` para `bolo` e carregares em Enter? Experimenta num site de pesquisa verdadeiro que uses e vê se acertaste.

## Critérios de conclusão

- [ ] Nos exercícios 1 e 2, justifiquei cada resposta com a pergunta do apoio, e não por palpite.
- [ ] No exercício 3, separei as partes do endereço e expliquei porque é que um endereço `file://` não funciona noutro computador.
- [ ] No exercício 4, escrevi o código e a família de cada situação.
- [ ] No exercício 5, o meu mapa tem a página inicial no topo, todas as páginas ligadas a ela, e um menu justificado.
- [ ] No exercício 6, verifiquei todas as ligações do wireframe, encontrei os três problemas e propus uma correção para cada um.

## Autoavaliação breve

O que já consigo fazer sozinho:

Uma dificuldade que tive e o que fiz para a resolver:

![Rodapé](../imagens/rodape.png)
