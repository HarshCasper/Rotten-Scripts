# importing the modules
import json
from difflib import get_close_matches

# loading the json data file
data = json.load(open("Python/dictionary_script/data.json"))


# defining a function to get the meaning of the word
def get_meaning(word_input):
    # changing all the letters of the word to lower case
    word_input = word_input.lower()
    if word_input in data:
        return data[word_input]
    elif word_input.title() in data:
        return data[word_input.title()]
    elif word_input.upper() in data:
        return data[word_input.upper()]
    # getting close matches for a word if it is not present in the dictionary
    elif len(get_close_matches(word_input, data.keys())) > 0:
        print("Did You mean %s instead " % get_close_matches(word_input, data.keys())[0])
        x = input("Press Y for Yes and N for No ")
        if x == "y" or x == "Y":
            return data[get_close_matches(word_input, data.keys())[0]]
        elif x == "N" or x == "n":
            return "There no such word exists in the dictionary"
        else:
            return "Enter only y or n"


# getting a word as a input from the user
word_input = input("Enter the word you want to search ")
output = get_meaning(word_input)

numbering = 1
if output is None:
    print("No such word found in the dictionary")
# if the word is found in the dictionary, showing the meaning of the word
else:
    if type(output) == list:
        print("The meaning of the word", word_input, "is ")
        for item in output:
            print(numbering, ". ", item)
            numbering = numbering + 1
    else:
        print(output)
