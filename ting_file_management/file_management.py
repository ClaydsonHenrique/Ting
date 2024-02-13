def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if path_file.split(".")[-1] != "txt":
        return None

    try:
        with open(path_file, "r") as file:
            lines = file.readline()
            return lines
    except FileNotFoundError:
        return None
