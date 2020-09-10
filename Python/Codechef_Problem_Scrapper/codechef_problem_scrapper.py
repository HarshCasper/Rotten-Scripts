from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

#Chrome settings to omit messages on the command line
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--hide-scrollbars')
options.add_argument('--disable-gpu')
options.add_argument("--log-level=3")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

#Codechef url for problems
url = "https://www.codechef.com/problems/"

#user defined problem code
problem_code = input("Enter the problem code: ")

#fetching the url with the driver
driver.get(url+problem_code)

#Logic to fetch dynamic content
extra_buttons = driver.find_elements_by_class_name("moreLink")
for x in range(len(extra_buttons)):
    if extra_buttons[x].is_displayed():
        driver.execute_script("arguments[0].click();", extra_buttons[x])
        time.sleep(1)

#Getting the page source 
page_source = driver.page_source

#Soup object to conduct scraping on
soup = BeautifulSoup(page_source, 'html.parser')

#List to store the content of the page source
content = []

#Getting the required content
problem_content = soup.find_all('div', class_='mathjax-support')
for problem in problem_content:

    content.append(problem.get_text())

#Removing unnecessary stuff and adding description text
content = ["Description" + "\n"] + content[:-2]


#Custom name for the file
file_name= soup.title.text.split("|")[0].strip()

#Text file to write our content
file1 = open(file_name+".txt","w", encoding='utf-8')

#Logic to write the content on the file 
for cont in content:
    file1.write(cont) 
file1.close() 

print("Your problem statement has been created successfully")








