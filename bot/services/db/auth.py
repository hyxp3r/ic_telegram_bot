from sqlalchemy import select, insert

from bot.schemas.users import UserTelegramView

from db import(
    Student,
    create_async_session, 
    async_session_maker)

from bot.schemas.users import User


async def insert_user(user:User) -> int:
    stmt = insert(Student).values(**user.model_dump()).returning(Student.id)
    async with create_async_session(async_session_maker) as session:
        sudent_id = await session.execute(stmt)
    return sudent_id

async def get_student_telegram_view(telegram_id:str) -> UserTelegramView | None:
    stmt = select(Student).filter_by(telegram_id=telegram_id)
    async with create_async_session(async_session_maker) as session:
        res = await session.execute(stmt)
        student = res.one_or_none()
    if student:
        return student[0].make_user_view()

async def get_api_key(telegram_id:str) -> str | None:
    stmt = select(Student.api_key).filter_by(telegram_id=telegram_id)
    async with create_async_session(async_session_maker) as session:
        res = await session.execute(stmt)
        api_key = res.scalar_one_or_none()
    return api_key