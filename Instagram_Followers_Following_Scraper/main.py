from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pandas as pd


def get_users(user_type, insta_id):
    '''Takes the user_type( a string named followers or following) 
    and a username as argument and returns an array of the user's 
    followers or following repectively'''
    button = browser.find_element_by_css_selector(
        "a[href='/"+insta_id+"/"+user_type+"/']")  # select followers/following button
    no = (int)(button.text.strip().split()[0])  # count of followers/following
    button.click()  # click on followers/following button to open dialog
    users = browser.find_element_by_class_name(
        "PZuss")  # for selecting the dialog
    users = users.find_elements_by_css_selector(
        "li")  # for getting list of users
    view = browser.find_element_by_class_name("isgrP")
    actionChain = webdriver.ActionChains(browser)
    # for handeling scroll event on dialog
    actionChain.context_click(on_element=view)
    n = len(users)  # no of followers/following in the list
    # while number of followers in the list is less than total number of followers of the user
    while(n < no):
        actionChain.key_down(Keys.SPACE).key_up(
            Keys.SPACE).perform()  # for scrolling down
        users = browser.find_element_by_class_name("PZuss")
        users = users.find_elements_by_css_selector("li")  # selecting users
        n = len(users)  # updating the number of users in the list
    for j in range(len(users)):
        users[j] = users[j].text  # extracting text
    browser.get("https://www.instagram.com/"+insta_id)
    return users  # return array of all the followers/following of the user


def convert_to_csv(followers, following, insta_id):
    '''Takes arrays of followers and following and a username 
    as arguments and creates <username>.csv file to store the data'''
    final_arr = []
    for i in range(0, max(len(followers), len(following))):
        follower_account = ""
        follower_name = ""
        following_account = ""
        following_name = ""
        if(i < len(followers)):
            follower_account = followers[i].split("\n")[0]
            follower_name = followers[i].split("\n")[1]
        if(i < len(following)):
            following_account = following[i].split("\n")[1]
            following_name = following[i].split("\n")[0]
        user = {
            "Follower Account": follower_account,
            "Follower Name": follower_name,
            "Following Account": following_account,
            "Following Name": following_name,
        }
        final_arr.append(user)
    df = pd.DataFrame(final_arr)  # convert to data frame
    df.to_csv(insta_id+".csv", index=None)  # convert to csv


if __name__ == "__main__":
    username = input("Enter your Instagram username: ")
    password = input("Enter your Instagram password: ")
    insta_id = input("Enter user's Instagram username for scraping: ")

    PATH = "C:\Program Files (x86)\chromedriver.exe"  # path to chromedriver
    browser = webdriver.Chrome(PATH)
    browser.implicitly_wait(5)
    browser.get("https://www.instagram.com/")

    username_input = browser.find_element_by_css_selector(
        "input[name='username']")
    password_input = browser.find_element_by_css_selector(
        "input[name='password']")

    # enters username and password
    username_input.send_keys(username)
    password_input.send_keys(password)

    # click on submit button
    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()

    # save password dialog
    not_now_button = browser.find_element_by_xpath(
        "//button[text()='Not Now']")
    not_now_button.click()
    sleep(2)

    # get user's instagram page
    browser.get("https://www.instagram.com/"+insta_id)
    sleep(2)

    try:
        arr = ["followers", "following"]
        followers = get_users("followers", insta_id)
        following = get_users("following", insta_id)
        convert_to_csv(followers, following, insta_id)
    except NoSuchElementException:
        print("Invalid Account/ Private Account")
        pass
