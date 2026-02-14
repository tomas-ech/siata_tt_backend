from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.dto.user import UserCreate, UserResponse
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=UserResponse)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    user_exists = db.query(User).filter(User.email == user_in.email).first()
    if user_exists:
        raise HTTPException(status_code=400, detail="El email ya está registrado")
    
    new_user = User(**user_in.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user