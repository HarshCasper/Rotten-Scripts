__author__ = "Sri Manikanta Palakollu"
__date__ = "01-07-2020"

import moviepy.editor as editor
import argparse

# Setting up the Command Line Arguments.
parser = argparse.ArgumentParser()

parser.add_argument("-v", "--videoFile", required=True, help="Video Filename with the complete path.")
parser.add_argument('-p', "--path", required=True, help="Audio Filename with absolute or relative path")

args = vars(parser.parse_args())

try:
    videoClip = editor.VideoFileClip(r"{}".format(args['videoFile']))
    videoClip.audio.write_audiofile(r"{}".format(args['path']))
except Exception:
    print("Something went wrong during the conversion of Video File to Audio.")