
def template():
    import random
    import requests
    import urllib
    index = random.randint(0,100)
    username = 'NamyaLG'
    password = 'Python2312$'
    userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
    #Fetch the available memes
    data = requests.get('https://api.imgflip.com/get_memes').json()['data']['memes']
    images = [{'name':image['name'],'url':image['url'],'id':image['id']} for image in data]
    
    return(images[index]['name'] , images[index]['url'])
