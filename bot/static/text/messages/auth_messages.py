from bot.static.text.refactor import refactor_text

PERSONAL_NUMBER = """
Введите личный номер студента\\.

💡Если вы забыли его, вы всегда можете посмотреть его в [Личном кабинете студента](https://lk.nsuem.ru/user/profile)\\!"""

PERSONAL_NUMBER_ERROR_VALIDATION = refactor_text("""
⚠️ *Личный номер может состоять только из цифр!*

Введите личный номер повторно: """)

PERSONAL_NUMBER_ERROR_NOT_FOUND = refactor_text("""
⚠️ *Студент с введенным личным номером не найден!*

Введите личный номер повторно: """)

def make_masked_email(email:str) -> str:
    username, domain = email.split('@')
    masked_email = username[0] + '\\*' * (len(username) - 1) + '@' + domain
    VERIFICATION_USER = f"""
На вашу личную почту {masked_email} был отправлен код подтверждения!

Если письмо не приходит, или указанная почта не принадлежит вам, вы можете обратиться в Информационный центр:
*Номер телефона:* [+7(383)-383-07-49]
*E-mail:* ic@nsuem.ru

💡Код подтверждения будет актуален в течении *5 минут*! Учитывайте регистр при вводе кода.

Введите код подтверждения: """  
    return refactor_text(VERIFICATION_USER)