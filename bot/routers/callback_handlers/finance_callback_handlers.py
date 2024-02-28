from aiogram import F, Router
from aiogram.types import CallbackQuery, FSInputFile

from bot.keybords.inline_keyboards.ic_inline import Action, IcCbData, build_ic_kb, build_finance_kb
from bot.static.text.messages.finance_messages import make_finance_message_true, make_finance_message_false
from bot.static.text.messages.home_messages import make_home_message
from bot.static.paths import PAYMENT_PATH
from bot.services.db.auth import get_api_key
from bot.services.http.finance import get_finance

router = Router(name=__name__)


@router.callback_query(IcCbData.filter(F.action == Action.finance))
async def handle_check_finance(call: CallbackQuery, user_info):
    await call.answer()
    document = FSInputFile(PAYMENT_PATH)
    response = await get_finance(user_info.api_key)
    await call.message.delete()
    if response.status == 200:
        response_json = await response.json()
        message = make_finance_message_true(response_json)
        await call.message.answer_document(
                                            document=document,
                                            caption=message
                                            ,reply_markup=build_finance_kb())
    elif response.status == 404:
        message = make_finance_message_false()
        await call.message.answer_document(
                                            document=document,
                                            caption=message
                                            ,reply_markup=build_finance_kb())


@router.callback_query(IcCbData.filter(F.action == Action.root))
async def handle_root(call: CallbackQuery, user_info):
    text = await make_home_message(user_info)
    await call.message.delete()
    await call.message.answer(
        text=text,
        reply_markup=build_ic_kb())