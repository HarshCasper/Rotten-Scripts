import os
import platform

if platform.system()[1].lower() == "windows":
    # For Windows Operating System.
    try:
        os.system("pip install -r Windows/requirements.txt")
    except Exception:
        print("Something went Wrong.!")
else:
    # Unix Based Systems i.e include (Linux/Mac OSX) etc
    try:
        os.system("pip3 install -r Unix/requirements.txt")
    except Exception:
        print("Something went Wrong.!")
