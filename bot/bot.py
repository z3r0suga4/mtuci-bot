import asyncio
import sys
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import start, news
from get_secrets.get_token import get_token

# Import Bot Token
TOKEN = get_token()

# Start Dispatcher
dp = Dispatcher(storage=MemoryStorage())

# Main Function, Start Polling
async def main():
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML, disable_web_page_preview=True)

    dp.include_routers(
            start.router,
            news.router
        )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
