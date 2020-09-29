# Importing libraries
import cv2
import numpy as np
from PIL import Image

# Taking input from the user
filename = input("Enter the file name: ")
img = Image.open(filename)
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
original = np.array(original, dtype=np.uint8)
original = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
cv2.imshow("original", original)
cv2.imshow("sepia", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
