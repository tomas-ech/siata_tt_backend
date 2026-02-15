from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

class DeliveryPlanCreate(BaseModel):
    user_id: int
    product_id: int
    amount: int = Field(..., gt=0)
    delivery_type_id: int
    ship_cost: float = Field(..., ge=0)
    delivery_date: datetime
    destination_id: int
    is_marine: bool = False
    
class DeliveryPlanResponse(BaseModel):
    id: int
    user_id: int
    product_id: int
    delivery_type_id: int
    amount: int
    ship_cost: float
    price: float
    discount: float
    tracking_code: str
    registry_date: datetime
    delivery_date: datetime
    
    model_config = ConfigDict(from_attributes=True)