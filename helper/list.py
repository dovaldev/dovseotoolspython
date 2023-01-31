def remove_empty_lines(file):
    without_empty = [linea for linea in file if linea.strip()]
    return without_empty


