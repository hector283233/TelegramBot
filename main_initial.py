import telebot
import webbrowser
from telebot import types
import sqlite3

bot = telebot.TeleBot('6502597930:AAE_c2FfHE_uq4a1Z-6VD1CAPHL3CV3CDcA')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Go to webiste')
    markup.row(btn1)
    btn2 = types.KeyboardButton('List the products')
    btn3 = types.KeyboardButton('Contact admin')
    markup.row(btn2, btn3)
    file = open('./avatar.webp', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    # bot.send_audio(message.chat.id, file, reply_markup=markup)
    # bot.send_video(message.chat.id, file, reply_markup=markup)
    # bot.send_message(message.chat.id,'Welcome to our store.', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)
    
def on_click(message):
    if message.text == 'Go to webiste':
        webbrowser.open('https://merv.vc')
    elif message.text == 'List the products':
        bot.send_message(message.chat.id, 'Listing the products')
    elif message.text == 'Contact admin':
        bot.send_message(message.chat.id, 'Contacting the admin')
    
    

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Go to webiste', url='https://merv.vc')
    markup.row(btn1, )
    btn2 = types.InlineKeyboardButton('Delete Image', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Change Text', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, "Beautiful Image", reply_markup=markup)
    
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text("Edit text", callback.message.chat.id, callback.message.message_id)


@bot.message_handler(commands=['site', 'webiste'])
def site(message):
    webbrowser.open('https://merv.vc')

# @bot.message_handler(commands=['start', 'hello', 'main'])
# def main(message):
#     bot.send_message(message.chat.id, f' Hello {message.from_user.first_name}')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Helo</b> <em>information</em>', parse_mode='html')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'hello':
         bot.send_message(message.chat.id, f' Hello {message.from_user.first_name} {message.from_user.last_name}')
    
# bot.polling(none_stop=True)
bot.infinity_polling()