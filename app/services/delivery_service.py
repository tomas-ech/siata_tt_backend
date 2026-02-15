import uuid
import random
import string
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.delivery import DeliveryPlan
from app.dto.delivery import DeliveryPlanCreate
from app.models.logistic import LandLogistic, MarineLogistic

class DeliveryService:
    def __init__(self, db: Session):
        self.db = db

    def generate_transport_id(self, is_marine: bool) -> str:
        
        letters = "".join(random.choices(string.ascii_uppercase, k=3))
        
        if is_marine:
            
            numbers = "".join(random.choices(string.digits, k=4))
            last_letter = random.choice(string.ascii_uppercase)
            
            return f"{letters}{numbers}{last_letter}"
            
        else:
            numbers = "".join(random.choices(string.digits, k=3))
            
            return f"{letters}{numbers}"

    def generate_delivery_plan(self, plan_data: DeliveryPlanCreate):
        
        normal_price = plan_data.ship_cost * plan_data.amount
        rate = 0.03 if plan_data.is_marine else 0.05
        discount = (normal_price * rate) if plan_data.amount > 10 else 0.0
        
        new_plan = DeliveryPlan(
            user_id=plan_data.user_id,
            product_id=plan_data.product_id,
            amount=plan_data.amount,
            ship_cost=plan_data.ship_cost,
            price=normal_price,
            discount=discount,
            tracking_code=str(uuid.uuid4()).upper()[:10],
            delivery_date=plan_data.delivery_date
        )

        try:
            self.db.add(new_plan)
            self.db.flush()

            transport_id = self.generate_transport_id(plan_data.is_marine)

            if not plan_data.is_marine:
                details = LandLogistic(
                    delivery_plan_id=new_plan.id,
                    delivery_storehouse_id=plan_data.destination_id,
                    vehicle_license=transport_id
                )
            else:
                details = MarineLogistic(
                    delivery_plan_id=new_plan.id,
                    delivery_port_id=plan_data.destination_id,
                    fleet_number=transport_id 
                )

            self.db.add(details)
            self.db.commit()
            self.db.refresh(new_plan)
            return new_plan

        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=400, detail=str(e))