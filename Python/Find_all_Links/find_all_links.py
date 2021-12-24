import re
import sys
import requests

from bs4 import BeautifulSoup


def help():
    print("Usage: python find_all_links.py <url>")


def parseURL(url):
    return url.replace("&amp;", "&")


def extractLinks(url):
    # Extracts links from the given webpage

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    links = re.findall("http.?://[^\s\"']+", str(soup))

    if len(links) == 0:
        print("No links on {}".format(url))

    for link in links:
        print(parseURL(link))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        help()
        sys.exit(0)

    url = sys.argv[1]
    extractLinks(url)
