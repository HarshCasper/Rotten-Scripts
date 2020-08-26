#!/usr/bin/env python3

#imports
from markovmeme.main import MemeImage
from markovmeme.text import generate_text
import random

#The module markovmeme, is installed as pip3 install markovmeme - python3
#                                       pip install markovmeme - python


#The file themes consists a list of all the topics based on which memes are generated

handle = []

with open('themes.txt', 'r') as file:
    handle = file.readlines()
    for i, j in enumerate(handle):
        handle[i] = handle[i].replace(" " , '').strip('\n')

#A random theme is chosen, from themes.txt
corpus = handle[random.randint(0,29)]

text = generate_text(corpus=corpus, use_model=True, size=10)

# Set image to full path, or None to select based on corpus
meme = MemeImage(image=None, corpus=corpus)

# Add text generated, centered on top
meme.write_text(text, fontsize=20, font='Anton-Regular.ttf')

#The meme is saved as markovmeme.png in the current diectory
meme.save_image('markovmeme.png')
