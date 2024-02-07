from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Server started')
    
    
kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text="/help")
b2 = KeyboardButton(text="Скачать Книгу", callback_data="download_book")
kb.add(b2)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Добро пожаловать в наш бот!",
                           reply_markup=kb)
    
# @dp.message_handler(commands=['vote'])
# async def vote_command(message: types.Message):
    
#     ikb = InlineKeyboardMarkup(row_width=2)
#     ib1 = InlineKeyboardButton(text="button 1", callback_data="download")
#     ib2 = InlineKeyboardButton(text="button 2", callback_data="skip")
#     ikb.add(ib1, ib2)
#     await bot.send_message(chat_id=message.from_user.id, text="https://merv.vc/media/files/book1.pdf")
#     # await bot.reply_document()
#     await bot.send_message(chat_id=message.from_user.id, text="")

@dp.callback_query_handler(text="download_book")
async def download_book(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="https://merv.vc/media/files/book1.pdf")

if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, on_startup=on_startup, skip_updates=True)