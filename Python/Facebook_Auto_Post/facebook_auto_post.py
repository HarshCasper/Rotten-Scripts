from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import time


try:
    driver = webdriver.Chrome(
        '<===============ENTER YOUR CHROME DRIVER PATH===========>')
    driver.get('https://www.facebook.com/')
    print("Facebook Open Succesfully...!")
    time.sleep(5)

    # Facebook Email

    facebookEmail = input("Enter your Email ID:")
    email = driver.find_element_by_xpath(
        "//input[@id='email' or @name='email']")
    email.send_keys(facebookEmail)
    print("Email Id Entered Successfully")

    # Facebook Password

    facebookPassword = getpass.getpass("Enter your Facebook password: ")
    password = driver.find_element_by_xpath("//input[@id='pass']")
    password.send_keys(facebookPassword)
    print("Password Entered Succesfully")

    # Submit Button
    button = driver.find_element_by_xpath("//input[@id='u_0_r']")
    button.click()
    print("Logged in Successfully")
    time.sleep(15)

    # Trying to Post the Content on Facebook.
    inputbox = driver.find_element_by_css_selector("span._5qtp")
    inputbox.click()
    time.sleep(5)

    Text = input("\tWhats on your mind? Write your thoughts here: \n")
    text = driver.find_element_by_css_selector("#composer_text_input_box")
    text.click()
    text.send_keys(Text)
    postbutton = driver.find_element_by_xpath("//*[text()='Post']")
    postbutton.click()
    time.sleep(15)
    driver.close()
except Exception:
    print("Something Went Wrong...!")
