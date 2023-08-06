import logging

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from src.core.config import app_settings
from src.core.logger import LOGGING
from src.db.postgres import create_database


app = FastAPI(
    title=app_settings.PROJECT_NAME,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)


@app.on_event('startup')
async def startup():
    """
    SQLAlchemy будет пытаться создать все таблицы, которые ещё не существуют в базе данных.
    Эта функция не повредит существующие таблицы или данные.
    """
    await create_database()


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
        log_config=LOGGING,
        log_level=logging.DEBUG,
    )
