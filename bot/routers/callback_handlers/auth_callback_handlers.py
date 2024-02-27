from aiogram import F, Router
from aiogram.types import CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext

from bot.routers.fsm.auth_fsm import Auth
from bot.keybords.inline_keyboards.auth_inline import Action, AuthCbData
from bot.static.text.messages.auth_messages import PERSONAL_NUMBER
from bot.static.paths import PERSONAL_NUMBER_PATH

router = Router(name=__name__)


@router.callback_query(AuthCbData.filter(F.action == Action.auth))
async def handle_auth(call: CallbackQuery, state: FSMContext):
    await call.answer()
    photo = FSInputFile(PERSONAL_NUMBER_PATH)
    await call.message.answer_photo(
        photo=photo,
        caption=PERSONAL_NUMBER
    )
    await call.message.delete()
    await state.set_state(Auth.personal_number)