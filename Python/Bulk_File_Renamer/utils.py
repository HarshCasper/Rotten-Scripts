from os.path import isdir, isfile
from os import listdir

def list_all_files(path):
    """Returns a List object of all the files present at the path argument"""

    if not isdir(path):
        raise NotADirectoryError("Invalid value passed to path argument")
    
    files = [file for file in listdir(path) if isfile(file)]
    return files

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
                if value != False:
                    self.FILTERS[key]['apply'] = True
                    self.FILTERS[key]['value'] = value
                    break
            
        print(self.FILTERS)
        
    def filter(self):
        pass

    def validate(self, value, key):
        """Returns the value as it is, if it is valid or raises a ValueError"""

        if key == "filesize":
            if value != "" and int(value) <= 0:
                print("Error: Filesize must be greater than or equal to 0")
                return False
        elif key == "time_of_modification":
            # TODO
            pass

        return 

def select_files(files):
    """Selects files from the passed object based on different criterion"""
    pass