from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from models.models import User  # Импорт модели User
from database import get_session  # Импорт функции get_session

router = APIRouter()  # Создание маршрутизатора

@router.get("/all")
def get_users(session: Session = Depends(get_session)):
    users = session.exec(select(User)).all()
    return users

@router.post("/create", status_code=201)
def create_user(user: User, session: Session = Depends(get_session)):
    print("HYETA")
    try:
        existing_user = session.exec(select(User).filter(User.id == user.id)).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="User already exists")

        session.add(user)
        session.commit()
        session.refresh(user)
        return {"status": 200, "message": "Success", "user": user}
    except Exception as e:
        print(f"Error occurred: {e}")
        raise HTTPException(status_code=500, detail=str(e))
