from datetime import datetime

from bot.static.text.refactor import refactor_text


def make_finance_message_true(response:dict):
    sum  = response.get("sum")
    contract_number = response.get("contract_number")
    file_created_time = response.get("file_created_time")
    date_obj = datetime.fromisoformat(file_created_time[:-1])
    formatted_date = date_obj.strftime("%d.%m.%Y %H.%M")
    FINANCE_TRUE = f"""
У вас обнаружена задолженность.

*Номер договора*: {contract_number}
*Сумма*: {sum}

Сведения актуальны на *{formatted_date}*
"""
    FINANCE_TRUE = refactor_text(FINANCE_TRUE)
    return FINANCE_TRUE