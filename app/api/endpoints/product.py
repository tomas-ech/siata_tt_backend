from typing import List
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.models.product import Product
from fastapi import APIRouter, Depends
from app.dto.product import ProductResponse
from app.utils.auth.get_user import get_user

router = APIRouter()

@router.get("/", response_model=List[ProductResponse])
def get_all_users(
    db: Session = Depends(get_db),
    current_user_id: int = Depends(get_user)
    ):
    
    return db.query(Product).all();