![Cabeçalho](../../../imagens/cabecalho.png)

# Conflito em Git: material de apoio

Material de apoio a um laboratório futuro, do bloco Colaboração, pull requests e conflitos.

No Git, cada pessoa pode trabalhar no seu ramo (em inglês, branch), uma linha de trabalho separada das outras. Mais tarde, junta-se o trabalho dos dois ramos (em inglês, faz-se um merge). Se as duas pessoas mudaram a mesma linha do mesmo ficheiro, cada uma à sua maneira, o Git não sabe qual das versões deve ficar. A isto chama-se um conflito. Quem o resolve é uma pessoa, que lê as duas versões e decide o que o ficheiro deve dizer. O laboratório deste bloco provoca um conflito de propósito, num repositório de treino, para aprenderes a lê-lo e a resolvê-lo com calma.

Esta pasta tem um único ficheiro, o [script run.py](run.py), escrito em Python. Faz sozinho o percurso todo, numa pasta temporária, e mostra no ecrã cada comando do Git que executa e o que o Git responde:

1. cria um repositório com um ficheiro `titulo.txt`, que tem uma só linha;
2. cria dois ramos, `equipa-a` e `equipa-b`, e em cada um muda essa linha de uma maneira diferente;
3. tenta juntar os dois ramos e confirma que aparece o conflito;
4. escolhe uma versão final, guarda-a e confirma que o conflito ficou resolvido.

No fim, apaga a pasta temporária. Não mexe nos teus repositórios nem na tua configuração do Git, e não precisa de internet nem de conta no GitHub.

Na aula, o script serve para o professor mostrar o percurso antes de o fazeres tu, à mão, num repositório de treino teu. Se tiveres Python instalado e quiseres vê-lo a funcionar, executa este comando na pasta principal deste repositório:

```sh
python3 laboratorios/git/conflito-controlado/run.py
```

O laboratório completo, com os comandos explicados um a um e o que fazer em cada passo, é publicado com o bloco, depois do guia sobre ramos e merge, que explica o que é um ramo e o que acontece quando se juntam dois.

![Rodapé](../../../imagens/rodape.png)
