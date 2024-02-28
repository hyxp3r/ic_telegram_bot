from datetime import datetime

from bot.static.text.refactor import refactor_text


def make_finance_message_true(response:dict):
    sum  = response.get("sum")
    contract_number = response.get("contract_number")
    file_created_time = response.get("file_created_time")
    date_obj = datetime.fromisoformat(file_created_time[:-1])
    formatted_date = date_obj.strftime("%d.%m.%Y")
    FINANCE_TRUE = f"""
❗ У вас обнаружена финансовая задолженность.

*Номер договора*: {contract_number}
*Сумма задолженности*: ||{sum}|| руб.
Сведения актуальны на *{formatted_date}*

💡 Вы можете внести оплату за образовательные услуги через любой удобный для вас банк, воспользовавшись приложенными реквизитами.
"""
    FINANCE_TRUE = refactor_text(FINANCE_TRUE)
    return FINANCE_TRUE

def make_finance_message_false():

    FINANCE_FALSE = f"""
✅ Финансовая задолженность не обнаружена.

💡 Вы можете внести оплату за образовательные услуги через любой удобный для вас банк, воспользовавшись приложенными реквизитами.
"""
    FINANCE_FALSE = refactor_text(FINANCE_FALSE)
    return FINANCE_FALSE