from enum import Enum

from aiogram.types import InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.static.text.buttons.home_buttons import (
                                                    IC_SITE,
                                                    IC_GROUP,
                                                    FINANCE
                                                )
class Action(str, Enum):
    finance = "finance"
    root = "root"
    
class IcCbData(CallbackData, prefix="ic"): 
    action: Action


def build_ic_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text=IC_SITE,
        url="https://ic.nsuem.ru/"
    )
    builder.button(
        text=IC_GROUP,
        url="https://vk.com/nsuem_ic"
    )
    builder.button(
        text=FINANCE,
        callback_data=IcCbData(action=Action.finance).pack()
    )
    builder.adjust(1)
    return builder.as_markup()
