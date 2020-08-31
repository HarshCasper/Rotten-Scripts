import sys
import os
import os.path
from selenium import webdriver          #Automated webdriver
from PIL import Image                   #For manipulating images
from fpdf import FPDF                   #For converting images to pdf

'''
method get_problem()
            - takes parameter url of the problem statement
            - using selenium webdriver, it takes a screenshot(with scroll if needed) of the whole problem statement
            - saves it as image.png and send this image path to function convert_image_to_pdf()
'''
def get_problem(url):
    path = 'image.png'
    options = webdriver.ChromeOptions()
    options.headless = True                         #True is required for taking the screenshot with scroll.
    path_to_chromedriver = r"chromedriver_win32\chromedriver.exe"  # path to the chromedriver locally
    driver = webdriver.Chrome(path_to_chromedriver, options=options)
    try:
        driver.get(url)
        required_height = driver.execute_script('return document.body.parentNode.scrollHeight')     #gets the scroll height
        driver.set_window_size(1366, required_height)                                               #sets the window height and width
        driver.find_element_by_class_name('problem-statement').screenshot(path)     #Every article in GeeksForGeeks has article tag
        convert_image_to_pdf(path)
    except:
        print('Unable to fetch from the url')
        return

'''
method convert_image_to_pdf()
            - takes parameter path of the image
            - converts the image to pdf
'''
def convert_image_to_pdf(path):
    cover = Image.open(path)
    width, height = cover.size
    margin = 20
    pdf = FPDF(unit='pt', format=[width + 2*margin, height + 2*margin])     #Setting up the dimensions
    pdf.add_page()                                                          #Adding new page to the pdf
    pdf.image(path, margin, margin)
    pdf_filename = input('Enter the file name: ')+'.pdf'
    pdf.output(pdf_filename, "F")
    print("Success!!")

'''
method main()
            - takes problem code input from the user
            - converts the problem code with the codeforces path and calls function get_problem()
'''
if __name__ == "__main__":
    url = 'https://codeforces.com/problemset/problem/'
    if len(sys.argv)>1:
        problem_code = " ".join(sys.argv[1:])
    else:
        problem_code = input('Enter the problem code: ')

    for i, c in enumerate(problem_code):
        if not c.isdigit():
            url = url + problem_code[0:i] + '/' + problem_code[i:]

    get_problem(url)

    if os.path.isfile('image.png'):
        os.remove('image.png')
