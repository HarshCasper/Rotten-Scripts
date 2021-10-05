# Import and dependencies
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

time_wait_ten = 10
time_wait_five = 5
time_wait_two = 2
time_wait_one = 1
URL = "https://www.linkedin.com/"
endpoint = "https://www.linkedin.com/mynetwork/"

# Here the process of automation is achieved by using the framework Selenium.
# Selenium is a portable framework for testing and automating web applications web applications


def automate_linkedin():
    PATH = input("Enter the file path of the chromedriver ")
    chrome_path = PATH
    # Initiating and setting up the driver
    driver = webdriver.Chrome(chrome_path)
    driver.get(URL)
    # The script is made to wait, to ensure that the page is loaded
    time.sleep(time_wait_five)
    # This process is used to implement the login details
    driver.find_element_by_xpath(
        "/html/body/main/section[1]/div[2]/form/div[2]/div[1]/input"
    ).click()
    name = input("Enter your username ")
    time.sleep(time_wait_two)
    driver.find_element_by_xpath(
        "/html/body/main/section[1]/div[2]/form/div[2]/div[1]/input"
    ).send_keys(name)
    time.sleep(time_wait_two)
    driver.find_element_by_xpath(
        "/html/body/main/section[1]/div[2]/form/div[2]/div[2]/input"
    ).click()
    time.sleep(time_wait_two)
    passwd = input("Enter your password ")
    driver.find_element_by_xpath(
        "/html/body/main/section[1]/div[2]/form/div[2]/div[2]/input"
    ).send_keys(passwd)
    time.sleep(time_wait_two)
    driver.find_element_by_xpath(
        "/html/body/main/section[1]/div[2]/form/button"
    ).click()
    time.sleep(time_wait_two)
    send_request = 1
    # The user can send out multiple connection requests from the endpoint https://www.linkedin.com/mynetwork/ with a customized message
    while send_request:
        driver.get(endpoint)
        time.sleep(time_wait_ten)
        driver.find_element_by_xpath(
            "/html/body/div[8]/div[3]/div/div/div/div/div/div/ul/li[1]/ul/li[1]/div/section/div[1]/a"
        ).click()
        time.sleep(time_wait_two)
        try:
            try:
                driver.find_element_by_xpath(
                    "/html/body/div[8]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/span[1]/div/button"
                ).click()
                driver.find_element_by_xpath(
                    "/html/body/div[4]/div/div/div[3]/button[1]"
                ).click()
                message = input("Enter the message you want to send ")
                driver.find_element_by_xpath(
                    "/html/body/div[4]/div/div/div[2]/div[1]/textarea"
                ).send_keys(message)
                time.sleep(time_wait_two)
                driver.find_element_by_xpath(
                    "/html/body/div[4]/div/div/div[3]/button[2]"
                ).click()
                time.sleep(time_wait_two)
            except:
                try:
                    driver.find_element_by_xpath(
                        "/html/body/div[8]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/div/div/button"
                    ).click()
                    time.sleep(time_wait_two)
                    driver.find_element_by_xpath(
                        "/html/body/div[8]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/div/div/div/div/ul/li[4]/div/div/span[1]"
                    ).click()
                    driver.find_element_by_xpath(
                        "/html/body/div[4]/div/div/div[3]/button[1]"
                    ).click()
                    message = input("Enter the message you want to send ")
                    driver.find_element_by_xpath(
                        "/html/body/div[4]/div/div/div[2]/div[1]/textarea"
                    ).send_keys(message)
                    time.sleep(time_wait_two)
                    driver.find_element_by_xpath(
                        "/html/body/div[4]/div/div/div[3]/button[2]"
                    ).click()
                    time.sleep(time_wait_two)
                except:
                    print("Cannot connect")
        except:
            print("Cannot connect")
        print("Do you want to make another connection? ")
        send_request = input(input("Enter 1 to continue, 0 to stop "))
        if send_request == 1:
            continue
        return "Sent all requests"


if __name__ == "__main__":
    automate_linkedin()
