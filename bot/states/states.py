from aiogram.fsm.state import State, StatesGroup

# NewsChoosing for news.py
class NewsState(StatesGroup):
    choosing_news = State()