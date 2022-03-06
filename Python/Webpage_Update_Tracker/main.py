# standard library
from datetime import datetime
from time import sleep

# installed library
from selenium import webdriver

# initialize Firefox webdriver
options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(options=options)

# get the current date and time in proper format
# to be included in the filename
now = datetime.now()
now_string = now.strftime("%d-%m-%Y_%H:%M:%S")

page = input("Enter the link of the webpage you want to snapshot:\n")

# access the page
driver.get(page)
sleep(1)

# take screenshot, save with proper filename
driver.get_screenshot_as_file(f"screenshot_{now_string}.png")
driver.quit()
print("Snapshot generated!")
