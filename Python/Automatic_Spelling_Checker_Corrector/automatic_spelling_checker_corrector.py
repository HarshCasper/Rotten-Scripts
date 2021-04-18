# imports
import sys
from spellchecker import SpellChecker
from nltk import word_tokenize

# create an instance of the spellchecker
spell = SpellChecker()

# tokens --> stores the tokenized words
tokens = []

# function to read the input file
def readTextFile(textFilename):
    global tokens
    words = []
    inputFile = open(textFilename, "r")
    tokens = word_tokenize(inputFile.read())

    # Create a list of words from these tokens checking if the word is alphanumeric 
    words = [
        word 
        for word in tokens if word.isalpha()
    ]
    inputFile.close()
    return words

# function to detect errors in the file if any
def findErrors(textWords):
    misspelledWords = []
    for word in textWords:
        # correction() --> method of spellchecker module to correct the word
        if spell.correction(word) != word:
            misspelledWords.append(word)

    return misspelledWords

# function to print errors
def printErrors(errorList):
    print("Misspelled words are:")
    for word in errorList:
        # candidates() --> method of spellchecker module to find suitable corrections of the word
        print(f'{word} : {spell.candidates(word)}')

# function to correct errors
def correctErrors(errorList):
    # open a new file to write the corrected text
    outputFile = open("output.txt","w+")
    for word in tokens:
        if word in errorList:
            # if word is incorrect we replace it with the corrected word
            word = spell.correction(word)
        
        # this writes text to the new output.txt file
        outputFile.write(" ".join(tokens))

    outputFile.close()

# main function
def main():
    textFile = input("Enter text file: ")

    textList = readTextFile(textFile)
    errorList = findErrors(textList)

    # if there are no errors
    if len(errorList) == 0:
        print("No errors detected")
        return

    # call to printErrors function
    printErrors(errorList)

    # ask if user needs to correct the text 
    user_answer  = input("Do you want to auto correct the errors, Y/N ? ")

    if user_answer.lower()=='y' or user_answer.lower()=='yes':
        # call to correctErrors function
        correctErrors(errorList)
        print("Check the output.txt file for the corrected text.")
        print("Thankyou for using spelling checker program.")
    else:
        print("Thankyou for using spelling checker program.")
 
# call to the main function
main()