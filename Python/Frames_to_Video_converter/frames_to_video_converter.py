import os
import sys
import cv2

# We store all the images in the folder into a variable(here images).
# Then get the height, and width required for the frames from any image
# Use VideoWriter function to initialize a video variable. The four arguments
# in VideoWriter is the video file name, fourcc code, fps and dimensions
# video.write() writes all the images into the video.


def convert_frames_to_video(img_folder_path, fps):
    images = [img for img in os.listdir(img_folder_path)]
    frame = cv2.imread(os.path.join(img_folder_path, images[0]))
    height, width, layers = frame.shape

    video_name = input('Enter the video name(just the filename): ')
    if not video_name.endswith('.avi'):
        video_name = video_name + '.avi'
    # fourcc code = 0 gives no warning with files other than .avi
    video = cv2.VideoWriter(video_name, 0, fps, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(img_folder_path, image)))

    cv2.destroyAllWindows()
    video.release()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        img_folder_path = str(" ".join(sys.argv[1:]))
    fps = int(input('Enter the fps needed: '))
    convert_frames_to_video(img_folder_path, fps)
