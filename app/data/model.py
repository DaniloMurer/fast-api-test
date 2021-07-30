from enum import Enum
from pydantic import BaseModel
from typing import Optional

class Category(str, Enum):
    LAPTOP = "laptop"
    KITCHEN = "kitchen"
    ELECTRONICS = "electronics"

class MyEmployee(BaseModel):
    first_name: str
    last_name: str
    email: str
    mobile_phone: Optional[str] = None

