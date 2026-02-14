from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Float, ForeignKey, DateTime
from typing import Optional

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    identity_number: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    contact_phone: Mapped[Optional[str]] = mapped_column(String(20))

class ProductType(Base):
    __tablename__ = "product_types"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(255))

class DeliveryPlan(Base):    
    __tablename__ = "delivery_plans"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    product_type_id: Mapped[int] = mapped_column(ForeignKey("product_types.id"))
    amount: Mapped[int] = mapped_column(nullable=False)
    registry_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(datetime.timezone.utc)) 
    delivery_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    shipping_price: Mapped[float] = mapped_column(Float, nullable=False)
    discount: Mapped[float] = mapped_column(Float, default=0.0)
    tracking_code: Mapped[str] = mapped_column(String(10), unique=True, nullable=False)
    user: Mapped["User"] = relationship()
    product_type: Mapped["ProductType"] = relationship()

class LandLogistic(Base):
    __tablename__ = "land_logistics"

    id: Mapped[int] = mapped_column(primary_key=True)
    delivery_plan_id: Mapped[int] = mapped_column(ForeignKey("delivery_plans.id"))
    warehouse_delivery: Mapped[str] = mapped_column(String(100), nullable=False)
    vehicle_license: Mapped[str] = mapped_column(String(6), nullable=False)
    
    delivery_plan: Mapped["DeliveryPlan"] = relationship()

class MarineLogistic(Base):
    __tablename__ = "marine_logistics"

    id: Mapped[int] = mapped_column(primary_key=True)
    delivery_plan_id: Mapped[int] = mapped_column(ForeignKey("delivery_plans.id"))
    port_delivery: Mapped[str] = mapped_column(String(100), nullable=False)
    fleet_number: Mapped[str] = mapped_column(String(8), nullable=False)
    delivery_plan: Mapped["DeliveryPlan"] = relationship()