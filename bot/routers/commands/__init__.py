__all__ = ("router",)

from aiogram import Router

from bot.routers.middlewares.user import UserInternalMessageMiddleware
from bot.routers.commands.fsm_commands import router as fsm_router
from bot.routers.commands.base_auth_commands import router as auth_command_router

auth_command_router.message.middleware(UserInternalMessageMiddleware())

router = Router(name=__name__)

router.include_routers(
    fsm_router,
    auth_command_router
)