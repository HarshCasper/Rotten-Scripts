from PIL import Image
import pytesseract
import nltk.data
import re
from newspaper import Article
from googlesearch import search


def google_search(query):    # function to google querys
    search_urls = []
    for i in search(query, tld='com',num= 1, start= 1, stop= 1):
        search_urls.append(i)
    
    return search_urls

def scrape(url):            # function to web scrape
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    text = article.text

    return text

img = Image.open("test-imgs/test-1.png")    # provide path of your image that you want to give as input.

text = pytesseract.image_to_string(img, lang="eng")   # image converted to string


tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

#print('\n-----\n'.join(tokenizer.tokenize(text)))
tokenized_text = '\n \n'.join(tokenizer.tokenize(text))   # text seperated into sentences.
print(tokenized_text)

print('\nDoes the text is recognized correctly ? \n')
print('\nIf the text is not recognized correctly try using a better quality image. \n')
print('\nDo you want to proceed with this text?(y\\n) \n')

if(input()=='y' or 'Y'):
    sentences = tokenized_text.split('\n \n')
    questions = []  
    # for loop to seperate questions
    for i in range(len(sentences)):    
        if(sentences[i].endswith('?') or  sentences[i].startswith("What") or sentences[i].startswith("When") or sentences[i].startswith("How") or sentences[i].startswith("Why") or sentences[i].startswith("Describe") or sentences[i].startswith("Explain")):
            questions.append(sentences[i])
            print(sentences[i])
        
    print('\nDo you want to proceed with these recognized questions?(y\\n) \n')
    if(input()=='y' or 'Y'):
        print('\nPlease wait while your questions are being searched! \n')
        search_querys = []
        # for loop to get URLs of answers
        for i in range(len(questions)):
            query = questions[i]
            output = google_search(query)
            search_querys.append(output)
            
        solutions = {}
        # for loop to scrape answers from URLs
        for i in range(len(search_querys)):
            keys = questions[i]
            try:
                answers = scrape(search_querys[i][0])
            except Exception as e:
                values = e
            values = answers
            solutions[keys] = values
        
        # for loopp to display
        for x,y in solutions.items():
            print('\n******************\n')
            print(x)
            print('\n answer = \n')
            print(y)
            print('\n******************\n')
        
        print('\nAll questions have been answered! \n')

        print('\nDo you want the URLs of the answers?(y\\n)\n')
        if(input()=='y' or 'Y'):
            # for loop to display URLs
            for i in range(len(search_querys)):
                print(search_querys[i][0])
                
            print('Thank You!')
        else:
            print('Thank You!')
    else:
        print('Thank You!')        
else:
    print('Thank You!')
        
    

   