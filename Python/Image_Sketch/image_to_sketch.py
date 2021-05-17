# Converting Image to Pencil Sketch

from google.colab.patches import cv2_imshow
import cv2
import numpy as np
import urllib.request

req = urllib.request.urlopen('https://i.imgur.com/psq5aL2.jpg')
arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
img = cv2.imdecode(arr, -1)  # getting our image
cv2_imshow(img)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # applying grayscale
cv2_imshow(img_gray)

img_invert = cv2.bitwise_not(img_gray)   # inverting image
cv2_imshow(img_invert)

img_smoothing = cv2.GaussianBlur(img_invert, (931, 931),sigmaX=0, sigmaY=0)  # blurring by applying Gaussian filter to the inverted image
cv2_imshow(img_smoothing)

def dodgeV2(x, y):                                  # dodging and merging
    return cv2.divide(x, 255 - y, scale=256)

# getting our sketch
final_img = dodgeV2(img_gray, img_smoothing)
cv2_imshow(final_img)

# Our pencil sketch is ready!!