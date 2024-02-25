import sqlalchemy as sa

from db.base import BaseTable


class Action(BaseTable):
    """Таблица со студентами"""
    telegram_id = sa.Column(sa.String(255), nullable=False, unique=True, doc='Telelgram ID')
    action = sa.Column(sa.String(255), nullable=False, doc='Действие')