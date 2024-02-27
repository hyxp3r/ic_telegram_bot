__all__ = ("router",)

from aiogram import Router

from bot.routers.commands import router as base_router
from bot.routers.fsm.auth_fsm import router as auth_fsm_router
from bot.routers.callback_handlers import router as callback_router


router = Router(name=__name__)


router.include_routers(
    base_router,
    auth_fsm_router,
    callback_router,
)