def exists_word(word, instance):
    """Aqui irá sua implementação"""
    result = []
    for index in range(len(instance)):
        data = instance.search(index)
        name = data["nome_do_arquivo"]
        lines = data["linhas_do_arquivo"]
        find_lines = []

        for line_number, line in enumerate(lines, start=1):
            if word.lower() in line.lower():
                find_lines.append({"linha": line_number})

        if find_lines:
            result.append(
                {
                    "palavra": word,
                    "arquivo": name,
                    "ocorrencias": find_lines,
                }
            )

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
