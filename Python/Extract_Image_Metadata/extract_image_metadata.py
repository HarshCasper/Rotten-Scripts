# Script to extract image metadata with Python


# Significant amounts of hidden data are recorded whenever you take a picture with a digital camera or a smartphone.
# Photo metadata is a set of data describing and providing information about rights and administration of an image.
# This data is also called EXIF metadata.

import os
from PIL import Image
# Importing Pillow Python Imaging Library:that adds support for opening, manipulating, and saving many different image file formats.
from PIL.ExifTags import TAGS
# importing required modules

# print(TAGS) checking if libraries are imported or not which basically returns a key value pairs of all the metadata.

# Enter your Image here
# This image is copyrighted under © 2010 Hartswood Films.
image_file = 'image.jpg'

# on execution an object of Image type is returned and stored in image_file variable.

try:
    image = Image.open(image_file)
except IOError:
    pass
# raise an IOError if file cannot be found,or the image cannot be opened.

# dictionary to store metadata keys and value pairs.
exif = {}

# iterating over the dictionary
for tag, value in image._getexif().items():

    # extarcting all the metadata as key and value pairs and converting them from numerical value to string values
    if tag in TAGS:
        exif[TAGS[tag]] = value

# checking if image is copyrighted
try:
    if 'Copyright' in exif:
        print("Image is Copyrighted, by ", exif['Copyright'])
except KeyError:
    pass

print()
print("Displaying all the metadatas of the image: \n")
print(exif)
