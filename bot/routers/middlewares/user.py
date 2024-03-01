from typing import Any, Callable, Dict, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from aiogram.types.update import Update


from bot.keybords.inline_keyboards.auth_inline import build_auth_kb
from bot.services.db.auth import get_student_telegram_view
from bot.services.db.log import insert_action
from bot.static.text.messages.start_message import START_MESSAGE

class UserInternalCallbackMiddleware(BaseMiddleware):

    async def get_telegram_user(self, telegram_id: int) -> int:
        user = await get_student_telegram_view(telegram_id)
        return user
    
    async def log_user_move(self, telegram_id: int, log_message:str = "Модуль ИЦ")->int:
        action_id = await insert_action(telegram_id, log_message)
        return action_id

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        user = data["event_from_user"]

        update: Update = data["event_update"]
        """
        for keyboard in update.callback_query.message.reply_markup.inline_keyboard:
            if update.callback_query.data == keyboard[0].callback_data:
                log = keyboard[0].text
        
        print(update.callback_query.message.reply_markup.inline_keyboard[2])
        """

        user_from_db = await self.get_telegram_user(user.id)
        if not user_from_db:
            await event.bot.delete_message(chat_id=event.message.chat.id, message_id=event.message.message_id)
            await event.message.answer(
                                        text=START_MESSAGE,
                                        reply_markup=build_auth_kb()
                                       )
            return
        action_id = await self.log_user_move(telegram_id=user.id, log_message=update.callback_query.data)
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
    
