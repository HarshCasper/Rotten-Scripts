# importing required libraries
import pyttsx3
import PyPDF2

# initializing the speaker
speaker = pyttsx3.init()

# opening the document in read mode. You can mention your document name here
book = open("sample_pdf.pdf", 'rb')

# creating an object of PyPDF2 and calling the PdfFileReader method
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

# telling the number of pages in the document
print("Number of pages in the document are: "+str(pages))
speaker.say("Number of pages in the document are ")
speaker.runAndWait()
speaker.say(pages)
speaker.runAndWait()

# asking which page has to be read
speaker.say("Which page do you want me to read?")
speaker.runAndWait()
print("Which page do you want me to read?")
start_page_number = int(input())  # input the start page number

# asking the end page number
speaker.say("Till what page number should I read?")
speaker.runAndWait()
print("Till what page number should I read?")
# input the end page number till which document has to be read
last_page_number = int(input())

for i in range(start_page_number-1, last_page_number):
    page = pdfReader.getPage(i)  # get page number
    text = page.extractText()  # extracting text from that page
    speaker.say(text)  # speaker starts reading the text in pdf
    speaker.runAndWait()
speaker.say('Hurray, done with reading !!')
speaker.runAndWait()
print('Hurray, done with reading !!')
