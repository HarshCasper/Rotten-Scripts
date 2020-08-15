# pip install bs4
# import the packages

import requests
from bs4 import BeautifulSoup
from queue import Queue, Empty
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse


class MultiThreadScraper:

    def __init__(self, base_url):

        self.base_url = base_url
        # root_url ensure that scraper does not end up on other sites
        self.root_url = '{}://{}'.format(urlparse(self.base_url).scheme, urlparse(self.base_url).netloc)         # urlparse to pull out the site homepage
        # threadpool allows to use a callback function to collect results
        self.pool = ThreadPoolExecutor(max_workers=20)    
        # set contains a list of URLs which has been crawled
        # prevent the crawler from visiting the same URL twice
        self.scraped_pages = set([])
        # queue will contain URLs we wish to crawl, we will continue to grab URLs from our queue until it’s empty
        self.to_crawl = Queue()
        # place in the base URL to the start of the queue
        self.to_crawl.put(self.base_url)


# to extract all of a sites internal links

    def parse_links(self, html):
        # generate soup object using Beautifulsoup
        soup = BeautifulSoup(html, 'html.parser')
        # find_all method returns every ‘a’ element which has a ‘href’ property
        links = soup.find_all('a', href=True)

        for link in links:
            url = link['href']      # pull out the acual href content
        
            #  check whether link is relative (starting with a ‘/’) or starts with our root URL
            if url.startswith('/') or url.startswith(self.root_url):
                # urljoin generates a crawlable URL and then put this in the queue provided that hasn't been crawled
                url = urljoin(self.root_url, url)
                if url not in self.scraped_pages:
                    self.to_crawl.put(url)

    # scrape_info method can be overridden so that it can extract data from the site you are crawling
    def scrape_info(self, html):
        return

    def post_scrape_callback(self, res):

        # by calling .result() in argument, we can get to the contents of the returned value
        result = res.result()

        # check if we have a result and whether the result has a 200 status code.
        # if both of these will be true, send the html to the parse_links and currently empty scrape_info function
        if result and result.status_code == 200:
            self.parse_links(result.text)
            self.scrape_info(result.text)

    # it takes URL and returns a response object if it was successful
    def scrape_page(self, url):
        try:
            # By limiting the amount of CPU work, we can increase the overall speed of the crawler
            res = requests.get(url, timeout=(3, 30))
            return res
        except requests.RequestException:
            return

# run scraper function brings all the previous work together and manages the thread pool
    def run_scraper(self):
        # run scraper will continue to run while there are still URLs to crawl
        # create while True loop and ignoring any exceptions except Empty, which will be thrown if our queue has been empty for more than 60 seconds
        while True:
            try:
                target_url = self.to_crawl.get(timeout=60)

                #  pull URLs from queue and submit them to the thread pool for execution
                if target_url not in self.scraped_pages:
                    print("Scraping URL: {}".format(target_url))
                    self.scraped_pages.add(target_url)
                    job = self.pool.submit(self.scrape_page, target_url)
                    # add callback which will run once the function has returned
                    job.add_done_callback(self.post_scrape_callback)
            except Empty:
                return
            except Exception as e:
                print(e)
                continue

# call the functions
if __name__ == '__main__':
    s = MultiThreadScraper("https://www.learnpython.org/")           # link for crawling
    s.run_scraper()
