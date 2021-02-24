#Import required Image library
from PIL import Image, ImageDraw, ImageFont

#Create an Image Object from an Image
path = '/content/sky.jpg' #main image path
img = Image.open(path)
width, height = img.size

draw = ImageDraw.Draw(img)
text = "©Madhurima.photography" #text on image to add

font = ImageFont.truetype("/content/JMH Typewriter-Thin.ttf", 50)
textwidth, textheight = draw.textsize(text,font=font)

# calculate the x,y coordinates of the text
margin = 5
x = width - textwidth - margin
y = height - textheight - margin

# draw watermark in the bottom right corner
draw.text((x, y), text,font=font, fill ="white")
#img.show()

#Save watermarked image
img.save('watermark.png')