import sqlalchemy as sa

from db.base import BaseTable


class Student(BaseTable):
    """Таблица со студентами"""
    telegram_id = sa.Column(sa.String(255), nullable=False, unique=True, index=True, doc='Telegram ID')
    fio = sa.Column(sa.String(255), nullable=False, doc='ФИО студента')
    personal_number = sa.Column(sa.String(10), nullable=False, doc='Личный номер студента', index=True)
    group = sa.Column(sa.String(100), nullable=False, doc='Группа')
    program = sa.Column(sa.String(100), nullable=False, doc='Направление')
    api_key = sa.Column(sa.String(255), nullable=True, doc='API ключ')
