from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import selenium
import time 


def scrap(email, password_input):
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://www.quora.com/")
    print("Logging in Quora")
    username = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/form/div[2]/div[1]/input')))
    username.send_keys(email)
    password =  WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/form/div[2]/div[2]/input')))
    password.send_keys(password_input)

    login = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/form/div[2]/div[3]/input')))

    login.click()

    profile = WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div[3]/div/div/div/div/div/div/div/div/div/div[2]')))
    print("Let's Go to Bookmark Section")
    profile.click()

    bookmarks = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div[3]/div/div[2]/div/div[1]/div/div/div[2]/a[4]/div/div[2]/div/div')))

    bookmarks.click()
    time.sleep(1)
    i = 1
    print("Finally Scrapping Starts!")
    while True:
        try:
            try:
                more = driver.find_element_by_xpath(f'/html/body/div[1]/div/div/div[4]/div/div/div[2]/div[2]/div[{i}]/div/div[1]/div/div[1]/div/div[4]/div/div/div/div/div[1]/div/div/div/div')
                more.click()
            except selenium.common.exceptions.NoSuchElementException:
                pass
            text = driver.find_element_by_xpath(f"/html/body/div[1]/div/div/div[4]/div/div/div[2]/div[2]/div[{i}]/div").text
            with open('answers.pdf','a',encoding='utf-8') as f:
                f.write(f"ANSWER - {i}\n")
                f.write(text)
                f.write("\n")
            i += 1 
        except selenium.common.exceptions.NoSuchElementException:
            break
    print("Thanks, Check the file!")

if __name__ == "__main__":
    print("*********WELCOME TO QUORA BOOKMARK QUESTIONS SCRAPPER*********")
    print("SET YOUR PREFERENCES: ")
    email = input("Enter Email ID of Quora: ")
    password = input("Enter Quora Password: ")
    print("Now Sit back and watch it scrapped! ")
    scrap(email=email, password_input=password)

    