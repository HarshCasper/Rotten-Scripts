import requests
from PIL import Image
def img_requests(txt):
    response=requests.get("https://source.unsplash.com/random/{0}".format(txt))
    file=open('sample_image.jpg','wb')
    file.write(response.content)
    img=Image.open(r"container.jpg")
    img.show()
    file.close
def img_random(txt):
    response=requests.get("https://source.unsplash.com/random?{0}".format(txt))
    file=open('sample_image.jpg','wb')
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
if choice==1:
    img_requests('1280x720')
    print("Please wait while we fetch the images from our database.")
elif choice==2:
    img_requests('1920x1080')
    print("Please wait while we fetch the images from our database.")
elif choice==3:
    img_requests('2048x1080')
    print("Please wait while we fetch the images from our database.")
elif choice==4:
    img_requests('4096x2160')
    print("Please wait while we fetch the images from our database.")
elif choice==5:
    st=input("Enter keywords seperated by commas ")
    print("Please wait while we fetch the images from our database.")
    img_random(st)
else:
    print("Please provide a valid Input")
