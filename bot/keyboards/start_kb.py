from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import emoji

option_1 = emoji.emojize(":newspaper:") + " Смотреть новости"

def start_kb():
    buttons = [
        [InlineKeyboardButton(text=option_1, callback_data="news")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard