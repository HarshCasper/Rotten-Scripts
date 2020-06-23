import os
import re
import time
import wget
import errno

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)

def mkdir_p(path):
  try:
    os.makedirs(path)
  except OSError as exc:  # Python ≥ 2.5
    if exc.errno == errno.EEXIST and os.path.isdir(path):
      pass
    else:
      raise

def parseURL(url):
  return url.replace("&amp;", "&")

def setup():
  try:
    os.mkdir("images")
  except FileExistsError:
    print("Using existing 'images/' directory")
  except:
    print("Unable to create 'images/' folder")
    exit(1)

def createAccountDirectory(query):
  dest = "images/{}".format(query)

  mkdir_p(dest)

  return dest

def downloadImages(page_source, query):
  dest = createAccountDirectory(query)

  soup = BeautifulSoup(page_source, 'html.parser')
  images = soup.findAll("img", {"class": ["FFVAD"]})

  image_count = 1
  for image in images:
    img_src = re.search(r'src="(.*?)"', str(image)).group(1)
    img_src = parseURL(img_src)

    if re.match(r'http.*?', img_src):
      img_count_str = f'{image_count:03}'
      image_count += 1

      filename = img_count_str + ".jpg"
      wget.download(img_src, "{}/{}".format(dest, filename))

      print(" Saved", "{}/{}".format(dest, filename))
  
def fetchImageSources(query):
  driver.get("https://www.instagram.com/{}".format(query))  
  last_height = driver.execute_script("return document.body.scrollHeight")

  while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
      break

    last_height = new_height

  downloadImages(driver.page_source, query)

queries = ["sanket_m2"]

setup()
for query in queries:
  fetchImageSources(query)

driver.close()
