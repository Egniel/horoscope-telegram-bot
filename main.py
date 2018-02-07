import time

import telebot
from telebot import types
from settings import TOKEN

from parse_horo import *


bot = telebot.TeleBot(TOKEN)

SIGN = ''

ZODIAC_SIGNS = {
    'Овен': 'Aries',
    'Телец': 'Taurus',
    'Близнецы': 'Gemini',
    'Рак': 'Cancer',
    'Лев': 'Leo',
    'Дева': 'Virgo',
    "Весы": 'Libra',
    "Скорпион": 'Scorpio',
    "Стрелец": 'Sagittarius',
    'Козерог': 'Capricorn',
    'Водолей': 'Aquarius',
    'Рыбы': 'Pisces',
}
weekdays = {
    'Сегодня': 'today',
    'Вчера': 'yesterday',
    'Завтра': 'tomorrow',
    'Неделя': 'week',
    'Год': 'year',
}
interval_markup = types.ReplyKeyboardMarkup(row_width=2)
m_button1 = types.KeyboardButton('Вчера')
m_button2 = types.KeyboardButton('Сегодня')
m_button3 = types.KeyboardButton('Завтра')
m_button4 = types.KeyboardButton('Неделя')
m_button5 = types.KeyboardButton('Год')
m_button6 = types.KeyboardButton('Выбрать другой знак')
interval_markup.add(
    m_button1, m_button2, m_button3, m_button4, m_button5, m_button6)


signs_markup = types.ReplyKeyboardMarkup(row_width=3)
# for button in ZODIAC_SIGNS.keys():
#     signs_markup.add(types.KeyboardButton(button))
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
    bot.send_message(
        message.chat.id,
        'Здравствуй, выбери знак зодиака',
        reply_markup=signs_markup)





@bot.message_handler()
def text_handler(message):
    time.sleep(0.8)
    global SIGN

    if message.text in ZODIAC_SIGNS.keys():
        SIGN = message.text
        print(SIGN)
        bot.send_message(
            message.chat.id,
            'На какое время тебе нужен гороскоп?',
            reply_markup=interval_markup)
    if message.text == 'Выбрать другой знак':
        bot.send_message(
            message.chat.id,
            'Выбери знак зодиака',
            reply_markup=signs_markup)
    if message.text in weekdays.keys():
        bot.send_message(
            message.chat.id, get_horoscope(
                ZODIAC_SIGNS.get(SIGN).lower(), weekdays.get(message.text)))


bot.polling()
