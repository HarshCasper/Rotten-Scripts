'''
This python program collects the top news headlines and their description from 'newsapi.org' website and will read the news headlines and
description in his own voice.
News API is a simple and easy-to-use API that returns JSON metadata for headlines and articles live all over the web right now.
***Visit newsapi.org for documentation and for your API key***
'''

import time
from win32com.client import Dispatch
import requests

def func():
    url = (
        'http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=paste your API key here')  # Only paste your API key here, don't change the whole link.
    # Example: ' http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=9895kn34nah45kan87ha12HG34Ng3s6 '

    response = requests.get(url)
    m = response.json()
    print(m)
    lst = m['articles']

    def speaker(str):
        speak = Dispatch("SAPI.SpVoice")
        speak.speak(str)

    while True:
        for dics in lst:
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
    func()