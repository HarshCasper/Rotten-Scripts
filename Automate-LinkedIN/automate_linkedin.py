#Import and dependencies
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
ten = 10
five = 5
two = 2
one = 1
URL = "https://www.linkedin.com/"
Endpoint = "https://www.linkedin.com/mynetwork/"

#Here the process of automation is achieved by using the framework Selenium.
#Selenium is a portable framework for testing and automating web applications web applications
#Path to chromedriver.exe

chrome_path = r"C:\Users\giril\AppData\Local\Programs\Python\Python36-32\chromedriver.exe"

#Initiating and setting up the driver
driver = webdriver.Chrome(chrome_path)
driver.get(URL)

#The script is made to wait, to ensure that the page is loaded
time.sleep(five)

def login():
    #This process is used to implement the login details
    driver.find_element_by_xpath("/html/body/main/section[1]/div[2]/form/div[2]/div[1]/input").click()
    name = input("Enter your username ")
    time.sleep(two)
    driver.find_element_by_xpath("/html/body/main/section[1]/div[2]/form/div[2]/div[1]/input").send_keys(name)
    time.sleep(two)
    driver.find_element_by_xpath("/html/body/main/section[1]/div[2]/form/div[2]/div[2]/input").click()
    time.sleep(two)
    passwd = input("Enter your password ")
    driver.find_element_by_xpath("/html/body/main/section[1]/div[2]/form/div[2]/div[2]/input").send_keys(passwd)
    time.sleep(two)
    driver.find_element_by_xpath("/html/body/main/section[1]/div[2]/form/button").click()
    time.sleep(two)


def send_request():
    done = one
    #The user can send out multiple connection requests from the endpoint https://www.linkedin.com/mynetwork/ with a customized message

    while done:
        driver.get(Endpoint)
        time.sleep(ten)
        driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/div/div/div/div/div/ul/li[1]/ul/li[1]/div/section/div[1]/a").click()
        time.sleep(two)
        try:
            try:
                driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/span[1]/div/button").click()
                driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[1]").click()
                message = input("Enter the message you want to send ")
                driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div[1]/textarea").send_keys(message)
                time.sleep(two)
                driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
                time.sleep(two)
            except:
                try:
                    driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/div/div/button").click()
                    time.sleep(two)
                    driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/div/div/div/div/ul/li[4]/div/div/span[1]").click()
                    driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[1]").click()
                    message = input("Enter the message you want to send ")
                    driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div[1]/textarea").send_keys(message)
                    time.sleep(two)
                    driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
                    time.sleep(two)
                except:
                    print("Cannot connect")

        except:
            print("Cannot connect")

        print("Do you want to make another connection? ")
        done = input(input("Enter 1 to continue, 0 to stop "))
        if done == 1:
            continue
        else:
            return("Sent all requests")
    
if __name__ == "__main__":
    login()
    send_request()

