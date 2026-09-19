#!/usr/bin/env python3
"""Demonstrate and verify a same-line Git conflict in a disposable directory.

Run from any working directory. No files or Git configuration in the teaching
workspace are modified. ``--keep`` preserves only the newly created lab folder.
"""

import argparse
import os
from pathlib import Path
import shutil
import subprocess
import tempfile


def execute_lab(folder):
    """Create two divergent branches, prove conflict, resolve and verify history."""
    # GIT_DIR e outras opções herdadas não podem redirecionar o exercício.
    environment = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    environment.update({
        "GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull,
        "GIT_AUTHOR_NAME": "Aluno Exemplo", "GIT_AUTHOR_EMAIL": "aluno@example.invalid",
        "GIT_COMMITTER_NAME": "Aluno Exemplo", "GIT_COMMITTER_EMAIL": "aluno@example.invalid",
        "GIT_EDITOR": "true", "GIT_MERGE_AUTOEDIT": "no",
    })

    def git(*arguments, expected=0):
        """Execute a Git command locally and fail if its result differs from intent."""
        print(f"$ git {' '.join(arguments)}", flush=True)
        result = subprocess.run(["git", *arguments], cwd=folder, env=environment,
                                capture_output=True, text=True, check=False)
        if result.stdout.strip():
            print(result.stdout.strip())
        if result.returncode != expected:
            raise RuntimeError(f"Git devolveu {result.returncode}, esperado {expected}: {result.stderr}")
        return result.stdout

    # O merge tem uma base comum; ambos os ramos alteram a mesma linha da base.
    git("init", "-b", "main")
    page = folder / "titulo.txt"
    page.write_text("Título: página inicial\n", encoding="utf-8")
    git("add", "titulo.txt")
    git("commit", "-m", "Criar título inicial")
    git("switch", "-c", "equipa-a")
    page.write_text("Título: catálogo de recursos\n", encoding="utf-8")
    git("commit", "-am", "Definir título da equipa A")
    git("switch", "main")
    git("switch", "-c", "equipa-b")
    page.write_text("Título: recursos da turma\n", encoding="utf-8")
    git("commit", "-am", "Definir título da equipa B")
    git("merge", "equipa-a", expected=1)
    conflict = page.read_text(encoding="utf-8")
    if not all(marker in conflict for marker in ("<<<<<<<", "=======", ">>>>>>>")):
        raise RuntimeError("O merge não produziu os três marcadores esperados")
    print("Conflito confirmado:\n" + conflict)
    if not git("ls-files", "-u").strip():
        raise RuntimeError("O índice deveria conter entradas por resolver")
    # A resolução é uma decisão de conteúdo, não apagar marcadores às cegas.
    page.write_text("Título: catálogo de recursos da turma\n", encoding="utf-8")
    git("add", "titulo.txt")
    git("commit", "-m", "Conciliar títulos das duas equipas")
    if git("status", "--porcelain").strip() or git("ls-files", "-u").strip():
        raise RuntimeError("A resolução deveria deixar índice e working tree limpos")
    if len(git("rev-list", "--parents", "-n", "1", "HEAD").split()) != 3:
        raise RuntimeError("Esperado commit de merge com dois pais")
    if page.read_text(encoding="utf-8") != "Título: catálogo de recursos da turma\n":
        raise RuntimeError("Conteúdo final incorreto")
    git("log", "--graph", "--oneline", "--all")
    print("OK: conflito, resolução, dois pais e working tree limpa verificados.")


def main():
    """Create isolated workspace and clean only the directory this process owns."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--keep", action="store_true", help="preservar a pasta temporária para inspeção")
    args = parser.parse_args()
    if not shutil.which("git"):
        parser.error("Git não está instalado ou não está no PATH")
    folder = Path(tempfile.mkdtemp(prefix="da-git-conflict-"))
    print(f"Repositório temporário: {folder}")
    try:
        execute_lab(folder)
    finally:
        if args.keep:
            print(f"Pasta preservada: {folder}")
        else:
            shutil.rmtree(folder)


if __name__ == "__main__":
    main()
