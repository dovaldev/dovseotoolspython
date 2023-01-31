from helper.files import read_file, save_list_in_file
from helper.list import remove_empty_lines, remove_duplicate_lines


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

