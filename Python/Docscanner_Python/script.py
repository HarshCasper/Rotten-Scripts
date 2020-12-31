import cv2
import numpy as np

filename=input('enter file name : ')
image=cv2.imread(filename,0)
th1=cv2.adaptiveThreshold(image,250,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
		cv2.THRESH_BINARY,145,20)

cv2.imwrite('output.jpg',th1)
