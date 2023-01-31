def read_file(path):
    with open(path, "r") as file:
        lines = file.readlines()
    return lines


def save_list_in_file(list, file_path):
    with open(file_path, "w") as f:
        f.writelines(list)
        print(f'File saved in: {file_path}')
