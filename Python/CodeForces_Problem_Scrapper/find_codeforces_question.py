import sys
import os
import os.path
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pdfkit

'''
method get_problem()
            - takes parameter url of the problem statement

'''
def get_problem(url):
    path_wkthmltopdf = r"D:\Downloads\pdftohtml\files\wkhtmltopdf\bin\wkhtmltopdf.exe"
    config = pdfkit.configuration(wkhtmltopdf = path_wkthmltopdf)
    pdfkit.from_url(url, 'out.pdf')
    # res = requests.get(url)
    # html_page = res.content
    # soup = BeautifulSoup(html_page, 'html.parser')
    # texts = soup.find("div", class_="problem-statement").get_text()
    # text_file = open("Output.txt", "w", encoding='utf-8')
    # text_file.writelines(texts)
    # text_file.close()
    #driver = webdriver.Chrome("chromedriver_win32\chromedriver.exe")
    try:
        print('successful')
        #driver.get(url)
        #item_ = driver.find_elements_by_xpath('//*[@id="pageContent"]/div[2]/div/div')
        #html = driver.page_source
        #html = driver.execute_script("return document.body.innerHTML;")
        #print(html)

    except:
        print('Unable to fetch from the url')
        return


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
