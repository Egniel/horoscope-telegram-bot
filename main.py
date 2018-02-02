import telebot

from settings import TOKEN

bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    bot.reply_to(message, message.text)


bot.polling()