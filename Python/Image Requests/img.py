import requests
from PIL import Image

def img_requests(txt):#this function will help the driver code to provide images with keywords.
    response=requests.get("https://source.unsplash.com/random/{0}".format(txt))
    file=open('container.jpg','wb')
    file.write(response.content)
    img=Image.open(r"container.jpg")
    img.show()
    file.close

def img_random(txt):#this function will help the driver code to provide random images.
    response=requests.get("https://source.unsplash.com/random?{0}".format(txt))
    file=open('container.jpg','wb')
    file.write(response.content)
    img=Image.open(r"container.jpg")
    img.show()
    file.close

choice=int(input("""Please provide an option for Image
1.HD Random Picture
2.FHD Random Picture
3.2K Random Picture
4.4k Random Picture
5.Picture with User Keywords """))

print("Please wait while we fetch the images from our database.")

#checking the user's choice.

if choice==1:
    img_requests('1280x720')
elif choice==2:
    img_requests('1920x1080')
elif choice==3:
    img_requests('2048x1080')
elif choice==4:
    img_requests('4096x2160')
elif choice==5:
    st=input("Enter keywords seperated by commas ")
    img_random(st)
else:
    print("Please provide a valid Input")
