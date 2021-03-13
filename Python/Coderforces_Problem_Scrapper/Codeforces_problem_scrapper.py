import os
from selenium import webdriver  # Automated webdriver
from PIL import Image
from fpdf import FPDF  # For converting images to pdf


def getproblem():
    Pblm_id = input("Enter the Problem ID: ")
    difficulty = input("Enter the difficulty level: ")
    filename = input('Enter the file name to store Question: ') + '.pdf'

    url = "https://codeforces.com/problemset/problem/" + Pblm_id + "/" + difficulty
    path = 'image.png'
    options = webdriver.ChromeOptions()

    options.headless = True
    driver = webdriver.Chrome("F:/chromedriver.exe", options=options)
    driver.get(url)
    required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    driver.set_window_size(1366, required_height)

    driver.find_element_by_class_name('ttypography').screenshot(path)
    cover = Image.open(path)
    WIDTH, HEIGHT = cover.size
    MARGIN = 10
    pdf = FPDF(unit='pt', format=[WIDTH + 2 * MARGIN, HEIGHT + 2 * MARGIN])
    pdf.add_page()  # Adding new page to the pdf
    pdf.image(path, MARGIN, MARGIN)
    pdf.output(filename, "F")

    print(f'\nGreat Success!!! Check your directory for {filename} file!')


getproblem()
os.remove('image.png')
