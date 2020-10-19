import requests
from bs4 import BeautifulSoup
import os
from Fetch_Tags import FetchTags
from URL_generator import GURL

def FetchURLs(query):
	directory = os.getcwd()

	if os.path.exists(directory + r"/links_fetched.txt"):
		os.remove(directory + r"/links_fetched.txt")

	obj = GURL(query)
	obj.generate()
	url = obj.get_url()

	fp = open(directory + r"/links_fetched.txt", 'w')
	fp.write("URL Fetched : {}\n\n".format(url))

	usr_agent = {
	        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
	                      'Chrome/61.0.3163.100 Safari/537.36'}


	req = requests.get(url, headers = usr_agent)
	req.raise_for_status()
	soup = BeautifulSoup(req.text, 'html.parser')


	results = []
	i =1

	for result in soup.find_all('div', attrs={'class': 'g'}):
	    link = result.find('a', href=True)
	    title = link.find('h3')
	    if link and title :
	    	results.append(link['href'])
	    	fp.write("{}) Link : {}\n\n".format(i, link['href']))
	    	fp.write("\n\n________________________________________\n\n")
	    	i+=1
	
	fp.close()

	return results