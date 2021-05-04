# BULK FILE RENAMER

This utility is used to Filter, Rename and/or Move multiple files at once using Python.

## USAGE

        python3 main.py

### FILTERS AVAILABLE

1. File Size -- Upper limit of the filesize (in Kb) to be considered for match 
2. File Name -- Name / Part of Name to be matched with the filename
3. Extension -- Extension of the files to be considered for matching

### SETTINGS FOR ORGANIZING FILES

1. Rename -- This setting will rename the filtered files in-place, with the name as passed in the argument. It takes 1 argument-
   1. filename : String to be used to rename the filtered files using the format "filename_count.extension"
2. Rename and Copy -- This setting will create a New folder and copy the filtered files there after renaming them. It takes 2 arguments-
   1. filename - String to be used to rename the filtered files using the format "filename_count.extension"
   2. folder-name - Name to be used to create a folder, in the directory where all the files were located.
3. Delete -- This setting will delete the filtered files.

### EXAMPLE

1. Starting with 300 files named from 1-100 with extensions **txt**, **pdf** and **png**.
![All Files](https://i.imgur.com/IV8yVAc.png)
2. Example for Renaming and/or Copying files.
![Rename and Copy](https://i.imgur.com/7XZZGFY.png) 
![Rename](https://i.imgur.com/TSKYQPR.png)
![Example of Rename and Copy](https://i.imgur.com/1D8GwI0.png?2)
3. Delete Files
![Delete Files](https://i.imgur.com/lYrX9u0.png)
![Example of Delete Files](https://i.imgur.com/4MBIx4O.png?1)