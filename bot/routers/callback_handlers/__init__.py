from aiogram import Router

from bot.routers.callback_handlers.auth_callback_handlers import router as auth_callback_router
from bot.routers.callback_handlers.finance_callback_handlers import router as finance_callback_router
router = Router(name=__name__)


router.include_routers(
    auth_callback_router,
    finance_callback_router
)