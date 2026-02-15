from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Numeric, ForeignKey

class ProductType(Base):
    __tablename__ = "product_types"
    id: Mapped[int] = mapped_column(primary_key=True)
    
    name: Mapped[str] = mapped_column(String(50))
    
    description: Mapped[str] = mapped_column(String(100))

class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True)
    
    name: Mapped[str] = mapped_column(String(100))
    
    description: Mapped[str] = mapped_column(String(100))
    
    price: Mapped[float] = mapped_column(Numeric(12, 2), nullable=False)
    
    type: Mapped[int] = mapped_column(ForeignKey("product_types.id"), nullable=False)
    
    product_type: Mapped["ProductType"] = relationship()