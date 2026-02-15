from .base import Base
from datetime import datetime
from typing import Optional, TYPE_CHECKING
from sqlalchemy import String, Numeric, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .logistic import LandLogistic, MarineLogistic
    
class DeliveryType(Base):
    __tablename__ = "delivery_types"
    id: Mapped[int] = mapped_column(primary_key=True)
    
    name: Mapped[str] = mapped_column(String(50))
    
    description: Mapped[str] = mapped_column(String(100))
    

class DeliveryPlan(Base):    
    __tablename__ = "delivery_plans"

    id: Mapped[int] = mapped_column(primary_key=True)
    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)
    
    delivery_type_id: Mapped[int] = mapped_column(ForeignKey("delivery_types.id"), nullable=False)
    
    amount: Mapped[int] = mapped_column(nullable=False)
    
    ship_cost: Mapped[float] = mapped_column(Numeric(12, 2), nullable=False)
    
    tracking_code: Mapped[str] = mapped_column(String(10), unique=True, nullable=False)
    
    price: Mapped[float] = mapped_column(Numeric(12, 2), nullable=False)
    
    discount: Mapped[float] = mapped_column(Numeric(12, 2), default=0.0)
    
    registry_date: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    
    delivery_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    land_logistic: Mapped[Optional["LandLogistic"]] = relationship(back_populates="delivery_plan")
    
    marine_logistic: Mapped[Optional["MarineLogistic"]] = relationship(back_populates="delivery_plan")