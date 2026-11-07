![Cabeçalho](../../imagens/cabecalho.png)

# Ficha de exercícios: A Web, os utilizadores e o planeamento

Praticas a Internet e a Web, as três linguagens, os endereços, os códigos de resposta e o mapa de um site. No fim, fazes o plano do teu. Os exercícios 1 a 7 são obrigatórios. Escreve as respostas no VS Code, num ficheiro `respostas.md`, com o número do exercício e a letra da alínea, e faz os desenhos em papel. Entregas o ficheiro, os desenhos e o plano do teu site onde o professor indicar. Para rever: o [guia do tema](../01-web-e-planeamento.md) e o [laboratório](../laboratorios/01-web-e-planeamento-laboratorio.md).

## Exercício 1: Distinguir a Internet da Web

Para cada situação, diz se a pessoa está a usar a Web, ou se está a usar a Internet mas não a Web. Justifica cada resposta numa frase curta.

**a)** A Rita abre o site da escola no browser para ver a ementa da cantina.

**b)** O Tiago joga um jogo em rede na consola, contra jogadores de outros países.

**c)** A avó faz uma videochamada numa aplicação instalada no telemóvel.

**d)** A Joana lê o correio eletrónico num site, aberto no browser do computador.

Rever: [A Internet e a Web não são a mesma coisa](../01-web-e-planeamento.md#a-internet-e-a-web-não-são-a-mesma-coisa).

<details>
<summary>Pista</summary>

Em cada caso, pergunta-te o que a pessoa tem aberto: páginas lidas num browser, ou outra aplicação que comunica pela rede?

</details>

## Exercício 2: A linguagem de cada trabalho

Nas alíneas a) a c), diz se cada mudança pedida num site é trabalho do HTML, do CSS ou do JavaScript. Justifica cada resposta numa frase curta.

**a)** Os títulos das páginas passam a ser azuis e maiores.

**b)** Quando se carrega no botão "Só sobremesas", a lista de receitas passa a mostrar só as sobremesas.

**c)** A lista de ingredientes, que estava escrita como um parágrafo corrido, passa a estar marcada como lista.

**d)** De que linguagem é esta linha de código? Justifica numa frase.

```text
nav { background: #2e7d32; }
```

Rever: [Três linguagens, três trabalhos](../01-web-e-planeamento.md#três-linguagens-três-trabalhos).

<details>
<summary>Pista</summary>

A mudança é sobre o que a coisa é, sobre como aparece, ou sobre o que acontece quando alguém faz alguma coisa? Na alínea d), compara a forma da linha com as três partes do botão "Gostar", no guia.

</details>

## Exercício 3: Partir um endereço

**a)** Parte este endereço em protocolo, domínio e caminho:

```text
https://www.example.com/clube/torneios/outono.html
```

**b)** Neste segundo endereço, diz qual é o protocolo e onde está o ficheiro:

```text
file:///C:/Users/aluno/Documents/clube-de-xadrez/index.html
```

**c)** Envias o endereço da alínea b) a um colega, por mensagem. O colega tem os mesmos ficheiros, tirados do mesmo ZIP, mas guardou-os noutra pasta do computador dele. Abre-lhe a página? E se ele os tivesse guardado exatamente no mesmo caminho? Explica cada resposta numa frase.

Rever: [O endereço de uma página](../01-web-e-planeamento.md#o-endereço-de-uma-página) e [Uma página do teu disco não vem de um servidor](../01-web-e-planeamento.md#uma-página-do-teu-disco-não-vem-de-um-servidor).

<details>
<summary>Pista</summary>

O protocolo acaba antes de `://`. O domínio é o nome do servidor, e vai até à barra seguinte. Na alínea c), pensa no sítio onde o ficheiro está guardado.

</details>

## Exercício 4: Os códigos de resposta

Diz que código de resposta recebe o browser em cada situação, e a família a que pertence. Justifica cada resposta numa frase curta.

**a)** A página pedida existe, e o servidor envia-a sem problemas.

**b)** Uma ligação aponta para uma página que foi apagada do site.

**c)** A página existe, mas, do lado do site, alguma coisa falha antes de ela ser enviada.

**d)** Escreveste o endereço antigo de uma página que mudou de endereço, e o browser levou-te sozinho ao novo.

Rever: [A resposta diz como correu o pedido](../01-web-e-planeamento.md#a-resposta-diz-como-correu-o-pedido).

<details>
<summary>Pista</summary>

O primeiro algarismo diz a família. Em cada situação, pergunta-te se correu bem e, se não correu, se o problema está no que se pediu ou no servidor.

</details>

## Exercício 5: Desenhar o mapa de um site

A Carolina quer fazer o site "Receitas da Avó", com este conteúdo, já agrupado:

- uma apresentação do site, a dizer que as receitas são da família e para quem é;
- 36 receitas, cada uma com os ingredientes e os passos: 12 sopas, 14 pratos principais e 10 doces;
- uma página com a história do caderno de receitas da família.

**a)** Desenha o mapa do site, com uma caixa por página e linhas para as ligações. As páginas das receitas, todas com a mesma forma, podem ser uma só caixa. Há mais do que um mapa certo: escolhe um e segue as regras do guia. Justifica numa frase onde puseste a lista das receitas.

**b)** Diz que páginas vão para o menu, que se repete em todas as páginas. Justifica numa frase porque é que as outras ficam de fora.

Rever: [O mapa do site](../01-web-e-planeamento.md#o-mapa-do-site) e [Passo 4: As páginas](../01-web-e-planeamento.md#passo-4-as-páginas).

<details>
<summary>Pista</summary>

Começa pela página inicial, no topo, e decide onde fica a lista das receitas. Para o menu, relê a regra das páginas de que há muitas.

</details>

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

**a)** Completa a tabela de verificação, com uma linha por ligação desenhada no wireframe e o destino que ela tem no mapa. As duas primeiras linhas já estão preenchidas.

| Ligação desenhada | Onde está | Destino no mapa | Resultado |
| --- | --- | --- | --- |
| Início | Menu | Início | Existe |
| Peças | Menu | Peças | Existe |

**b)** Olhando para o mapa e para este wireframe, há dois problemas no plano do Rafael. Diz quais são e propõe uma correção para cada um. Pode haver mais do que uma correção certa: diz qual escolherias e porquê.

Rever: [O mapa e os wireframes têm de concordar](../01-web-e-planeamento.md#o-mapa-e-os-wireframes-têm-de-concordar) e [Passo 9: Verificar a coerência](../01-web-e-planeamento.md#passo-9-verificar-a-coerência).

<details>
<summary>Pista</summary>

Na alínea a), faz uma linha por cada ligação que as anotações marcam, em todas as zonas do wireframe. Na alínea b), aplica as verificações do guia que se podem fazer com um só wireframe.

</details>

## Exercício 7: O plano do teu site

Faz o plano do teu site, com o tema que escolheste do menu do professor. Faz uma cópia do [modelo do brief e wireframe](../../projeto/modelos/brief-e-wireframe.md) e preenche os campos que a tabela do guia diz que se preenchem neste tema. O mapa do site tem pelo menos duas páginas. O mapa e os wireframes desenham-se em papel e fotografam-se.

O plano está pronto quando um colega encontra nele uma informação que lhe pedes, sem explicações tuas. Escreve no brief o que aconteceu. Guarda a cópia do brief e as fotografias onde o professor indicar. Ficam numa pasta com o nome do teu site, em minúsculas e sem espaços, como `estante-digital`.

Rever: [Um site planeia-se antes de se escrever](../01-web-e-planeamento.md#um-site-planeia-se-antes-de-se-escrever), [O brief junta o plano num só documento](../01-web-e-planeamento.md#o-brief-junta-o-plano-num-só-documento) e [Exemplo guiado: o plano da Estante Digital](../01-web-e-planeamento.md#exemplo-guiado-o-plano-da-estante-digital).

<details>
<summary>Pista</summary>

Segue a ordem do diagrama do guia: o utilizador, o conteúdo, o mapa, os wireframes, a verificação e o brief. Escolhe uma pessoa concreta, e não "toda a gente". Começa pequeno: três páginas bem pensadas valem mais do que vinte vazias.

</details>

## Desafios

1. Desenha o wireframe largo da página inicial do clube de teatro do exercício 6, já com os dois problemas corrigidos. Põe lado a lado o que achares que ganha em ficar lado a lado, sem mudar a ordem de leitura do wireframe estreito.

2. Num site de receitas, pesquisaste "sopa" e, nos resultados, carregaste em Seguinte. A barra de endereço passou a mostrar `https://receitas.example.com/pesquisa.html?termo=sopa&pagina=2#resultados`. Parte o endereço em protocolo, domínio, caminho, parâmetros e fragmento, e diz o que achas que faz cada parâmetro. Rever: [O endereço de uma página](../01-web-e-planeamento.md#o-endereço-de-uma-página).

## Critérios de conclusão

- Nos exercícios 1, 2 e 4, cada resposta tem uma justificação.
- No exercício 3, as partes dos endereços estão separadas, e as duas perguntas da alínea c) têm a resposta explicada.
- No exercício 5, o mapa tem a página inicial no topo e todas as páginas ligadas a ela.
- No exercício 6, a tabela está completa, e os dois problemas têm uma correção cada.
- O plano do teu site tem o brief, o mapa e os dois wireframes, e um colega encontrou nele o que procurava.

![Rodapé](../../imagens/rodape.png)
