# All Imports
from selenium import webdriver
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from pathlib import Path
import os
import time

env_path = Path(".", ".env")
load_dotenv(dotenv_path=env_path)


def read_creds():

    """This function reads the environmental variables."""

    credentials = {"username": os.getenv("username"), "password": os.getenv("password")}
    return credentials


def login(browser):

    """This function help in Login to Linkedin.
    Arguments:
    browser: browser where task runs
    """

    linkedin_url = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
    creds = read_creds()
    browser.get(linkedin_url)
    elementID = browser.find_element_by_id("username")
    elementID.send_keys(creds["username"])
    elementID = browser.find_element_by_id("password")
    elementID.send_keys(creds["password"])
    elementID.submit()


def count_notification(browser):
    """This function help in returning the notification count.
    Arguments:
    browser: browser where task runs
    """
    pagesource = browser.page_source
    soup = BeautifulSoup(pagesource, "html.parser")
    if soup.select_one("a[data-test-global-nav-link='notifications'] span.notification-badge__count") is not None:
        element = browser.find_element_by_css_selector(
            "a[data-test-global-nav-link='notifications'] span.notification-badge__count"
        )
        return int(element.text)

    return 0


def wish(browser):
    """This function help in sending wish.
    Arguments:
    browser: browser where task runs
    """
    login(browser)
    time.sleep(2)
    notification_count = count_notification(browser)
    print(notification_count)

    # It check whether there are any new notification or not
    if notification_count == 0:
        # If no new notification then script will not run
        print("Currently there are no new Notifications")
        browser.close()
    else:
        element = browser.find_element_by_css_selector('a[data-test-global-nav-link="notifications"]')
        element.click()
        time.sleep(5)
        # All notification cards
        msg_sent = 0
        elements = browser.find_elements_by_css_selector(".nt-segment__occludable-area.ember-view")
        count = 0
        for element in elements:
            if count >= notification_count:
                break
            count += 1
            element_source = element.get_attribute("innerHTML")
            soup = BeautifulSoup(element_source, "html.parser")

            # Check for button that directs to message box
            if (
                soup.select_one(
                    ".message-anywhere-button.artdeco-button.artdeco-button--secondary.artdeco-button--default"
                )
                is not None
            ):
                wish_btn = element.find_element_by_css_selector(
                    ".message-anywhere-button.artdeco-button.artdeco-button--secondary.artdeco-button--default"
                )

                # If message is regaring birthday
                if "happy birthday" in element.text:
                    wish_text = element.find_element_by_css_selector(".nt-card__text--3-line span.visually-hidden").text
                    date_txt = wish_text.split("(")[1].split(")")[0]

                    # If the day of birthday is not same as of reading notfication
                    if date_txt != "today":
                        # then script will not send message
                        continue
                wish_btn.click()
                time.sleep(2)
                msg_box = browser.find_element_by_css_selector(".msg-overlay-conversation-bubble")
                send_btn = msg_box.find_element_by_css_selector(".msg-form__send-button")
                send_btn.click()
                time.sleep(1)
                clos_btn = msg_box.find_element_by_css_selector(
                    "button[data-control-name='overlay.close_conversation_window']"
                )
                clos_btn.click()
                msg_sent += 1
                print("Send greetings")

        if msg_sent == 0:
            print("Currently No new Notification for any wish")

        browser.close()


def main():
    """Main function of execution"""
    browser = webdriver.Chrome()
    browser.maximize_window()
    wish(browser)


if __name__ == "__main__":
    main()
