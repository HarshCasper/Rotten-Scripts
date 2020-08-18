from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pandas as pd


def get_users(user_type, insta_id):
    button = browser.find_element_by_css_selector(
        "a[href='/"+insta_id+"/"+user_type+"/']")
    no = (int)(button.text.strip().split()[0])
    print(no)
    button.click()
    users = browser.find_element_by_class_name("PZuss")
    users = users.find_elements_by_css_selector("li")
    view = browser.find_element_by_class_name("isgrP")
    actionChain = webdriver.ActionChains(browser)
    actionChain.context_click(on_element=view)
    n = len(users)
    while(n < no):
        actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
        users = browser.find_element_by_class_name("PZuss")
        users = users.find_elements_by_css_selector("li")
        n = len(users)
    for j in range(len(users)):
        users[j] = users[j].text
    browser.get("https://www.instagram.com/"+insta_id)
    return users


def convert_to_csv(followers, following, insta_id):
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
    df = pd.DataFrame(final_arr)
    df.to_csv(insta_id+".csv", index=None)


if __name__ == "__main__":
    username = input("Enter your Instagram username: ")
    password = input("Enter your Instagram password: ")
    insta_id = input("Enter user's Instagram username for scraping: ")

    PATH = "C:\Program Files (x86)\chromedriver.exe"
    browser = webdriver.Chrome(PATH)
    browser.implicitly_wait(5)
    browser.get("https://www.instagram.com/")

    username_input = browser.find_element_by_css_selector(
        "input[name='username']")
    password_input = browser.find_element_by_css_selector(
        "input[name='password']")

    username_input.send_keys(username)
    password_input.send_keys(password)

    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()

    not_now_button = browser.find_element_by_xpath(
        "//button[text()='Not Now']")
    not_now_button.click()
    sleep(2)

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
