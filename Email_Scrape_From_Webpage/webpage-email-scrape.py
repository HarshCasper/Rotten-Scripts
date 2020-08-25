# Script to scrap all the E-Mails in a Webpage.

# Importing required libraries and modules.
import re                               # For regular expression operations
import requests                         # For sending HTTP request to server 
from urllib.parse import urlsplit       # For Spliting the URL 
from collections import deque           # A list-like container
from bs4 import BeautifulSoup           # A Python package for parsing HTML and XML documents 
import requests.exceptions              # For handling eceptions

# Enter here the webpage to scrape in the original_url. 
original_url = input("Enter the webpage url: ")

# a queue of URLs to be scraped
unprocessed_urls = deque([original_url])

# set of already crawled urls.
processed_urls = set()

# a set of fetched emails to save fetched emails
emails = set()

# moving unsraped_url from the queue to scraped_urls set
url = unprocessed_urls.popleft()
# Remove and return an element from the left side of the deque.
processed_urls.add(url)

# extracting base url to resolve relative links,i.e extract different parts of the url.
parts = urlsplit(url)

# As urlsplit() returns a 5-tuple which are (addressing scheme, network location, path, query, fragment identifier).
# So we will get the base and path part for the website URL.
base_url = "{0.scheme}://{0.netloc}".format(parts)
path = url[:url.rfind('/')+1] if '/' in parts.path else url

# Sending an HTTP GET request to the website.
try:
    response = requests.get(url)
except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
    # ignoring pages with errors and continue with next url
    pass

# extracting all email addresses and add them into the resulting set
new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
emails.update(new_emails)
print(emails)

# Finding all linked URLs in the website.
# Creating a Beautiful Soup to parse the HTML document.
soup = BeautifulSoup(response.text, 'lxml')

# Once this document is parsed and processed,
# now find and process all the anchors as it may contains emails i.e. linked urls in this document.
for anchor in soup.find_all("a"):
    # extracting link url from the anchor tag
    link = anchor.attrs["href"] if "href" in anchor.attrs else ''
    # resolve relative links (starting with /)
    if link.startswith('/'):
        link = base_url + link
    elif not link.startswith('http'):
        link = path + link

    # add the new url to the queue if it was not in unprocessed list nor in processed list yet
    if not link in unprocessed_urls and not link in processed_urls:
        unprocessed_urls.append(link)

# End of the script.