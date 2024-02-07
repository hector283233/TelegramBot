from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API
import config

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

sub_verification_menu = types.InlineKeyboardMarkup(row_width=1)
sub_verification_menu.insert(types.InlineKeyboardButton(text="Подпишитесь на канал", 
                                                  url=config.CHANNEL_URL))

sub_verification_menu.insert(types.InlineKeyboardButton(text="Уже подписан", 
                                                  callback_data="sub_check"))

menu_keyboard = types.InlineKeyboardMarkup(row_width=1)
download_button = types.InlineKeyboardButton(
    text="Скачать книги", 
    callback_data="download_books"
)
menu_keyboard.add(download_button)

def sub_verification(chat_member):
    if chat_member["status"] != "left":
        return True
    else:
        return False

@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    if sub_verification(
        await bot.get_chat_member(
            chat_id=config.CHANNEL_ID, 
            user_id=message.from_user.id
        )
    ):
        await bot.send_message(chat_id=message.from_user.id,
                               text="Добро пожаловать в наш бот!",
                               reply_markup=menu_keyboard)
    else:
        await bot.send_message(chat_id=message.from_user.id,
                               text="Вы не зарегестрированы в нашем канале, пожалуйста пройдите по ссылке и зарегестрируйтесь чтобы получить бесплатные книги!",
                               reply_markup=sub_verification_menu)
        
@dp.callback_query_handler(text="sub_check")
async def sub_check(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    if sub_verification(
        await bot.get_chat_member(
            chat_id=config.CHANNEL_ID, 
            user_id=message.from_user.id
        )
    ):
        await bot.send_message(chat_id=message.from_user.id,
                               text="Добро пожаловать в наш бот!",
                               reply_markup=menu_keyboard)
    else:
        await bot.send_message(chat_id=message.from_user.id,
                               text="Вы не зарегестрированы в нашем канале, пожалуйста пройдите по ссылке и зарегестрируйтесь чтобы получить бесплатные книги!",
                               reply_markup=sub_verification_menu)          

@dp.callback_query_handler(text="download_books")
async def download_books(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="https://merv.vc/media/files/Na_pensiyu_v_35_let.pdf")
    await bot.send_message(chat_id=message.from_user.id, text="https://merv.vc/media/files/k_potryaseniyam-procvetaniyu.pdf")
    await bot.send_message(chat_id=message.from_user.id, text="https://merv.vc/media/files/million_for_my_daughter.pdf")
    await bot.send_message(chat_id=message.from_user.id, text="https://merv.vc/media/files/pravila_investirovanija.pdf")
    await bot.send_message(chat_id=message.from_user.id, text="https://merv.vc/media/files/razumnyy_investor.pdf")

        
if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)