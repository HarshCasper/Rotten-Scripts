# importing the required libraries

import numpy as np
import cv2
import matplotlib.pyplot as plt

%matplotlib inline

# reading the image and then converting the image from BGR to RGB 
# then displaying the image

img = cv2.imread("Asus rog logo.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)

# here also we are reading the image and then converting the image from BGR to RGB 
# then displaying the image

bg = cv2.imread("black wood Background.jpg")
bg = cv2.cvtColor(bg, cv2.COLOR_BGR2RGB)
plt.imshow(bg)

# masking the image

upper_green = (20, 40, 255)
lower_green = (0, 0, 0)

mask = cv2.inRange(img, lower_green, upper_green)

# displaying the masked image

plt.imshow(mask, cmap='gray')

# resizing the masked image, so that both the images can be of same size

bg = cv2.resize(bg, (img.shape[1], img.shape[0]))

bg.shape, img.shape

# created an and operation using bg, img
# b variable is for background image, a variable is for image
# and whenever there will be a mask image it will return 0 otherwise it will return 1 means the image
# after that displaying and saving the final image

b = cv2.bitwise_and(bg, bg, mask=mask)
a = cv2.bitwise_and(img, img, mask=~mask)

plt.imshow(b)
plt.show()
plt.imshow(a)
plt.show()

final_image = cv2.add(a, b)
plt.imsave("Final_image.png", final_image)
plt.imshow(final_image)
plt.show()
