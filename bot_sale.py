import telebot
import random
import webbrowser
from telebot import types
import setting
from config import API_KEY


bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Футболки')
    button2 = types.KeyboardButton('Кофты')
    button3 = types.KeyboardButton('Штаны')
    button4 = types.KeyboardButton('Кроссовки')
    button5 = types.KeyboardButton('Шорты')
    button6 = types.KeyboardButton('Справка')
    markup.row(button1, button2, button3)
    markup.row(button4, button5)
    markup.row(button6)

    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}! \nЧерез меня ты можешь купить себе вещь'
                                      f' или связаться с менеджером', reply_markup=markup)


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.send_message(message.chat.id, 'У меня нет возможности просматривать фото')


@bot.message_handler(func=lambda message: True)
def info(message):
    if message.text == 'Футболки':
        shirtChapter(message)
    elif message.text == 'Кофты':
        sweaterChapter(message)
    elif message.text == 'Штаны':
        pantsChapter(message)
    elif message.text == 'Кроссовки':
        sneakersChapter(message)
    elif message.text == 'Шорты':
        shortsChapter(message)
    elif message.text == 'Справка':
        referenceChapter(message)
    elif message.text == 'Футболка Obey':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Купить')
        button2 = types.KeyboardButton('Доп. фото Obey')
        button3 = types.KeyboardButton('Назад в меню')
        markup.row(button1, button2)
        markup.row(button3)

        photo = open('Bot_Baryga/img/obey.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption='👕Информация о футболке Obey: '
                                                       '\nСостояние: Идеальное '
                                                       '\nРазмер: M'
                                                       '\nЦена: 200грн', reply_markup=markup)
    elif message.text == 'Доп. фото Obey':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Купить')
        button2 = types.KeyboardButton('Назад в меню')
        markup.row(button1, button2)

        photos = ['Bot_Baryga/img/o1.jpg', 'Bot_Baryga/img/o2.jpg', 'Bot_Baryga/img/o3.jpg', 'Bot_Baryga/img/o4.jpg']
        media = [telebot.types.InputMediaPhoto(open(photo, 'rb')) for photo in photos]

        bot.send_media_group(message.chat.id, media)
        bot.send_message(message.chat.id, 'Доп. фото', reply_markup=markup)
    elif message.text == 'Доп. фото Weekend':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Купить')
        button2 = types.KeyboardButton('Назад в меню')
        markup.row(button1, button2)

        photos = ['Bot_Baryga/img/w1.jpg', 'Bot_Baryga/img/w2.jpg']
        media = [telebot.types.InputMediaPhoto(open(photo, 'rb')) for photo in photos]

        bot.send_media_group(message.chat.id, media)
        bot.send_message(message.chat.id, 'Доп фото', reply_markup=markup)
    elif message.text == 'Футболка Weekend Offender':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Купить')
        button2 = types.KeyboardButton('Доп. фото Weekend')
        button3 = types.KeyboardButton('Назад в меню')
        markup.row(button1, button2)
        markup.row(button3)

        photo = open('Bot_Baryga/img/weekend.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption='👕Информация о футболке Weekend Offender: '
                                                       '\nСостояние: Отличное '
                                                       '\nРазмер: S'
                                                       '\nЦена: 300грн', reply_markup=markup)
    elif message.text == 'Свитшот Champion с лампасами':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Купить')
        button2 = types.KeyboardButton('Доп. фото Свитшот Champion с лампасами')
        button3 = types.KeyboardButton('Назад в меню')
        markup.row(button1, button2)
        markup.row(button3)

        photo = open('Bot_Baryga/img/ch1.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption='Информация об этом товаре: '
                                                       '\nСостояние: Хорошее '
                                                       '\nРазмер: XS-S'
                                                       '\nЦена: 300грн', reply_markup=markup)
    elif message.text == 'Доп. фото Свитшот Champion с лампасами':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Купить')
        button2 = types.KeyboardButton('Назад в меню')
        markup.row(button1, button2)

        photos = ['Bot_Baryga/img/c1.jpg', 'Bot_Baryga/img/c2.jpg', 'Bot_Baryga/img/c3.jpg', 'Bot_Baryga/img/c4.jpg']
        media = [telebot.types.InputMediaPhoto(open(photo, 'rb')) for photo in photos]

        bot.send_media_group(message.chat.id, media)
        bot.send_message(message.chat.id, 'Доп фото', reply_markup=markup)
    elif message.text == 'Свитшот Champion':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Купить')
        button2 = types.KeyboardButton('Доп. фото Свитшот Champion')
        button3 = types.KeyboardButton('Назад в меню')
        markup.row(button1, button2)
        markup.row(button3)

        photo = open('Bot_Baryga/img/photo1.png', 'rb')
        bot.send_photo(message.chat.id, photo, caption='Информация об этом товаре: '
                                                       '\nСостояние: Хорошее '
                                                       '\nРазмер: XS-S'
                                                       '\nЦена: 300грн', reply_markup=markup)
    elif message.text == 'Доп. фото Свитшот Champion':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Купить')
        button2 = types.KeyboardButton('Назад в меню')
        markup.row(button1, button2)

        photos = ['Bot_Baryga/img/chm1.jpg', 'Bot_Baryga/img/chm2.jpg']
        media = [telebot.types.InputMediaPhoto(open(photo, 'rb')) for photo in photos]

        bot.send_media_group(message.chat.id, media)
        bot.send_message(message.chat.id, 'Доп фото', reply_markup=markup)
    elif message.text == 'Свитшот Nike':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Купить')
        button2 = types.KeyboardButton('Доп. фото Свитшот Nike')
        button3 = types.KeyboardButton('Назад в меню')
        markup.row(button1, button2)
        markup.row(button3)

        photo = open('Bot_Baryga/img/sw_nike.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption='Информация об этом товаре: '
                                                       '\nСостояние: Хорошее '
                                                       '\nРазмер: XS'
                                                       '\nЦена: 250грн', reply_markup=markup)
    elif message.text == 'Доп. фото Свитшот Nike':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Купить')
        button2 = types.KeyboardButton('Назад в меню')
        markup.row(button1, button2)

        photos = ['Bot_Baryga/img/sw1.jpg']
        media = [telebot.types.InputMediaPhoto(open(photo, 'rb')) for photo in photos]

        bot.send_media_group(message.chat.id, media)
        bot.send_message(message.chat.id, 'Доп фото', reply_markup=markup)
    elif message.text == 'Кроссовки Adidas Gazelle':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Купить')
        button2 = types.KeyboardButton('Доп. фото Adidas Gazelle')
        button3 = types.KeyboardButton('Назад в меню')
        markup.row(button1, button2)
        markup.row(button3)

        photo = open('Bot_Baryga/img/gazele.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption='👟Информация про Adidas Gazelle: '
                                                       '\nСостояние: Отличное'
                                                       '\nРазмер: 38(23.5 см)'
                                                       '\nЦена: 600грн', reply_markup=markup)
    elif message.text == 'Доп. фото Adidas Gazelle':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Купить')
        button2 = types.KeyboardButton('Назад в меню')
        markup.row(button1, button2)

        photos = ['Bot_Baryga/img/g1.jpg', 'Bot_Baryga/img/g2.jpg', 'Bot_Baryga/img/g3.jpg']
        media = [telebot.types.InputMediaPhoto(open(photo, 'rb')) for photo in photos]

        bot.send_media_group(message.chat.id, media)
        bot.send_message(message.chat.id, 'Доп фото', reply_markup=markup)
    elif message.text == 'Кроссовки New Balance':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Купить')
        button2 = types.KeyboardButton('Доп. фото New Balance')
        button3 = types.KeyboardButton('Назад в меню')
        markup.row(button1, button2)
        markup.row(button3)

        photo = open('Bot_Baryga/img/nb.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption='👟Информация про кроссовки New Balance: '
                                                        '\nСостояние: Идеальное'
                                                       '\nРазмер: 39(25 см)'
                                                       '\nЦена: 900грн', reply_markup=markup)
    elif message.text == 'Доп. фото New Balance':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Купить')
        button2 = types.KeyboardButton('Назад в меню')
        markup.row(button1, button2)

        photos = ['Bot_Baryga/img/nb1.jpg', 'Bot_Baryga/img/nb2.jpg']
        media = [telebot.types.InputMediaPhoto(open(photo, 'rb')) for photo in photos]

        bot.send_media_group(message.chat.id, media)
        bot.send_message(message.chat.id, 'Доп фото', reply_markup=markup)
    elif message.text == 'Кроссовки Nike Zoom':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Купить')
        button2 = types.KeyboardButton('Доп. фото Nike Zoom')
        button3 = types.KeyboardButton('Назад в меню')
        markup.row(button1, button2)
        markup.row(button3)

        photo = open('Bot_Baryga/img/zoom.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption='👟Информация про кроссовки Nike Zoom: '
                                                       '\nСостояние: Отличное '
                                                       '\nРазмер: 40(25.5 см)'
                                                       '\nЦена: 800грн', reply_markup=markup)
    elif message.text == 'Доп. фото Nike Zoom':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Купить')
        button2 = types.KeyboardButton('Назад в меню')
        markup.row(button1, button2)

        photos = ['Bot_Baryga/img/z1.jpg', 'Bot_Baryga/img/z2.jpg']
        media = [telebot.types.InputMediaPhoto(open(photo, 'rb')) for photo in photos]

        bot.send_media_group(message.chat.id, media)
        bot.send_message(message.chat.id, 'Доп фото', reply_markup=markup)
    elif message.text == 'Кроссовки Nike Revolution':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Купить')
        button2 = types.KeyboardButton('Доп. фото Nike Revolution')
        button3 = types.KeyboardButton('Назад в меню')
        markup.row(button1, button2)
        markup.row(button3)

        photo = open('Bot_Baryga/img/nike_r.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption='👟Информация про кроссовки Nike Revolution: '
                                                       '\nРазмер: 45(29 см) '
                                                       '\nСостояние: Новых '
                                                       '\nЦена: 1900грн', reply_markup=markup)
    elif message.text == 'Доп. фото Nike Zoom':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Купить')
        button2 = types.KeyboardButton('Назад в меню')
        markup.row(button1, button2)

        photos = ['Bot_Baryga/img/z1.jpg', 'Bot_Baryga/img/z2.jpg']
        media = [telebot.types.InputMediaPhoto(open(photo, 'rb')) for photo in photos]

        bot.send_media_group(message.chat.id, media)
        bot.send_message(message.chat.id, 'Доп фото', reply_markup=markup)
    elif message.text == 'Доп. фото Nike Revolution':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Купить')
        button2 = types.KeyboardButton('Назад в меню')
        markup.row(button1, button2)

        photos = ['Bot_Baryga/img/rew1.jpg', 'Bot_Baryga/img/rew2.jpg', 'Bot_Baryga/img/rew3.jpg',
                  'Bot_Baryga/img/rew12.jpg']
        media = [telebot.types.InputMediaPhoto(open(photo, 'rb')) for photo in photos]

        bot.send_media_group(message.chat.id, media)
        bot.send_message(message.chat.id, 'Доп фото', reply_markup=markup)
    elif message.text == '👟Кроссовки Nike Air Max 2090':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Купить')
        button2 = types.KeyboardButton('Доп. фото Nike Air Max 2090')
        button3 = types.KeyboardButton('Назад в меню')
        markup.row(button1, button2)
        markup.row(button3)

        photo = open('Bot_Baryga/img/2090.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, caption='👟Информация про кроссовки Nike Air Max 2090: '
                                                       '\nРазмер: 39(24.5 см) '
                                                       '\nСостояние: Идеальное '
                                                       '\nЦена: 1200грн', reply_markup=markup)
    elif message.text == 'Доп. фото Nike Air Max 2090':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Купить')
        button2 = types.KeyboardButton('Назад в меню')
        markup.row(button1, button2)

        photos = ['Bot_Baryga/img/a1.jpg', 'Bot_Baryga/img/a2.jpg', 'Bot_Baryga/img/a3.jpg']
        media = [telebot.types.InputMediaPhoto(open(photo, 'rb')) for photo in photos]

        bot.send_media_group(message.chat.id, media)
        bot.send_message(message.chat.id, 'Доп фото', reply_markup=markup)
    elif message.text == 'Способ оплаты':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Назад в меню')
        markup.row(button1)

        bot.send_message(message.chat.id, 'Покупка происходит только по полной либо же минимальной предоплате. '
                                          '\nДля покупки напиши менеджеру: '
                                          '\nhttps://t.me/sergo6608',
                         reply_markup=markup)
    elif message.text == 'Способ доставки':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Назад в меню')
        markup.row(button1)

        bot.send_message(message.chat.id, 'Отправление посылок только через Новую почту', reply_markup=markup)
    elif message.text == 'Информация о боте':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Назад в меню')
        markup.row(button1)

        bot.send_message(message.chat.id, 'Привет👋 Я бот для продажи вещей. Для начала напиши "/start"'
                                          '\nОбновление вещей будет каждую неделю👕 \nЕсли ты нашел какую-то '
                                          'не доработку, либо тебе что-то не понятно, сообщи менеджеру: '
                                          '\nhttps://t.me/sergo6608')
    elif message.text == 'Купить':
        bot.send_message(message.chat.id, 'Для покупки напиши менеджеру: \nhttps://t.me/sergo6608')
    elif message.text == 'Назад в меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Футболки')
        button2 = types.KeyboardButton('Кофты')
        button3 = types.KeyboardButton('Штаны')
        button4 = types.KeyboardButton('Кроссовки')
        button5 = types.KeyboardButton('Шорты')
        button6 = types.KeyboardButton('Справка')
        markup.row(button1, button2, button3)
        markup.row(button4, button5)
        markup.row(button6)
        bot.send_message(message.chat.id, 'Вы вышли в меню', reply_markup=markup)

    else:
        bot.send_message(message.chat.id, 'Прости, я не понял, что ты хочешь сказать')

def shirtChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Футболка Obey')
    button2 = types.KeyboardButton('Футболка Weekend Offender')
    button3 = types.KeyboardButton('Назад в меню')
    markup.row(button1, button2)
    markup.row(button3)

    bot.send_message(message.chat.id, 'Эти товары сейчас находятся в наличии: ', reply_markup=markup)

def sweaterChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Свитшот Champion с лампасами')
    button2 = types.KeyboardButton('Свитшот Champion')
    button3 = types.KeyboardButton('Свитшот Nike')
    button4 = types.KeyboardButton('Назад в меню')
    markup.row(button1, button2, button3)
    markup.row(button4)

    bot.send_message(message.chat.id, 'Эти товары сейчас находятся в наличии: ', reply_markup=markup)

def sneakersChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttun1 = types.KeyboardButton('Кроссовки Adidas Gazelle')
    button2 = types.KeyboardButton('Кроссовки Nike Revolution')
    button3 = types.KeyboardButton('Кроссовки Nike Zoom')
    button4 = types.KeyboardButton('Кроссовки New Balance')
    button5 = types.KeyboardButton('Кроссовки Nike Air Max 2090')
    button6 = types.KeyboardButton('Назад в меню')
    markup.row(buttun1, button2)
    markup.row(button3, button4)
    markup.row(button5)
    markup.row(button6)

    bot.send_message(message.chat.id, 'Кроссовки в наличии: ', reply_markup=markup)

def referenceChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Способ оплаты')
    button2 = types.KeyboardButton('Способ доставки')
    button3 = types.KeyboardButton('Информация о боте')
    button4 = types.KeyboardButton('Назад в меню')
    markup.row(button1, button2, button3)
    markup.row(button4)

    bot.send_message(message.chat.id, 'Справка', reply_markup=markup)

def pantsChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button3 = types.KeyboardButton('Назад в меню')
    markup.row(button3)

    bot.send_message(message.chat.id, 'Штанов нету пока в наличии 😔', reply_markup=markup)

def shortsChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Назад в меню')
    markup.row(button1)

    bot.send_message(message.chat.id, 'Шорт нету пока в наличии 😔', reply_markup=markup)

bot.polling(none_stop=True)