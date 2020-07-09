#!/usr/bin/env python3

#imports
import urllib
import requests # to get image from the web
import shutil # to save it locally

#The shutil module can be downloaded by pip install pytest-shutil

data = requests.get('https://api.imgflip.com/get_memes').json()['data']['memes']
#Data is stored in a JSON format in this URL.

images = [{'name':image['name'],'url':image['url'],'id':image['id']} for image in data]
#List all the memes
print('Here is the list of available memes : \n')
ctr = 1
for img in images:
    print(str(ctr) + " Template: " + img['name'] + '\n' + "URL: " + img['url'])
    image_url = img['url']
    filename = image_url.split("/")[-1]
    # Open the url image, set stream to True, this will return the stream content.
    req = requests.get(image_url, stream = True)

    # Check if the image was retrieved successfully
    if req.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        req.raw.decode_content = True
            
                # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(req.raw, f)
            print('Image sucessfully Downloaded: ',filename)
        else:
            print('Image Couldn\'t be retreived')
    ctr = ctr+1

#This prints the image template and downloads the image into the local machine
