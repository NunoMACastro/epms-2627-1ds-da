# Formulário local, eventos e DOM

UC02833 · exemplo executável sobre formulários, DOM e eventos.

Competências trabalhadas: formulários, validação no cliente, DOM, eventos, arrays e objetos. Pré-requisitos: HTML semântico, CSS, seleção DOM, funções, arrays e objetos. Se algum destes temas ainda não tiver sido abordado, pede orientação antes de explorares o código completo.

O HTML define o formulário inicial; o browser constrói o DOM. O JavaScript mantém um array de tarefas e atualiza a interface quando recebe eventos. O CSS controla apresentação e adaptação à largura. A entrada de texto é inserida com `textContent`, para não executar HTML fornecido pelo utilizador. A validação no cliente ajuda a utilização; não substitui validação num futuro servidor.

Abrir [index.html](index.html) num browser moderno. Não exige Node, npm, conta, rede ou servidor. Alternativa para praticar uma origem HTTP local: executar `python3 -m http.server 8000 --directory laboratorios/frontend/formulario_local` na raiz deste repositório e abrir `http://localhost:8000`. Parar com Ctrl+C.

1. Ler o HTML e identificar labels, constraints, secções e a mensagem de estado.
2. Inspecionar o DOM em Elements antes de submeter o formulário.
3. Adicionar uma tarefa e comparar o ficheiro HTML com o DOM atual.
4. Colocar um breakpoint em `addTask`; observar `event`, `title` e `tasks`.
5. Explicar a sequência evento → handler → dados → renderização.
6. Limpar tarefas, recarregar a página e explicar por que motivo não persistem.

Casos verificáveis: título vazio usa a validação nativa; título com espaços mostra a mensagem do exercício; texto `<strong>teste</strong>` aparece literalmente; duas submissões criam dois itens; limpar desativa o botão; recarregar apaga o estado. Testar a 320 px e 1280 px, a 200% de zoom, com Tab/Shift+Tab/Enter e apenas teclado. Verificar foco visível, nomes, ordem de leitura e mensagens com tecnologia de apoio quando disponível. Estas observações são uma lista de trabalho; o exemplo não tem certificação WCAG.

Exercício progressivo: primeiro alterar texto e áreas; depois explicar cada handler; finalmente acrescentar um contador por área, se arrays/condições estiverem disponíveis. Não introduzir persistência nem backend neste lab.

Debug: se nada acontecer, abrir Console e confirmar o caminho de `app.js`; se a lista não atualizar, confirmar o breakpoint em `renderTasks`; se a página navegar, observar `preventDefault`. Recuperação: consultar `git diff` e repor apenas a alteração do exercício depois de guardar trabalho útil. Artefacto: pequena alteração explicada, checklist de testes e commit lógico. Avaliação formativa: o aluno explica a diferença entre array, HTML e DOM, demonstra um caso inválido e justifica uma correção.
