from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


options = Options()
options.add_argument("--headless")   #Comment this out when running on remote server
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--autoplay-policy=no-user-gesture-required")

driver = webdriver.Chrome(options=options)

try:
    # Go to Simplilearn website
    driver.get(
        "https://accounts.simplilearn.com/user/login?redirect_url=https%3A%2F%2Flms.simplilearn.com%2F"
    )
    time.sleep(8)  # Wait for the page to load

    #Login
    email_field = driver.find_element(By.NAME, 'user_login')
    email_field.send_keys("rohitr9832@gmail.com")  #remove square bracs

    password_field = driver.find_element(By.NAME, 'user_pwd')
    password_field.send_keys("Eren8653")  #remove square bracs
    time.sleep(4);

    # Click the login button
    login_submit = driver.find_element(By.NAME, 'btnlogin')
    login_submit.click()
    time.sleep(20)

    #Click Continue Learning
    driver.find_element(By.CSS_SELECTOR, "button.btn.prime.custom_button_ep.ng-star-inserted").click()
    time.sleep(15)

    #Click the self learning
    driver.find_element(By.CSS_SELECTOR, "p.osl-section-name[title='Self learning']").click()
    time.sleep(5)

    print("Watching the video..")
    # At this point, the video should be playing.
    # The script won't exit, so it will stay connected as long as it's running.

    while True:
        # This loop keeps the script running so the browser stays active
        time.sleep(30)

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the browser
    driver.quit()
