import os
import img2pdf
from pdf2image import convert_from_path

# *.jpg to output_filename.pdf convertor
with open("output_filename.pdf", "wb") as f:
    f.write(img2pdf.convert([i for i in os.listdir('.') if i.endswith(".jpg")]))

# file.pdf to output_images_folder_name/page_no.jpg convertor
pages = convert_from_path('file.pdf', 500)
page_no = 1
for page in pages:
    pages[i].save('output_images_folder_name/page_{}.jpg'.format(page_no), 'JPEG')      # output_images_folder_name = folder needs to be created manually to store all images
    page_no += 1