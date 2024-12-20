from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlmodel import SQLModel
from router import users  # Импортируем роуты из файла
from database import engine  # Подключение к базе данных

app = FastAPI()


# Создание таблиц
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

# Подключаем маршруты
app.include_router(users.router,  prefix="/users")
