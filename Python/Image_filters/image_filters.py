#This script implements convolution over images.
#This can be used to apply filters to images.

#Imports

import numpy as np
from PIL import Image
import cv2

#size of image
width = 300
height = 360

#kernels or image filters
#This is to blur the image, experiment with different values, each of the streams can have different values
'''b_kernel = np.array([0.11 , 0.11 , 0.11 , 0.11 , 0.11 , 0.11 , 0.11 , 0.11 , 0.11]).reshape(3,3)
r_kernel = np.array([0.11 , 0.11 , 0.11 , 0.11 , 0.11 , 0.11 , 0.11 , 0.11 , 0.11]).reshape(3,3)
g_kernel = np.array([0.11 , 0.11 , 0.11 , 0.11 , 0.11 , 0.11 , 0.11 , 0.11 , 0.11]).reshape(3,3)
'''
print("Enter 9 values for each of the streams")
b_kernel = np.array(list(map(int, input("Enter the kernel to be applied to the blue stream").split()))).reshape(3,3)
r_kernel = np.array(list(map(int, input("Enter the kernel to be applied to the red stream").split()))).reshape(3,3)
g_kernel = np.array(list(map(int, input("Enter the kernel to be applied to the green stream").split()))).reshape(3,3)

#Image is read and resized

img = cv2.imread('path to image')
img = cv2.resize(img, (width , height))

#The pixels are extracted from the image
pixels = []
for i in range(height):
      for j in range(width):
              pixels.append(img[i,j])

              #The RGB streams are stored in different arrays to facilitate the process of convolution
              b = []
              g = []
              r = []

              for i in pixels:
                b.append(i[0])
                g.append(i[1])
                r.append(i[2])

#Each of the streams are resized
r = np.array(r).reshape(height, width)
b = np.array(b).reshape(height, width)
g = np.array(g).reshape(height, width)

#function to apply convolution or multiply kernels
def convolute(arr , height , width ,kernel):
      convoluted_matrix = []
      for i in range(1,height-2):
          for j in range(1,width-2):
            temp = arr[i:i+3 , j:j+3]
            prod = np.multiply(temp,kernel)
            convoluted_matrix.append(np.sum(prod))

      convoluted_matrix = (np.array(convoluted_matrix).reshape(height-3,width-3))
      return(convoluted_matrix)

r_convol = convolute(r, height, width, r_kernel)
g_convol = convolute(g, height, width, g_kernel)
b_convol = convolute(b, height, width, b_kernel)


width = width - 3
height = height - 3

combine = np.zeros([height, width, 3], dtype=np.uint8)

for i in range(height):
      for j in range(width):
            combine[i ,j] = [int(r_convol[i][j]) , int(g_convol[i][j]) , int(b_convol[i][j])]


#The 3 matrices or streams are combined, and stored
img = Image.fromarray(combine)
img.save('Funkyfilter.jpg')


