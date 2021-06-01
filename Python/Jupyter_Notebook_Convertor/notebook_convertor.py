"""
This Program helps user to convert jupyter notebook to HTML,MarkDown,PDF,python file
"""

import os
import pyfiglet

print(pyfiglet.figlet_format("Jupyter NoteBook Converter"))

while True:

    print(
        """\n-------The Jupyter Notebook Converter-------\n
            1. Convert To pdf
            2. Convert To markdown
            3. Convert To python script
            4. Convert To HTML
            5. Exit \n
            """
    )
    print("Enter Your Choice")
    opt = input()
    if opt == "1":
        print("Enter Your Notebook Name (with .ipynb)")
        file = input()
        os.system("jupyter nbconvert {} --to pdfviahtml".format(file))
    elif opt == "2":
        print("Enter Your Notebook Name (with .ipynb)")
        file = input()
        os.system("jupyter nbconvert {} --to markdown".format(file))
    elif opt == "3":
        print("Enter Your Notebook Name (with .ipynb)")
        file = input()
        os.system("jupyter nbconvert {} --to python".format(file))
    elif opt == "4":
        print("Enter Your Notebook Name (with .ipynb)")
        file = input()
        os.system("jupyter nbconvert {} --to html".format(file))
    elif opt == "5":
        break
    else:
        print("Choose From Valid options")
