from .base import Base
from typing import TYPE_CHECKING
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .delivery import DeliveryPlan

class LandLogistic(Base):
    __tablename__ = "land_logistics"

    id: Mapped[int] = mapped_column(primary_key=True)
    
    delivery_plan_id: Mapped[int] = mapped_column(
        ForeignKey("delivery_plans.id", ondelete="CASCADE"), nullable=False
    )
   
    delivery_storehouse_id: Mapped[int] = mapped_column(
        ForeignKey("storehouses.id"), nullable=False
    )
    
    vehicle_license: Mapped[str] = mapped_column(String(6), nullable=False)
    
    delivery_plan: Mapped["DeliveryPlan"] = relationship()

class MarineLogistic(Base):
    __tablename__ = "marine_logistics"

    id: Mapped[int] = mapped_column(primary_key=True)
    
    delivery_plan_id: Mapped[int] = mapped_column(
        ForeignKey("delivery_plans.id", ondelete="CASCADE"), nullable=False
    )
   
    delivery_port_id: Mapped[int] = mapped_column(
        ForeignKey("ports.id"), nullable=False
    )
    
    fleet_number: Mapped[str] = mapped_column(String(8), nullable=False)
    
    delivery_plan: Mapped["DeliveryPlan"] = relationship()
    