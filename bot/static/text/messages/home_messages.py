from bot.static.text.refactor import refactor_text
from bot.schemas.users import UserTelegramView


async def make_home_message(user_info: UserTelegramView ) -> str:
    HOME = f"""
*Личный номер*: {user_info.personal_number}
*ФИО*: {user_info.fio}
*Направление подготовки*: {user_info.program}
*Группа*: {user_info.group}
"""
    HOME = refactor_text(HOME)
    return HOME
