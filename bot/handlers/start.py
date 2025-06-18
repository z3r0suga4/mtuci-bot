from aiogram import Router, F
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards.start_kb import start_kb
from keyboards.news_kb import news_kb

from states.states import NewsState

router = Router()

@router.message(StateFilter(None), CommandStart)
async def inline_start(message: Message, state: FSMContext):
    await message.answer("Привет! Я бот для парсинга новостей на тему недвижимости.", reply_markup=start_kb())

@router.callback_query(StateFilter(None), F.data=="news")
async def inline_news(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text="Выбери сайт:",
        reply_markup=news_kb()
    )
    await state.set_state(NewsState.choosing_news)