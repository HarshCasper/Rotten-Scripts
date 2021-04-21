from os.path import abspath, isdir, isfile, getsize
from os import listdir

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
            },
        "time_of_modification": 
            {
                "apply" : False,
                "description": "Upper limit on modification time of file [DD:MM:YYYY HH:MM:SS]: "
            },                                    
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
        """Returns a List object of all the files present at the path argument"""

        if not isdir(path):
            raise NotADirectoryError("Invalid value passed to path argument")
        
        path = abspath(path)

        return ["{}/{}".format(path, file) for file in listdir(path) if isfile(f"{path}/{file}")]


    @staticmethod
    def apply_filter(files, filter_argument, filter_value):
        """Takes in a filter_argument and a filter_value, based on which it filters\
            out the list of files"""

        if filter_argument == "filesize":
            # Convert filesize from Kb to Bytes
            size = filter_value*1024
            
            return [file for file in files if getsize(file) <= size]


    def filter(self, path=None):
        """Looks for all the files located at 'path' argument, and applies the filters to them"""
        if path is None:
            raise ValueError("Invalid value passed to path argument")
        
        files = SelectFiles.list_all_files(path)

        print(f"\nNo of files at '{abspath(path)}': {len(files)}")

        if len(files) == 0:
            return []
        
        for key in self.FILTERS:
            if self.FILTERS[key]["apply"]:
                files = SelectFiles.apply_filter(files, key, self.FILTERS[key]["value"])
        
        print("Filtered files: ")
        print(*files, sep="\n")

    
    def validate(self, value, key):
        """Returns the value as it is, if it is valid or raises a ValueError"""

        if key == "filesize":
            if value != "" and int(value) <= 0:
                print("Error: Filesize must be greater than or equal to 0")
                return False
            else:
                return int(value)

        elif key == "extension":
            if value != "":
                return value.split(" ")

        elif key == "time_of_modification":
            if value != "" and value:
                return False
            # TODO

        return value

def select_files(files):
    """Selects files from the passed object based on different criterion"""
    pass