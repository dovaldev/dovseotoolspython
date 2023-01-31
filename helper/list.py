# remove empty lines and print the diference between 2 list
def remove_empty_lines(list):
    without_empty = [linea for linea in list if linea.strip()]
    diference_lines = len(list) - len(without_empty)
    print(f'Removed {diference_lines}')
    return without_empty


# remove duplicates in list and save new list2 without duplicates
def remove_duplicate_lines(list1, list2=None):
    if list2 is None:
        list2 = []

    for item in list1:
        if item not in list2:
            list2.append(item)

    return list2

