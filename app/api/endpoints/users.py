from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.dto.user import UserCreate, UserResponse
from app.models.user import User
from typing import List

router = APIRouter()

@router.post("/", response_model=UserCreate)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    
    email_exists = db.query(User).filter(User.email == user_in.email).first()
    
    identity_exists = db.query(User).filter(User.identity_number == user_in.identity_number).first()
    
    if email_exists or identity_exists:
        raise HTTPException(status_code=400, detail="El usuario ya está registrado")
    
    new_user = User(**user_in.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/", response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    
    return db.query(User).all();