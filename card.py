import collections

from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater
import sys
from mongoengine import *
from abc import ABCMeta,abstractmethod
import os
import logging

from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

connect('testbd1')


class FlashCard(Document):
    """
    FlashCard затычка
    """
    term = StringField(required=True)
    term_native = StringField(required=True)  # In russian
    description = StringField(required=True)
    pic = StringField(required=True)  # URL/path to the image

    meta = {'allow_inheritance': True}
'''FlashCard(term='hello', term_native="привет", description='thisimage', pic='url:/gdfg').save()
FlashCard(term='hello1', term_native="привет1", description='thisimage1', pic='url:/gdfg1').save()
FlashCard(term='hello2', term_native="привет2", description='thisimage2', pic='url:/gdfg2').save()'''
for c in FlashCard.objects:
    print(c.term + c.term_native + c.description, c.pic)



updater = Updater(token='349763703:AAEJJVColK86rVmlaXxzh-tGU4XYN3YQWi4')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(bot, update):
    keyboard = [[InlineKeyboardButton("1 - Add card", callback_data='1'),
                 InlineKeyboardButton("2 - Change card", callback_data='2')],
                 [InlineKeyboardButton("4 - All cards", callback_data='4'),
                 InlineKeyboardButton("3 - Delete card", callback_data='3')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)



def button(bot, update):
    query = update.callback_query

    '''bot.edit_message_text(text="Selected option: %s" % query.data,
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)'''
    print(query.data)
    if str(query.data) == '4':
        #bot.send_message(chat_id=query.message.chat_id, text="Selected option: %s" % query.data)

        def all_user_card(bot, update, args):
             for c in FlashCard.objects:
                 print(c.term + c.term_native + c.description, c.pic)
                 all = c.term + c.term_native + c.description, c.pic
             bot.send_message(chat_id=query.message.chat_id, text=all)

        #all_handler = CommandHandler('all_user_card', all_user_card, pass_args=True)
        all_handler = MessageHandler(Filters.text, all_user_card)
        dispatcher.add_handler(all_handler)


def add(user_term, user_term_native, user_description, user_pic):
    FlashCard(term=user_term, term_native=user_term_native, description=user_description, pic=user_pic).save()


def delete(id):
    obj = FlashCard.objects(term=id)
    obj.delete()
    #FlashCard.remove({'term':id})#.update(unset__sensordict__S=id)
delete("hello")
def error(bot, update, error):
    logging.warning('Update "%s" caused error "%s"' % (update, error))


# Create the Updater and pass it your bot's token.
updater = Updater("349763703:AAEJJVColK86rVmlaXxzh-tGU4XYN3YQWi4")

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.dispatcher.add_error_handler(error)

# Start the Bot
updater.start_polling()

# Run the bot until the user presses Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT
updater.idle()