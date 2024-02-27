from pydantic_settings import BaseSettings

class TelegramBot(BaseSettings):

    token: str

    class Config:
        env_prefix = "TG_"
        env_file = '.env'


class ApiUrls(BaseSettings):
    send_code: str
    verify_code: str
    check_finance: str

    class Config:
        env_prefix = "API_"
        env_file = ".env"

