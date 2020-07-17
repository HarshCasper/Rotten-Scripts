"""

Copyright (C) 2019-2020 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

Modified from https://github.com/Visual-mov/Colorful-Julia (MIT License)

"""

import os
import sys

here = os.path.dirname(os.path.abspath(__file__))


def get_font(filename="OpenSans-Regular.ttf"):
    """Return the default font for writing on the images. A user could
       add additional fonts to this folder, if desired.
    """
    font_file = os.path.join(here, "fonts", filename)
    if not os.path.exists(font_file):
        sys.exit("Font %s does not exist." % font_file)
    return font_file


def list_corpus(remove_ext=True):
    """Based on the .txt files in the data/corpus folder, return the relative 
       paths. This allows the user to install the package with some custom 
       corpus. We remove the extensions since we are providing as options
       on the command line.
    """
    data = os.path.join(here, "data", "corpus")
    return list_folder(data, remove_ext=remove_ext, ext=".txt")


def list_images(remove_ext=True):
    """Based on the .png files in the data/images folder, return the paths.
    """
    data = os.path.join(here, "data", "images")
    return list_folder(data, remove_ext=remove_ext, ext=".png")


def list_folder(folder, remove_ext=True, ext=".txt"):
    """List files (recursively) in a folder, and optionally remove extensions
    """
    folders = []
    for root, dirs, files in os.walk(folder):
        for filename in files:
            if filename.endswith(ext):
                filename = os.path.join(root, filename)
                filename = filename.replace(folder, "").strip("/")
                if remove_ext:
                    filename = filename.replace(ext, "")
                folders.append(filename)
    return folders
