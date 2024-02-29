from sqlalchemy import  insert

from bot.schemas.users import UserTelegramView

from db import(
    Action,
    create_async_session, 
    async_session_maker)

from bot.schemas.users import User


async def insert_action(telegram_id:str, log_message:str) -> int:
    stmt = insert(Action).values(telegram_id=str(telegram_id), action=log_message).returning(Action.id)
    async with create_async_session(async_session_maker) as session:
        action_id = await session.execute(stmt)
    return action_id