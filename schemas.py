from pydantic import BaseModel, Field

class AddressBase(BaseModel):
    street: str
    city: str
    state: str
    country: str
    postal_code: str
    latitude: float = Field(..., gt=-90, lt=90)
    longitude: float = Field(..., gt=-180, lt=180)

class AddressCreate(AddressBase):
    pass

class Address(AddressBase):
    id: int

    class Config:
        orm_mode = True
