from helper.files import read_file, save_list_in_file
from helper.list import remove_empty_lines, remove_duplicate_lines, remove_similarity_lines, get_not_duplicates_lines


def remove_duplicate_and_empty_lines():
    file_list1 = read_file('files/list_1.txt')
    file_list2 = read_file('files/list_2.txt')

    # remove empty lines
    file_list1 = remove_empty_lines(file_list1)
    file_list2 = remove_empty_lines(file_list2)

    file_list1 = remove_duplicate_lines(file_list1, file_list2)

    file_list1 = sorted(file_list1)

    # save the new list without empty lines in the new file, storage result
    save_list_in_file(file_list1, 'result/list_result.txt')

    return file_list1


def remove_duplicate_empty_lines_and_similarity():
    file_list1 = read_file('files/list_1.txt')
    file_list2 = read_file('files/list_2.txt')

    # remove empty lines
    file_list1 = remove_empty_lines(file_list1)
    file_list2 = remove_empty_lines(file_list2)

    file_list1 = remove_duplicate_lines(file_list1, file_list2)

    file_list1 = sorted(file_list1)

    file_list1 = remove_similarity_lines(file_list1)

    # save the new list without empty lines in the new file, storage result
    save_list_in_file(file_list1, 'result/list_result.txt')

    return file_list1


def get_unique_lines_with_similitary():
    similitary = input('Set similitary value (default is 0.90)\n\t-1 is equal\n\t-0 is completely different\n-->')

    try:
        similitary = int(similitary)
    except ValueError:
        similitary = 0.90

    if 1 >= similitary >= 0:
        print(f'Similitary: {similitary}')
        file_list1 = read_file('files/list_1.txt')
        file_list2 = read_file('files/list_2.txt')

        not_duplicated_list = get_not_duplicates_lines(file_list1, file_list2, similitary)
        save_list_in_file(not_duplicated_list, 'result/not_duplicated_list.txt')
