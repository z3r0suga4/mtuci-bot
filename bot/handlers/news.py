import time
import emoji

from aiogram import Router, types, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from keyboards.news_inline_kb import news_kb
from keyboards.start_inline_kb import start_kb

from news_parsers.irn_parser import irn_parser
from news_parsers.rbk_parser import rbk_parser
from news_parsers.ria_parser import ria_parser
from news_parsers.erz_parser import erz_parser
from news_parsers.cian_parser import cian_parser
from news_parsers.yandex_parser import yandex_parser

from states.states import NewsState

router = Router()

@router.callback_query(NewsState.choosing_news, F.data=="irn")
async def irn(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text="Ищу новости...",
        reply_markup=news_kb()
    )
    irn_news = irn_parser()
    await callback.message.edit_text(
        text=irn_news,
        reply_markup=news_kb()
    )

@router.callback_query(NewsState.choosing_news, F.data=="rbk")
async def rbk(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text="Ищу новости...",
        reply_markup=news_kb()
    )
    rbk_news = rbk_parser()
    await callback.message.edit_text(
        text=rbk_news,
        reply_markup=news_kb()
    )

@router.callback_query(NewsState.choosing_news, F.data=="ria")
async def ria(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text="Ищу новости...",
        reply_markup=news_kb()
    )
    ria_news = ria_parser()
    await callback.message.edit_text(
        text=ria_news,
        reply_markup=news_kb()
    )

@router.callback_query(NewsState.choosing_news, F.data=="erz")
async def erz(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text="Ищу новости...",
        reply_markup=news_kb()
    )
    erz_news = erz_parser()
    await callback.message.edit_text(
        text=erz_news,
        reply_markup=news_kb()
    )

@router.callback_query(NewsState.choosing_news, F.data=="cian")
async def cian(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text="Ищу новости...",
        reply_markup=news_kb()
    )
    cian_news = cian_parser()
    await callback.message.edit_text(
        text=cian_news,
        reply_markup=news_kb()
    )

@router.callback_query(NewsState.choosing_news, F.data=="yandex")
async def yandex(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text="Ищу новости...",
        reply_markup=news_kb()
    )
    yandex_news = yandex_parser()
    await callback.message.edit_text(
        text=yandex_news,
        reply_markup=news_kb()
    )

@router.callback_query(NewsState.choosing_news, F.data=="cancel")
async def cancel_news(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text="Привет! Я бот для парсинга новостей на тему недвижимости.",
        reply_markup=start_kb()
    )
    await state.clear()

