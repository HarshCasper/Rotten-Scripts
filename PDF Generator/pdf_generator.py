import os
import img2pdf

'''
- Change "output_filename.pdf" with the name of the output pdf file you want
- "os.listdir('.')" points to the present working directory, change it to "os.listdir('the/directory/path/where/you/want/to/get/images/from')"
- Change "i.endswith(".jpg")" to your desired input image format
'''

with open("output_filename.pdf", "wb") as f:
    f.write(img2pdf.convert([i for i in os.listdir('.') if i.endswith(".jpg")]))