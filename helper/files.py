def read_file(path):
    with open(path, "r") as file:
        lines = file.readlines()
    return lines


def save_list_in_file(file_list, file_path):
    with open(file_path, "w") as f:
        f.writelines(file_list)
        print(f'File saved in: {file_path}')
