from fastapi import FastAPI
from sqlmodel import SQLModel

from database import engine  # Подключение к базе данных
from router import users  # Импортируем роуты из файла

app = FastAPI()


# Создание таблиц
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

# Подключаем маршруты
app.include_router(users.router,  prefix="/users")
