import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if not path_file.split(".")[-1] == "txt":
        print(
            "Formato inválido",
            file=sys.stderr,
        )
        return None

    try:
        with open(path_file, "r") as arquivo:
            lines = [line.rstrip("\n") for line in arquivo.readlines()]
            return lines
    except FileNotFoundError:
        print(
            f"Arquivo {path_file} não encontrado",
            file=sys.stderr,
        )
        return None
