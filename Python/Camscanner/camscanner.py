import sys,cv2
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    # the image that needs to be scanned
    filename= sys.argv[1]

    img= cv2.imread(filename)
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    thresh1 = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    cv2.imwrite('try1.jpg',thresh1)

    thresh2 = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 31, 3)
    cv2.imwrite('try2.jpg',thresh2)

    thresh3 = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 13, 5)
    cv2.imwrite('try3.jpg',thresh3)

    thresh4 = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 4)
    cv2.imwrite('try4.jpg',thresh4)

    thresh5 = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    cv2.imwrite('try5.jpg',thresh5)

    thresh6 = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 31, 5)
    cv2.imwrite('try6.jpg',thresh6)

    thresh7 = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21,5 )
    cv2.imwrite('try7.jpg',thresh7)

    thresh8 = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 5)
    cv2.imwrite('try8.jpg',thresh8)


    cv2.waitKey(0)
    cv2.destroyAllWindows()