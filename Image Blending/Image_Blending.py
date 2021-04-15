'''
    For using this script, you need to install OpenCV in your machine
'''

#importing opencv library
import cv2 as cv

#Taking input for path
path=input("Enter the path of the image 1")
img1=cv.imread(path)
path=input("Enter the path of the image 2")
img2=cv.imread(path)

#Performing the blending operation
img1=cv.resize(img1,(400,400))
img2=cv.resize(img2,(400,400))
#You can replace the value (0.3,0.7) for setting transparency of an image.
#Keep it in between[0.0,1.0] 
blend_image=cv.addWeighted(img1,0.2,img2,0.7,0)

#Display the images
cv.imshow(img1)
cv.imshow(img2)
cv.imshow(blend_image)

#Saving the image.
cv.imwrite('/Blended_image.png',blend_image)

cv.waitkey(0)
cv.destroyAllWindows()
