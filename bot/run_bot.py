import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from bot.config import TelegramBot
from bot.routers import router as main_router



async def main() -> None:
    settings = TelegramBot()
    dp = Dispatcher()
    dp.include_router(main_router)
    bot = Bot(settings.token, parse_mode=ParseMode.MARKDOWN_V2)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())