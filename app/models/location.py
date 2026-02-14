from .base import Base
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column


class Storehouse(Base):
    __tablename__ = "storehouses"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    
    address: Mapped[str] = mapped_column(Text, nullable=True)


class Port(Base):
    __tablename__ = "ports"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    
    address: Mapped[str] = mapped_column(Text, nullable=True)
