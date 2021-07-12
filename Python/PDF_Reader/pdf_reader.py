# importing required libraries
import pyttsx3
import PyPDF2

def main():
    # initializing the speaker
    speaker = pyttsx3.init()

    # enter the file path with the pdf name
    path = input("Enter the file path of the PDF along with PDF name: ")

    # opening the document in read mode. You can mention your document name
    book = open(path, 'rb')

    # creating an object of PyPDF2 and calling the PdfFileReader method
    PDFReader = PyPDF2.PdfFileReader(book)
    pages = PDFReader.numPages

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
    # input the start page number
    start_page_number = int(input())

    # asking the end page number
    speaker.say("Till what page number should I read?")
    speaker.runAndWait()
    print("Till what page number should I read?")
    # input the end page number till which document has to be read
    last_page_number = int(input())

    for i in range(start_page_number-1, last_page_number):
        # get page number
        page = PDFReader.getPage(i)
        # extracting text from that page
        text = page.extractText()
        # speaker starts reading the text in pdf
        speaker.say(text)
        speaker.runAndWait()
    speaker.say('Hurray, done with reading !!')
    speaker.runAndWait()
    print('Hurray, done with reading !!')

if __name__ == '__main__':
    main()
    
    
    
    
