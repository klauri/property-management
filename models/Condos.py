from pydantic import BaseModel
from typing import Optional

class Owner(BaseModel):
    owner_id: int
    first_name: str
    last_name: str
    suffix: str
    phone_number: str
    cell_number: Optional[str]
    email: str
    billing_addr_street: str
    billing_addr_city: str
    billing_addr_state: str    

class Condo(BaseModel):
    condo_id: int
    owner_id: int
    has_pets: bool
    dog_amount: Optional[str]
    cat_amount: Optional[str]
    occupants: int
    rental: bool = False
