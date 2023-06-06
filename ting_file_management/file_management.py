import sys


def txt_importer(path_file):
    try:
        file = open(path_file, "r")
        file_extension = path_file.split(".")[-1]

        if file_extension != "txt":
            sys.stderr.write("Formato inválido ")

        content = file.read()
        content_list = content.split("\n")
        file.close()

        return content_list
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
