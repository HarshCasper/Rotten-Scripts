from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import mycontacts
import tkinter as tk
from tkinter import *
import xpath
import time

# Function checking whether the given user exists in the user's whatsapp contact list


def checkuser(str):
    try:
        driver.find_element_by_xpath(str)
    except NoSuchElementException:
        return False
    return True


# Taking all the Credentials from the user
contact_name = []
print(
    "\n\nEnter the name of the contact you want to send message to (Type 'ALL' if you want to send message to all your contacts: )"
)
print(
    R"For multiple contacts use newline and type 'stop' at the end to stop adding contacts: "
)
while 1:
    a = input()
    if a == "stop":
        break
    contact_name.append(a)

print("Enter the message you want to send:- ", end=" ")
message = input()

print(
    "Enter the number of times you want to bomb the message to your contact: ", end=" "
)
count_message = int(input())


# defining the driver for the chrome
driver = webdriver.Chrome()
d1 = driver.get("https://web.whatsapp.com/")
driver.maximize_window()
time.sleep(10)

# If the user chooses ALL then the message will be sent to all the contacts added in mycontacts.py
if "ALL" in contact_name:
    for contact in mycontacts.my_contacts:

        # locating the chat icon using xpath
        chat = driver.find_element_by_xpath(xpath.newchat_xpath)
        chat.click()

        # locating the search box using xpath and adding the contact to search
        search = driver.find_element_by_xpath(xpath.search_xpath)
        search.send_keys(contact)
        time.sleep(1)

        # Checking whether the contact exist or not
        if checkuser("//span[@title='{}']".format(contact)) is False:
            continue

        # Searching the contact and clicking on it
        find_user = driver.find_element_by_xpath("//span[@title='{}']".format(contact))
        find_user.click()
        time.sleep(1)

        # Finding the box to type the message and clicking on it
        find_message = driver.find_element_by_xpath(xpath.message_xpath)
        find_message.click()
        time.sleep(1)

        # Sending the messages on the basis of count given by the user
        for i in range(count_message):
            find_message.send_keys(message)
            driver.find_element_by_xpath(xpath.sendbutton_xpath).click()
            time.sleep(0.5)
        time.sleep(1)
# Else the messages will be sent to the users mentioned in the input
else:
    for contact in contact_name:
        chat = driver.find_element_by_xpath(xpath.newchat_xpath)
        chat.click()

        search = driver.find_element_by_xpath(xpath.search_xpath)
        search.send_keys(contact)
        time.sleep(1)

        if checkuser("//span[@title='{}']".format(contact)) is False:
            continue

        find_user = driver.find_element_by_xpath("//span[@title='{}']".format(contact))
        find_user.click()
        time.sleep(1)

        find_message = driver.find_element_by_xpath(xpath.message_xpath)
        find_message.click()
        time.sleep(1)

        for i in range(count_message):
            find_message.send_keys(message)
            driver.find_element_by_xpath(xpath.sendbutton_xpath).click()
            time.sleep(0.5)
        time.sleep(1)

print("Sms Bombing Completed...!!!!")
