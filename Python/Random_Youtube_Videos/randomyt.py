import json
import urllib.request
import string
import random
from webbrowser import open

try:
    API_KEY = str(input("Enter your generated API-KEY : "))
    random = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))
    urlData = "https://www.googleapis.com/youtube/v3/search?key={}&maxResults=1&part=snippet&type=video&q={}".format(API_KEY,random)
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    results = json.loads(data.decode(encoding))
    open('https://youtu.be/' + str(results['items'][0]['id']['videoId']))
except Exception as e:
    print("Invalid API KEY")