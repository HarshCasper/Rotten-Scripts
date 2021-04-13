'''
    SIFT(Scale Invariant Feature Transform) Algorithm for the feature detection.
    This algorithm is patented, so this algorithm is included in the Non-free module in OpenCV.
'''

#Importing required libraries
import cv2
import numpy as np

# Load the image
path=input("Enter the path of the image: ")
image = cv2.imread(path)

# Convert the image to RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert the image to gray scale
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

#Display the input image
cv2.imshow('Input image.jpg',image)

#Detect keypoints and Create Descriptor
sift = cv2.xfeatures2d.SIFT_create()

kp, dp = sift.detectAndCompute(gray, None)

img=cv2.drawKeypoints(gray,kp,flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Print the number of keypoints detected in the image
print("Number of Keypoints Detected In The Image: ", len(kp))

#Display the final output image
cv2_imshow('sift_keypoints.jpg',img)
cv.waitKey(0)
cv.destroyAllWindows()
