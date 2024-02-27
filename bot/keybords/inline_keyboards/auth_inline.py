from enum import Enum

from aiogram.types import InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.static.text.buttons.auth_buttons import START_BUTTON
class Action(str, Enum):
    auth = "auth"
    
class AuthCbData(CallbackData, prefix="auth"): 
    action: Action


def build_auth_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text=START_BUTTON,
        callback_data=AuthCbData(action=Action.auth).pack()
    )
    builder.adjust(1)
    return builder.as_markup()
