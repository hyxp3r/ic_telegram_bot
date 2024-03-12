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
    logging.info("Вебхук установлен")


def main() -> None:
    settings = TelegramBot()

    dp = Dispatcher()
    dp.include_router(main_router)
    dp.startup.register(on_startup)
    logging.info("Зарегистрирован")

    bot = Bot(settings.token, parse_mode=ParseMode.MARKDOWN_V2)
    logging.info("Бот старт")

    app = web.Application()
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
    )
    logging.info("web")
    webhook_requests_handler.register(app, web_hook_settings.path)
    #setup_application(app, dp, bot=bot)
    logging.info("set up")
    #web.run_app(app, host=web_settings.host, port=web_settings.port)
    return app
    logging.info("run web")
    #await dp.start_polling(bot)



logging.basicConfig(level=logging.INFO, stream=sys.stdout)
app = main()