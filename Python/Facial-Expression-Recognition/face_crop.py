
import cv2
import os


#------------------------------------------------------------------------------

##Make changes to these lines for getting the desired results.

## DIRECTORY of the images
directory = "#"

## directory where the images to be saved:
f_directory = "#"

#------------------------------------------------------------------------------
            
def facecrop(image):
    facedata = "haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(facedata)

    img = cv2.imread(image)

    try:
    
        minisize = (img.shape[1],img.shape[0])
        miniframe = cv2.resize(img, minisize)

        faces = cascade.detectMultiScale(miniframe)

        for f in faces:
            x, y, w, h = [ v for v in f ]
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

            sub_face = img[y:y+h, x:x+w]

            f_name = image.split('/')
            f_name = f_name[-1]

            ## Change here the Desired directory.
            cv2.imwrite(f_directory + f_name, sub_face)
            print ("Writing: " + image)

    except:
        pass

if __name__ == '__main__':
    images = os.listdir(directory)
    i = 0
    
    for img in images:
        file = directory + img
        print (i)
        facecrop(file)
        i += 1
