import os
import cv2
import argparse

# Necessary Arguments

ap = argparse.ArgumentParser()
ap.add_argument('-i', "--input", required=True, type=str, help="Input video file")
ap.add_argument('-o', "--output", required=True, type=str, help="Output video file name")
ap.add_argument('-frate', "--frate", required=True, default=0.1, type=float, help="To determine the amount of frames to be extracted per second")
ap.add_argument('-fps', "--framesps", default=int(cv2.CAP_PROP_FPS), help="Extract at the desired Frame rate")
args = vars(ap.parse_args())

video_path = args['input']
video_name = args['output']
frameRate = args['frate']
skip_frames = args['framesps']
save_path = "./Images_stopmotion/"

# Creating a temporary directory for images.
os.mkdir(save_path)

def length_of_video(video_p):
    '''
    Gets the input length of video and returns it.
    '''
    cap = cv2.VideoCapture(video_p)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    return length

def extracting_frames():
    '''
    Extracting function for the images.
    '''
    length = length_of_video(video_path)
    if length == 0:
        print("Length is 0,Video not Available")
        return 0

    cap = cv2.VideoCapture(video_path)
    count = 0

    ret, frame = cap.read()
    test_file_path = save_path + str(count) +".png"
    cv2.imwrite(test_file_path, frame)

    if os.path.isfile(test_file_path):
        print("Saving Test Frame successful, Image Extraction process initiated.")
        count = 1
        while ret:
            ret, frame = cap.read()
            if ret and count % int(skip_frames/(frameRate)) == 0:
                # Image naming
                name = save_path + str(count) +".png"
                cv2.imwrite(name, frame)
                count += 1
            else:
                count += 1
    else:
        print("Problem saving the Test Frame.")
        return 0
    cap.release()

def Image_video_stopmotion():
    """
    Create a stop motion video from extracted Images.
    """
    images = [img.split(".") for img in os.listdir(save_path) if img.endswith(".png")]
    sort_img_order = sorted([int(img[0]) for img in images])

    frame = cv2.imread(os.path.join(save_path, str(sort_img_order[0]) + ".png"))
    height, width, layers = frame.shape
    video = cv2.VideoWriter(video_name, 0, 1, (width,height))

    print("Stop motion process initiated.")
    for image in sort_img_order:
        video.write(cv2.imread(os.path.join(save_path, str(image) + ".png")))

    cv2.destroyAllWindows()
    video.release()

def file_deletion():
    """
    Deletes temporary redundant Images.
    """
    image_delete = [img for img in os.listdir(save_path) if img.endswith(".png")]
    for delete_img in image_delete:
        os.remove(save_path+"/"+delete_img)
    os.rmdir(save_path)

def main():
    extracting_frames()
    Image_video_stopmotion()
    file_deletion()

if __name__=="__main__":
    main()

