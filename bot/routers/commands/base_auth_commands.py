from aiogram import  Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.keybords.inline_keyboards.ic_inline import build_ic_kb
from bot.static.text.messages.home_messages import make_home_message


router = Router(name=__name__)


@router.message(Command("ic"))
async def ic_command_handler(message: Message, user_info) -> None:
    text = await make_home_message(user_info)
    await message.answer(
        text=text,
        reply_markup=build_ic_kb()) 
