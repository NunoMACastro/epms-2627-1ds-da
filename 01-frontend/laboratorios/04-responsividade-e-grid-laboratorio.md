![Cabeçalho](../../imagens/cabecalho.png)

# Laboratório: Responsividade e Grid

## O que vais construir

Pões o teu site a funcionar num telemóvel e num ecrã largo. Nada sai da página, os cartões passam a uma grelha, e duas partes da página inicial ficam lado a lado. Registas três defeitos e guardas cada passo num commit. Os exemplos usam o clube de xadrez: escreve os teus textos.

No fim, a página inicial do exemplo fica assim, a 320 e a 1280 píxeis de largura:

```text
320 píxeis                              1280 píxeis
┌──────────────────────────────────┐    ┌────────────────────────────────────────────────────┐
│ Clube de Xadrez  Início Torneios │    │ Clube de Xadrez                   Início  Torneios │
├──────────────────────────────────┤    ├────────────────────────────────────────────────────┤
│ Aprende a jogar                  │    │ Aprende a jogar xadrez connosco                    │
│ xadrez connosco                  │    │                                                    │
│ Quando nos encontramos           │    │ Quando nos encontramos   O que precisas de trazer  │
│ Às quartas-feiras...             │    │ Às quartas-feiras...     - Vontade de aprender.    │
│ O que precisas de trazer         │    │                                                    │
│ - Vontade de...                  │    │ As peças e como se movem                           │
│ As peças e como se               │    │ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ │
│ movem                            │    │ │ Rei          │ │ Dama         │ │ Torre        │ │
│ ┌─────────────────────────────┐  │    │ └──────────────┘ └──────────────┘ └──────────────┘ │
│ │ Rei: anda uma casa, em      │  │    │ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ │
│ │ qualquer direção.           │  │    │ │ Bispo        │ │ Cavalo       │ │ Peão         │ │
│ └─────────────────────────────┘  │    │ └──────────────┘ └──────────────┘ └──────────────┘ │
│ ┌─────────────────────────────┐  │    │ ┌──────────────┐                                   │
│ │ Dama: anda as casas que...  │  │    │ │ Roque        │                                   │
│ └─────────────────────────────┘  │    │ └──────────────┘                                   │
│ ...                              │    └────────────────────────────────────────────────────┘
└──────────────────────────────────┘
```

1. [Fase 1: As ferramentas do programador simulam outros ecrãs](#fase-1-as-ferramentas-do-programador-simulam-outros-ecrãs)
2. [Fase 2: Uma imagem não pode ser mais larga do que a caixa](#fase-2-uma-imagem-não-pode-ser-mais-larga-do-que-a-caixa)
3. [Fase 3: A Grid arruma em linhas e colunas](#fase-3-a-grid-arruma-em-linhas-e-colunas)
4. [Fase 4: O minmax e o auto-fill escolhem o número de colunas](#fase-4-o-minmax-e-o-auto-fill-escolhem-o-número-de-colunas)
5. [Fase 5: Uma media query muda a arrumação a partir de uma largura](#fase-5-uma-media-query-muda-a-arrumação-a-partir-de-uma-largura)
6. [Fase 6: O ponto de mudança escolhe-se pelo conteúdo](#fase-6-o-ponto-de-mudança-escolhe-se-pelo-conteúdo)
7. [Fase 7: Um texto comprido não pode sair da caixa](#fase-7-um-texto-comprido-não-pode-sair-da-caixa)
8. [Fase 8: A página testa-se em várias larguras, com o zoom e com o teclado](#fase-8-a-página-testa-se-em-várias-larguras-com-o-zoom-e-com-o-teclado)

## O que precisas

- O VS Code e o Chrome ou o Edge, com as ferramentas do programador.
- A pasta do teu site, com o CSS do [laboratório do tema 03](03-css-e-flexbox-laboratorio.md), no GitHub, e o `registo.md` ao lado dela. Se o site ainda não está no GitHub, faz primeiro o [laboratório do tema 02 do Git](../../02-git/laboratorios/02-partilhar-versoes-com-o-github-laboratorio.md). Se não acabaste o laboratório 03, copia o `estilos.css` completo da paragem 13 dele e guarda-o num commit.

## Preparar o projeto

1. No VS Code, abre a pasta do teu site e um terminal, como no laboratório do tema 02 do Git. Começa pela rotina: corre o `git pull` e escreve a tua frase-passe. O que deves ver: `Already up to date.`, ou os commits que fizeste noutro sítio.

2. Corre o `git status`. O que deves ver, no fim: `nothing to commit, working tree clean`.

3. Abre o `registo.md`, com Open Recent, no menu File, e confirma o caminho, porque o portátil pode mostrar o de outro colega. Escreve no fim o título `## Laboratório da página que se adapta` e guarda.

4. Abre a página inicial do teu site no browser, com duplo clique no `index.html`, no Explorador de Ficheiros. Deixa o browser e o VS Code lado a lado.

## Fase 1: As ferramentas do programador simulam outros ecrãs

Vês o teu site com a largura de um telemóvel, de um tablet e de um portátil, e encontras o primeiro defeito. Rever: [As ferramentas do programador simulam outros ecrãs](../04-responsividade-e-grid.md#as-ferramentas-do-programador-simulam-outros-ecrãs).

1. No browser, abre as ferramentas do programador, com F12, e liga a barra de dispositivos, com Ctrl+Shift+M, ou Cmd+Shift+M no Mac. O que deves ver: por cima da página, uma barra com Dimensions: Responsive e duas caixas com números, a largura e a altura. Se não aparecer, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

2. Na primeira caixa, escreve `1280` e carrega em Enter. Depois experimenta `768` e `320`. O que deves ver, no exemplo: a 1280 e a 768, a página como a deixaste no tema 03. A 320, os cartões um por linha, com a largura toda.

3. Ainda a 320, abre a segunda página pelo menu, `torneios.html` no exemplo, que tem a imagem. O que deves ver: a imagem passa da margem direita, cortada, e a página mexe para o lado quando a arrastas com o rato. É a barra de deslocamento horizontal. Na barra de dispositivos, essa barra é fina e pode desaparecer, e o sinal seguro é a página mexer para o lado. É o primeiro defeito.

4. Encontra o culpado. No separador Elements, passa o rato pelos elementos, de fora para dentro. Abre o `main` e a `section`, com o triângulo de cada um, e passa o rato pelo `img`. O que deves ver: o browser pinta na página cada elemento por onde passas. O `img` passa da margem direita, e a caixa que aparece ao lado diz `img 400 × 300`. A imagem tem 400 píxeis, e o ecrã só 320.

5. No VS Code, abre as duas páginas e procura no `head` a linha do `viewport`, do tema 02. O que deves ver: `<meta name="viewport" content="width=device-width, initial-scale=1">` nas duas. Sem ela, o telemóvel desenhava a página com 980 píxeis. Se faltar numa página, copia-a da outra.

### Paragem 1

Sabes ver o teu site em qualquer largura e encontrar a caixa que sai da página.

Pensa antes de continuares: porque é que não chega estreitar a janela do browser para ver a página como num telemóvel? A resposta: a janela não fica mais estreita do que uns 500 píxeis. A barra de dispositivos dá qualquer largura, como os 320 de um telemóvel pequeno.

## Fase 2: Uma imagem não pode ser mais larga do que a caixa

Corriges o primeiro defeito com uma regra que vale para todas as imagens do site. Rever: [Uma imagem não pode ser mais larga do que a caixa](../04-responsividade-e-grid.md#uma-imagem-não-pode-ser-mais-larga-do-que-a-caixa).

1. Em `estilos.css`, a seguir à regra do `body`, acrescenta esta regra, só com o `max-width`, e guarda:

   ```css
   /* Nenhuma imagem passa da largura da caixa onde está. */
   img {
     max-width: 100%;
   }
   ```

2. Antes de recarregares a página dos torneios, a 320 píxeis, prevê: a imagem fica com que largura, e com que altura? Depois recarrega, com F5. O que deves ver: a página já não mexe para o lado, e a imagem tem 288 píxeis de largura, a do conteúdo do `main`. Mas a altura ficou nos 300 do HTML, e a imagem provisória ganhou espaço vazio por cima e por baixo. Uma fotografia ficava esticada.

3. Acrescenta à regra a linha que falta e o comentário dela:

   ```css
   /* Nenhuma imagem passa da largura da caixa onde está.
      O height: auto mantém a proporção quando a largura encolhe. */
   img {
     max-width: 100%;
     height: auto;
   }
   ```

   Guarda e recarrega. O que deves ver: a imagem com 288 por 216 píxeis, sem espaço vazio. A 1280, volta aos 400 por 300, porque cabe na caixa.

4. No `registo.md`, por baixo do título do laboratório, escreve o defeito em quatro linhas, como no exemplo:

   ```text
   Defeito 1: a imagem dos torneios saía pela direita e criava uma barra horizontal.
   Largura: 320 píxeis.
   Causa: a imagem tem width="400" no HTML, e o conteúdo do main só tem 288 de largura.
   Correção: a regra img com max-width: 100% e height: auto.
   ```

5. Guarda o passo num commit:

   ```bash
   git add estilos.css
   git diff --staged
   git commit -m "Põe as imagens a caber na largura do ecrã"
   ```

   O que deves ver: no `git diff --staged`, as linhas da regra `img` com `+`. No commit, `1 file changed`.

### Paragem 2

Nenhuma imagem do teu site passa da largura do ecrã, e o primeiro defeito está no registo.

Pensa antes de continuares: porque é que a regra tem `max-width` e não `width`? A resposta: com `width: 100%`, as imagens pequenas também esticavam. O `max-width` só encolhe as que não cabem.

## Fase 3: A Grid arruma em linhas e colunas

Acrescentas um cartão à coleção, vês o problema do Flexbox e passas os cartões para uma grelha de três colunas. Rever: [A Grid arruma em linhas e colunas](../04-responsividade-e-grid.md#a-grid-arruma-em-linhas-e-colunas).

1. Em `index.html`, acrescenta um item à lista com a classe `cartoes`, a seguir ao último. No exemplo:

   ```html
   <li>Roque: o rei e uma torre mexem-se na mesma jogada, uma vez por partida.</li>
   ```

   Guarda e recarrega a página inicial a 1280 píxeis. O que deves ver: se o último cartão ficar sozinho na linha dele, ocupa a linha toda e é muito maior do que os outros. No exemplo, com sete cartões, o sétimo tem 928 píxeis, e os outros cerca de 299. Se nenhum cartão ficar sozinho na tua última linha, acrescenta itens até ficar um.

2. Em `estilos.css`, na regra `.cartoes`, troca as duas linhas do Flexbox, `display: flex;` e `flex-wrap: wrap;`, por estas duas:

   ```css
     display: grid;
     grid-template-columns: 1fr 1fr 1fr;
   ```

   Guarda e recarrega, a 1280. O que deves ver: três colunas iguais, e o último cartão na primeira coluna da última linha, com a mesma largura dos outros.

3. Põe a largura em 320. O que deves ver: as três colunas continuam lá, com uns 100 píxeis cada. O texto dos cartões fica com uma ou duas palavras por linha, e a página volta a mexer para o lado. Três colunas fixas não servem num telemóvel, e a fase seguinte resolve isto.

### Paragem 3

Os cartões estão numa grelha de três colunas iguais, que funciona num ecrã largo, mas não num telemóvel.

Pensa antes de continuares: porque é que, com a Grid, o último cartão deixou de esticar? A resposta: as colunas são as mesmas para todas as linhas. O último cartão fica numa coluna, com a largura dela, e não ocupa o espaço que sobra na linha.

## Fase 4: O minmax e o auto-fill escolhem o número de colunas

Trocas as três colunas fixas por tantas colunas quantas couberem, cada uma com pelo menos 15rem. Rever: [O minmax e o auto-fill escolhem o número de colunas](../04-responsividade-e-grid.md#o-minmax-e-o-auto-fill-escolhem-o-número-de-colunas).

1. Na regra `.cartoes`, troca o `grid-template-columns` por este:

   ```css
     grid-template-columns: repeat(auto-fill, minmax(15rem, 1fr));
   ```

   E na regra `.cartoes li`, apaga as linhas do `flex-basis` e do `flex-grow`, que só servem no Flexbox. Muda o comentário da regra `.cartoes` para dizer o que ela faz agora. No exemplo:

   ```css
   /* A lista dos cartões, sem bolinhas nem recuo, numa grelha com tantas colunas
      quantas couberem, cada uma com pelo menos 15rem. */
   ```

2. Guarda e recarrega, nas três larguras de amostra. O que deves ver, no exemplo:

   | Largura | Colunas | Largura de cada cartão |
   | ---: | ---: | ---: |
   | 320 | 1 | 288 píxeis |
   | 768 | 2 | 360 píxeis |
   | 1280 | 3 | 299 píxeis |

   Em nenhuma largura a página mexe para o lado, e o último cartão tem sempre a largura dos outros.

3. No `registo.md`, escreve o segundo defeito, com as mesmas quatro linhas. O defeito é o cartão sozinho na última linha, que esticava com o Flexbox, a 1280 píxeis.

4. Guarda o passo num commit, com os dois ficheiros:

   ```bash
   git add index.html estilos.css
   git diff --staged
   git commit -m "Arruma os cartões numa grelha"
   ```

   O que deves ver: o `git diff --staged` é comprido e aparece aos bocados; sai com a tecla `q`. O commit responde `2 files changed`.

### Paragem 4

Os cartões arrumam-se sozinhos em uma, duas ou três colunas, conforme a largura, sem nenhuma media query.

Pensa antes de continuares: a 768 píxeis, porque é que há duas colunas, e não três? A resposta: três colunas de 240 píxeis, com os dois espaços, precisam de 752, e o conteúdo do `main` só tem 736. Cabem duas, e crescem até encher a linha.

## Fase 5: Uma media query muda a arrumação a partir de uma largura

Pões duas partes da página inicial lado a lado nos ecrãs largos, como no teu wireframe largo do tema 01. Rever: [Uma media query muda a arrumação a partir de uma largura](../04-responsividade-e-grid.md#uma-media-query-muda-a-arrumação-a-partir-de-uma-largura).

1. Escolhe duas partes curtas da página inicial para pôr lado a lado. Se o teu wireframe largo, do tema 01, já põe duas lado a lado, usa essas. No exemplo, são as duas secções curtas, "Quando nos encontramos" e "O que precisas de trazer". Em `index.html`, põe-nas dentro de uma caixa nova, com a classe `duas-colunas`:

   ```html
   <!-- Esta caixa só serve para o CSS pôr as duas secções lado a lado nos ecrãs largos. -->
   <div class="duas-colunas">
     <section>
       <h2>Quando nos encontramos</h2>
       ...
     </section>

     <section>
       <h2>O que precisas de trazer</h2>
       ...
     </section>
   </div>
   ```

   Os `...` são o conteúdo que as secções já têm. Para acertar a indentação, usa o Format Document: Shift+Alt+F, ou Shift+Option+F no Mac.

2. No fim de `estilos.css`, acrescenta a regra de base da caixa e a media query:

   ```css
   /* As duas secções curtas: uma por baixo da outra no ecrã estreito. */
   .duas-colunas {
     display: grid;
     gap: var(--espaco);
   }

   /* A partir de 30rem, as duas secções ficam lado a lado. */
   @media (min-width: 30rem) {
     .duas-colunas {
       grid-template-columns: 1fr 1fr;
     }
   }
   ```

3. Guarda e recarrega a página inicial. Experimenta as larguras `470` e `480`, que é 30 vezes 16. O que deves ver: a 470, as duas secções uma por baixo da outra. A 480, lado a lado, cada uma com 216 píxeis. Se nada mudar, vê [Se alguma coisa falhar](#se-alguma-coisa-falhar).

4. Ainda a 480, olha para os títulos das duas secções. O que deves ver, no exemplo: os dois partidos em duas linhas, "Quando nos" e "encontramos", "O que precisas de" e "trazer". As colunas são estreitas demais para eles. A largura de 30rem foi um palpite, e a fase seguinte troca-a por uma que vem do conteúdo.

### Paragem 5

A página inicial muda de arrumação a partir de uma largura, com uma media query, mas o ponto de mudança ainda está mal escolhido.

Pensa antes de continuares: a 1280 píxeis, a media query de 30rem também vale? A resposta: vale. O `min-width` quer dizer "a partir de", e por isso a media query vale em todas as larguras de 480 píxeis para cima.

## Fase 6: O ponto de mudança escolhe-se pelo conteúdo

Encontras a largura a partir da qual as duas partes cabem lado a lado e mudas o ponto de mudança para ela. Rever: [O ponto de mudança escolhe-se pelo conteúdo](../04-responsividade-e-grid.md#o-ponto-de-mudança-escolhe-se-pelo-conteúdo).

1. Escolhe o que tem de caber em cada coluna. No exemplo, cada título numa só linha, porque um título partido custa a ler.

2. Põe a largura em `700` e vai diminuindo, de 10 em 10: `690`, `680`, e assim por diante. Para em cada uma e olha para os títulos. O que deves ver, no exemplo: os dois numa linha até 630, e um deles partido a 620. O ponto de mudança fica entre 620 e 630.

3. Passa a largura para `rem`: divide-a por 16 e arredonda para cima. No exemplo, 630 a dividir por 16 dá 39,4, que arredonda para 40.

4. Em `estilos.css`, muda a media query e o comentário dela para a tua largura. No exemplo:

   ```css
   /* A partir de 40rem, as duas secções ficam lado a lado,
      e os dois títulos cabem numa linha cada. */
   @media (min-width: 40rem) {
   ```

5. Guarda e recarrega. Experimenta a última largura em que um título se partia e a tua largura em `rem` vezes 16. No exemplo, 620 e 640. O que deves ver: na primeira, as duas secções uma por baixo da outra; na segunda, lado a lado, com os dois títulos numa linha.

6. Guarda o passo num commit:

   ```bash
   git add index.html estilos.css
   git diff --staged
   git commit -m "Põe as duas secções lado a lado nos ecrãs largos"
   ```

   O que deves ver: `2 files changed`, no fim da resposta do commit.

### Paragem 6

O ponto de mudança é a largura em que o teu conteúdo cabe na arrumação larga, e o comentário da media query diz porquê.

Pensa antes de continuares: porque é que não se usou 768 píxeis, a largura de um tablet? A resposta: a 768, os títulos já cabiam há muito, e entre 640 e 768 a página ficava numa coluna sem precisar. O ponto de mudança vem do conteúdo, e não de uma lista de aparelhos.

## Fase 7: Um texto comprido não pode sair da caixa

Pões na página um endereço comprido, vês os dois problemas que ele cria e corriges os dois com uma linha. Rever: [Um texto comprido não pode sair da caixa](../04-responsividade-e-grid.md#um-texto-comprido-não-pode-sair-da-caixa).

1. Numa das duas secções lado a lado, acrescenta uma frase com um endereço comprido, inventado, acabado em `.example.com`. No exemplo, no parágrafo de "Quando nos encontramos":

   ```html
   <p>Às quartas-feiras à tarde, na sala 12. Sabe mais em www.clubedexadrezdaescola.example.com.</p>
   ```

   O domínio `example.com` existe só para exemplos, como o email do tema 01 do Git.

2. Guarda e recarrega, a 320. O que deves ver: o endereço passa da margem direita, e a página volta a mexer para o lado. No separador Elements, passa o rato pela `section` do endereço: no exemplo, tem cerca de 315 píxeis e passa da margem direita.

3. Põe a largura em 640. O que deves ver, no exemplo: as duas secções lado a lado, mas com larguras diferentes. Passa o rato pelas duas `section`, no separador Elements: a da esquerda tem 315 píxeis, e a da direita 277. A coluna do endereço alargou até ele caber, e apertou a outra.

4. Em `estilos.css`, na regra do `body`, acrescenta no fim:

   ```css
     /* Uma palavra que não cabe na linha parte-se, em vez de sair pelo lado. */
     overflow-wrap: anywhere;
   ```

   Guarda e recarrega. O que deves ver: a 320, o endereço parte-se e a página não mexe para o lado; no exemplo, parte-se depois de `example.`. A 640, as duas secções voltam a ter a mesma largura, no exemplo 296 píxeis cada.

5. No `registo.md`, escreve o terceiro defeito, com as mesmas quatro linhas. O defeito é o endereço que saía da página, a 320 píxeis.

6. Guarda o passo num commit:

   ```bash
   git add index.html estilos.css
   git diff --staged
   git commit -m "Parte as palavras compridas que não cabem na linha"
   ```

   O que deves ver: o commit responde `2 files changed`.

### Paragem 7

Nenhuma palavra sai da caixa, e as colunas ficam iguais com qualquer texto. O registo tem os três defeitos.

Pensa antes de continuares: porque é que o `overflow-wrap` se escreveu no `body`, e não só no parágrafo do endereço? A resposta: herda-se, e por isso vale para todo o texto do site. Uma palavra comprida que apareça mais tarde, noutro sítio, já não sai da página.

## Fase 8: A página testa-se em várias larguras, com o zoom e com o teclado

Fazes a verificação completa nas duas páginas e envias o trabalho para o GitHub. Rever: [A página testa-se em várias larguras, com o zoom e com o teclado](../04-responsividade-e-grid.md#a-página-testa-se-em-várias-larguras-com-o-zoom-e-com-o-teclado).

1. Na barra de dispositivos, abre cada página a 320, a 768 e a 1280. Depois arrasta devagar a margem direita da página, a partir de 320, até onde der. O que deves ver: em nenhuma largura a página mexe para o lado. Se aparecer, encontra a caixa culpada como na fase 1 e corrige-a.

2. Fecha as ferramentas do programador, com F12, e maximiza a janela do browser. Carrega em Ctrl e na tecla + cinco vezes, ou Cmd e + no Mac, até o browser mostrar 200%. O que deves ver: a página com letra grande, e sem mexer para o lado. A página ficou com metade dos píxeis. Conforme a largura do teu ecrã, as duas secções podem ficar lado a lado ou uma por baixo da outra. Volta ao zoom normal com Ctrl e 0, ou Cmd e 0 no Mac.

3. Abre as ferramentas e liga outra vez a barra de dispositivos, com a largura em 320. Carrega num sítio sem texto da página e, a seguir, várias vezes na tecla Tab. Repete a 1280. O que deves ver: o foco passa pelas ligações pela ordem do HTML, e a moldura do foco vê-se sempre.

4. Envia o trabalho para o GitHub, com a rotina do tema 02 do Git:

   ```bash
   git status
   git log --oneline -4
   git push
   ```

   O que deves ver: o `git status` diz `Your branch is ahead of 'origin/main' by 4 commits.`. O `git log` mostra os quatro commits deste laboratório. O `git push` pede a frase-passe e acaba em `main -> main`.

### Paragem 8

O teu site funciona de 320 a 1280 píxeis, com o zoom e com o teclado. Está no GitHub, com os quatro commits deste laboratório.

Pensa antes de continuares: porque é que o zoom a 200% pode mudar a arrumação da página? A resposta: com o zoom, cada píxel do CSS ocupa dois do ecrã, e a página fica com metade da largura. As media queries respondem a essa largura, como se o ecrã fosse mais estreito.

## Se alguma coisa falhar

Primeiro, três verificações rápidas:

1. Guardaste o ficheiro? Um ficheiro por guardar tem uma bolinha no separador do VS Code.
2. Recarregaste a página? Depois de guardar, carrega em F5. Se continuar igual, carrega em Ctrl+F5, que obriga o browser a ler o CSS outra vez.
3. A regra aparece no separador Styles? Carrega no elemento, no separador Elements, e procura a regra. Se estiver riscada, outra regra está a ganhar-lhe.

### A barra de dispositivos não aparece

O atalho só funciona com o foco nas ferramentas do programador. Carrega primeiro dentro delas e repete o Ctrl+Shift+M. Se se abrir o menu dos perfis do browser, carrega em Esc. Também podes carregar no ícone do telemóvel e do tablet, Toggle device toolbar, no canto de cima das ferramentas. Se a lista Dimensions mostrar o nome de um telemóvel, escolhe Responsive.

### A imagem continua a sair da página

A regra `img` não está a ser aplicada. Confirma no separador Styles, com o `img` escolhido, que a regra lá está. Confirma também que o `max-width` está bem escrito, com o hífen, e que a imagem não tem um `style` no HTML.

### As colunas não aparecem

O `display: grid` e o `grid-template-columns` estão na regra errada, como `.cartoes li`. Passa-os para a regra do contentor, `.cartoes`, ou `.duas-colunas`.

### A media query não faz nada

Confirma três coisas. A media query está no fim de `estilos.css`, depois das regras com o mesmo seletor. Escreveste `@media (min-width: 30rem)`, ou a tua largura, com os parênteses e sem espaço entre o número e o `rem`. E fechaste as duas chavetas: a da regra de dentro e a da media query.

### O git pull ou o git push pedem a frase-passe e falham

A frase-passe é a da tua chave SSH, do tema 02 do Git. Vê o "Se alguma coisa falhar" do [laboratório desse tema](../../02-git/laboratorios/02-partilhar-versoes-com-o-github-laboratorio.md#se-alguma-coisa-falhar).

## Desafios

1. Na segunda página do teu site, põe o texto e a imagem lado a lado nos ecrãs largos, com uma media query. Escolhe o ponto de mudança pelo conteúdo e escreve no comentário dela porquê. Pista: o texto e a imagem precisam de uma caixa nova, só com os dois, como as duas secções da fase 5.
2. Encontra a largura em que o menu do teu cabeçalho passa para baixo do nome do site. No `registo.md`, escreve essa largura e se o cabeçalho precisa de uma media query. Pista: o cabeçalho usa o `flex-wrap` do tema 03.

## Antes de terminares

- [ ] Nenhuma página do teu site mexe para o lado, de 320 a 1280 píxeis.
- [ ] As imagens têm a regra com `max-width: 100%` e `height: auto`.
- [ ] Os cartões estão numa grelha com `repeat(auto-fill, minmax(15rem, 1fr))`, e o último tem a largura dos outros.
- [ ] Duas partes da página inicial ficam lado a lado nos ecrãs largos, com uma media query.
- [ ] O comentário da media query diz porque escolheste o ponto de mudança.
- [ ] O `registo.md` tem os três defeitos, cada um com o que viste, a largura, a causa e a correção.
- [ ] O site está no GitHub, com os quatro commits deste laboratório.

![Rodapé](../../imagens/rodape.png)
