# Importing libraries
import cv2
import numpy as np

img = cv2.imread('taj_mahal.jpg')
original = img.copy()
# Converting into float
img = np.array(img, dtype=np.float64)
# Multipying image with special sepia matrix
img = cv2.transform(img, np.matrix([[0.272, 0.534, 0.131],
                                    [0.349, 0.686, 0.168],
                                    [0.393, 0.769, 0.189]]))
img[np.where(img > 255)] = 255
# Converting into integer again
img = np.array(img, dtype=np.uint8)
cv2.imshow("original", original)
cv2.imshow("sepia", img)
cv2.waitKey(0)
cv2.destroyAllWindows()