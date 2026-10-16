![Cabeçalho](../imagens/cabecalho.png)

# Ficha de exercícios: A Web, os utilizadores e o planeamento

Ficha do tema A Web, os utilizadores e o planeamento, do módulo Conceber aplicações para a web na vertente frontend. Praticas os assuntos do tema, um de cada vez. São a Internet e a Web, as três linguagens, os endereços, os códigos de resposta e o plano de um site. Fazes sozinho, ao teu ritmo: o que não acabares na aula, acabas em casa ou na aula seguinte.

## O que precisas de saber

O [guia do tema](01-web-e-planeamento.md) e o [laboratório](01-web-e-planeamento-laboratorio.md). Cada exercício usa uma parte do guia:

- Exercício 1: a secção "A Internet e a Web não são a mesma coisa".
- Exercício 2: a secção "Três linguagens, três trabalhos".
- Exercício 3: as secções "O endereço de uma página" e "Cliente e servidor".
- Exercício 4: a secção "O que se diz num pedido e numa resposta".
- Exercício 5: a secção "O mapa do site" e os passos 3 a 5 do exemplo guiado.
- Exercício 6: a secção "O mapa e os wireframes têm de concordar" e o passo 9 do exemplo guiado.

Se encravares, volta a essa parte do guia antes de olhares para o apoio, no fim da ficha.

## Como trabalhar

Resolve os exercícios pela ordem. Cada exercício treina uma só coisa:

| Exercício | O que treina |
| --- | --- |
| 1 | Distinguir a Internet da Web |
| 2 | Atribuir cada trabalho à linguagem certa |
| 3 | Partir um endereço nas suas partes |
| 4 | Ler os códigos de resposta |
| 5 | Desenhar o mapa de um site a partir do seu conteúdo |
| 6 | Confirmar que um mapa e um wireframe concordam |
| Desafio opcional | Passar um wireframe estreito a largo |
| Para ires mais longe | Ler um endereço com parâmetros |

Os exercícios 1 a 6 são obrigatórios. O desafio e a secção "Para ires mais longe" são opcionais.

Entregas as respostas escritas dos exercícios 1 a 6, com o mapa do exercício 5 desenhado à mão. Se fizeres o desafio e o exercício de "Para ires mais longe", entregas também esses.

Os sites desta ficha são inventados, e não são o teu site nem a Estante Digital.

## Exercício 1: Distinguir a Internet da Web

Para cada situação, diz se a pessoa está a usar a Web, ou se está a usar a Internet mas não a Web. Justifica cada resposta numa frase curta.

**a)** A Rita abre o site da escola no browser para ver a ementa da cantina.

**b)** O Tiago joga um jogo em rede na consola, contra jogadores de outros países.

**c)** A avó faz uma videochamada numa aplicação instalada no telemóvel.

**d)** O Duarte lê, no browser do telemóvel, uma página de um site de notícias.

## Exercício 2: A linguagem de cada trabalho

Para cada mudança pedida num site, diz se é trabalho do HTML, do CSS ou do JavaScript. Justifica cada resposta numa frase curta.

**a)** Os títulos das páginas passam a ser azuis e maiores.

**b)** Quando se carrega no botão "Só sobremesas", a lista de receitas passa a mostrar só as sobremesas.

**c)** A lista de ingredientes, que estava escrita como um parágrafo corrido, passa a estar marcada como lista.

**d)** Esta linha de código:

```text
nav { background: #1f4e8c; }
```

## Exercício 3: Partir um endereço

**a)** Parte este endereço em protocolo, domínio, caminho e fragmento:

```text
https://www.example.com/clube/torneios/outono.html#inscricoes
```

**b)** Neste segundo endereço, diz qual é o protocolo e onde está o ficheiro:

```text
file:///C:/Users/aluno/Documents/clube-de-xadrez/index.html
```

**c)** Envias o endereço da alínea b) a um colega, por mensagem. O colega tem os mesmos ficheiros, tirados do mesmo ZIP, mas guardou-os noutra pasta do computador dele. Abre-lhe a página? E se ele o tivesse guardado exatamente no mesmo caminho? Explica cada resposta numa frase.

## Exercício 4: Os códigos de resposta

Diz que código de resposta recebe o browser em cada situação, e a família a que pertence. Justifica cada resposta numa frase curta.

**a)** A página pedida existe, e o servidor envia-a sem problemas.

**b)** Uma ligação aponta para uma página que foi apagada do site.

**c)** A página existe, mas o programa que a monta no servidor tem um erro e para a meio.

**d)** Escreveste o endereço antigo de uma página que mudou de endereço, e o browser levou-te sozinho ao novo.

## Exercício 5: Desenhar o mapa de um site

A Carolina quer fazer o site "Receitas da Avó", com este conteúdo, já agrupado:

- uma apresentação do site, a dizer que as receitas são da família e para quem é;
- 36 receitas, cada uma com os ingredientes e os passos: 12 sopas, 14 pratos principais e 10 doces;
- uma página com a história do caderno de receitas da família, sem dados pessoais.

**a)** Desenha o mapa do site, com uma caixa por página e linhas para as ligações. Há mais do que um mapa certo: escolhe um e segue as regras do guia. Justifica numa frase onde puseste a lista das receitas.

**b)** Diz que páginas vão para o menu, que se repete em todas as páginas. Justifica numa frase porque é que as outras ficam de fora.

## Exercício 6: Confirmar que o mapa e o wireframe concordam

O Rafael fez o plano do site do clube de teatro da escola. Este é o mapa dele:

```text
Início
├── Peças
│   ├── A Ilha dos Relógios
│   └── O Último Autocarro
├── Galeria
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
│ [X] [X] [X]                    │   fotografias do último
│                                │   espetáculo, sem ligação
├────────────────────────────────┤
│ Clube de Teatro da escola      │   rodapé, sem ligações
└────────────────────────────────┘
```

**a)** Completa a tabela de verificação, como a do passo 9 do exemplo guiado. Tem uma linha por ligação desenhada no wireframe, com o destino que essa ligação tem no mapa. As duas primeiras linhas já estão preenchidas. Acrescenta as que faltam.

| Ligação desenhada | Onde está | Destino no mapa | Resultado |
| --- | --- | --- | --- |
| Início | Menu | Início | Existe |
| Peças | Menu | Peças | Existe |

**b)** Há dois problemas no plano do Rafael. Diz quais são.

**c)** Para cada problema, propõe uma correção. Pode haver mais do que uma correção certa: diz qual escolhias e porquê.

## Apoio

Usa estas pistas só depois de tentares sozinho. Nenhuma dá a resposta: indicam onde olhar.

- Exercício 1: em cada caso, pergunta-te o que a pessoa tem aberto. São páginas lidas num browser, ou outra aplicação que comunica pela rede?
- Exercício 2: em cada caso, pergunta-te sobre o que é a mudança. É sobre o que a coisa é, sobre como aparece, ou sobre o que acontece quando alguém faz alguma coisa? Na alínea d), compara a forma da linha com as três formas do botão "Gostar", no guia.
- Exercício 3: o protocolo acaba antes de `://`. O domínio é o nome do servidor, e vai até à barra seguinte. O fragmento começa no cardinal. O resto é o caminho. Na alínea c), pensa no sítio onde o ficheiro está guardado.
- Exercício 4: relê a tabela das quatro famílias de códigos. O primeiro algarismo diz de quem é o problema, se houver problema.
- Exercício 5: começa pela página inicial, no topo. Depois decide que páginas fazem falta para as receitas, e onde fica a lista delas. Para o menu, relê a nota sobre as páginas dos recursos da Estante Digital, no fim da secção "O mapa do site".
- Exercício 6: na alínea a), faz uma linha por cada ligação que as anotações marcam, em todas as zonas do wireframe. Para cada uma, procura no mapa a caixa que lhe corresponde. Na alínea b), relê as quatro verificações da secção "O mapa e os wireframes têm de concordar" e aplica-as uma a uma.

## Desafio opcional

Desenha o wireframe largo da página inicial do clube de teatro do exercício 6, para o ecrã de um computador. Desenha-o já com os dois problemas corrigidos. Põe lado a lado o que achares que ganha em ficar lado a lado. Depois lê-o da esquerda para a direita e de cima para baixo, e confirma que a ordem de leitura é a mesma do wireframe estreito. Se não for, explica o que mudavas.

## Para ires mais longe

Esta secção é opcional.

### Mais longe 1: Um endereço com parâmetros

Num site de receitas, escreveste "sopa" na caixa de pesquisa e carregaste em Pesquisar. A barra de endereço passou a mostrar isto:

```text
https://receitas.example.com/pesquisa.html?termo=sopa&pagina=2
```

**a)** Parte o endereço em protocolo, domínio, caminho e parâmetros.

**b)** Quantos parâmetros há, e o que achas que diz cada um?

**c)** O que esperas que aconteça se mudares, na barra de endereço, `sopa` para `bolo` e carregares em Enter? Experimenta num site de pesquisa verdadeiro que uses e vê se acertaste.

## Critérios de conclusão

- [ ] Nos exercícios 1, 2 e 4, justifiquei cada resposta numa frase, e não por palpite.
- [ ] No exercício 3, separei as partes dos endereços e expliquei quando é que um endereço `file://` abre noutro computador.
- [ ] No exercício 4, escrevi o código e a família de cada situação.
- [ ] No exercício 5, o meu mapa tem a página inicial no topo e todas as páginas ligadas a ela.
- [ ] No exercício 5, justifiquei onde ficou a lista das receitas e que páginas vão para o menu.
- [ ] No exercício 6, completei a tabela, encontrei os dois problemas e propus uma correção para cada um.

## Autoavaliação

1. O que já consegues fazer sozinho?
2. Que dificuldade tiveste, e o que fizeste para a resolver?

![Rodapé](../imagens/rodape.png)
