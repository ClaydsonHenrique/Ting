import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""

    name = path_file

    for names in instance.queue:
        if names.get("nome_do_arquivo") == name:
            print(
                f"O arquivo {name} já foi processado anteriormente.",
                file=sys.stdout,
            )
            return

    lines = txt_importer(path_file)
    if lines is None:
        print(f"Falha ao processar o arquivo {name}.", file=sys.stdout)
        return

    result = {
        "nome_do_arquivo": name,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }

    # Adiciona os dados do resultado na instância de Processamento
    instance.enqueue(result)
    print(result, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
