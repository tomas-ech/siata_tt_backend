from pydantic import BaseModel, EmailStr, Field, ConfigDict
from datetime import datetime

class UserBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    identity_number: str = Field(..., min_length=5, max_length=20)
    email: EmailStr
    contact_phone: str | None = Field(None, max_length=15)


class UserResponse(UserBase):
    id: int
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)