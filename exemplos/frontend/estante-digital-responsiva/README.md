![Cabeçalho](../../../imagens/cabecalho.png)

# Estante Digital responsiva

As mesmas três páginas da [Estante Digital com CSS](../estante-digital-com-css/README.md), agora a adaptar-se à largura do ecrã. Mostra a Grid nos cartões e nos três grupos de recursos, e uma media query a partir do ecrã estreito. Mostra também as imagens e as palavras que nunca passam da largura da caixa. É usado no tema [04 Responsividade e Grid](../../../01-frontend/04-responsividade-e-grid.md).

O conteúdo é todo inventado: os recursos, o livro e o horário da biblioteca.

## O que está nesta pasta

- `estilos.css`: a folha de estilos das três páginas, com um comentário a explicar cada regra. As regras de base servem o ecrã estreito, e a media query do fim acrescenta o que muda nos ecrãs largos.
- `index.html`: a página inicial. Os três grupos de recursos estão dentro de uma caixa nova, com a classe `grupos`, e os recursos de cada grupo são cartões.
- `primeiros-passos-na-web.html`: a página de um livro, com a capa, que encolhe nos ecrãs estreitos.
- `sobre.html`: a página "Sobre".
- `imagens/`: o logótipo e a capa do livro, iguais aos da Estante Digital.

O HTML é o da Estante Digital com CSS, com uma diferença. Na página inicial, os três grupos de recursos estão dentro de um `div` com a classe `grupos`, que só serve para o CSS os arrumar.

## Como correr

Estas páginas não precisam de servidor nem de instalar nada. Abre o `index.html` no browser, com duplo clique, ou com Ctrl+O (Cmd+O no Mac). Para as ver noutras larguras, abre as ferramentas do programador, com F12. Depois liga a barra de dispositivos, com Ctrl+Shift+M (Cmd+Shift+M no Mac). Para ler o código, abre a pasta no Visual Studio Code.

O que deves ver, na página inicial:

- a 320 píxeis de largura, os três grupos uns por baixo dos outros, com um cartão por linha;
- a 768 píxeis, os grupos ainda uns por baixo dos outros, com dois cartões lado a lado em cada um;
- a partir de 784 píxeis, que são 49rem, os três grupos lado a lado, com os cartões de cada um em coluna;
- em nenhuma largura, uma barra de deslocamento horizontal.

Com a tecla Tab, o foco passa por "Início", "Sobre" e "Primeiros passos na Web", por esta ordem, em todas as larguras.

## Versões e compatibilidade

As páginas foram abertas no Chromium 156, o motor do Chrome e do Edge, a 320, 768, 784 e 1280 píxeis de largura. A folha de estilos usa a Grid, as media queries, as variáveis de CSS e o `overflow-wrap: anywhere`. Qualquer versão atual do Chrome ou do Edge os aceita.

![Rodapé](../../../imagens/rodape.png)
