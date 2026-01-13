import telebot

# Tokeningizni mana shu yerga qo'ydim:
bot = telebot.TeleBot("8513575851:AAE40PrEkbs8cwijIKo9OmsvdBGHOv-zLts")

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Assalomu alaykum! Bot muvaffaqiyatli ishga tushdi.")

# Botni doimiy ishlab turishi uchun:
bot.polling(none_stop=True)
