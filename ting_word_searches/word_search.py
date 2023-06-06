def exists_word(word, instance):
    word_occurrence_list = []

    for index in range(len(instance)):
        content = instance.search(index)
        line_list = content["linhas_do_arquivo"]

        for sub_index in range(len(line_list)):
            line = line_list[sub_index].lower()

            if word in line:
                word_occurrence_list.append({"linha": sub_index + 1})

    if len(word_occurrence_list) == 0:
        return []

    return [
        {
            "palavra": word,
            "arquivo": content["nome_do_arquivo"],
            "ocorrencias": word_occurrence_list,
        }
    ]


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
