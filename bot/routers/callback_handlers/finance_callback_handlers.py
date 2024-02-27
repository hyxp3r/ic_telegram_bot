from aiogram import F, Router
from aiogram.types import CallbackQuery, FSInputFile

from bot.keybords.inline_keyboards.ic_inline import Action, IcCbData
from bot.static.text.messages.finance_messages import make_finance_message_true
from bot.static.paths import PAYMENT_PATH
from bot.services.db.auth import get_api_key
from bot.services.http.finance import get_finance

router = Router(name=__name__)


@router.callback_query(IcCbData.filter(F.action == Action.finance))
async def handle_check_finance(call: CallbackQuery):
    await call.answer()
    document = FSInputFile(PAYMENT_PATH)
    api_key = await get_api_key(str(call.from_user.id))
    response = await get_finance(api_key)
    if response.status == 200:
        response_json = await response.json()
        message = make_finance_message_true(response_json)
        await call.message.answer_document(
                                            document=document,
                                            caption=message)
    elif response.status == 404:
        pass
        

    await call.message.delete()