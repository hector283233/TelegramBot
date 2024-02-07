from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import config
from keyboards import menu_keyboard, sub_verification_menu

bot = Bot(config.TOKEN_API)
dp = Dispatcher(bot)

def sub_verification(chat_member):
    if chat_member["status"] != "left":
        return True
    else:
        return False
    
@dp.message_handler(commands="start")
async def start(message: types.Message):
    if sub_verification(
        await bot.get_chat_member(
            chat_id=config.CHANNEL_ID, 
            user_id=message.from_user.id
        )
    ):
        await bot.send_message(message.from_user.id, "Вы подписаны", reply_markup=menu_keyboard)
    else:
        await message.answer(
            "Чтобы получать бесплатные книги, подпишитесь на канал",
            reply_markup=sub_verification_menu
        )

# @dp.message_handler(commands="download_book")
# async def download_book(message: types.Message):
#     await message.reply_document(document="https://merv.vc/media/files/book1.pdf")

@dp.callback_query_handler(text="download_book")
async def download_book(message: types.Message):
    await bot.send_message("https://merv.vc/media/files/book1.pdf")
        
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)