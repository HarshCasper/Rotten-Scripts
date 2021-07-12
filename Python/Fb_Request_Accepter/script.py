from selenium import webdriver
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from pathlib import Path
import os
import time
from selenium.webdriver.chrome.options import Options

option = Options()


# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
env_path = Path(".", ".env")
load_dotenv(dotenv_path=env_path)


def read_creds():

    """This function reads the environmental variables."""

    credentials = {"username": os.getenv("username"), "password": os.getenv("password")}
    return credentials


def aceept_requests_main(browser):
    """function for accepting requests
    Parameter:-
    browser: where task runs
    """
    login(browser)
    time.sleep(7)
    accept_requests(browser)
    print("All Request Accepted")


def login(browser):
    """
    Function to login to Facebook
    Arguments:
    browser: where task runs
    """
    url = "https://www.facebook.com/friends"
    creds = read_creds()
    browser.get(url)
    element_id = browser.find_element_by_css_selector("input#email")
    element_id.send_keys(creds["username"])
    element_id = browser.find_element_by_css_selector("input#pass")
    element_id.send_keys(creds["password"])
    element_id.submit()


def accept_requests(browser):
    """Main function for execution of accepting friend requests"""
    pagesource = browser.page_source
    soup = BeautifulSoup(pagesource, "html.parser")
    confirm_btns = browser.find_elements_by_css_selector("div[aria-label='Confirm']")
    for btn in confirm_btns:
        btn.click()
        time.sleep(2)

    if soup.select_one("div.k4urcfbm.f10w8fjw.pybr56ya.taijpn5t.btwxx1t3.j83agx80.bp9cbjyn") is not None:
        see_more_btn = browser.find_element_by_css_selector(
            "div.k4urcfbm.f10w8fjw.pybr56ya.taijpn5t.btwxx1t3.j83agx80.bp9cbjyn"
        )
        see_more_btn.click()
        time.sleep(12)
        accept_requests(browser)


def main():
    """Main function of execution"""
    browser = webdriver.Chrome(options=option)
    browser.maximize_window()
    aceept_requests_main(browser)


if __name__ == "__main__":
    main()
