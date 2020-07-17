#Imports and dependencies
#An explanation to each is given in the modules
from telegram.ext import Updater, InlineQueryHandler, CommandHandler , MessageHandler
import re
import requests
import urllib
from bs4 import BeautifulSoup
import logging
import os
from jokes import get_jokes
from riddles import get_riddles
from noun import insult
from markovmeme.main import MemeImage
from markovmeme.text import generate_text
import random
import pyjokes
from memetemplates import template
from imageflipmemes import memes

#get access to a server
PORT = int(os.environ.get('PORT' , 5000))

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = 'Your bot\'s token key'

#A detailed explanation of the function riddles:
#The function takes the parameters bot, update
#These refer to the bot and the state of the bot
#From the function get_riddles a riddle is returned to the variable riddle
#The chat_id is updated, i.e a response is prepared when it is triggered
#A message containing the riddle is and to the specified chat_id is sent
#All the functions work in the same way
#The modules have been included in the headers

def riddles(bot, update):
    ridddle = get_riddles()
    chat_id = update.effective_chat.id
    bot.send_message(chat_id=chat_id , text=riddle)

def jokes(bot, update):
    jk = get_joke()
    chat_id = update.effective_chat.id
    bot.send_message(chat_id=chat_id, text=jk)

def insults(bot, update):
    insultme = insult()
    chat_id = update.effective_chat.id
    bot.send_message(chat_id=chat_id , text=insultme)

def proghumor(bot, update):
    #The module pyjokes is used to get a joke

    #Installed as pip install pyjokes

    jk = pyjokes.get_joke()
    chat_id = update.effective_chat.id
    bot.send_message(chat_id=chat_id , text=jk)

def template(bot, update):
    msg, url = template()
    chat_id = update.effective_chat.id
    #To send a photo, the following syntax is used

    bot.send_photo(chat_id=update.effective_chat.id, photo=url)
    bot.send_message(chat_id=chat_id , text=msg)

def imageflip(bot, update):
    url = memes()
    chat_id = update.effective_chat.id
    bot.send_photo(chat_id=update.effective_chat.id, photo=url)

def markov(bot, update):
    #This script is built in Python and generates memes. It is built on the markovmeme library. 
    #It can be installed using pip install markovmeme
    #A theme can be chosen from the markov_themes.txt file
    #Here I am generating a random theme

    with open('markov_themes.txt', 'r') as file:
        themes = file.readlines()
        for i in range(len(s)):
            themes[i] = themes[i].replace(" " , '').strip('\n')

    corpus = random.choice(themes)
    text = generate_text(corpus=corpus, use_model=True, size=14)

    # Set image to full path, or None to select based on corpus
    meme = MemeImage(image=None, corpus=corpus)

    # Add text generated, centered on top
    meme.write_text(text, fontsize=18, font='Anton-Regular.ttf')

    # Leave outfile as None to generate random name
    meme.save_image('image.png')
    chat_id = update.effective_chat.id
    bot.send_photo(chat_id=chat_id, photo=open('./image.png', 'rb'))

def main():
    updater = Updater(token=TOKEN)

    #setting up the handler to dispatch content
    dp = updater.dispatcher

    #On the execution of the commands, the respective functions will be invoked
    dp.add_handler(CommandHandler('joke',jokes))
    dp.add_handler(CommandHandler('riddle',riddles))
    dp.add_handler(CommandHandler('insult', insults))
    dp.add_handler(CommandHandler('meme', imageflip))
    dp.add_handler(CommandHandler('proghumor', proghumor))
    dp.add_handler(CommandHandler('template', template))
    dp.add_handler(CommandHandler('markov', markov))
    
    #setting up connection to the server on Heroku
    updater.start_webhook(listen = "0.0.0.0", port = int(PORT) , url_path = TOKEN)
    updater.bot.setWebhook('Your heroku URL' + TOKEN)
    updater.idle()

if __name__ == '__main__':
    #Invoking the main function
    main()
