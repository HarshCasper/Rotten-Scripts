import urllib
import os
import hashlib
import sys

def get_hash(name):
    readsize = 64*1024
    with open(name,'rb') as f:
        size = os.path.getsize(name)
        data = f.read(readsize)
        f.seek(-readsize, os.SEEK_END)
        data += f.read(readsize)
    return hashlib.md5(data).hexdigest()

def main():
    userAgent = 'SubDB1.0 (seema1711/0.1; https://github.com/seema1711/subtitle-downloader)'
    moviePath = sys.argv[1]
    movieName = os.path.join(os.getcwd(), moviePath)
    language = 'en'
    action = 'download'
    baseURL = 'http://api.thesubdb.com/?'
    hashed = get_hash(movieName)

    content = {
        'action': action, 
        'hash': hashed,
        'language': language,
    }

    url = baseURL + urllib.urlencode(content)
    request = urllib.Request(url)
    request.add_header('User-Agent', userAgent)
    response = urllib.urlopen(request)
    subtitles = response.read()

    index = movieName.rfind('.')
    fileName = movieName[0:index] + '.srt'
    with open(fileName,'w') as f:
        f.write(subtitles)
    print("Subtitle Downloaded!!")

