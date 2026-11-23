![Cabeçalho](../../../imagens/cabecalho.png)

# Estante Digital acessível

As páginas da [Estante Digital responsiva](../estante-digital-responsiva/README.md), depois da auditoria de acessibilidade. O menu passa a dizer em que página se está, com o `aria-current`. A pasta tem também uma página de comparação, com os cartões dos livros feitos com o CSS da Estante e com o Bootstrap. É usado no tema [05 Acessibilidade e frameworks de CSS](../../../01-frontend/05-acessibilidade-e-frameworks-de-css.md).

O conteúdo é todo inventado: os recursos, o livro e o horário da biblioteca.

## O que está nesta pasta

- `auditoria.md`: o relatório da auditoria de acessibilidade das três páginas, com o problema encontrado e a correção.
- `estilos.css`: a folha de estilos das páginas. Ganhou a regra da ligação da página atual e a regra que muda as variáveis dos cartões do Bootstrap.
- `index.html`: a página inicial. No menu, a ligação "Início" tem `aria-current="page"`.
- `sobre.html`: a página "Sobre". No menu, a ligação "Sobre" tem `aria-current="page"`.
- `primeiros-passos-na-web.html`: a página de um livro. Não está no menu, e por isso nenhuma ligação do menu é a da página atual.
- `comparacao-bootstrap.html`: a página de comparação. Liga-se ao Bootstrap, pelo jsDelivr, e depois ao `estilos.css`. Não está no menu, porque não faz parte do site.
- `imagens/`: o logótipo e a capa do livro, iguais aos da Estante Digital.

## Como correr

As três páginas do site não precisam de servidor nem de instalar nada. Abre o `index.html` no browser, com duplo clique, ou com Ctrl+O (Cmd+O no Mac). A página de comparação, que não está no menu, abre-se da mesma forma, no `comparacao-bootstrap.html`. Precisa de Internet, porque o CSS do Bootstrap vem do jsDelivr. Para ler o código, abre a pasta no Visual Studio Code.

O que deves ver:

- no menu, a ligação da página onde estás a negrito: "Início" na página inicial e "Sobre" na página "Sobre";
- com a tecla Tab, o foco passa por "Início", "Sobre" e "Primeiros passos na Web", por esta ordem, e vê-se sempre;
- na página de comparação, os dois livros duas vezes, em cartões quase iguais: primeiro com o CSS da Estante, depois com o Bootstrap.

Sem Internet, os cartões do Bootstrap aparecem como uma lista simples, com bolinhas e sem bordas. A caixa dos cartões feitos com o CSS da Estante não muda.

## Versões e compatibilidade

A página de comparação usa o Bootstrap 5.3.9, só o CSS, sem o JavaScript do Bootstrap. As páginas foram abertas no Chromium 156, o motor do Chrome e do Edge, a 320, 900 e 1280 píxeis de largura. Qualquer versão atual do Chrome ou do Edge as mostra.

![Rodapé](../../../imagens/rodape.png)
