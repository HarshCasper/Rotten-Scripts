from os.path import abspath, isdir, isfile, getsize, splitext, split, join
from os import listdir, rename

class SelectFiles:

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
                "description": "Extension(s) of the files to be considered (Space separated)[pdf png]: "
            }                        
        }

    def __init__(self):
        """Takes in arguments from the user for filtering files"""
        
        print("Enter the values for filters you want to apply (Press enter to skip)")

        for key in self.FILTERS:
            while True:
                value = self.validate(input(self.FILTERS[key]['description']), key)
                if value == "":
                    break
                elif value != False:
                    self.FILTERS[key]['apply'] = True
                    self.FILTERS[key]['value'] = value
                    break
            
    @staticmethod
    def list_all_files(path):
        """Returns a Dict object of all the files present at the path argument"""
        
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
        """Looks for all the files located at 'path' argument, and applies the filters to them"""

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

    def validate(self, value, key):
        """Returns the value as it is, if it is valid or raises a ValueError"""

        if key == "filesize":
            if value != "":
                if int(value) <= 0:
                    print("Error: Filesize must be greater than or equal to 0")
                    return False
                else:
                    return int(value)

        elif key == "extension":
            if value != "":
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

    def __init__(self, files):
        """Organizes files object in a particular order"""

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


    def organize(self):
        print(f"\nFiles available to organize: {len(self.files)}")
        arguments = {}
        choice = input("Choose the method to re-organize:\n1. Rename in-place\n2. Rename and move to new folder\n3. Delete Files\n: ")
        if choice == "1":
            arguments["method"] = "rename"
            arguments["value"] = OrganizeFiles.set_arguments("filename")

        elif choice == "2":
            arguments["method"] = "rename-copy"
            arguments["value"] = OrganizeFiles.set_arguments("filename", "folder-name")
        
        else:
            arguments["method"] = "delete"
        
        OrganizeFiles.organize_files(self.files, arguments)