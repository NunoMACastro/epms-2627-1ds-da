![Cabeçalho](../../../imagens/cabecalho.png)

# Estante Digital com CSS

As mesmas três páginas da [Estante Digital](../estante-digital/README.md), agora com uma folha de estilos. Mostra uma folha de estilos externa ligada a várias páginas, as variáveis de CSS e o modelo de caixa. Mostra também o Flexbox no cabeçalho, no menu e numa lista de cartões. É usado no tema [03 CSS e Flexbox](../../../01-frontend/03-css-e-flexbox.md).

O conteúdo é todo inventado: os recursos, o livro e o horário da biblioteca.

## O que está nesta pasta

- `estilos.css`: a folha de estilos das três páginas, com um comentário a explicar cada regra.
- `index.html`: a página inicial. As três listas de recursos têm a classe `cartoes`, e cada recurso aparece num cartão.
- `primeiros-passos-na-web.html`: a página de um livro, com a dica numa caixa com uma barra à esquerda.
- `sobre.html`: a página "Sobre".
- `imagens/`: o logótipo e a capa do livro, iguais aos da Estante Digital.

O HTML é o da Estante Digital, com duas diferenças. Cada página tem o `link` para o `estilos.css`, e as listas de recursos da página inicial têm a classe `cartoes`.

## Como correr

Estas páginas não precisam de servidor nem de instalar nada. Abre o `index.html` no browser, com duplo clique, ou com Ctrl+O (Cmd+O no Mac). Para ler o código, abre a pasta no Visual Studio Code.

O que deves ver: no topo, uma faixa azul, com o logótipo e o nome do site à esquerda. Do lado direito, a branco, estão as ligações Início e Sobre. O fundo da página é cor de papel, e os títulos são azuis. Cada recurso está num cartão branco com cantos redondos, dois cartões lado a lado em cada secção. Se estreitares a janela, os cartões passam a ficar uns por baixo dos outros. Com a tecla Tab, cada ligação ganha uma moldura bem visível.

## Versões e compatibilidade

As páginas foram abertas no Chromium 156, o motor do Chrome e do Edge, numa janela larga e numa de 360 píxeis de largura. A folha de estilos usa o Flexbox, as variáveis de CSS e o `text-decoration-thickness`, que qualquer versão atual do Chrome ou do Edge aceita.

![Rodapé](../../../imagens/rodape.png)
