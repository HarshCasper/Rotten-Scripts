from bs4 import BeautifulSoup
import requests
import re
import os
import urllib3

class FetchTags(object):


	def __init__(self, ListOfUrl):
		self.ListOfUrl = ListOfUrl
		self.url = None
		self.usr_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
										'Chrome/61.0.3163.100 Safari/537.36' }
		self.directory = os.getcwd()
		self.alt_dict = {}
		self.title_dict = {}
		self.h2_dict = {}
		self.h3_dict = {}


	def get_results(self):
		i = 1
		for url in self.ListOfUrl:
			html = self.get_html(url)
			if html:
				self.get_keywords(html)
				print("Retrieved query no : {}".format(i))
				i += 1
			else:
				continue

		return self.alt_dict, self.title_dict, self.h2_dict, self.h3_dict

	def get_html(self, url):
		urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
		try :
			response = requests.get(url, headers = self.usr_agent, verify = False)
			response.raise_for_status()
			return response.text
		except:
			return None

	def get_keywords(self, html):
		soup = BeautifulSoup(html, 'html.parser')
		# print(soup.prettify())
		# FetchTags.save_file(soup.prettify(), self.directory)
		# meta = soup.find_all('meta')
		h1 = []
		h2 = []
		h3 = []
		title = soup.find('title')
		if title:
			title = title.get_text().strip()
	
		header2 = soup.find_all('h2')
		if header2:
			for ele in header2:
				if ele:
					h2.append(ele.get_text().strip())

		header3 = soup.find_all('h3')
		if header3:
			for ele in header3:
				if ele:
					h3.append(ele.get_text().strip())

		alt = []
		for div in soup.find_all('div'):
			for img in div.find_all('img', alt = True):
				if img['alt'] not in alt:
					alt.append(img['alt'])

		content = [alt, title,  h1, h2, h3]
		# self.save_file(content, self.directory)
		self.count_frequency(alt, title, h2, h3)

	def save_file(self, content, address):
		alternative_text_list = content[0]
		content = content[1::]
		if os.path.exists(address + r"/webpage.html"):
			os.remove(address + r"/webpage.html")
		fp = open(address + r'/webpage.html', 'w')
		for line in content:
			fp.write(str(line) + '\n\n')
		for text in alternative_text_list:
			fp.write(str(text) + '\n\n')
		fp.close()

	def count_frequency(self, alt_tag_list, title, h2_list, h3_list):

		special_characteres = "-|"

		if len(alt_tag_list) != 0:
			for data in alt_tag_list:
				l = data.split()
				# print(l)
				for word in l:
					self.alt_dict[word] = self.alt_dict.get(word, 0) + 1
		
		if title:	
			for word in title.split():
				if word not in special_characteres:
					self.title_dict[word] = self.title_dict.get(word, 0) + 1

		if len(h2_list) != 0:
			for line in h2_list:
				if line != None:
					for word in line.split():
						if word not in special_characteres:
							self.h2_dict[word] = self.h2_dict.get(word, 0) + 1

		if len(h3_list) != 0:
			for line in h3_list:
				if line != None:
					for word in line.split():
						if word not in special_characteres:
							self.h3_dict[word] = self.h3_dict.get(word, 0) + 1

		# print(self.alt_dict, self.title_dict, self.h2_dict, self.h3_dict, sep = '\n')
		





if __name__ == '__main__':
	links = ['http://uehy.mcminstrument.it/scrape-google-search-results-python.html', 'http://iduphul.gpkztwwz.site/web-scrape-google-search-results-python.html']
	obj = FetchTags(links)
	html = obj.get_html('https://ahrefs.com/blog/image-seo/')
	# html = obj.get_html('https://www.scrapinghub.com/what-is-web-scraping/')
	obj.get_keywords(html)
