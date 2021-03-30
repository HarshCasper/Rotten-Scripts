import cv2,sys
import numpy as np

if __name__ == '__main__':

	# the image that needs to be scanned
	filename= sys.argv[1]
	im = cv2.imread(filename)
	# convert to gray
	im = im/255.0
	# enhance the image to scan it
	scannedImage = cv2.pow(im,2.0)
	cv2.imshow('Original Image',im)
	cv2.imshow('Scanned Image',scannedImage)
	
	# scannedImageFile= filename.split('.')[0]+'_scanned.jpeg'
	# print (scannedImageFile)
	# cv2.imwrite(scannedImageFile, scannedImage)
	cv2.waitKey(0)
