from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    name: str
    country: str
    device: str

class UserResponse(User):
    id: int
