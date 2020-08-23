
#Imports and dependencies
#gtts, stands for the Google-Text-To-Speech module that is used to convert text to speech
from gtts import gTTS 
import os

#These packages are used for OCR(Optical character recognition)
import pytesseract
from PIL import Image

#This module is a wrapper around python, basic information about a topic can be obtained
import wikipedia

#This script can be used to convert text to speech, either from a text file or when a user enters text
#Text can be read from images using the Optical recognition framework built for Python

print("Option 1, enter text and convert it to speech \n")
print("Option 2, convert the contents of a text file to speech \n")
print("Option 3, convert the text in an image to speech \n")
print("Option 4, convert information about a topic from wikipedia into speech \n")


#Conversion will be done to the English language
language = "en"

def convert_text_to_speech(option):

    text = ""
    if option == 1:
        text = input("Enter the text, that has to be converted to speech ")

    elif option == 2:
        file_name = input("Enter the name of the text file, that has to be converted to speech ")
        with open(file_name , "r") as handle:
            text = handle.read().replace("\n" , "")

    elif option == 3:
        image_path = input("Enter the path of the image that has to be read and converted to speech ")
        text = pytesseract.image_to_string(Image.open(image_path).replace("\n" , ""))

    elif option == 4:
        wikipedia = input("Enter the topic about which information is to be obtained ")
        text = wikipedia.summary(wikipedia)

    speech = gTTS(text = text, lang = language, slow = True)
    speech.save("text_content.mp3")


if __name__ == "__main__":
    option = int(input("Enter the option "))
    convert_text_to_speech(option)
