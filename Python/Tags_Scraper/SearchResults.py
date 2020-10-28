import os
import requests
from bs4 import BeautifulSoup
from URL_generator import GURL

def FetchURLs(query):

    """
    FetchURLs method takes in the query from the main method , connects to google and search
    for the query , scrapes the URLs of the search results and returns the list of the 
    Links.
    """
    directory = os.getcwd()

    if os.path.exists(directory + r"/links_fetched.txt"):
        os.remove(directory + r"/links_fetched.txt")

    obj = GURL(query)
    obj.generate()
    url = obj.get_url()

    links_file = open(directory + r"/links_fetched.txt", 'w')
    links_file.write("URL Fetched : {}\n\n".format(url))

    usr_agent = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/61.0.3163.100 Safari/537.36'}


    req = requests.get(url, headers=usr_agent)
    req.raise_for_status()
    soup = BeautifulSoup(req.text, 'html.parser')


    results = []
    i = 1

    for result in soup.find_all('div', attrs={'class': 'g'}):
        link = result.find('a', href=True)
        title = link.find('h3')
        if link and title:
            results.append(link['href'])
            links_file.write("{}) Link : {}\n\n".format(i, link['href']))
            links_file.write("\n\n________________________________________\n\n")
            i += 1
    links_file.close()
    return results
