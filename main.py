import telebot
from telebot import types
from settings import TOKEN

from parse_horo import *


bot = telebot.TeleBot(TOKEN)

interval_markup = types.ReplyKeyboardMarkup(row_width=3)
m_button1 = types.KeyboardButton('Вчера')
m_button2 = types.KeyboardButton('Сегодня')
m_button3 = types.KeyboardButton('Завтра')
m_button4 = types.KeyboardButton('Неделя')
m_button5 = types.KeyboardButton('Год')
interval_markup.add(
    m_button1, m_button2, m_button3, m_button4, m_button5)
ZODIAC_SIGNS = (
    'Овен',
    'Телец',
    'Близнецы',
    'Рак',
    'Лев',
    'Дева',
    "Весы",
    "Скорпион",
    "Стрелец",
)


signs_markup = types.ReplyKeyboardMarkup(row_width=3)
m_button1 = types.KeyboardButton('Овен')
m_button2 = types.KeyboardButton('Телец')
m_button3 = types.KeyboardButton('Близнецы')
m_button4 = types.KeyboardButton('Рак')
m_button5 = types.KeyboardButton('Лев')
m_button6 = types.KeyboardButton('Дева')
m_button7 = types.KeyboardButton('Весы')
m_button8 = types.KeyboardButton('Скорпион')
m_button9 = types.KeyboardButton('Стрелец')
m_button10 = types.KeyboardButton('Козерог')
m_button11 = types.KeyboardButton('Водолей')
m_button12 = types.KeyboardButton('Рыбы')
signs_markup.add(
    m_button1, m_button2, m_button3, m_button4, m_button5, m_button6,
    m_button7, m_button8, m_button9, m_button10, m_button11, m_button12)


@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    bot.reply_to(message, message.text, reply_markup=signs_markup)


@bot.message_handler()
def text_handler(message):
    if message.text in ZODIAC_SIGNS:
        bot.send_message(
            message.chat.id,
            'На какое время тебе нужен гороскоп?',
            reply_markup=interval_markup)


bot.polling()
