#!/usr/bin/env python3

#imports
import requests
import urllib

data = requests.get('https://api.imgflip.com/get_memes').json()['data']['memes']
#Data is stored in a JSON format in this URL.

images = [{'name':image['name'],'url':image['url'],'id':image['id']} for image in data]
#List all the memes
print('Here is the list of available memes : \n')
ctr = 1
for img in images:
    print(str(ctr) + " Template: " + img['name'] + '\n' + "URL: " + img['url'])
    ctr = ctr+1
