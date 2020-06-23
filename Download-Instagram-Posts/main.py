import os
import re
import time
import wget
import subprocess

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.Firefox()

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
  try:
    os.mkdir(dest)
  except FileExistsError:
    print("Using existing '{}' directory".format(dest))
  except:
    print("Unable to create '{}' folder".format(dest))
    exit(1)

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
      subprocess.run(["wget", img_src, "-O", "{}/{}".format(dest, filename)])

      print("+ Saved", "{}/{}".format(dest, filename))
  
def fetchImageSources(query):
  driver.get("https://www.instagram.com/{}".format(query))  
  last_height = driver.execute_script("return document.body.scrollHeight")

  while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

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
