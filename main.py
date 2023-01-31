from tools.duplicates import remove_duplicate_and_empty_lines

def app():
    start = input('Limpiar contenido en archivos txtAI\t'
                  + '\n¿Que quieres hacer?\n'
                  + '\t1 - Quitar líneas en blanco y duplicadas\n'
                  + '\t-> ')
    if int(start) == 1:
        remove_duplicate_and_empty_lines()
        app()

    elif int(start) == 2:
        pass
    else:
        app()


# def
app()
