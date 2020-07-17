#Imports and dependencies
from telegram.ext import Updater, InlineQueryHandler, CommandHandler , MessageHandler
import re
import requests
import urllib
import logging
import os
from k import ur
from k import riddle
import random
from noun import insult
#from mememe import meme1
from markovmeme.main import MemeImage
from markovmeme.text import generate_text
import random
import pyjokes
from memetemplates import template
from mem import tenpages

#get access to a server
PORT = int(os.environ.get('PORT' , 5000))

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = 'Your bot\'s token key'

def get_joke():
    index = random.randint(1 ,79)
    return(ur()[index])

def get_riddle():
    index = random.randint(1,105)
    return(riddle()[index])


def jokes(bot, update):
    jk = get_joke()
    chat_id = update.effective_chat.id
    bot.send_message(chat_id=chat_id, text=jk)

def riddles(bot, update):
    rd = get_riddle()
    chat_id = update.effective_chat.id
    bot.send_message(chat_id=chat_id , text=rd)

def insults(bot, update):
    insultme = insult()
    chat_id = update.effective_chat.id
    bot.send_message(chat_id=chat_id , text=insultme)

def proghumor(bot, update):
    jk = pyjokes.get_joke()
    chat_id = update.effective_chat.id
    bot.send_message(chat_id=chat_id , text=jk)


def temple(bot, update):
    msg, url = template()
    chat_id = update.effective_chat.id
    bot.send_photo(chat_id=update.effective_chat.id, photo=url)
    bot.send_message(chat_id=chat_id , text=msg)


def imageflip(bot, update):
    url = tenpages[random.randint(0,135)]
    chat_id = update.effective_chat.id
    bot.send_photo(chat_id=update.effective_chat.id, photo=url)


def markov(bot, update):
    with open('st.txt', 'r') as file:
        s = file.readlines()
        for i in range(len(s)):
            s[i] = s[i].replace(" " , '').strip('\n')

    corpus = s[random.randint(0,29)]
    text = generate_text(corpus=corpus, use_model=True, size=14)

    # Set image to full path, or None to select based on corpus
    meme = MemeImage(image=None, corpus=corpus)

    # Add text generated, centered on top
    meme.write_text(text, fontsize=18, font='Anton-Regular.ttf')

    # Leave outfile as None to generate random name
    meme.save_image('image.png')
    chat_id = update.effective_chat.id
    bot.send_photo(chat_id=chat_id, photo=open('./image.png', 'rb'))
    #bot.send_photo(chat_id=update.effective_chat.id, photo=meme)

def main():
    updater = Updater(token=TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('joke',jokes))
    dp.add_handler(CommandHandler('riddle',riddles))
    dp.add_handler(CommandHandler('insult', insults))
    dp.add_handler(CommandHandler('meme', imageflip))
    dp.add_handler(CommandHandler('proghumor', proghumor))
    dp.add_handler(CommandHandler('template', temple))
    dp.add_handler(CommandHandler('markov', markov))
    updater.start_webhook(listen = "0.0.0.0", port = int(PORT) , url_path = TOKEN)
    updater.bot.setWebhook('https://pacific-thicket-17598.herokuapp.com/' + TOKEN)
    updater.idle()

if __name__ == '__main__':
    main()
