#! env bin/python
# codding = utf-8
from abc import ABCMeta,abstractmethod
import os
import logging

from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
'''import pymongo
from pymongo import MongoClient
client = MongoClient('loclhost', 27017)
db = client.enclever_test
collection  =  db [ 'enclever_test' ]
import  pprint
pprint.pprint(posts.find_one())
print(db)
print(collection)'''
from mongoengine import *

connect('testbd')


class UserCard(Document):
    word = StringField(max_length=120, required=True)
    image = StringField(max_length=120, required=True)
    translation = StringField(max_length=120, required=True)

    meta = {'allow_inheritance': True}

#ross = UserCard(word='hello', image='thisimage', translation="привет").save()


for c in UserCard.objects:
    print(c.word + c.image + c.translation)

updater = Updater(token='349763703:AAEJJVColK86rVmlaXxzh-tGU4XYN3YQWi4')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Select a theme")
    bot.send_message(chat_id=update.message.chat_id, text="All theme")
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def card_menu(bot, update):
    lst = ['/add_card', '/change_card', '/delete_card']
    bot.send_message(chat_id=update.message.chat_id, text="Select a category")
    for x in lst:
        bot.send_message(chat_id=update.message.chat_id, text=x)
card_menu_handler = CommandHandler('card_menu', card_menu)
dispatcher.add_handler(card_menu_handler)


def add_card(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Add? Yes/No")

    def yes_card(bot1, update1):
        text_yes_no = update1.message.text.upper()
        #print(text_yes_no)
        if text_yes_no == 'YES':
            # t = text_yes_no  # update.message.text
            bot1.send_message(chat_id=update1.message.chat_id, text="Enter the word1")


            def w1(bot11, update11):
                word = update11.message.text.upper()
                print(word)
                if word != "":
                    bot11.send_message(chat_id=update11.message.chat_id, text="Enter the word2")
                    word1 = update11.message.text.upper()
                    print(word1)

            w1_handler = MessageHandler(Filters.text, w1)
            dispatcher.add_handler(w1_handler)
            w1_handler = MessageHandler(Filters.text, w1)
            dispatcher.add_handler(w1_handler)
            w1_handler = MessageHandler(Filters.text, w1)
            dispatcher.add_handler(w1_handler)
            '''def w1(bot11, update11):
                word = update11.message.text.upper()
                bot11.send_message(chat_id=update11.message.chat_id, text="Enter the word")
                # print(a)

                print(word)
            w1_handler = MessageHandler(Filters.text, w1)
            dispatcher.add_handler(w1_handler)'''

            '''def w2(bot22, update22):
                bot22.send_message(chat_id=update22.message.chat_id, text="Enter the image")
                # print(a)
                picture = update22.message.text.upper()
                print(picture)

            w2_handler = MessageHandler(Filters.text, w1)
            dispatcher.add_handler(w2_handler)'''

            '''def word_card(bot2, update2):
                word = update2.message.text.upper()
                bot2.send_message(chat_id=update2.message.chat_id, text="word added")
                #bot2.send_message(chat_id=update2.message.chat_id, text="picture")
                picture = update2.message.text.upper()
                bot2.send_message(chat_id=update2.message.chat_id, text="word added")
                bot2.send_message(chat_id=update2.message.chat_id, text="a translation of a word")
                translation = update2.message.text.upper()
                print(word)
                print(picture)
                print(translation)'''

            #word_handler = MessageHandler(Filters.text, word_card)
            #dispatcher.add_handler(word_handler)
        else:
            t = "ok"
            bot1.send_message(chat_id=update1.message.chat_id, text=t)

    yes_handler = MessageHandler(Filters.text, yes_card)
    dispatcher.add_handler(yes_handler)

    #yes_handler = CommandHandler('yes_card', yes_card)
    #dispatcher.yes_handler(yes_handler)

add_handler = CommandHandler('add_card', add_card)
dispatcher.add_handler(add_handler)



'''def echo(bot, update):
     bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)'''



'''args = update.message.text
 def start_add(bot, update, args):
     text_caps = ' '.join(args).upper()
     if text_caps == 'YES':
         text = text_caps
     else:
         text = 'no...'
     bot.send_message(chat_id=update.message.chat_id, text=text)

 caps_handler = CommandHandler('text', start_add, pass_args=True)
 dispatcher.add_handler(caps_handler)'''

'''def caps(bot, update, args):
     text_caps = ' '.join(args).upper()
     bot.send_message(chat_id=update.message.chat_id, text=text_caps)

caps_handler = CommandHandler('caps', caps, pass_args=True)
dispatcher.add_handler(caps_handler)'''

updater.start_polling()


#import telegram
#bot = telegram.Bot()
#updater = Updater(token='TOKEN')
'''dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)'''