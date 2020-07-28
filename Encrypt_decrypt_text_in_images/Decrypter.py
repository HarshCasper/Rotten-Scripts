import cv2
import numpy as np
import time

now = time.time()
img2 = cv2.imread('output.png')

str=''
arr=[]
arr1 =[]
c=0
def two_dim_conv(x):
    c=0
    for i in x:
        for j in i:
            for k in j:
                if c>img2[0][0][0]:
                    break
                arr.append(k)
                c+=1
    return arr

two_dim_conv(img2)
l = arr[0]
string_arr = arr[1:l+1]

for i in string_arr:
    str += chr(i)

print(str)
print("Intercercepted message length >>> ",end=' ')
print(img2[0][0][0])
print("Total time taken to Decode >>> ",end=' ')
print(time.time()-now)
