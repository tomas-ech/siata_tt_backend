from typing import List
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.models.delivery import DeliveryPlan
from fastapi import APIRouter, Depends, HTTPException
from app.services.delivery_service import DeliveryService
from app.dto.delivery import DeliveryPlanResponse, DeliveryPlanCreate

router = APIRouter()

@router.get("/", response_model=list[DeliveryPlanResponse])
def get_all_deliveries(db: Session = Depends(get_db)):
    return db.query(DeliveryPlan).all()

@router.get("/user/{user_id}", response_model=List[DeliveryPlanResponse])
def get_deliveries_by_user(user_id: int, db: Session = Depends(get_db)):
    
    deliveries_by_user = db.query(DeliveryPlan)\
        .filter(DeliveryPlan.user_id == user_id)\
        .all()
    
    return deliveries_by_user

@router.post("/", response_model=DeliveryPlanResponse)
def create_delivery_plan(plan_in: DeliveryPlanCreate, db: Session = Depends(get_db)):
    service = DeliveryService(db)
    
    new_plan = service.generate_delivery_plan(plan_in)
    
    return new_plan

@router.get("/{delivery_id}", response_model=DeliveryPlanResponse)
def get_delivery_by_id(delivery_id: int, db: Session = Depends(get_db)):
    db_plan = db.query(DeliveryPlan).filter(DeliveryPlan.id == delivery_id).first()
    if not db_plan:
        raise HTTPException(status_code=404, detail="Plan de entrega no encontrado")
    return db_plan

