import emoji
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

emoji_diamond = emoji.emojize(":small_orange_diamond:")
emoji_back = "🔙"

option_1 = emoji_diamond + " IRN"
option_2 = emoji_diamond + " РБК"
option_3 = emoji_diamond + " РИА"
option_4 = emoji_diamond + " ЕРЗ РФ"
option_5 = emoji_diamond + " Циан"
option_6 = emoji_diamond + " Я.Недвижимость"
option_7 = emoji_back + " Назад"

def news_kb():
    buttons = [[
        InlineKeyboardButton(text=option_1, callback_data="irn"),
        InlineKeyboardButton(text=option_2, callback_data="rbk")
    ],
    [
        InlineKeyboardButton(text=option_3, callback_data="ria"),
        InlineKeyboardButton(text=option_4, callback_data="erz")
    ],
    [
        InlineKeyboardButton(text=option_5, callback_data="cian"),
        InlineKeyboardButton(text=option_6, callback_data="yandex")
    ],
    [
        InlineKeyboardButton(text=option_7, callback_data="cancel"),
    ]]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard