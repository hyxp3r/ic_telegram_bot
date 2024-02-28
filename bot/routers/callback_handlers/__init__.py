from aiogram import Router

from bot.routers.callback_handlers.auth_callback_handlers import router as auth_callback_router
from bot.routers.callback_handlers.finance_callback_handlers import router as finance_callback_router
from bot.routers.middlewares.user import UserInternalCallbackMiddleware
router = Router(name=__name__)

finance_callback_router.callback_query.outer_middleware(UserInternalCallbackMiddleware())
router.include_routers(
    auth_callback_router,
    finance_callback_router
)
