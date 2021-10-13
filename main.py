import os
import sys


def view_menu():
    print("1 - Create directory")
    print("2 - Create file")
    print("3 - Rename file or directory")
    print("4 - Print list files in directory")
    print("5 - Delete directory")
    print("6 - Delete file")
    print("7 - Open file")
    print("q - Close program")


def create_dir(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        print("Directory already exists")


def create_file(path):
    f = open(path, "w+")


def rename_file_or_dir(name, new_name):
    try:
        os.rename(name, new_name)
    except:
        print(sys.exc_info())


def print_current_work_directory():
    print(os.getcwd())


def list_files_in_directory(path):
    print(os.listdir(path))
    print(len(os.listdir(path)))


def delete_dir(dir_path):
    if os.path.exists(dir_path):
        if len(os.listdir(dir_path)) == 0:
            os.rmdir(dir_path)
        else:
            print("Directory is no empty or there is no such folder")


def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print("File not found in the directory")


def open_file(path):
    tx = open(path, "r")
    for data in tx:
        print(data)


def main_fun(num):
    if num == 1:
        print("Enter path")
        path = input()
        create_dir(path)
    elif num == 2:
        print("Enter path")
        path = input()
        create_file(path)
    elif num == 3:
        print("Enter paths")
        path = input()
        print("Enter new paths")
        new_path = input()
        rename_file_or_dir(path, new_path)
    elif num == 4:
        print("Enter path")
        path = input()
        list_files_in_directory(path)
    elif num == 5:
        print("Enter path")
        path = input()
        delete_dir(path)
    elif num == 6:
        print("Enter path")
        path = input()
        delete_file(path)
    elif num == 7:
        print("Enter path")
        path = input()
        open_file(path)
    else:
        print("Something is wrong")


if __name__ == '__main__':
    view_menu()

    while True:
        print("Enter number: ")
        choice = input()
        if choice.isdigit():
            choice = int(choice)
        else:
            if choice == 'q':
                sys.exit(0)
            else:
                print("Something is wrong")
        main_fun(choice)


