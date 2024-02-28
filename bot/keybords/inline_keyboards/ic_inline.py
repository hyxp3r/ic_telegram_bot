from enum import Enum

from aiogram.types import InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.static.text.buttons.home_buttons import (
                                                    IC_SITE,
                                                    IC_SITE_URL,
                                                    IC_SITE_GROUP,
                                                    IC_GROUP,
                                                    FINANCE,
                                                    ROOT
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
        url=IC_SITE_URL
    )
    builder.button(
        text=IC_GROUP,
        url=IC_SITE_GROUP
    )
    builder.button(
        text=FINANCE,
        callback_data=IcCbData(action=Action.finance).pack()
    )
    builder.adjust(1)
    return builder.as_markup()

def build_finance_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text=ROOT,
        callback_data=IcCbData(action=Action.root).pack()
    )
    builder.adjust(1)
    return builder.as_markup()
