import os
import sys
import keyboard
import argparse


def view_menu():
    print("Application features:")
    print("1 - Create directory")
    print("2 - Create file")
    print("3 - Rename file or directory")
    print("4 - Print list files in directory")
    print("5 - Delete directory")
    print("6 - Delete file")
    print("7 - Open file")
    print("q/Q - Close program")


def create_dir(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        print("Wrong path or directory already exists")


def create_file(path):
    try:
        f = open(path, "w+")
    except FileExistsError:
        print("Wrong path or file already exists")


def rename_file_or_dir(name, new_name):
    try:
        os.rename(name, new_name)
    except:
        print(sys.exc_info())


def list_files_in_directory(path):
    try:
        print(os.listdir(path))
        print(len(os.listdir(path)))
    except:
        print("Wrong path")


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
    try:
        tx = open(path, "r")
        for data in tx:
            print(data)
    except:
        print("File does not exist")


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
        print("This statement does not exist, Try again! \n")


def createdir_parser(path):
    if path is not None:
        create_dir(path)
    else:
        print("Parameter is not specified")


def createfile_parser(path):
    if path is not None:
        create_file(path)
    else:
        print("Parameter is not specified")


def deletedir_parser(path):
    if path is not None:
        delete_dir(path)
    else:
        print("Parameter is not specified")


def deletefile_parser(path):
    if path is not None:
        delete_file(path)
    else:
        print("Parameter is not specified")


def openfile_parser(path):
    if path is not None:
        open_file(path)
    else:
        print("Parameter is not specified")


def rename_file_or_dir_parser(path, new_path):
    if path is not None and new_path is not None:
        rename_file_or_dir(path, new_path)
    else:
        print("Parameter is not specified")


def list_files_in_directory_parser(path):
    if path is not None:
        list_files_in_directory(path)
    else:
        print("Wrong path")


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--open_file', '-opf', action='store_true', help='open file')
    parser.add_argument('--output_openfile', '-oof', type=str, help='file path', default=None)

    parser.add_argument('--delete_file', '-delf', action='store_true', help='delete file')
    parser.add_argument('--output_del_file', '-odf', type=str, help='file path', default=None)

    parser.add_argument('--delete_dir', '-deld', action='store_true', help='delete directory')
    parser.add_argument('--output_del_dir', '-odd', type=str, help='directory path', default=None)

    parser.add_argument('--create_file', '-crf', action='store_true', help='create file')
    parser.add_argument('--output_file', '-ouf', type=str, help='file path', default=None)

    parser.add_argument('--create_dir', '-crd', action='store_true', help='create directory')
    parser.add_argument('--output_directory', '-oud', type=str, help='file path', default=None)

    parser.add_argument('--rename_file_or_dir', '-crfd', action='store_true', help='Rename file or directory')
    parser.add_argument('--output_name', '-oname', type=str, help='file path', default=None)
    parser.add_argument('--output_new_name', '-onewn', type=str, help='file path', default=None)

    parser.add_argument('--list_files', '-lfile', action='store_true', help='Rename file or directory')
    parser.add_argument('--output_list_files', '-olfile', type=str, help='file path', default=None)

    args = parser.parse_args()

    if args.open_file is True:
        openfile_parser(args.output_openfile)
    elif args.delete_file is True:
        deletefile_parser(args.output_del_file)
    elif args.create_file is True:
        createfile_parser(args.output_file)
    elif args.create_dir is True:
        createdir_parser(args.output_directory)
    elif args.delete_dir is True:
        deletedir_parser(args.output_del_dir)
    elif args.rename_file_or_dir is True:
        rename_file_or_dir_parser(args.output_name, args.output_new_name)
    elif args.list_files is True:
        list_files_in_directory_parser(args.output_list_files)
    else:
        while True:
            view_menu()
            print("Enter choice: ")
            choice = input()
            if choice.isdigit():
                choice = int(choice)
            else:
                if choice == 'q' or choice == "Q":
                    sys.exit(0)
                else:
                    print("Unrecognized command. Press enter and try again!")
                    keyboard.wait('enter')
            main_fun(choice)
