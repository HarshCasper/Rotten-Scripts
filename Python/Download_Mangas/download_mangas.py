import argparse
import requests
from PIL import Image
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--name', action='store', type=str, required=True, help="Enter the name of the manga")
my_parser.add_argument('--start', action='store', type=int, required=False, help="Enter the starting chapter for your download")
my_parser.add_argument('--end', action='store', type=int, required=False, help="Enter the ending chapter for your download")
my_parser.add_argument('--chapter', action='store', type=int, required=False, help="Enter a specific chapter number to download")

args = my_parser.parse_args()
name = args.name
starting_chapter = args.start
ending_chapter = args.end
one_chapter = args.chapter

# main function to download each chapter
def chapterDownload(one_chapter, name):
    name = name.lower()
    name = name.replace(' ', '-')

    # webdriver is used to get the number of pages in each chapter
    driver = webdriver.Chrome(ChromeDriverManager().install())
    URL = "http://www.mangareader.net/" + name + "/" + str(one_chapter)
    driver.get(URL)
    
    # the element pageMenu is a drop-down which has options for each page
    page = driver.find_element_by_name("pageMenu")
    number_of_pages = [x for x in page.find_elements_by_tag_name("option")]
    last_page = int(number_of_pages[-1].get_attribute("value").split('/')[-1])
    first_page = 1

    driver.quit()

    images = []
    for i in range(first_page, last_page+1):
        # since we now have the number of pages, we can use beautiful soup to get the images
        url = "http://www.mangareader.net/" + name + "/" + str(one_chapter) + "/" + str(i)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        image = soup.find('img')
        imageURL = image['src']
        data = requests.get(imageURL, stream=True).raw
        images.append(data)

    main_image = Image.open(images[0]).convert('RGB')
    image_list = []
    for i in range(1, len(images)):
        img = Image.open(images[i]).convert('RGB')
        image_list.append(img)
    
    # conversion of a list of images to pdf
    filename = name + "-chapter-" +str(one_chapter) + '.pdf'
    main_image.save(filename, save_all=True, append_images=image_list)

# to download a single chapter
if(one_chapter is not None):
    chapterDownload(one_chapter, name)

# to download a range of chapters
elif(starting_chapter is not None and ending_chapter is not None):
    for i in range(starting_chapter, ending_chapter+1):
        chapterDownload(i, name)

# if nothing is mentioned besides the name of the manga
else:
    chapterDownload(1, name)
