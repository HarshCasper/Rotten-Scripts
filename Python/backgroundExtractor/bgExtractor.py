
import numpy as np
import cv2

file_path = 'india.mp4' # INPUT VIDEO 

######################### Method 1 ###################################
cap = cv2.VideoCapture(file_path)
first_iter = True
result = None
while True:
    ret, frame = cap.read()
    if frame is None:
        break

    if first_iter:
        avg = np.float32(frame)
        first_iter = False

    cv2.accumulateWeighted(frame, avg, 0.005)
    result = cv2.convertScaleAbs(avg)
############ the result image is out required output
cv2.waitKey(0)

# When everything done, releasing the capture
cap.release()
cv2.destroyAllWindows()
######################## Method 2 #####################################

video = cv2.VideoCapture(file_path)

FOI = video.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=30)

#creating an array of frames from frames chosen above
frames = []
for frameOI in FOI:
    video.set(cv2.CAP_PROP_POS_FRAMES, frameOI)
    ret, frame = video.read()
    frames.append(frame)

#calculate the average
########### The image we want is background frame
backgroundFrame = np.median(frames, axis=0).astype(dtype=np.uint8)

############################ OUTPUTS #################################
# Showing the output
cv2.imshow("Result",np.vstack((result,backgroundFrame)))
cv2.waitKey(0)
#cv2.imshow("Result 1", result)
#cv2.imshow("Result 2",backgroundFrame)
# Saving the image on device
#cv2.imwrite("bg1.jpg", result)
#cv2.imwrite("bg2.jpg",backgroundFrame)
