# pip install 're' and 'sys' module

import re    # defines several functions and constants to work with Regex
import sys
from re import findall

print("Regex Pattern Match\n")

def text():

    # open the file with the correct location in the system
    # it will read that particular file to match the regex pattern
    
    with open('./test.txt', 'r') as f:
        test_string = f.read()

        # enter regex pattern to search
        pattern=input("Enter pattern:")
        # search all the matches and returns them as a list of strings
        regex= re.findall(pattern,test_string)

        # prints the list of matched strings
        print(regex)

    # checks whether the regex pattern matched or not
    if regex:
        print("\nPattern matched successfully.\n")
    else:
        print("Pattern match unsuccessful.")  


# call the function    
if __name__ == '__main__':
    try:
        text()
    except:
        print("\nError")	    
    
