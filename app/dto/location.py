from pydantic import BaseModel, ConfigDict

class LocationBase(BaseModel):
    name: str
    address: str | None = None
    
    model_config = ConfigDict(from_attributes=True)

class StorehouseResponse(LocationBase):
    id: int

class PortResponse(LocationBase):
    id: int