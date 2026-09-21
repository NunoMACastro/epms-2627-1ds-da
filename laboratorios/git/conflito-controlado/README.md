![Cabeçalho](../../../imagens/cabecalho.png)

# Duas branches, a mesma linha, um conflito

UC00617 · branches, merge e conflitos. Pré-requisitos: repositório, staging, commits e branches. Git deve estar disponível; não é necessária conta GitHub. O exemplo usa identidade fictícia, não configura a tua identidade global e não contacta serviços externos.

Um merge combina alterações desde um antepassado comum. Quando duas branches alteram a mesma linha de formas diferentes, o Git pode não decidir sozinho o resultado. Os marcadores mostram ambas as versões; a resolução exige escolher o conteúdo correto e criar um commit. Apagar apenas os marcadores não garante uma resolução correta.

Executar, a partir da raiz:

```sh
python3 laboratorios/git/conflito-controlado/run.py
```

O script cria um repositório temporário com `main`, cria `equipa-a` e `equipa-b` a partir da mesma base, altera a mesma linha e tenta juntar A em B. Verifica o conflito, mostra os marcadores, escolhe uma versão combinada e confirma um commit com dois pais e working tree limpa. A pasta temporária é removida no fim. Usar `--keep` para a preservar e inspecionar.

Prática do aluno, numa pasta de laboratório nova: seguir os comandos apresentados até ao merge; parar no conflito; ler `git status`, o ficheiro e `git diff`; escrever uma justificação para a versão final; só depois executar `git add titulo.txt` e `git commit`. O professor pode executar primeiro o script como demonstração e o aluno reproduz o percurso manualmente.

```text
*   resolução (equipa-b)
|\
| * alteração A (equipa-a)
* | alteração B
|/
* base (main)
```

O nome final é `Título: catálogo de recursos da turma`. Verificar `git log --graph --oneline --all`, `git status --porcelain` vazio e `git ls-files -u` vazio. A ordem visual dos ramos pode variar; o merge deve ter dois pais.

Recuperação durante o conflito: `git merge --abort` regressa ao estado anterior à tentativa de merge, neste repositório de exercício inicialmente limpo. Se um aluno alterou outros ficheiros, guardar primeiro esse trabalho e pedir apoio. Se não houver conflito, confirmar que ambas as branches partiram do commit inicial e modificaram a mesma linha.

Evidência: ficheiro com os marcadores antes da resolução, justificação da escolha, conteúdo final, histórico e estado limpo. Exercício seguinte: criar alterações em linhas diferentes e explicar por que motivo o merge automático pode funcionar. Avaliação formativa: explicar os dois pais, distinguir commit de merge de simples cópia e demonstrar recuperação.

![Rodapé](../../../imagens/rodape.png)
