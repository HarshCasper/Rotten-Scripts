'''
This python program collects the top news headlines and their description from 'newsapi.org' website and will read the news headlines and
description in his own voice.
News API is a simple and easy-to-use API that returns JSON metadata for headlines and articles live all over the web right now.
Visit newsapi.org for documentation and for your API key
'''

import time
from win32com.client import Dispatch
import requests

file = open("Url.txt", 'r+')
#Fetching the link with API key from Url.txt file.
url_from_file = file.read()

def func(url_from_file):

    url = (url_from_file)
    response = requests.get(url)
    json_news_content = response.json()
    print(json_news_content)
    lists = json_news_content['articles']

    #function for converting text into voice
    def speaker(str):
        speak = Dispatch("SAPI.SpVoice")
        speak.speak(str)

    while True:
        for dics in lists:
            for key in dics:
                if key == 'title':
                    title = str(dics[key])
                    print(str(dics[key]))
                    speaker("Title")
                    time.sleep(1)
                    speaker(title)

                if key == 'description':
                    description = str(dics[key])
                    print(dics[key])
                    speaker("Description")
                    time.sleep(1)
                    speaker(description)

if __name__ == "__main__":

    func(url_from_file)

#End_of_program
