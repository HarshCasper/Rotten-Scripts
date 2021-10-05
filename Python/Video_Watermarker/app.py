from PIL import Image, ImageDraw, ImageFont
from cv2 import cv2
from tqdm import tqdm
import moviepy.editor as mpe
import sys
import os


def capture(path, choice, margin, text):
    video = cv2.VideoCapture(path)  # video object
    countFrame = 0
    img_array = []  # store all the watermaked frames
    progress_bar = tqdm(unit=" Frames Processed", unit_scale=True)
    while video.isOpened():
        sucess, frame = video.read()
        if sucess is False:
            break
        cv2.imwrite("frame" + str(countFrame) + ".jpg", frame)
        image = Image.open("frame" + str(countFrame) + ".jpg")
        width, height = image.size
        size = (width, height)
        draw = ImageDraw.Draw(image)  # drawing object
        font = ImageFont.truetype("arial.ttf", 36)
        textwidth, textheight = draw.textsize(text, font)
        if choice == "C":
            x = (width - textwidth) / 2
            y = (height - textheight) / 2
        elif choice == "RB":
            x = width - textwidth - margin
            y = height - textheight - margin
        elif choice == "LT":
            x = margin
            y = margin
        elif choice == "LB":
            x = margin
            y = height - textheight - margin
        elif choice == "RT":
            x = width - textwidth - margin
            y = margin
        else:
            print("Invalid choice!")
            break

        draw.text((x, y), text, font=font)
        image.save("frame converted" + str(countFrame) + ".jpg")
        img = cv2.imread("frame converted" + str(countFrame) + ".jpg")
        img_array.append(img)
        os.remove("frame" + str(countFrame) + ".jpg")
        os.remove("frame converted" + str(countFrame) + ".jpg")
        progress_bar.update()
        countFrame += 1

    video.release()
    video_write = cv2.VideoWriter(
        "output.avi", cv2.VideoWriter_fourcc(*"DIVX"), 30, size
    )
    for i in range(len(img_array)):
        video_write.write(img_array[i])
    video_write.release()

    my_clip = mpe.VideoFileClip("output.avi")
    audio_background = mpe.VideoFileClip(path).audio
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile("output.mp4")

    os.remove("output.avi")


if __name__ == "__main__":
    capture(sys.argv[1], sys.argv[2], int(sys.argv[3]), " ".join(sys.argv[4:]))
