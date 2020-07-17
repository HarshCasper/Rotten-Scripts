#!/usr/bin/env python3


from markovmeme.main import MemeImage
from markovmeme.text import generate_text
import random

with open('themes.txt', 'r') as file:
    s = file.readlines()
    for i in range(len(s)):
        s[i] = s[i].replace(" " , '').strip('\n')

corpus = s[random.randint(0,26)]
text = generate_text(corpus=corpus, use_model=True, size=10)

# Set image to full path, or None to select based on corpus
meme = MemeImage(image=None, corpus=corpus)

# Add text generated, centered on top
meme.write_text(text, fontsize=18, font='Anton-Regular.ttf')

# Leave outfile as None to generate random name
mem = meme.save_image('imag.png')
