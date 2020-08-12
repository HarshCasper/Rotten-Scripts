# pip install 're' and 'sys' module  

import re  # defines several functions and constants to work with Regex
import sys
from re import findall

print("Regex Pattern Match\n")

def text():

    # search a string for all matches of this regular expression
    # shows a list of string ends with 'at' with 4 letters
    nameRegex = re.compile(r'.{1,2}at')

    # few paragraphs from the book 'Hamlet' for matching the pattern
    textString ='''
            And then it started like a guilty thing
            Upon a fearful summons. I have heard,
            The cock, that is the trumpet to the morn,
            Doth with his lofty and shrill-sounding throat
            Awake the god of day; and, at his warning,
            Whether in sea or fire, in earth or air,
            The extravagant and erring spirit hies
            To his confine: and of the truth herein
            This present object made probation.

            It faded on the crowing of the cock.
            Some say that ever against that season comes
            Wherein our Saviour's birth is celebrated,
            The bird of dawning singeth all night long:
            And then, they say, no spirit dares stir abroad;
            The nights are wholesome; then no planets strike,
            No fairy takes, nor witch hath power to charm,
            So hallow'd and so gracious is the time.

            So have I heard and do in part believe it.
            But, look, the morn, in russet mantle clad,
            Walks over the dew of yon high eastward hill:
            Break we our watch up; and by my advice,
            Let us impart what we have seen to-night
            Unto young Hamlet; for, upon my life,
            This spirit, dumb to us, will speak to him.
            Do you consent we shall acquaint him with it,
            As needful in our loves, fitting our duty?
    '''

    # 're.search' scans through string where regular expression pattern produces a match and return a corresponding match object
    nameRegex.search(textString)
    # stores all non-overlapping matches of pattern in string as a list of strings
    result=nameRegex.findall(textString)

    # prints the list of matched strings
    print(result)

    if result:
      print("\nPattern matched successfully.")
    else:
      print("Pattern match unsuccessful.")    
       
# call the function    
if __name__ == '__main__':
    try:
        text()
    except:
        ptint("error")	    
    

    
