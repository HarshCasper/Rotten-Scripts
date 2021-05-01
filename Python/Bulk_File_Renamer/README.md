# BULK FILE RENAMER

This utility is used to Filter, Rename and/or Move multiple files at once using Python.

## USAGE

        python3 main.py

### FILTERS AVAILABLE

1. File Size -- Upper limit of the filesize (in Kb) to be considered for match 
2. File Name -- Name / Part of Name to be matched with the filename
3. Extension -- Extension of the files to be considered for matching

### SETTINGS FOR ORGANIZING FILES

1. Rename -- This setting will rename the filtered files in-place, with the name as passed in the argument.
2. Rename and Move -- This setting will create a New folder and copy the filtered files there after renaming them.
3. Delete -- This setting will delete the filtered files.