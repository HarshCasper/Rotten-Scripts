#Import and dependencies
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

#Here the process of automation is achieved by using the framework Selenium.
#Selenium is a portable framework for testing and automating web applications web applications

#Path to chromedriver.exe
chrome_path = r"C:\Users\giril\AppData\Local\Programs\Python\Python36-32\chromedriver.exe"

#Initiating and setting up the driver
driver = webdriver.Chrome(chrome_path)

def login():

    #For logging into web telegram, the user must verify the phone number
    URL = "https://web.telegram.org/#/login"
    driver.get(URL)
    time.sleep(60)

def automate_telegram():

    #This process is automated using the XML path of the elements that can be found on inspecting the page using Developer Tools
    user = 1
    while user:
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div[1]/div/input").click()
        name = input("Enter the name of the contact ")
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div[1]/div/input").send_keys(name)
        time.sleep(4)
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div[2]/div/div[1]/ul/li").click()
        done = 1
        while done:
            message = input("Enter message ")
            driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[3]/div[2]/div/div/div/form/div[2]/div[5]").send_keys(message)
            driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[3]/div[2]/div/div/div/form/div[2]/div[5]").send_keys(Keys.ENTER)
            print("Do you want to send another message? ")
            done = int(input("Enter 1 to continue, 0 to stop "))
            if done == 0:
                break
            
        print("Do you want to send messages to another contact? ")
        user = int(input("Enter 1 to continue, 0 to stop "))
        if user == 0:
            return("All messages sent")

if __name__ == "__main__":
    login()
    automate_telegram()
        
