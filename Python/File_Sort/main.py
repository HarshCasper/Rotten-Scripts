import os
import shutil

DIR_NAME = 'sorted'
source_path = input("Please input the directory name to be sorted: ")

if source_path == '.':
    source_path = os.getcwd()

path = os.path.join(source_path, DIR_NAME)
print(source_path, path)

if not os.path.exists(path):
    os.mkdir(path)

os.chdir(path)
files = []


def get_files():
    """getting all the files that have been put to the sorting folder by user and
    extending them to our files list to sort them in the future"""

    files.extend(list(os.walk(source_path))[0][2])  # extending the list of all the files in a source path


def sort_files(clear_files=True) -> int:
    get_files()

    n_of_sorted_files = 0  # keeps track of the sorted files
    to_remove = []  # transferred files can be removed(from files list) only after the for loop ends bc we're
    # iterating through this list -> the list can't be changed during the iteration

    for file in files:

        extension = file.split('.')[-1]  # get the extension of the current file
        current_file_path = os.path.join(source_path, file)  # putting the file into out sorting folder
        new_folder = os.path.join(path, extension)  # declares a new folder variable with the extension name

        # Creating this folder if it hasn't already been created
        if not os.path.exists(new_folder):
            os.mkdir(new_folder)

        shutil.copy(current_file_path, new_folder)  # putting a file to the folder with its extension

        if clear_files:
            os.remove(current_file_path)  # removing the file from the sorting folder

        to_remove.append(file)  # appending sorted files to remove them later

    # removing files that are already sorted from our files list
    for i in to_remove:
        files.remove(i)

    n_of_sorted_files += len(to_remove)  # increasing the counter of sorted files

    return n_of_sorted_files


def main():
    counter = 0  # counts an amount of transferred files

    counter += sort_files()
    print(f'Number of sorted files: {counter}')


if __name__ == '__main__':
    main()
