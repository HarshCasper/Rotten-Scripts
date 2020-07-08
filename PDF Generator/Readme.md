# PDF Generator

A simple Python Script to generate PDF using Images and vice-versa.

## *.jpg to output_filename.pdf convertor

- Change `output_filename.pdf` with the name of the output pdf file you want
- `os.listdir('.')` points to the present working directory, change it to `os.listdir('the/directory/path/where/you/want/to/get/images/from')`
- Change `i.endswith(".jpg")` to your desired input image format

## file.pdf to output_images_folder_name/page_no.jpg convertor

- Change `file.pdf` to the name of the file you want to convert to images
- Change `output_images_folder_name/page_{}.jpg` to `folder_name_that_stores_the_output_images/output_image_name_{}.jpg`
- `{}` should not be removed if you want to store the page no. with the output image name so that you don't loose track of different pages