import sqlalchemy as sa

from bot.schemas.users import UserTelegramView
from db.base import BaseTable


class Student(BaseTable):
    """Таблица со студентами"""
    telegram_id = sa.Column(sa.String(255), nullable=False, unique=True, index=True, doc='Telegram ID')
    fio = sa.Column(sa.String(255), nullable=False, doc='ФИО студента')
    personal_number = sa.Column(sa.String(10), nullable=False, doc='Личный номер студента', index=True)
    form = sa.Column(sa.String(10), nullable=False, doc='Форма')
    group = sa.Column(sa.String(100), nullable=False, doc='Группа')
    program = sa.Column(sa.String(100), nullable=False, doc='Направление')
    api_key = sa.Column(sa.String(255), nullable=True, doc='API ключ')
    
    @staticmethod
    def __make_short_fio(fio: str) -> str:
        short_fio = fio.split(' ')
        short_fio = f'{short_fio[0]} {short_fio[1][0:1]}.{short_fio[2][0:1]}.'
        return short_fio

    def make_user_view(self) -> UserTelegramView:
        short_fio = self.__make_short_fio(self.fio)
        user = UserTelegramView(
            personal_number=self.personal_number,
            fio=short_fio,
            program=self.program,
            group=self.group
        )
        return user
