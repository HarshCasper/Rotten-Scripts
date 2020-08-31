# Python Code to implement Invisible Cloak

import cv2
import time
import numpy as np

## Preparation for writing the ouput video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0, (640,480))

##reading from the webcam 
cap = cv2.VideoCapture(0)

## Allow the system to sleep for 3 seconds before the webcam starts
time.sleep(3)
count = 0
background = 0

## Capture the background in range of 60
for i in range(60):
    ret,background = cap.read()
background = np.flip(background,axis=1)


## Read every frame from the webcam, until the camera is open
while(cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break
    count+=1
    img = np.flip(img,axis=1)
    
    ## Convert the color space from BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    ## Generat masks to detect red color
    lower_red = np.array([0,100,0])
    upper_red = np.array([9,255,255])
    mask1 = cv2.inRange(hsv,lower_red,upper_red)

    lower_red = np.array([170,100,00])
    upper_red = np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lower_red,upper_red)

    mask1 = mask1+mask2

    ## Open and Dilate the mask image
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3),np.uint8))
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3,3),np.uint8))
 
 
    ## Create an inverted mask to segment out the red color from the frame
    mask2 = cv2.bitwise_not(mask1)
 
 
    ## Segment the red color part out of the frame using bitwise and with the inverted mask
    res1 = cv2.bitwise_and(img,img,mask=mask2)

    ## Create image showing static background frame pixels only for the masked region
    res2 = cv2.bitwise_and(background, background, mask = mask1)
 
 
    ## Generating the final output and writing
    finalOutput = cv2.addWeighted(res1,1,res2,1,0)
    out.write(finalOutput)
    cv2.imshow("magic",finalOutput)
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
