# Simple Python Script To arrange your files in one click

import os
import glob
# glob function of glob module to detect all files inside current directory
files_list = glob.glob("*")
# Creating a set of extension types inside the folder to avoid duplicate entries
extension_set = set()
# adding each type of extension to the set
for file in files_list:
    extension = file.split(sep=".")
    try:
        extension_set.add(extension[1])
    except IndexError:
        continue

# print(extension_set)

# Function to create directory for each type of extension


def createDirs():
    for dir in extension_set:
        try:
            os.makedirs(dir+"_files")
        except FileExistsError:
            continue

# Function to move files to respective folders


def arrange():
    for file in files_list:
        fextension = file.split(sep=".")
        try:
            os.rename(file, fextension[1]+"_files/"+file)
        except (OSError, IndexError):
            continue


# Calling the functions in order
createDirs()
arrange()
