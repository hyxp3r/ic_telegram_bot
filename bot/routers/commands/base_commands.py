from aiogram import  Router, types
from aiogram.filters import CommandStart

from bot.keybords.inline_keyboards.auth_inline import build_auth_kb
from bot.static.text.messages.start_message import START_MESSAGE


router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(
                        text=START_MESSAGE,
                        reply_markup=build_auth_kb())