# this module is for text-to-speech feature


# ! this module contains other modules
# Todo: Develop a feature for text-to-speech

# importing the modules

import pyttsx3

# In this file I am using general functional
# development method


def speak(textCommand):
  # engine object for pyttsx3 module
  engineObject = pyttsx3.init()
  # executing the speech function
  engineObject.say(text=textCommand)
  engineObject.runAndWait()

  if (textCommand == None):
    print("The speech command is valid, but empty!")
    print("Give a non-empty textCommand")