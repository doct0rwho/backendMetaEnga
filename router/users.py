from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from models.models import User  # Импорт модели User
from database import get_session  # Импорт функции get_session

router = APIRouter()  # Создание маршрутизатора

@router.get("/users")
def get_users(session: Session = Depends(get_session)):
    users = session.exec(select(User)).all()
    return users

@router.post("/users")
def create_user(user: User, session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
