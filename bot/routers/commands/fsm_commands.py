from aiogram import  F, Router, types
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    Message,
    ReplyKeyboardRemove,
)

from bot.keybords.inline_keyboards.auth_inline import build_auth_kb
from bot.static.text.messages.start_message import START_MESSAGE
from bot.static.text.messages.auth_messages import CANCEL
from bot.services.db.auth import get_student_telegram_view


router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: types.Message,  state: FSMContext):
    if await state.get_state():
        return
    if await get_student_telegram_view(message.from_user.id):
        return
    await message.answer(
                        text=START_MESSAGE,
                        reply_markup=build_auth_kb())
    
@router.message(Command("cancel"))
@router.message(F.text.casefold() == "cancel")
async def cancel_handler(message: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if not current_state :
        return
    await state.clear()
    await message.answer(
        CANCEL,
        reply_markup=ReplyKeyboardRemove(),
    )