# All Imports
from selenium import webdriver
import datetime
from bs4 import BeautifulSoup
import json
import time



def read_creds(filename):

    """This function reads username and password from credentials.json
    Arguments:
    filename: name of the file which stores the credentials
    :return: returns the credentials 
    """
    
    with open(filename) as f:
        credentials = json.load(f)
    return credentials


def login(browser):

    """This function help in Login to Linkedin.
    Arguments:
    browser: browser where task runs
    """     

    linkedin_url="https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
    creds=read_creds('credentials.json')
    browser.get(linkedin_url)
    elementID=browser.find_element_by_id("username")
    elementID.send_keys(creds['username'])
    elementID=browser.find_element_by_id("password")
    elementID.send_keys(creds['password'])
    elementID.submit()

def count_notification(browser):
    """This function help in returning the notification count.
    Arguments:
    browser: browser where task runs
    """   
    pagesource=browser.page_source;
    soup=BeautifulSoup(pagesource,'html.parser')
    if soup.find("span",class_="notification-badge__count")!=None :
        element=browser.find_element_by_css_selector("span.notification-badge__count");
        return int(element.text);
    else:
        return 0;


def wish(browser):
    """This function help in sending wish.
    Arguments:
    browser: browser where task runs
    """   
    login(browser)
    time.sleep(2)
    notification_count=count_notification(browser)

    # It check whether there are any new notification or not
    if notification_count==0:
        #If no new notification then script will not run
        print("Currently there are no new Notifications");
        browser.close()
    else:
        element =browser.find_element_by_css_selector('a[data-test-global-nav-link="notifications"]');
        element.click();
        time.sleep(5);
        # All notification cards
        elements=browser.find_elements_by_css_selector(".nt-card")
        count=0
        for element in elements:
            if count>=notification_count:
                break
            count+=1
            element_source=element.get_attribute('innerHTML')
            soup=BeautifulSoup(element_source,'html.parser')
            
            # Check for button that directs to message box
            if soup.select_one(".message-anywhere-button.artdeco-button.artdeco-button--secondary.artdeco-button--default")!=None:     
                wish_btn=element.find_elements_css_selector(".message-anywhere-button.artdeco-button.artdeco-button--secondary.artdeco-button--default")[0]
                
                # If message is regaring birthday
                if "happy birthday" in element.text:
                    wish_text=element.find_elements_by_css_selector(".nt-card__text--3-line span.visually-hidden")[0]
                    date_txt=wish_text.split("(")[1].split(")")[0];
                    current_date=datetime.datetime.now().strftime("%b %d").lstrip("0").replace(" 0", " ")

                    # If the day of birthday is not same as of reading notfication
                    if date_txt!=current_date:
                        # then script will not send message
                        continue
                wish_btn.click()
                time.sleep(2)
                msg_box=browser.find_element_by_css_selector(".msg-overlay-conversation-bubble")
                send_btn=msg_box.find_elements_by_css_selector(".msg-form__send-button")[0]
                send_btn.click()
                time.sleep(1)
                clos_btn=msg_box.find_elements_by_css_selector("button[data-control-name='overlay.close_conversation_window']")[0]
                clos_btn.click()
                print("Send greetings")

            

        browser.close()        



def main():
    browser = webdriver.Chrome()
    browser.maximize_window()
    wish(browser)



if __name__ == "__main__":
    main()