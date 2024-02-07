from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton

menu_keyboard = InlineKeyboardMarkup(row_width=1)
button = InlineKeyboardButton(
    text="Скачать книги", 
    callback_data="download_book"
)
menu_keyboard.add(button)

sub_verification_menu = InlineKeyboardMarkup(row_width=1)
sub_verification_menu.insert(InlineKeyboardButton(text="Подпишитесь на канал", url="https://t.me/MervVCTelBotTest1"))
sub_verification_menu.insert(InlineKeyboardButton(text="Уже подписан", callback_data="sub_check"))