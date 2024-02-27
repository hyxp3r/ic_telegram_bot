from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession

@asynccontextmanager
async def create_async_session(async_session: Any = AsyncSession, **kwargs: Any) -> AsyncGenerator[AsyncSession, None]:
    new_async_session = async_session(**kwargs)
    try:
        yield new_async_session
        await new_async_session.commit()
    except Exception:
        await new_async_session.rollback()
        raise
    finally:
        await new_async_session.close()