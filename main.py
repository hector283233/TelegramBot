from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6502597930:AAE_c2FfHE_uq4a1Z-6VD1CAPHL3CV3CDcA')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб сайт', web_app=WebAppInfo(url='https://telegram.merv.vc/')))
    await message.answer('Привет', reply_markup=markup)

executor.start_polling(dp)