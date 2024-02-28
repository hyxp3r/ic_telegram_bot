from pydantic import BaseModel


class User(BaseModel):
    telegram_id: str
    fio: str
    personal_number: str
    group: str
    program: str
    form: str
    api_key: str
    

class UserTelegramView(BaseModel):
    personal_number: str
    fio: str
    program: str
    group: str
    api_key:str

    class Config:
        from_attributes = True

    

