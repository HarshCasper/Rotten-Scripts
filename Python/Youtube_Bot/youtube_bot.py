__author__ = 'Sri Manikanta'
__date__ = '22-07-2020'

import time
import argparse
from selenium import webdriver

refreshTime = 20

browser = webdriver.Chrome("PATH_OF_YOUR_CHROME_DRIVER")

parser = argparse.ArgumentParser()

parser.add_argument("-l", "--videoLink", required=True,
                    help="Youtube Video link")
parser.add_argument('-vc', "--viewsCount", required=True,
                    help="number of views want to increase")
args = vars(parser.parse_args())

viewsCount = int(args['viewsCount'])

while viewsCount != 0:
    browser.get(args['videoLink'])
    time.sleep(refresh_time)
    count -= 1

browser.close()
