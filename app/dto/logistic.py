from pydantic import BaseModel
from pydantic import Field

class LandLogisticCreate(BaseModel):
    delivery_storehouse_id: int
    vehicle_license: str = Field(min_length=6, max_length=6, pattern="^[A-Z]{3}\\d{3}$")


class MarineLogisticCreate(BaseModel):
    delivery_port_id: int
    fleet_number: str = Field(min_length=8, max_length=8, pattern="^[A-Z]{3}\\d{4}[A-Z]$")