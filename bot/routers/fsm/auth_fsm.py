from aiogram import  Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from bot.services.db.auth import insert_user
from bot.services.http.auth import send_verification_code, verify_code
from bot.schemas.users import User
from bot.static.text.messages.auth_messages import (make_masked_email,
                                                    PERSONAL_NUMBER_ERROR_VALIDATION,
                                                    PERSONAL_NUMBER_ERROR_NOT_FOUND)
from bot.static.text.messages.home_messages import make_home_message
from bot.keybords.inline_keyboards.ic_inline import build_ic_kb

router = Router(name = __name__)


class Auth(StatesGroup):
    personal_number = State()
    verification_code = State()



def make_user_schema(data:dict) -> User:
    user = User(
        telegram_id = data.get("telegram_id"),
        fio = data.get("fio"),
        personal_number = data.get("personal_number"),
        group = data.get("group"),
        program = data.get("program"),
        form = data.get("form"),
        api_key = data.get("api_key"),
    )
    return user

@router.message(Auth.personal_number)
async def process_personal_number(message: Message, state: FSMContext) -> None:
    try:
        int(message.text)
    except:
        await message.answer(PERSONAL_NUMBER_ERROR_VALIDATION)
        await state.set_state(Auth.personal_number)
        return None
    response = await send_verification_code(message.text)
    if response.status == 200:
        response_json = await response.json()
        email = response_json.get("email")
        await message.answer(make_masked_email(email))
        await state.update_data(personal_number = message.text)
        await state.set_state(Auth.verification_code)
    elif response.status == 404:
            await message.answer(PERSONAL_NUMBER_ERROR_NOT_FOUND)
            await state.set_state(Auth.personal_number)


@router.message(Auth.verification_code)
async def process_verification_code(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    personal_number = data.get("personal_number")
    response = await verify_code(personal_number, message.text)
    if response.status == 200:
        response_json = await response.json()
        response_json["telegram_id"] = str(message.from_user.id)
        user = make_user_schema(response_json)
        user_id = await insert_user(user)
        home_text = await make_home_message(str(message.from_user.id))
        await message.answer(
                            text=home_text,
                            reply_markup=build_ic_kb())
    elif response.status == 401:
        await message.answer("Неверный подтверждающий код\\! Введите код повторно")
        await state.set_state(Auth.verification_code)
    elif response.status == 404:
        await message.answer("Код просрочен\\! Пройдите процесс авторизации заново, использовав команду /start")
        await state.clear()



