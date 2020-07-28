import numpy as np
import cv2
from PIL import Image
import time

str = input("Please input your message here >>> ")
now = time.time()

img2 = cv2.imread('input.jpg')
shape_original = np.shape(img2)
arr =[]

def two_dim_conv(x):
    for i in x:
        for j in i:
            for k in j:

              arr.append(k)
    return arr
two_dim_conv(img2)
l = len(str)
c=1
for i in range(0,len(arr)):
    if i==0:
        arr[i]=l
        continue
    if c-1<l:
        arr[c]=ord(str[c-1])
        c+=1
    else:
        break
        
arr2= np.reshape(arr,shape_original)
svimg= Image.fromarray(arr2.astype('uint8'))

b, g, r = svimg.split()
svimg = Image.merge("RGB", (r, g, b))

svimg.save('output.png')
print("DONE!")
print("Total time taken: ",end=' ')
print(time.time()-now)




