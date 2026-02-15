from typing import List
from app.models.user import User
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.utils.auth.get_user import get_user
from app.dto.user import UserCreate, UserResponse
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()

@router.post("/", response_model=UserCreate)
def create_user(user_in: UserCreate, db: Session = Depends(get_db),
    ):
    
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
def get_all_users(
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_user)
    ):
    
    return db.query(User).all();