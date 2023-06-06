from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    content_list = txt_importer(path_file)

    processed_content = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(content_list),
        "linhas_do_arquivo": content_list,
    }

    instance.enqueue(processed_content)
    sys.stdout.write(str(processed_content))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
