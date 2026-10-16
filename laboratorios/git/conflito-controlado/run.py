#!/usr/bin/env python3
"""run.py: demonstra um conflito de Git na mesma linha, numa pasta temporária.

É uma demonstração completa, que o professor corre na aula antes de os alunos
fazerem o mesmo à mão. Cria um repositório de treino, provoca o conflito,
resolve-o e confirma o resultado, e mostra cada comando do Git e a resposta.

Pode correr a partir de qualquer pasta. Não mexe em ficheiros nem na configuração
do Git fora da pasta temporária que cria. Com a opção --manter, essa pasta fica
no disco no fim, para se ver o repositório; sem ela, é apagada.
"""

import argparse
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import tempfile


def executar_laboratorio(pasta):
    """Cria dois ramos que mudam a mesma linha, provoca o conflito, resolve-o e verifica o histórico.

    Não devolve nada: escreve no ecrã cada comando do Git e a resposta dele.
    Se um passo não der o resultado esperado, para com um RuntimeError que
    diz o que falhou.

    pasta: a pasta vazia (um Path) onde se cria o repositório de treino.
    """
    # Copia as variáveis de ambiente, menos as do Git. Uma variável como GIT_DIR,
    # herdada do terminal, podia pôr os comandos a mexer noutro repositório.
    ambiente = {nome: valor for nome, valor in os.environ.items() if not nome.startswith("GIT_")}
    # Uma identidade fictícia e nenhuma configuração do computador: a demonstração
    # não lê nem muda o nome, o email ou as opções de quem a corre.
    ambiente.update({
        "GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull,
        "GIT_AUTHOR_NAME": "Aluno Exemplo", "GIT_AUTHOR_EMAIL": "aluno@example.invalid",
        "GIT_COMMITTER_NAME": "Aluno Exemplo", "GIT_COMMITTER_EMAIL": "aluno@example.invalid",
        # Sem editor: o Git não abre nenhuma janela à espera de uma mensagem.
        "GIT_EDITOR": "true", "GIT_MERGE_AUTOEDIT": "no",
    })

    def git(*argumentos, esperado=0):
        """Corre um comando do Git na pasta do laboratório e mostra no ecrã o comando e a resposta.

        Devolve o texto que o Git escreveu na saída normal. Para com um
        RuntimeError se o código de saída não for o esperado.

        argumentos: as palavras do comando, sem o "git", como "commit", "-m", "Mensagem".
        esperado: o código de saída que se espera. O 0 quer dizer que correu bem;
            uma junção com conflito dá 1.
        """
        # O shlex.join põe aspas onde são precisas, e o comando mostrado pode
        # escrever-se tal e qual num terminal.
        print(f"$ {shlex.join(['git', *argumentos])}", flush=True)
        resultado = subprocess.run(["git", *argumentos], cwd=pasta, env=ambiente,
                                   capture_output=True, text=True, check=False)
        if resultado.stdout.strip():
            print(resultado.stdout.strip())
        if resultado.returncode != esperado:
            raise RuntimeError(f"O Git devolveu {resultado.returncode}, e esperava-se {esperado}: {resultado.stderr}")
        return resultado.stdout

    # O ponto de partida: um commit no ramo main, com um ficheiro de uma só linha.
    # É a base comum dos dois ramos, e é por ela que a junção sabe o que cada um mudou.
    git("init", "-b", "main")
    ficheiro = pasta / "titulo.txt"
    ficheiro.write_text("Título: página inicial\n", encoding="utf-8")
    git("add", "titulo.txt")
    git("commit", "-m", "Criar título inicial")

    # Os dois ramos partem do mesmo commit e mudam a mesma linha de maneiras diferentes.
    git("switch", "-c", "equipa-a")
    ficheiro.write_text("Título: catálogo de recursos\n", encoding="utf-8")
    git("commit", "-am", "Definir título da equipa A")
    git("switch", "main")
    git("switch", "-c", "equipa-b")
    ficheiro.write_text("Título: recursos da turma\n", encoding="utf-8")
    git("commit", "-am", "Definir título da equipa B")

    # Juntar o ramo da equipa A no da equipa B dá conflito, e o Git devolve 1.
    git("merge", "equipa-a", esperado=1)
    conteudo = ficheiro.read_text(encoding="utf-8")
    if not all(marcador in conteudo for marcador in ("<<<<<<<", "=======", ">>>>>>>")):
        raise RuntimeError("A junção não deixou no ficheiro os três marcadores do conflito")
    print("Conflito confirmado:\n" + conteudo)
    # O git ls-files -u lista os ficheiros com um conflito por resolver.
    if not git("ls-files", "-u").strip():
        raise RuntimeError("O titulo.txt devia estar na lista dos ficheiros por resolver")

    # Resolver é decidir o que o ficheiro deve dizer, e não só apagar os marcadores.
    # Aqui, a versão final junta as ideias das duas equipas.
    ficheiro.write_text("Título: catálogo de recursos da turma\n", encoding="utf-8")
    git("add", "titulo.txt")
    git("commit", "-m", "Conciliar títulos das duas equipas")

    # As verificações do fim: nada por resolver nem por guardar, um commit de
    # junção com dois pais e, no ficheiro, a versão escolhida.
    if git("status", "--porcelain").strip() or git("ls-files", "-u").strip():
        raise RuntimeError("Depois da resolução, a pasta de trabalho devia ficar limpa e sem conflitos")
    # O rev-list --parents mostra o código do commit e os dos pais:
    # três códigos querem dizer dois pais.
    if len(git("rev-list", "--parents", "-n", "1", "HEAD").split()) != 3:
        raise RuntimeError("O último commit devia ser uma junção, com dois pais")
    if ficheiro.read_text(encoding="utf-8") != "Título: catálogo de recursos da turma\n":
        raise RuntimeError("O titulo.txt não tem a versão final escolhida")
    git("log", "--graph", "--oneline", "--all")
    print("Tudo certo: o conflito apareceu e foi resolvido, a junção tem dois pais e a pasta de trabalho está limpa.")


def main():
    """Cria a pasta temporária, corre a demonstração nela e, no fim, apaga só essa pasta.

    Não devolve nada. Com a opção --manter, a pasta fica no disco, e o caminho
    dela aparece no ecrã. Se o Git não estiver instalado, para logo, com uma
    mensagem.
    """
    analisador = argparse.ArgumentParser(description=__doc__)
    analisador.add_argument("--manter", action="store_true",
                            help="não apagar a pasta temporária no fim, para se ver o repositório")
    opcoes = analisador.parse_args()
    if not shutil.which("git"):
        analisador.error("o Git não está instalado, ou o terminal não o encontra")
    pasta = Path(tempfile.mkdtemp(prefix="da-conflito-git-"))
    print(f"Repositório temporário: {pasta}")
    try:
        executar_laboratorio(pasta)
    finally:
        # O finally corre mesmo quando um passo falha, e a pasta não fica esquecida no disco.
        if opcoes.manter:
            print(f"Pasta mantida: {pasta}")
        else:
            shutil.rmtree(pasta)


if __name__ == "__main__":
    main()
