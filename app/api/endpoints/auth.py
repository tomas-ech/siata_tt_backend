from app.config import security
from app.models.user import User
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.dto.user import UserCreate, UserResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user_in.email).first():
        raise HTTPException(status_code=400, detail="El email ya está registrado")
    
    if db.query(User).filter(User.identity_number == user_in.identity_number).first():
        raise HTTPException(status_code=400, detail="El número de identidad ya existe")

    hashed_pw = security.get_password_hash(user_in.password)
    
    db_user = User(
        email=user_in.email,
        name=user_in.name,
        identity_number=user_in.identity_number,
        contact_phone=user_in.contact_phone,
        hashed_password=hashed_pw
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/login")
def login(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    
    user = db.query(User).filter(User.email == form_data.username).first()
    
    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = security.create_access_token(data={"sub": str(user.id)})
    
    return {"access_token": access_token, "token_type": "bearer"}