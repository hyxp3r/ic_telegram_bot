from typing import Any, Dict

from pydantic import BaseModel
from pydantic_settings import BaseSettings
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine


class BaseDBModel(BaseModel):
    url: str
    engine_config: Dict[str, Any] = {}
    echo: int = 0

    @property
    def async_engine(self) -> AsyncEngine:
        return create_async_engine(str(self.url), **self.engine_config, echo=self.echo)


class DBSettings(BaseDBModel, BaseSettings):
    class Config:
        env_prefix = 'DB_'

    def setup_engine_async(self) -> AsyncEngine:
        engine = self.async_engine
        return engine