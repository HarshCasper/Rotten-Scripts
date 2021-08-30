import string
import random
import webbrowser
import requests
import os
import dotenv

dotenv.load_dotenv()

try:
    API_KEY = os.getenv('API_KEY')
    random = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))
    urlData = "https://www.googleapis.com/youtube/v3/search?key={}&maxResults=1&part=snippet&type=video&q={}".format(API_KEY,random)
    jsondata = requests.get(urlData)
    results = jsondata.json()
    if 'error' in results.keys():
        raise ValueError
    webbrowser.open('https://youtu.be/' + str(results['items'][0]['id']['videoId']))
except ValueError:
    print(results['error']['message'])
