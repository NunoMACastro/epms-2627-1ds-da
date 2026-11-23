![Cabeçalho](../../imagens/cabecalho.png)

# Ficha de exercícios: Partilhar versões com o GitHub

Praticas o envio e a receção de commits, as respostas do Git quando há um remoto e o cuidado com o que fica público. Os exercícios 1 a 6 são obrigatórios. Guarda o trabalho numa pasta só desta ficha, fora da pasta do site. As respostas escritas vão para um ficheiro `respostas.md` nessa pasta, com o número do exercício e a letra da alínea. O exercício 5 faz-se no repositório do teu site, no GitHub e no portátil. No fim, entregas essa pasta como o professor indicar. Para rever: o [guia do tema](../02-partilhar-versoes-com-o-github.md) e o [laboratório](../laboratorios/02-partilhar-versoes-com-o-github-laboratorio.md).

## O cenário

A Rádio do Pátio é a rádio inventada de uma escola. O site tem duas páginas: a inicial, `index.html`, e a da grelha dos programas, `programas.html`. A Marta trabalha no site no portátil da escola e no computador de casa. O repositório está no GitHub, na conta `marta-radio`, com o nome `radio-do-patio`.

## Exercício 1: Que comando usar

Para cada situação, escreve o comando, ou os comandos, que a Marta usa, e justifica numa frase.

**a)** A Marta tem um computador novo em casa e quer lá o site, com o histórico inteiro.

**b)** Acabou de fazer dois commits na escola, e a aula está a acabar.

**c)** Chega a casa e quer saber se há commits novos no GitHub, sem mexer ainda nos ficheiros.

**d)** Viu o que veio na alínea c), e quer os ficheiros de casa iguais aos do GitHub.

Rever: [Parte 1: O repositório remoto](../02-partilhar-versoes-com-o-github.md#parte-1-o-repositório-remoto) e [Parte 2: Enviar e receber commits](../02-partilhar-versoes-com-o-github.md#parte-2-enviar-e-receber-commits).

## Exercício 2: Ler o git status com um remoto

Estas são três respostas do `git status`, em três momentos diferentes:

A:

```text
On branch main
Your branch is ahead of 'origin/main' by 2 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```

B:

```text
On branch main
Your branch is behind 'origin/main' by 2 commits, and can be fast-forwarded.
  (use "git pull" to update your local branch)

nothing to commit, working tree clean
```

C:

```text
On branch main
Your branch and 'origin/main' have diverged,
and have 1 and 2 different commits each, respectively.
  (use "git pull" if you want to integrate the remote branch with yours)

nothing to commit, working tree clean
```

**a)** Para cada resposta, diz o que ela quer dizer sobre o repositório local e o remoto. Diz também que comando, ou comandos, se corre a seguir.

**b)** Num quarto momento, a Marta abre o site em casa e o `git status` diz `Your branch is up to date with 'origin/main'.`. Isso garante que ela tem tudo o que está no GitHub? Explica porquê.

Rever: [O git push envia os commits](../02-partilhar-versoes-com-o-github.md#o-git-push-envia-os-commits) e [O git fetch traz os commits sem mexer nos teus ficheiros](../02-partilhar-versoes-com-o-github.md#o-git-fetch-traz-os-commits-sem-mexer-nos-teus-ficheiros).

## Exercício 3: Um envio recusado

Na sexta-feira, na escola, a Marta fez dois commits na página dos programas e enviou-os para o GitHub. No sábado, em casa, abriu o site e mudou logo o título da página inicial. Fez o commit e correu o `git push`, que respondeu:

```text
To github.com:marta-radio/radio-do-patio.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'github.com:marta-radio/radio-do-patio.git'
hint: Updates were rejected because the remote contains work that you do not
hint: have locally. This is usually caused by another repository pushing to
hint: the same ref. If you want to integrate the remote changes, use
hint: 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

**a)** Porque é que o envio foi recusado?

**b)** Escreve, por ordem, os comandos que resolvem a situação, sem perder nenhum commit.

**c)** Que passo da rotina faltou, e em que computador?

Rever: [Antes de começar, pull; no fim, push](../02-partilhar-versoes-com-o-github.md#antes-de-começar-pull-no-fim-push).

## Exercício 4: Corrigir o último commit

Para cada situação, diz se a Marta pode usar o `git commit --amend`. Se puder, escreve os comandos; se não puder, diz o que faz.

**a)** Acabou de fazer um commit com a mensagem "Acrescenta o programa de sexta", e o programa é de sábado. O `git status` responde `Your branch is ahead of 'origin/main' by 1 commit.`.

**b)** Acabou de fazer o commit da grelha nova, mas esqueceu-se de juntar a imagem `imagens/locutor.svg`, que faz parte da mesma alteração. O `git status` diz `ahead of 'origin/main' by 1 commit` e mostra a imagem em `Untracked files`.

**c)** Ontem enviou um commit com a mensagem "Corrige o horario da manha", sem acentos. O `git status` diz `Your branch is up to date with 'origin/main'.`.

Rever: [O git commit --amend substitui o último commit](../02-partilhar-versoes-com-o-github.md#o-git-commit---amend-substitui-o-último-commit).

## Exercício 5: Uma alteração feita no GitHub

Este exercício faz-se no teu site. No GitHub, numa janela privada, muda o `README.md` do repositório do teu site no editor do GitHub, com uma mensagem de commit tua. Na secção "Limitações e continuidade", troca o "Ainda por fazer." logo por baixo do título. Escreve lá o que o teu site ainda não faz.

Depois, no portátil, na pasta do teu site, põe o repositório local igual ao do GitHub. Antes de mexeres nos ficheiros, vê o que vem.

No `respostas.md`:

**a)** escreve os comandos que usaste, por ordem;

**b)** diz o que o `git status` respondeu antes de o portátil falar com o GitHub, e o que respondeu quando já sabia do commit. Explica porque mudou;

**c)** cola a resposta do `git log --oneline -3`.

Rever: [O git fetch traz os commits sem mexer nos teus ficheiros](../02-partilhar-versoes-com-o-github.md#o-git-fetch-traz-os-commits-sem-mexer-nos-teus-ficheiros) e [Exemplo guiado: a Estante Digital em dois computadores](../02-partilhar-versoes-com-o-github.md#exemplo-guiado-a-estante-digital-em-dois-computadores).

## Exercício 6: O que pode ficar público

Para cada coisa, diz se pode ficar pública, à vista de qualquer pessoa, e porquê, numa frase.

**a)** O ficheiro `gh-marta-radio.pub`.

**b)** O ficheiro `gh-marta-radio`, sem `.pub`.

**c)** A frase-passe da chave e a palavra-passe da conta do GitHub.

**d)** O email `87654321+marta-radio@users.noreply.github.com`.

**e)** Uma fotografia da turma, tirada na aula, no README do site.

Rever: [A chave SSH prova que és tu](../02-partilhar-versoes-com-o-github.md#a-chave-ssh-prova-que-és-tu), [A conta e o email privado](../02-partilhar-versoes-com-o-github.md#a-conta-e-o-email-privado) e [O inventário de conteúdos](../../01-frontend/01-web-e-planeamento.md#o-inventário-de-conteúdos).

## Desafios

1. Nas pastas de treino do laboratório, reproduz a situação C do exercício 2. Faz um commit novo na `treino-escola` e dois na `treino-casa`, em ficheiros diferentes, e envia só os de casa. Põe as três pastas com o mesmo histórico. Cola no `respostas.md` a resposta do `git log --oneline --graph -6` da escola.
2. Um colega da Marta guardou a frase-passe num ficheiro `notas.txt`, dentro da pasta do site, e fez o commit e o envio para o GitHub. Explica no `respostas.md` o que ele tem de fazer, e porque é que apagar o ficheiro num commit novo não chega.

## Critérios de conclusão

- O `respostas.md` tem as respostas aos exercícios 1 a 6, com o número do exercício e a letra da alínea.
- O README do teu site, no GitHub e no portátil, tem a frase do exercício 5, e o `git status` do site diz `up to date`.
- Nenhuma resposta tem a tua frase-passe, a tua palavra-passe nem a tua chave privada.
- Fechaste a janela privada do browser depois do exercício 5.

![Rodapé](../../imagens/rodape.png)
