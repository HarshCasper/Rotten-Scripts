from PIL import Image

import os, sys

path = "/root/Desktop/python/images/"

dirs = os.listdir( path )

def resize():

    for item in dirs:

        if os.path.isfile(path+item):

            im = Image.open(path+item)

            f, e = os.path.splitext(path+item)

            imResize = im.resize((200,200), Image.ANTIALIAS)

            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)

resize()
