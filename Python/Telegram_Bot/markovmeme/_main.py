"""

Copyright (C) 2019-2020 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""

import random
from .namer import RobotNamer
from .utils import list_corpus, list_images, get_font
from PIL import Image, ImageDraw, ImageFont

import math
import os
import sys

here = os.path.dirname(os.path.abspath(__file__))


class MemeImage:
    """A Meme Image includes markov (or randomly selected) text from a corpus, and
    a matching image. The image and corpus can be customized, otherwise
    the image is matched to the text. If the user selects a custom corpus,
    a custom image must also be provided. If an image doesn't exist for a
    given corpus, the user is required to specify it.
    """

    def __init__(self, image=None, corpus=None, quiet=False):

        self.corpus = self.get_corpus(corpus)
        self.quiet = quiet
        self.imagefile = self.get_image(image, self.corpus)
        self.image = Image.open(self.imagefile).convert("RGBA")
        self.draw = ImageDraw.Draw(self.image)

    def get_corpus(self, corpus):
        """Given an input corpus, validate that it's available. If it's not
        a full path to a file, or if it doesn't exist, select one at random.
        """
        if os.path.exists(corpus):
            return corpus

        options = list_corpus()
        if corpus in options:
            return corpus
        return random.choice(corpus)

    def get_image(self, image, corpus):
        """If the image is provided, the full path must exist. Otherwise,
        we list images that come with the modula and randomly select one
        that matches the corpus.
        """
        # If a full path to an image is provided that exists, we're good
        if image is not None:
            if os.path.exists(image):
                return image

        # Otherwise, filter to subset in corpus
        options = [x for x in list_images() if corpus in x]
        if not options:
            sys.exit("No images exist for corpus %s. Please specify --image." % corpus)

        choice = random.choice(options)
        return os.path.join(here, "data", "images", "%s.png" % choice)

    def __str__(self):
        return "[mememl][%s]" % (self.corpus)

    def __repr__(self):
        return self.__str__()

    def print(self, message):
        """A wrapper to print to check if quiet is True, and skip if so."""
        if not self.quiet:
            print(message)

    def write_text(
        self,
        text,
        fontsize=32,
        rgb=(255, 255, 255),
        ycoord=10,
        font="Anton-Regular.ttf",
    ):
        """Given a text string, font size, and output coordinates, write text
        onto the image. The default font provided with the package
        """
        if text not in [None, ""]:

            # Break image into width and height
            width, height = self.image.size
            fontfile = get_font(font)
            font = ImageFont.truetype(fontfile, fontsize)

            # How much space do we need for all of text?
            expect_width, expect_height = self.draw.textsize(text, font)

            # Do we need multiple lines?
            lineCount = 1
            if expect_width > width:
                lineCount = int(round((expect_width / width) + 1))

            # Split text into <lineCount> lines
            lines = self.text2lines(text, lineCount, font)

            # Draw each line on the image
            for i in range(0, lineCount):
                w, h = self.draw.textsize(lines[i], font)

                # We want the text to be centered
                xcoord = width / 2 - w / 2
                ycoord = i * h

                # Black outline
                self.draw.text((xcoord - 2, ycoord - 2), lines[i], (0, 0, 0), font=font)
                self.draw.text((xcoord + 2, ycoord - 2), lines[i], (0, 0, 0), font=font)
                self.draw.text((xcoord + 2, ycoord + 2), lines[i], (0, 0, 0), font=font)
                self.draw.text((xcoord - 2, ycoord + 2), lines[i], (0, 0, 0), font=font)

                # Main text
                self.draw.text((xcoord, ycoord), lines[i], font=font, fill=rgb)

    def text2lines(self, text, lineCount, font):
        """given a linecount, split text into lines. We minimally return one
        line, the given text as a single entry in a list.
        I was originally using textwrap, but this is much more direct
        https://blog.lipsumarium.com/caption-memes-in-python/
        """
        if lineCount == 1:
            return [text]

        lines = []
        lastCut = 0
        is_last = False

        for i in range(0, lineCount):

            cut = lastCut
            if lastCut == 0:
                cut = (len(text) / lineCount) * i
            cut = math.floor(cut)

            if i < lineCount - 1:
                nextCut = int((len(text) / lineCount) * (i + 1))
            else:
                nextCut = len(text)
                is_last = True

            # make sure we don't cut words in half
            if nextCut != len(text) and text[nextCut] == " ":
                while text[nextCut] != " ":
                    nextCut += 1

            line = text[cut:nextCut].strip()

            # is line still fitting (we overshot)
            w, h = self.draw.textsize(line, font)
            if not is_last and w > self.image.width:
                nextCut -= 1
                while text[nextCut] != " ":
                    nextCut -= 1

            lastCut = nextCut
            lines.append(text[cut:nextCut].strip())

        return lines

    def Xwrite_text(
        self,
        text,
        fontsize=32,
        rgb=(255, 255, 255),
        xcoord=10,
        ycoord=10,
        font="Anton-Regular.ttf",
    ):
        """Given a text string, font size, and output coordinates, write text
        onto the image. The default font provided with the package
        """
        if text not in [None, ""]:
            import textwrap

            # Break image into width and height
            width, height = self.image.size
            fontfile = get_font(font)
            font = ImageFont.truetype(fontfile, fontsize)
            lines = textwrap.wrap(text, 40)

            # Keep track of y coordinate (height)
            total_height = ycoord
            for line in lines:

                # Calculate a specific width and height for the line
                w, h = font.getsize(line)

                # If we have space, honor the x coordinate, otherwise center
                xstart = (width - w) / 2
                if width - xcoord > w:
                    xstart = xcoord

                # Don't draw if we go over total height
                if total_height + 2 >= height:
                    break

                # Black outline
                self.draw.text(
                    (xstart - 2, total_height - 2), text, (0, 0, 0), font=font
                )
                self.draw.text(
                    (xstart + 2, total_height - 2), text, (0, 0, 0), font=font
                )
                self.draw.text(
                    (xstart + 2, total_height + 2), text, (0, 0, 0), font=font
                )
                self.draw.text(
                    (xstart - 2, total_height + 2), text, (0, 0, 0), font=font
                )

                # Main text
                self.draw.text((xstart, total_height), line, font=font, fill=rgb)
                total_height += h

    def save_image(self, outfile=None):
        """Save the image to an output file, if provided. Optionally add some
        text to it.
        """
        if not outfile:
            outfile = "%s.png" % self.generate_name()
        print("Saving image to %s" % outfile)
        self.image.save(outfile, "PNG")

    def generate_name(self):
        """Generate a random filename from the Robot Namer"""
        return RobotNamer().generate()
