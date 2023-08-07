#!/usr/bin/env python
""" Provides a script that takes a (full) path to a directory of image files and converts it to a
.gif file in the current working directory under a folder called 'gifs'. There will be a subfolder
based on the parent folder of the images. """
import os
import sys
import math

from PIL import Image
import imageio

try:
    user_input = raw_input  # python2.x compat
except NameError:
    user_input = input

EXTENSIONS = [
    ".jpg",
    ".jpeg",
    ".png",
]
GIF_FRAMES = 120


def in_extensions(file):
    """ Check if a file has a valid extension. """
    return any(file.lower().endswith(ext) for ext in EXTENSIONS)


def main():
    """Turns a directory of images into a smaller GIF."""
    if len(sys.argv) < 2:
        print("Usage: images_to_gif.py /fullpath/to/images/directory")
        inp = user_input("Enter fullpath to directory: ")
        if not inp:
            print("No directory provided, exiting.")
            sys.exit()
        else:
            sys.argv.append(inp)

    base_dir = sys.argv[1]
    working_dir = os.getcwd()
    output_dir = os.path.join(working_dir, "gifs")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")

    folder_name = os.path.dirname(base_dir).split("/")[-1]
    gif_dir = os.path.join(output_dir, folder_name)
    if not os.path.exists(gif_dir):
        os.makedirs(gif_dir)

    save_dir = os.path.join(working_dir, "resized", folder_name)

    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)
        print(f"Created resized img directory {save_dir}")

    for file in sorted(os.listdir(base_dir)):
        path = os.path.join(base_dir, file)
        if os.path.isfile(os.path.join(save_dir, file)):
            continue
        try:
            img = Image.open(path)
        except IOError as err:
            print(f"Error opening {file}", err)
            continue
        try:
            img = img.resize((256, 192), Image.ANTIALIAS)
            img.save(save_dir + "/" + file)
        except OSError as err2:
            print("Error resizing ", err2)
            continue

    resized = []
    count = 0

    # imageio takes files as input
    for file in sorted(os.listdir(save_dir)):
        if not in_extensions(file):
            continue

        path = os.path.join(save_dir, file)
        tiny_img = imageio.imread(path)
        resized.append(tiny_img)
        suffix = folder_name + str(1 + (math.floor(count / GIF_FRAMES))) + ".gif"
        save_path = os.path.join(gif_dir, suffix)
        count += 1

        # create .gif files with a number of image files equal to GIF_FRAMES
        if not len(resized) % GIF_FRAMES:
            imageio.mimsave(save_path, resized)
            resized = []

    imageio.mimsave(save_path, resized)
    print(f"GIF saved to {gif_dir}")


if __name__ == "__main__":
    main()
