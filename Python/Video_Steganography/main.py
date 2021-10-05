# Importing requiered modules
from stegano import lsb
from os.path import isfile, join
import time
import cv2
import numpy as np
import math
import os
import shutil
from subprocess import call, STDOUT


# Function to split the message.
def split_string(split_str, count=10):
    per_c = math.ceil(len(split_str) / count)
    c_cout = 0
    out_str = ""
    split_list = []
    for s in split_str:
        out_str += s
        c_cout += 1
        if c_cout == per_c:
            # The message is divided into substrings
            split_list.append(out_str)
            out_str = ""
            c_cout = 0
    if c_cout != 0:
        split_list.append(out_str)
    return split_list


# As we know video is a collection of frames, where each frame is a picture.
# This function will extract each frame along with audio from the video.
def frame_extraction(video):
    if not os.path.exists("./temp"):
        os.makedirs("temp")
    # Temporary folder created to store the frames and audio from the video.
    temp_folder = "./temp"
    print("[INFO] temp directory is created")
    vidcap = cv2.VideoCapture(video)
    count = 0
    while True:
        success, image = vidcap.read()
        if not success:
            break
        cv2.imwrite(os.path.join(temp_folder, "{:d}.png".format(count)), image)
        count += 1


# This function would embed the splitted string into the frames extracted from the video.
def encode_string(input_string, root="./temp/"):
    # Acquire the splitted string from the message.
    split_string_list = split_string(input_string)
    for i in range(0, len(split_string_list)):
        f_name = "{}{}.png".format(root, i)
        # Embedded the splitted string into each frame.
        secret_enc = lsb.hide(f_name, split_string_list[i])
        # Saved the frames after hidding the strings.
        secret_enc.save(f_name)
        print("[INFO] frame {} holds {}".format(f_name, lsb.reveal(f_name)))
    print("The message is stored in the Embedded_Video.mp4 file")


# This function would decode the hidden message by extracting frames from the video
def decode_string(video):
    frame_extraction(video)  # Extracting each frame from the video
    secret = []
    root = "./temp/"
    for i in range(len(os.listdir(root))):
        f_name = "{}{}.png".format(root, i)
        # Revealing the message inside each string
        secret_dec = lsb.reveal(f_name)
        if secret_dec is None:
            break
        secret.append(secret_dec)
    print("".join([i for i in secret]))
    clean_temp()


# This function would delete the temp directory


def clean_temp(path="./temp"):
    if os.path.exists(path):
        shutil.rmtree(path)
        print("[INFO] temp files are cleaned up")


# This function would extraxt audio from the video so as to stitch them back later.
def input_main(f_name):
    input_string = input("Enter the message :")  # To collect the message
    frame_extraction(f_name)
    # The call function would be used to extract the audio and then stitch it again properly with the frames extracted.
    call(
        ["ffmpeg", "-i", f_name, "-q:a", "0", "-map", "a", "temp/audio.mp3", "-y"],
        stdout=open(os.devnull, "w"),
        stderr=STDOUT,
    )
    encode_string(input_string)
    call(
        [
            "ffmpeg",
            "-i",
            "temp/%d.png",
            "-vcodec",
            "png",
            "temp/Embedded_Video.mp4",
            "-y",
        ],
        stdout=open(os.devnull, "w"),
        stderr=STDOUT,
    )
    call(
        [
            "ffmpeg",
            "-i",
            "temp/Embedded_Video.mp4",
            "-i",
            "temp/audio.mp3",
            "-codec",
            "copy",
            "Embedded_Video.mp4",
            "-y",
        ],
        stdout=open(os.devnull, "w"),
        stderr=STDOUT,
    )
    clean_temp()


if __name__ == "__main__":
    while True:
        print("1.Hide a message in video\n2.Reveal the secret from the video\n")
        print("Any other value to exit\n")
        choice = input("Enter your choice :")
        if choice == "1":
            f_name = input("Enter the name of video file with extension:")
            input_main(f_name)
        elif choice == "2":
            decode_string(input("Enter the name of video with extension :"))
        else:
            break
