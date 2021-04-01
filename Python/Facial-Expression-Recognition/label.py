import cv2
import label_image

size = 4

classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

webcam = cv2.VideoCapture(0) 

while True:
    (rval, im) = webcam.read()
    im=cv2.flip(im,1,0) 

    mini = cv2.resize(im, (int(im.shape[1]/size), int(im.shape[0]/size)))

    faces = classifier.detectMultiScale(mini)

    for f in faces:
        (x, y, w, h) = [v * size for v in f] 
        cv2.rectangle(im, (x,y), (x+w,y+h), (0,255,0), 4)
        
        sub_face = im[y:y+h, x:x+w]

        FaceFileName = "test.jpg" 
        cv2.imwrite(FaceFileName, sub_face)
        
        text = label_image.main(FaceFileName)
        text = text.title()
        font = cv2.FONT_HERSHEY_TRIPLEX
        cv2.putText(im, text,(x+w,y), font, 1, (0,0,255), 2)

    cv2.imshow('Capture',   im)
    key = cv2.waitKey(10)
    if key == 0: #The Esc key
        break
