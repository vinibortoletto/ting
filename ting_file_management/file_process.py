from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    content_list = txt_importer(path_file)

    processed_content = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(content_list),
        "linhas_do_arquivo": content_list,
    }

    for index in range(len(instance)):
        file_name = instance.search(index)["nome_do_arquivo"]

        if file_name == path_file:
            return False

    instance.enqueue(processed_content)
    sys.stdout.write(str(processed_content))


def remove(instance):
    if len(instance) == 0:
        sys.stdout.write("Não há elementos\n")
    else:
        removed_item = instance.dequeue()
        path_file = removed_item["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
