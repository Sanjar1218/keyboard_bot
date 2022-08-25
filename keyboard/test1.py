from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '5128554563:AAFAxYqhCb4w5eKXuh5P3iU23apTrLyRz5Q'
bot = Bot(TOKEN)


update = bot.getUpdates()[-1]

chat_id = update.message.chat.id
text = update.message.text

keyboard1 = InlineKeyboardButton('shohruh', callback_data='data', url='https://t.me/shohw23')

reply_markup = InlineKeyboardMarkup([
   [keyboard1, keyboard1],
])


bot.sendMessage(chat_id, 'asdf', reply_markup=reply_markup)