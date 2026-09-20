from pydantic import BaseModel


class Restaurant(BaseModel):
    id: int
    name: str
    address: str
    phone_number: str
    email: str
    website: str
    cuisine_type: str
    opening_hours: str
    rating: float

class RestaurantCreate(BaseModel):
    name: str
    address: str
    phone_number: str
    email: str
    website: str
    cuisine_type: str
    opening_hours: str
    rating: float
