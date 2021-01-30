import cv2
import numpy as np
from matplotlib import pyplot as plt
import tkinter as tk 
from tkinter import filedialog 
root = tk.Tk() 
root.withdraw() 
file_path = filedialog.askopenfilename()


img = cv2.imread(file_path,0)
edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()

