from pydantic_settings import BaseSettings

class ApiKeySettings(BaseSettings):

    token: str
