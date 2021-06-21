from time import sleep

import pyttsx3  # pip install pyttsx3
import PyPDF2  # pip install PyPDF2

print(
    "Enter the pdf you want me to read for you. Remember to put it in same folder, or either give me location of it."
)
story = input("If you dont have one, Enter mybook.pdf to run it.   :  ")

# story = open('mybook.pdf', 'rb') #Name of your script make sure it's in pdf format
pdfReader = PyPDF2.PdfFileReader(story)
pages = pdfReader.numPages
# pages = pdfReader.getPage(number)  Replace nu,ber with any specific page number you want this to read
engine = pyttsx3.init()
voices = engine.getProperty("voices")
# For male voice change the value to 1.
engine.setProperty("voice", voices[0].id)

for num in range(0, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    engine.say(text)
    engine.runAndWait()
