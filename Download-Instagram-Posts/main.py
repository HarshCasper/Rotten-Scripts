import re
import time
import subprocess
import base64

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.Firefox()

def downloadImages(page_source, query):
  soup = BeautifulSoup(page_source, 'html.parser')
  images = soup.findAll("img", {"class": ["FFVAD"]})

  image_count = 1
  for image in images:
    img_src = re.search(r'src="(.*?)"', str(image)).group(1)
    print(img_src)

    if re.match(r'http.*?', img_src):
      img_count_str = f'{image_count:03}'
      image_count += 1

      filename = img_count_str + ".jpg"
      subprocess.run(["wget", img_src, "-O", filename])
      print("+ Saved", filename)
  
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
    break

  downloadImages(driver.page_source, query)

queries = ["sanket_m2"]

for query in queries:
  fetchImageSources(query)

driver.close()
