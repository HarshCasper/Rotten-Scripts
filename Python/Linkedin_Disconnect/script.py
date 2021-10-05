from selenium import webdriver
from bs4 import BeautifulSoup
import json
import time
from selenium.webdriver.common.by import By


def read_creds(filename):

    """This function reads username and password from creddentials.json
    Arguments:
    filename: name of the file which stores the credentials
    :return: returns the credentials
    """

    with open(filename) as f:
        credentials = json.load(f)
    return credentials


def get_Users(filename):

    """This function reads users from disconnected_users.json
    Arguments:
    filename: name of the file which stores the users
    :return: returns the user(list)
    """

    with open(filename) as f:
        userjson = json.load(f)

    return userjson["users"]


def username_disconnected(browser):

    """This function disconnect the user from Linkedin Provided with Linkedin Username.
    Arguments:
    browser: browser where task runs
    """

    login(browser)
    Users = get_Users("disconnected_users.json")

    profile_url = "https://www.linkedin.com/in/"

    for user in Users:
        browser.get(profile_url + user)
        time.sleep(1)
        pagesource = browser.page_source
        soup = BeautifulSoup(pagesource, "html.parser")
        element = browser.find_element_by_css_selector(
            'span[aria-label="More actions"]'
        )
        element.click()
        if soup.find("div", {"data-control-name": "disconnect"}) is not None:
            element = browser.find_element_by_css_selector(
                'div[data-control-name="disconnect"]'
            )
            element.click()
            print(f"Disconnected User {user}")

        if soup.find("div", {"data-control-name": "unfollow"}) is not None:
            element = browser.find_element_by_css_selector(
                'div[data-control-name="unfollow"]'
            )
            element.click()
            print(f"Unfollowed User {user}")

    print("Connections Disconnected")

    browser.close()


def profilename_disconnected(browser):

    """This function disconnect the user from Linkedin Provided with their Profile Name.
    Arguments:
    browser: browser where task runs
    """

    login(browser)
    linkedin_connection_url = (
        "https://www.linkedin.com/mynetwork/invite-connect/connections/"
    )
    browser.get(linkedin_connection_url)
    time.sleep(1)
    Users = get_Users("disconnected_users.json")
    for user in Users:
        elementId = browser.find_element_by_id("mn-connections-search-input")
        elementId.send_keys(user)
        time.sleep(1)
        removed_btn = browser.find_element_by_css_selector(
            ".mn-connection-card__action-container button.artdeco-button--circle"
        )

        removed_btn.click()
        time.sleep(2)
        element = browser.find_element_by_css_selector(
            "div.artdeco-dropdown__content-inner"
        )
        element.click()
        time.sleep(2)
        element = browser.find_elements_by_css_selector(
            'div[role="alertdialog"] span.artdeco-button__text'
        )[2]
        element.click()
        print(f"Disconnected the User {user}")

    print("Connections Disconnected")
    browser.close()


def login(browser):

    """This function help in Login to Linkedin.
    Arguments:
    browser: browser where task runs
    """

    linkedin_url = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
    creds = read_creds("credentials.json")
    browser.get(linkedin_url)
    elementID = browser.find_element_by_id("username")
    elementID.send_keys(creds["username"])
    elementID = browser.find_element_by_id("password")
    elementID.send_keys(creds["password"])
    elementID.submit()


def main():

    print("Welcome To This Amazing Script🥳\n")
    print(
        "If You have Added Profile Name of User Enter choice 1 or if you have added Linkedin-username of User Enter Choice 2"
    )
    choice = input("Enter Choice:- ")
    browser = webdriver.Chrome()
    browser.maximize_window()
    if int(choice) == 2:
        username_disconnected(browser)
    else:
        profilename_disconnected(browser)


if __name__ == "__main__":
    main()
