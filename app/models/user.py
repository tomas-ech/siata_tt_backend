from .base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    name: Mapped[str] = mapped_column(String(100))
    
    identity_number: Mapped[str] = mapped_column(String(50), unique=True)
    
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    
    contact_phone: Mapped[str] = mapped_column(String(20))
    
    hashed_password: Mapped[str] = mapped_column(String(20), nullable=False)