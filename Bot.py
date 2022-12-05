import telebot
from config import token
from telebot import types
from bs4 import BeautifulSoup as bs
import requests
bot = telebot.TeleBot(token)

def test_goroscop(message):
    markup = types.InlineKeyboardMarkup(row_width=5)
    item1 = types.InlineKeyboardButton("♈ Овен", callback_data='1')
    item2 = types.InlineKeyboardButton("♉ Телец", callback_data='2')
    item3 = types.InlineKeyboardButton("♊ Близнецы", callback_data='3')
    item4 = types.InlineKeyboardButton("♋ Рак", callback_data='4')
    item5 = types.InlineKeyboardButton("♌ Лев", callback_data='5')
    item6 = types.InlineKeyboardButton("♍ Дева", callback_data='6')
    item7 = types.InlineKeyboardButton("♎ Весы", callback_data='7')
    item8 = types.InlineKeyboardButton("♏ Скорпион", callback_data='8')
    item9 = types.InlineKeyboardButton("♐ Стрелец", callback_data='9')
    item10 = types.InlineKeyboardButton("♑ Козерог", callback_data='10')
    item11 = types.InlineKeyboardButton("♒ Водолей", callback_data='11')
    item12 = types.InlineKeyboardButton("♓ Рыбы", callback_data='12')
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item4)
    markup.add(item5)
    markup.add(item6)
    markup.add(item7)
    markup.add(item8)
    markup.add(item9)
    markup.add(item10)
    markup.add(item11)
    markup.add(item12)
    bot.send_message(message.chat.id, 'Выберете знак задиака:', reply_markup=markup)


def goroscop(message_text):
    if message_text == '1':
        url = 'https://7days.ru/astro/horoscope/aries/today'
    if message_text == '2':
        url = 'https://7days.ru/astro/horoscope/taurus/today'
    if message_text == '3':
        url = 'https://7days.ru/astro/horoscope/gemini/today'
    if message_text == '4':
        url = 'https://7days.ru/astro/horoscope/cancer/today'
    if message_text == '5':
        url = 'https://7days.ru/astro/horoscope/leo/today'
    if message_text == '6':
        url = 'https://7days.ru/astro/horoscope/virgo/today'
    if message_text == '7':
        url = 'https://7days.ru/astro/horoscope/libra/today'
    if message_text == '8':
        url = 'https://7days.ru/astro/horoscope/scorpio/today'
    if message_text == '9':
        url = 'https://7days.ru/astro/horoscope/sagittarius/today'
    if message_text == '10':
        url = 'https://7days.ru/astro/horoscope/capricorn/today'
    if message_text == '11':
        url = 'https://7days.ru/astro/horoscope/aquarius/today'
    if message_text == '12':
        url = 'https://7days.ru/astro/horoscope/pisces/today'
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    return soup.find('div',class_="horoscope-7days__content_text").text
    

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет ✌️ ")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Гороскоп")
    markup.add(item1)
    bot.send_message(message.chat.id, 'Гороскоп', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    bot.send_message(message.chat.id, test_goroscop(message))


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    tag = int(call.data)
    if tag < 13:
        if call.message:
            bot.send_message(call.message.chat.id, text=goroscop(call.data))

bot.infinity_polling()
