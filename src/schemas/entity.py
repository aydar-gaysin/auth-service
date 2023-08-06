from uuid import UUID

from pydantic import BaseModel


class UserCreate(BaseModel):
    login: str
    password: str
    first_name: str
    last_name: str


class UserInDB(BaseModel):
    id: UUID
    first_name: str
    last_name: str

    class Config:
        """
        Благодаря этому Pydantic будет самостоятельно преобразовывать модель базы данных в объект этого класса.
        """
        orm_mode = True
