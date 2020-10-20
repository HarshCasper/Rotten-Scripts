"""
Manages your desktop by automatically placing different files to their
respective directories in config.ini [hs-desktop]
"""

"""
TODO:
Users should be able to define their own extensions and the locations to which
those extension file types should be moved to.
Example config:
extensions1 = [".txt", ".doc", ".ppt"]
location1 = C:\\Users\\Shivay\\Documents
Syntax:
hs-manage -d <directory> :: Directory to organize files of
hs-manage -c or <none>   :: Manage files in current directory
"""

# Python imports
import argparse
import os
import sys

# Local imports
from src import help
from src.errors import *
from src.initialize import Initialize
from src.configreader import ConfigReader

initializer = Initialize()
white_space = initializer.white_space
config_file = initializer.config_file
config_reader = ConfigReader(config_file)
# Gets the path to Desktop
desktop = os.path.join(os.environ['USERPROFILE'], "Desktop")

# Paths/Directories for different file types
paths = config_reader.read_config("hs-desktop")



def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--help',
                        '-help',
                        action='store_true')

    args = parser.parse_args()

    if args.help:
        cmd = sys.argv[0].partition(".")[0]
        help.display_help(cmd)
        return

    execute()



'''
def execute():
    if "" not in paths.values():
        files = os.listdir(desktop)
        for file in files:
            # Creates a full path to the file in desktop
            file_page = os.path.join(desktop, file)
            if not os.path.isdir(file):
                # Splits file path and file extension
                file_name, file_extn = os.path.splitext(file_page)
                # Further we check if the extension of the file is mentioned in
                # any of the extension lists above and then we put the file in
                # the directory (from dict 'paths') matching the file type
                # Check for images
                if file_extn.lower() in image_extns:
                    new_location = os.path.join(paths["images"], file)
                # Check for videos
                elif file_extn.lower() in video_extns:
                    new_location = os.path.join(paths["videos"], file)
                # Check for text files
                elif file_extn.lower() in text_file_extns:
                    new_location = os.path.join(paths["textFiles"], file)
                # If the file type is unknown to the program then we skip it
                else:
                    new_location = None
                # If the file type is not unknown then ...
                if new_location:
                    try:
                        # This moves the file to "new_location"
                        os.rename(file_page, new_location)
                        print("{0} Moved {1}".format(
                            white_space,
                            os.path.basename(file_page)))
                    # If a file with the same name already exists then we rename
                    # the file we're operating on
                    except WindowsError:
                        file_name, file_extn = os.path.splitext(new_location)
                        count = 1
                        # Randomly append an integer to the end of the file name
                        while os.path.exists(new_location):
                            new_location = (
                                file_name +
                                " (" +
                                str(count) +
                                ")" +
                                file_extn
                            )
                            count += 1
                        # Moves the file to "new_location"
                        os.rename(file_page, new_location)
                        print("{0} Renamed {1} to {2} since {1} already exists in destination folder".format(
                            white_space,
                            os.path.basename(file),
                            os.path.basename(new_location)))
    else:
        raise ConfigError("All paths are not specified in the configuration file")
'''


if __name__ == "__main__":
    main()
