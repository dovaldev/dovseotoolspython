from tools.duplicates import remove_duplicate_and_empty_lines, remove_duplicate_empty_lines_and_similarity, \
    get_unique_lines_with_similitary


def app():
    start = input('=========\nLimpiar contenido en archivos txt AI\t'
                  + '\n¿Que quieres hacer?\n'
                  + '\t1 - Quitar líneas en blanco y duplicadas (se guardará en: list_result-option-1.txt)\n'
                  + '\t2 - Quitar líneas en blanco y duplicadas y eliminar similitudes (se guardará en: '
                    'list_result-option-2.txt)\n'
                  + '\t3 - Obtener los elementos que no se repiten (se guardará en: list_result-option-3.txt)\n'
                  + '\t-> ')
    if int(start) == 1:
        remove_duplicate_and_empty_lines()
        app()

    elif int(start) == 2:
        remove_duplicate_empty_lines_and_similarity()
        app()
    elif int(start) == 3:
        get_unique_lines_with_similitary()
        app()
    else:
        app()


# def
app()
