from typing import Any, Callable, Dict, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from bot.keybords.inline_keyboards.auth_inline import build_auth_kb
from bot.services.db.auth import get_student_telegram_view
from bot.static.text.messages.start_message import START_MESSAGE

class UserInternalCallbackMiddleware(BaseMiddleware):

    async def get_telegram_user(self, telegram_id: int) -> int:
        user = await get_student_telegram_view(telegram_id)
        return user

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        user = data["event_from_user"]
        user_from_db = await self.get_telegram_user(user.id)
        if not user_from_db:
            await event.bot.delete_message(chat_id=event.message.chat.id, message_id=event.message.message_id)
            await event.message.answer(
                                        text=START_MESSAGE,
                                        reply_markup=build_auth_kb()
                                       )
            return
        data["user_info"] = user_from_db
        return await handler(event, data)
    

class UserInternalMessageMiddleware(BaseMiddleware):

    async def get_telegram_user(self, telegram_id: int) -> int:
        user = await get_student_telegram_view(telegram_id)
        return user

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        user = data["event_from_user"]
        user_from_db = await self.get_telegram_user(user.id)
        if not user_from_db:
            await event.bot.delete_message(chat_id=event.chat.id, message_id=event.message_id)
            await event.answer(
                                        text=START_MESSAGE,
                                        reply_markup=build_auth_kb()
                                       )
            return
        data["user_info"] = user_from_db
        return await handler(event, data)
    
