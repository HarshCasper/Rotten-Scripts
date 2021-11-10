import sys
import os
import urllib.request  # Working with urls. This scripts uses it for downloading images
import shutil  # Allows file/folder operations
from selenium import webdriver  # Web scrapper to extract urls
from fpdf import FPDF  # To convert images to PDF
from PIL import Image  # For image manipulation


def get_image_urls_list(url):
    print("Getting individual slide urls...")
    driver = webdriver.Chrome(
        r"chromedriver_win32\chromedriver.exe"
    )  # Web driver loaded
    driver.get(url)
    url_list = []
    for image in driver.find_elements_by_class_name("slide_image"):
        try:
            # 'data-full' contains the url of the image
            url_path = image.get_attribute("data-full")
            url_list.append(url_path)
        except Exception as e:
            print(e)
            return
    print("The urls have been stored. Closing web-driver...")
    driver.close()
    download_individual_image(url_list)


def download_individual_image(url_list):
    print("Downloading individual images...")
    os.mkdir("new_folder")
    os.chdir(os.path.join(os.getcwd() + "/new_folder"))
    image_paths = []
    for i, url in enumerate(url_list):
        filename = str(i) + ".jpg"
        # downloads image from url with filename to current directory
        urllib.request.urlretrieve(url, filename)
        image_paths.append(os.getcwd() + "/" + filename)
    print("Download complete.")
    convert_images_to_pdf(image_paths)


def convert_images_to_pdf(image_paths):
    print("Converting all images into a PDF file")
    cover = Image.open(image_paths[0])
    width, height = cover.size
    margin = 10
    # initializes a pdf file with units=points and dimensions
    pdf = FPDF(unit="pt", format=[width + 2 * margin, height + 2 * margin])
    for path in image_paths:
        pdf.add_page()  # Adding new page to the pdf
        pdf.image(path, margin, margin)  # Appending the image in the new page
    os.chdir("..")
    pdf_filename = input("Enter the file name: ") + ".pdf"
    pdf.output(pdf_filename, "F")
    print("Success!!")


if __name__ == "__main__":
    if len(sys.argv) > 1:  # Get the url of the site from where you want to download
        url = " ".join(sys.argv[1:])
    else:
        url = input("Enter the URL: ")
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    get_image_urls_list(url)
    shutil.rmtree("new_folder")
