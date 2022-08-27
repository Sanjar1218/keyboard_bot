from turtle import update
from telegram import Update
from telegram.ext import Updater, Filters, MessageHandler, CallbackContext
import os
TOKEN = os.environ['token']
import main

def like(update: Update, context: CallbackContext):
    count = main.Count()
    chat_id = update.message.chat.id
    txt = update.message.text
    bot = context.bot
    count.add(txt)
    bot.sendMessage(chat_id, f'likes: {count.like}\nDislikes: {count.dislike}')

updater= Updater(TOKEN)

updater.dispatcher.add_handler(MessageHandler(Filters.text(['👍', '👎']), like))

updater.start_polling()
updater.idle()