
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
from openpyxl import Workbook
from datetime import datetime

d=datetime.now()
dt = str(d.hour) + d.strftime("%d-%m-%y")

# CREDENTIALS  
bot_email = "enter the bot email here"                                 # enter the email address created for the bot
bot_password = "enter the bot password here"                        # enter the password for login into that google account


val  = input("enter the meeting code :")    # enter the meeting link

# setting soem chrome options
opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")

opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 2,
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 2
    })

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=opt)
driver.get("https://meet.google.com")

# loggin in to the google account
signin = driver.find_element(By.XPATH,'//*[@id="drawer"]/div/div[3]/div[1]/div/span[1]/a')
signin.click()
em = driver.find_element(By.ID,'identifierId')
em.send_keys(bot_email)
em.send_keys(Keys.RETURN)
time.sleep(2)
pas = driver.find_element(By.NAME,'password')
pas.send_keys(bot_password)
pas.send_keys(Keys.RETURN)

# typing the meeting link
wait = WebDriverWait(driver,30)
mlink = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="i3"]')))
mlink.click()
mlink.send_keys(val)
mlink.send_keys(Keys.RETURN)

# waiting for the dismiss banner to appear 
wait = WebDriverWait(driver,30)
dismiss = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#yDmH0d > div.llhEMd.iWO5td > div > div.g3VIld.vdySc.Up8vH.J9Nfi.iWO5td > div.XfpsVe.J9fJmf > div > span')))
dismiss.click()


# clicking the join button
wait = WebDriverWait(driver,30)
join = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span')))
join.click()


# accessing the members area to find how many peple are in the class
wait = WebDriverWait(driver,60)
members = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#ow3 > div.T4LgNb > div > div:nth-child(9) > div.crqnQb > div.DAQYgc.xPh1xb.P9KVBf > div.MaVIwe > div.Ok4Bg > div > div > div:nth-child(2) > span > button > i.google-material-icons.VfPpkd-kBDsod.NtU4hc')))
members.click()
time.sleep(2)


lst = []
names = driver.find_elements(By.CLASS_NAME, 'zWGUib')
for nm in names:
    lst.append(nm.text)
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, '#ow3 > div.T4LgNb > div > div:nth-child(9) > div.crqnQb > div.DAQYgc.xPh1xb.P9KVBf > div.rceXCe > div > div.NHaLPe.CoOyx > span > button > i').click()

wb = Workbook()                # creating a excel workbook to save the contents of the list
sh = wb.create_sheet("Attendence")

for i,name in enumerate(lst):
     sh.append((name,))                     #inserting the contents of the list in the excel sheet


path = os.path.expanduser('~')
spath = path + '\\Desktop\\' + f'attendence-{dt}.xlsx'               # path to save the file

wb.save(spath)
print("Attendence recorded succesfully :) ")