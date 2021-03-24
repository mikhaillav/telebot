import telebot
from telebot import types
import configure

bot = telebot.TeleBot(configure.config["token"])
CHATID =  152474157

@bot.message_handler(commands = ["start"])
def get_start(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_info_yes = types.InlineKeyboardButton(text= "да", callback_data = "info_yes")
    item_info_no = types.InlineKeyboardButton(text= "не особо", callback_data = "info_no")
    markup_inline.add(item_info_yes,item_info_no)
    bot.send_message(message.chat.id, "хотите узнать что я умею?", reply_markup= markup_inline)

@bot.message_handler(commands = ["get_info", "info"])
def get_user_info(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_Yes = types.InlineKeyboardButton(text= "JA", callback_data = "yes")
    item_No = types.InlineKeyboardButton(text= "NET", callback_data = "no")

    markup_inline.add(item_Yes, item_No)
    bot.send_message(message.chat.id, "хотите узнать инфу о вас", reply_markup= markup_inline)

@bot.callback_query_handler(func = lambda call: True)
def answer(call):
    if call.data == "yes":
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item_id = types.KeyboardButton("МОЙ ID")
        item_name = types.KeyboardButton("МОЙ НИК")

        markup_reply.add(item_id, item_name)
        bot.send_message(call.message.chat.id, "нажмите на 1 из кнопок",reply_markup = markup_reply)
    elif call.data == "no":
        pass
    elif call.data == "da":
        photo = open('D:/WORK/PYTHON/telebot/photo.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo)

    elif call.data == "net":
        markup_inline = types.InlineKeyboardMarkup()
        item_Yes = types.InlineKeyboardButton(text= "а давай", callback_data = "ok")
        item_No = types.InlineKeyboardButton(text= "не спасибо", callback_data = "never")
        markup_inline.add(item_Yes, item_No)
        bot.send_message(call.message.chat.id ,"тогда могу сказать ваш ID и НИК", reply_markup= markup_inline)

    elif call.data == "info_yes":
        markup_inline = types.InlineKeyboardMarkup()
        item_Yes = types.InlineKeyboardButton(text= "покажи", callback_data = "da")
        item_No = types.InlineKeyboardButton(text= "лучше не надо", callback_data = "net")
        markup_inline.add(item_Yes, item_No)
        bot.send_message(call.message.chat.id ,"могу показать фото собаки", reply_markup= markup_inline)

    elif call.data == "info_no":
        bot.send_message(call.message.chat.id, "хорошо")

    elif call.data == "ok":
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item_id = types.KeyboardButton("МОЙ ID")
        item_name = types.KeyboardButton("МОЙ НИК")
        item_start = types.KeyboardButton("/start")
        item_test = types.KeyboardButton("отправить сообщение бате")

        markup_reply.add(item_id, item_name, item_start,item_test)
        bot.send_message(call.message.chat.id, "окей",reply_markup = markup_reply)

    elif call.data == "never":
        bot.send_message(call.message.chat.id, "хорошо")

@bot.message_handler(content_types = ["text"])
def get_message(message):
    if message.text == "МОЙ ID":
        bot.send_message(message.chat.id, f"твой ID: {message.from_user.id}")
    elif message.text == "МОЙ НИК":
        bot.send_message(message.chat.id, f"твой ник: {message.from_user.first_name} {message.from_user.last_name}")
    elif message.text == "что ты умеешь?" or message.text == "что я умею?":       
        markup_inline = types.InlineKeyboardMarkup()
        item_Yes = types.InlineKeyboardButton(text= "покажи", callback_data = "da")
        item_No = types.InlineKeyboardButton(text= "лучше не надо", callback_data = "net")
        markup_inline.add(item_Yes, item_No)
        bot.send_message(message.chat.id ,"могу показать фото собаки", reply_markup= markup_inline)
    elif message.text == "отправить сообщение бате":
        bot.send_message(CHATID, "hi world")

bot.polling(none_stop = True, interval= 0)