![Cabeçalho](../../../imagens/cabecalho.png)

# Auditoria de acessibilidade da Estante Digital

Este é o relatório da auditoria feita à mão às três páginas da [Estante Digital responsiva](../estante-digital-responsiva/README.md): `index.html`, `sobre.html` e `primeiros-passos-na-web.html`. Cada verificação fez-se nas três páginas, com o Chrome e as ferramentas do programador.

## As verificações

| Verificação | Resultado |
| --- | --- |
| Teclado | Passou. Com Tab e Shift+Tab, o foco chega a todas as ligações, pela ordem do HTML, e Enter segue cada uma |
| Foco | Passou. A moldura vê-se em todas as ligações, branca no cabeçalho e azul no resto |
| Nomes | Passou. O logótipo tem `alt=""`, porque o nome do site está ao lado, e a capa tem um `alt` que a descreve. Cada ligação diz para onde leva |
| Títulos | Passou. Cada página tem um `h1` e as secções têm `h2`, sem saltos |
| Contraste | Passou. O mais baixo são os títulos azuis no fundo claro, com 7,63 |
| Cor | Passou. As ligações do texto estão sublinhadas |
| Idioma e localização | Falhou uma parte. As páginas têm `lang="pt-PT"` e um `title` diferente cada uma, mas o menu não diz em que página se está |
| Zoom | Passou. A 200%, os grupos ficam uns por baixo dos outros, e nada se perde |

## O problema encontrado

- O que falha e onde: no menu das páginas "Início" e "Sobre", a ligação da página onde se está é igual às outras.
- Quem fica sem conseguir o quê: quem usa um leitor de ecrã ouve "Início, ligação" e não sabe se já está nessa página. Quem vê a página também não tem nenhum sinal no menu.
- A causa: o HTML não tem nenhum elemento para dizer "esta é a página atual".
- A correção e como se confirmou: a ligação da página atual ganhou `aria-current="page"`, e uma regra de CSS põe-na a negrito. No separador Accessibility, a secção ARIA Attributes da ligação mostra `aria-current: page`, e no menu a ligação da página aparece a negrito.

![Rodapé](../../../imagens/rodape.png)
