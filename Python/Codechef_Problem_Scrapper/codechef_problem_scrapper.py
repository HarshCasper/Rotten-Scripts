from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
import os

#Modified chrome settings to adjust the behaviour of chrome driver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--hide-scrollbars')
options.add_argument('--disable-gpu')
options.add_argument("--log-level=3") 
options.add_experimental_option('excludeSwitches',['enable-logging'])
driver = webdriver.Chrome(options=options)

#Problem code entered by the user
problem_code = input("Enter the problem code: ")

#Base url of codechef
url = "https://www.codechef.com/problems/"

#Running the selenium driver on the desired url
driver.get(url+problem_code.upper())

#Title of the problem specified by the user
page_title = driver.title[:-10].strip()

#Logic to scroll the entire page and capture it as a screenshot
Scroll_object = lambda scroll: driver.execute_script('return document.body.parentNode.scroll'+scroll)
driver.set_window_size(Scroll_object('Width'),Scroll_object('Height'))                                                                                                         
driver.find_element_by_tag_name('body').screenshot(page_title+'.png')

#For openeing the screenshot created by the web driver
screenshot_image = Image.open(page_title+'.png')

#Collecting the height and width of our screenshot
width, height = screenshot_image.size 

#Setting the parameters that will be used for the image cropping   
left = 5
top = height / 18
right = width*.63
bottom = 3 * height / 4

#Logic that performs the screenshot cropping to extract the useful portion
screenshot_image = screenshot_image.crop((left, top, right, bottom)) 

driver.quit()

#Creating an object from our screenshot that will be used in pdf making
pdf_object = screenshot_image.convert('RGB')

#Saving our pdf object in a pdf file
pdf_object.save(page_title+'.pdf')

#finally eliminating the screenshot image
os.remove(page_title+'.png')

print("Your problem has been successfully stored as a pdf!!")