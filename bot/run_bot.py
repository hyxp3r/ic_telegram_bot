import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

from bot.config import TelegramBot, WebServer, Webhook
from bot.routers import router as main_router

web_settings = WebServer()
web_hook_settings = Webhook()

async def on_startup(bot: Bot) -> None:
    await bot.set_webhook(f"{web_hook_settings.url}{web_hook_settings.path}")


async def main() -> None:
    settings = TelegramBot()

    dp = Dispatcher()
    dp.include_router(main_router)
    dp.startup.register(on_startup)

    bot = Bot(settings.token, parse_mode=ParseMode.MARKDOWN_V2)

    app = web.Application()
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
    )
    webhook_requests_handler.register(app, path=web_hook_settings.path)
    setup_application(app, dp, bot=bot)

    web.run_app(app, host=web_settings.host, port=web_settings.port)
    #await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())