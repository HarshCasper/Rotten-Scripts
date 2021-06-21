# Imports and dependencies
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

time_wait_sixty = 60
time_wait_four = 4

# Here the process of automation is achieved by using the framework Selenium.
# Selenium is a portable framework for testing and automating web applications web applications


def automate_telegram():
    # Path to the chromedriver must be entered without quotations
    PATH = input("Enter path to chromedriver path ")
    chrome_path = PATH
    # Initiating and setting up the driver
    driver = webdriver.Chrome(chrome_path)
    # For logging into web telegram, the user must verify the phone number
    URL = "https://web.telegram.org/#/login"
    driver.get(URL)
    time.sleep(time_wait_sixty)
    user = 1
    while user:
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div/div[1]/div[1]/div/input"
        ).click()
        name = input("Enter the name of the person ")
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div/div[1]/div[1]/div/input"
        ).send_keys(name)
        time.sleep(time_wait_four)
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div/div[1]/div[2]/div/div[1]/ul/li"
        ).click()
        msg = 1
        while msg:
            message = input("Enter message ")
            driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[3]/div[2]/div/div/div/form/div[2]/div[5]"
            ).send_keys(message)
            driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[3]/div[2]/div/div/div/form/div[2]/div[5]"
            ).send_keys(Keys.ENTER)
            print("Do you want to send another message? ")
            msg = int(input("Enter 1 to continue, 0 to stop "))
            if msg == 0:
                break

        print("Do you want to send messages to another contact? ")
        user = int(input("Enter 1 to continue, 0 to stop "))

    return "All messages sent"


if __name__ == "__main__":
    automate_telegram()
