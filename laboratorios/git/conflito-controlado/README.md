![Cabeçalho](../../../imagens/cabecalho.png)

# Conflito em Git: material de apoio

Material de apoio ao laboratório do tema 04 de Git, sobre a colaboração e os conflitos.

No Git, cada pessoa pode trabalhar no seu ramo (em inglês, branch), uma linha de trabalho separada das outras. Mais tarde, junta-se o trabalho dos dois ramos (em inglês, faz-se um merge). Se as duas pessoas mudaram a mesma linha do mesmo ficheiro, cada uma à sua maneira, o Git não sabe que versão deve ficar. A isto chama-se um conflito. Quem o resolve é uma pessoa, que lê as duas versões e decide o que o ficheiro deve dizer.

O laboratório provoca um conflito de propósito, num repositório de treino, para aprenderes a lê-lo e a resolvê-lo com calma.

## A demonstração

Esta pasta tem um único ficheiro, o programa [run.py](run.py), escrito em Python. É uma demonstração completa, que o professor corre na aula. Depois, fazes o mesmo percurso à mão, num repositório de treino teu.

O programa faz sozinho o percurso todo, numa pasta temporária. Mostra no ecrã cada comando do Git que corre e o que o Git responde:

1. cria um repositório com um ficheiro `titulo.txt`, que tem uma só linha;
2. cria dois ramos, `equipa-a` e `equipa-b`, e em cada um muda essa linha de uma maneira diferente;
3. tenta juntar os dois ramos e confirma que aparece o conflito;
4. escolhe uma versão final, guarda-a e confirma que o conflito ficou resolvido.

No fim, apaga a pasta temporária. Não mexe nos teus repositórios nem na tua configuração do Git, e não precisa de internet nem de conta no GitHub.

## Se quiseres vê-lo a funcionar

Precisas do Python e do Git instalados. Corre este comando na pasta principal deste repositório:

```sh
python3 laboratorios/git/conflito-controlado/run.py
```

No Windows, o comando pode ser `python` ou `py`, em vez de `python3`.

O que deves ver: os comandos do Git, um a um, cada um com a resposta. A meio, o ficheiro com os três marcadores do conflito, `<<<<<<<`, `=======` e `>>>>>>>`, entre as duas versões da linha. No fim, o histórico, com os dois ramos desenhados a juntarem-se num só, e a frase que começa por "Tudo certo".

O tema 03 explica os ramos e o que acontece quando se juntam dois. É a base para compreenderes os conflitos deste exemplo.

![Rodapé](../../../imagens/rodape.png)
