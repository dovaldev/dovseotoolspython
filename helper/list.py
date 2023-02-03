from helper.similarity import compare_sentences_basic


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


def remove_similarity_lines(list1):
    final_list = []
    list2 = list1.copy()
    for line_list1 in list1:
        for line_list2 in list2:
            similarty = compare_sentences_basic(line_list1, line_list2)
            if similarty < 0.90:
                if line_list1 not in final_list:
                    final_list.append(line_list1)
                    print(f'{similarty} --> {line_list1} | {line_list2}')
    return final_list


def get_not_duplicates_lines(list1, list2, similarity):
    final_list = list1.copy()
    print(f'List1: {len(list1)}\nList2: {len(list2)}')
    for line1 in list1:
        for line2 in list2:
            sim = compare_sentences_basic(line1, line2)
            if sim >= similarity:
                print(f'Similitud: {sim} {line1} | {line2}')
                if line1 in final_list:
                    final_list.remove(line1)
                    print(f'Similarity: {sim} |\n->{line1}\n->{line2}')

    return final_list
