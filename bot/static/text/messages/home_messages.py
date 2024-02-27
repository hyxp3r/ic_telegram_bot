from bot.services.db.auth import get_student_telegram_view
from bot.static.text.refactor import refactor_text


async def make_home_message(telegram_id:str):
    user = await get_student_telegram_view(telegram_id)
    HOME = f"""
*Личный номер*: {user.personal_number}
*ФИО*: {user.fio}
*Направление подготовки*: {user.program}
*Группа*: {user.group}
"""
    HOME = refactor_text(HOME)
    return HOME
