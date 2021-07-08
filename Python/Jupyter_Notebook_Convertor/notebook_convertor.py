

import shlex
import subprocess
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
    print("Enter Your Notebook Name (with .ipynb)")
    file = shlex.quote(input())
    print("Enter Your Choice")
    opt = input()
    if opt == "1":
        subprocess.getoutput(
            "jupyter nbconvert {} --to pdfviahtml".format(file))
    elif opt == "2":
        k = subprocess.getoutput(
            "jupyter nbconvert {} --to markdown".format(file))
        print(subprocess.getstatusoutput(k))
    elif opt == "3":
        subprocess.getoutput("jupyter nbconvert {} --to python".format(file))
    elif opt == "4":
        subprocess.getoutput("jupyter nbconvert {} --to html".format(file))
    elif opt == "5":
        break
    else:
        print("Choose From Valid options")
