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



class WebServer(BaseSettings):
    host:str
    port:int


    class Config:
        env_prefix = "WEB_SERVER_"
        env_file = ".env"

class Webhook(BaseSettings):
    path:str
    url:str

    class Config:
        env_prefix = "WEBHOOK_"
        env_file = ".env"