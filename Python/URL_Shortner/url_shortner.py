__author__ = "Sri Manikanta Palakollu"
__date__ = "29-06-2020"

import requests
from urllib.parse import urlencode
import sys

def make_tiny(url):
    request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url': url}))
    result = requests.get(request_url)
    return result.text

def main():
    for tinyurl in map(make_tiny, sys.argv[1:]):
        print(tinyurl)

if __name__ == '__main__':
    main()
