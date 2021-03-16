import os
from selenium import webdriver  # Automated webdriver
from PIL import Image
from fpdf import FPDF  # For converting images to pdf

"""
getproblem() : It takes input from the user of codeforces problemID and difficulty
level and then by using selenium and chrome webdriver, capturing screenshot of the
Codeforces problem using ttypography tag because all the problems of codeforces are
stored inside this div tag and saving it in a image.png file.
Then saving the image.png as pdf file by using fdf library.
"""


def getproblem():
    Pblm_id = input("Enter the Problem ID: ")
    difficulty = input("Enter the difficulty level: ")
    filename = input('Enter the file name to store Question: ') + '.pdf'

    url = "https://codeforces.com/problemset/problem/" + Pblm_id + "/" + difficulty
    path = 'image.png'
    options = webdriver.ChromeOptions()

    options.headless = True
    driver = webdriver.Chrome(r"chromedriver_win32\chromedriver.exe", options=options)
    driver.get(url)
    required_height = driver.execute_script(
                        'return document.body.parentNode.scrollHeight')
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


if __name__ == "__main__":
    getproblem()
    os.remove('image.png')
