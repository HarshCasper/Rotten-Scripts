#!/usr/bin/env python3
#Import and dependencies

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

#Constants
three = 3
twenty-five = 25
one = 1

#Here the process of automation is achieved by using the framework Selenium.
#Selenium is a portable framework for testing and automating web applications web applications

#Path to chromedriver.exe
chrome_path = r"C:\Users\giril\AppData\Local\Programs\Python\Python36-32\chromedriver.exe"

#Initiating and setting up the driver
driver = webdriver.Chrome(chrome_path)

URL = "https://web.whatsapp.com/"
driver.get(URL)

#The script is made to wait, to ensure that the page is loaded
time.sleep(twenty-five)

def send_messages():
    
    chats = int(input("Enter the number of personal chats/groups you would want to message "))

    for chat in range(chats):

        #This is used to enable the user to search for the contact
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/header/div[2]/div/span/div[2]/div').click()

        name = input("Enter name to whom you want to send a message ")
        time.sleep(three)

        #On entering the contact, the name is entered into the search bar
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/div/div[2]').send_keys(name)
        time.sleep(three)

        #The contact's chat will be opened
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/div/div[2]').send_keys(Keys.ENTER)
    
        #This enables the user to send more than one message to the same contact
        done = one
        while done:
            message = input("Enter the message you want to enter ")

            #The cursor is positioned and the chat box is activated
            driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]').send_keys(message)
            time.sleep(three)

            #On clicking the send button, a message is sent to the contact
            driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button').click()

            print("Would you want to send another message to the same contact ?")
        
            done = int(input("Enter 1 to continue, 0 to stop "))
        
    print("All messages sent successfully")

send_messages()
