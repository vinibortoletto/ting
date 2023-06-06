import sys


def txt_importer(path_file):
    try:
        file_extension = path_file.split(".")[-1]

        if file_extension != "txt":
            sys.stderr.write("Formato inválido ")

        with open(path_file) as file:
            content = file.read()
            return content.split("\n")

    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
