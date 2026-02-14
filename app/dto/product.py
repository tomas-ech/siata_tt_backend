from pydantic import BaseModel, Field, ConfigDict

class ProductBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    description: str | None = Field(None, max_length=500)
    product_type_id: int
    

class ProductResponse(ProductBase):
    id: int
    
    model_config = ConfigDict(from_attributes=True)


class ProductTypeResponse(BaseModel):
    id: int
    name: str
    description: str | None
    
    model_config = ConfigDict(from_attributes=True)