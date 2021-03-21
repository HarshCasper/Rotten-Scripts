import cv2
import numpy as np
import pandas as pd
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True)
args = vars(ap.parse_args())
img_path = args['image']
img = cv2.imread(img_path)


clicked = False

index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('colors.csv', names=index)


# following code finds the closest colour to the clicked colour 
def getColor(R,G,B):
    minimum = 1000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname


def click_event(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global blue,green,red, clicked
        clicked = True
        blue=int(img[y,x,0])
        green=int(img[y,x,1])
        red=int(img[y,x,2])
       
cv2.namedWindow('image')
cv2.setMouseCallback('image',click_event)

while(1):

    cv2.imshow("image",img)
    if (clicked):
    
        cv2.rectangle(img,(20,20), (750,60), (blue,green,red), -1)

        text = getColor(red,green,blue) 

        cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)    
        clicked=False

# to quit the window click q
    if cv2.waitKey(1) == ord('q'):
        break
    
cv2.destroyAllWindows()
