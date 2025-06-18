from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import emoji

option_1 = emoji.emojize(":framed_picture:") + " Создать изображение"
option_2 = emoji.emojize(":newspaper:") + " Новости"
option_3 = emoji.emojize(":house_with_garden:") + " Развлекательный контент"

def start_kb():
    buttons = [
        [InlineKeyboardButton(text=option_1, callback_data="create_image")],
        [InlineKeyboardButton(text=option_2, callback_data="news")],
        [InlineKeyboardButton(text=option_3, callback_data="fun")],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard