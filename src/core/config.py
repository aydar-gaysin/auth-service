from pydantic_settings import BaseSettings
from logging import config as logging_config

from src.core.logger import LOGGING

logging_config.dictConfig(LOGGING)


class Settings(BaseSettings):
    """
    Указаны значения по умолчанию. При запуске приложения Pydantic BaseSettings загружает переменные окружения из файла, указанного в env_file (.env)
    и переопределяет значения по умолчанию.
    """
    PROJECT_NAME: str = 'Auth Service'
    REDIS_HOST: str = '127.0.0.1'
    REDIS_PORT: int = 6379

    POSTGRES_USER: str = 'postgres'
    POSTGRES_PASSWORD: str = 'password'
    POSTGRES_SERVER: str = 'localhost'
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = 'database_name'
    POSTGRES_SCHEMA: str = 'default_schema'
    POSTGRES_TABLE: str = 'default_table'

    @property
    def database_url(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    class Config:
        env_file = ".env"


app_settings = Settings()
