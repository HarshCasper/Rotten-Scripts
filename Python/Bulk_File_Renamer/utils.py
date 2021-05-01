from os.path import abspath, isdir, isfile, getsize, splitext, split, join
from os import listdir, rename, mkdir, remove
from shutil import copy2
from sys import exit

class SelectFiles:
    """Class containing method to select and filter files at a path.\
        It contains different filters based on which, the files can be filtered"""

    FILTERS = {
        "filesize":
            {
                "apply" : False,
                "description": "Upper limit of the filesize (Kb): "
            },
        "filename": 
            {
                "apply" : False,
                "description": "Name/Part of Name to match with filename: "
            },
        "extension":
            {
                "apply" : False,
                "description": "Extension(s) of the files to be considered"
                               " (Space separated)[pdf png]: "
            }
        }

    def __init__(self):
        """Takes in arguments from the user for filtering files"""
        print("Enter the values for filters you want to apply (Press enter to skip)")

        for key in self.FILTERS:
            while True:
                value = SelectFiles.validate(input(self.FILTERS[key]['description']), key)
                if value == "":
                    break
                elif not isinstance(value, bool):
                    self.FILTERS[key]['apply'] = True
                    self.FILTERS[key]['value'] = value
                    break

    @staticmethod
    def list_all_files(path):
        """Returns a Dict object of all the files present at the path argument."""
        path = abspath(path)

        if not isdir(path):
            raise NotADirectoryError("Invalid value passed to path argument")

        files = {}
        count = 1
        for file in listdir(path):
            abs_path = "{}/{}".format(path, file)
            if isfile(abs_path):
                files[count] = {
                    "name": file,
                    "path": abs_path,
                }
            count += 1

        return files

    @staticmethod
    def apply_filter(files, filter_argument, filter_value):
        """Takes in a filter_argument and a filter_value, based on which it filters\
            out the list of files"""
        if filter_argument == "filesize":
            # Convert filesize from Kb to Bytes
            size = filter_value*1024

            # Removes the instances of files which does not match the criteria
            for key in files.copy():
                if getsize(files[key]["path"]) > size:
                    files.pop(key)

        elif filter_argument == "filename":

            for key in files.copy():
                if filter_value not in files[key]["name"]:
                    files.pop(key)

        elif filter_argument == "extension":

            for key in files.copy():
                ext = splitext(files[key]["name"])[1]
                if ext not in filter_value:
                    files.pop(key)

        return files

    def filter(self):
        """Looks for all the files located at 'path' argument, \
            and applies the filters to them"""
        path = input("Enter the path (Press enter to select current path): ")
        if path == "":
            path = "./"

        files = SelectFiles.list_all_files(path)

        print(f"\nNo of files at '{abspath(path)}': {len(files)}")

        if len(files) == 0:
            return []

        # Apply all filters
        for key in self.FILTERS:
            if self.FILTERS[key]["apply"]:
                files = SelectFiles.apply_filter(files, key, self.FILTERS[key]["value"])

        print(f"No. of files filtered: {len(files)}")

        return files

    @staticmethod
    def validate(value, key):
        """Returns the value as it is, if it is valid or raises a ValueError."""
        if key == "filesize":
            if value != "":
                if int(value) <= 0:
                    print("Error: Filesize must be greater than or equal to 0")
                    return False

                return int(value)

        elif key == "extension" and value != "":
            extensions = []
            for ext in value.split():
                if ext[0] != ".":
                    extensions.append("." + ext)
                else:
                    extensions.append(ext)

            return extensions

        # For cases when user enters nothing
        return value


class OrganizeFiles:
    """Class which contains methods to rename/relocate or delete files."""


    def __init__(self, files):
        """Organizes files object in a particular order."""
        if files is None or len(files) == 0:
            print("0 files to organize. Exiting")
            exit(0)
        self.files = files

    @staticmethod
    def set_arguments(*names):
        """Takes input from the user for all arguments in "names"\
             and returns it in a dictionary"""
        args = {}
        for name in names:
            value = ""
            while value == "":
                value = input(f"Enter the value for '{name}' argument: ")
                if value == "":
                    print("Error: No value received")
            args[name] = value

        return args

    @staticmethod
    def organize_files(files, arguments):
        """Organizes files based on the arguments passed. Different values of arguments\
            can be: rename, rename and copy to new folder, delete files"""
        if arguments["method"] == "rename":
            count = 1
            new_name = arguments["value"]["filename"]
            for file in files.keys():
                extension = splitext(files[file]["name"])[1]
                name = f"{new_name}_{count}{extension}"
                prefix = split(files[file]["path"])[0]
                count += 1

                rename(files[file]["path"], join(prefix, name))

            print(f"Renamed {len(files)} files successfully!!")

        elif arguments["method"] == "rename-copy":
            count = 1
            new_name = arguments["value"]["filename"]

            # Create directory
            for file in files.keys():
                folder_name = join(split(files[file]["path"])[0],\
                                arguments["value"]["folder-name"])
                break
            if not isdir(folder_name):
                mkdir(folder_name)
                print(f"Created folder '{folder_name}' successfully!!")

            for file in files.keys():
                split_name = splitext(files[file]["name"]) 
                name = f"{split_name[0]}_{new_name}{split_name[1]}"
                prefix_file = split(files[file]["path"])[0]
                count += 1

                copy2(files[file]["path"], join(folder_name, name))

            print(f"\nCopied {len(files)} files successfully!!")

        elif arguments["method"] == "delete":
            confirm = "n"
            confirm = input(f"Deleting {len(files)}, press Y to confirm: ")
            if confirm.lower() != "y":
                print("Exiting")
                exit(0)
            else:
                for file in files.keys():
                    remove(files[file]["path"])

                print(f"Deleted {len(files)} files successfully!")

    def organize(self):
        """Driver function to call organize_files method and set relevant arguments."""
        print(f"\n\nFiles available to organize: {len(self.files)}")

        arguments = {}
        choice = input("Choose the method to re-organize:\n1. Rename in-place"
                        "\n2. Rename and move to new folder\n3. Delete Files\n: ")
        if choice == "1":
            arguments["method"] = "rename"
            arguments["value"] = OrganizeFiles.set_arguments("filename")

        elif choice == "2":
            arguments["method"] = "rename-copy"
            arguments["value"] = OrganizeFiles.set_arguments("filename", "folder-name")

        else:
            arguments["method"] = "delete"

        OrganizeFiles.organize_files(self.files, arguments)
