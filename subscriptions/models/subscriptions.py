from pydantic import BaseModel
from typing import List, Optional

class UserModel(BaseModel):
    id: int
    device: str
    country: str

class SubResponse(UserModel):
    plan: str
    currency: str

class Subscribers:
    id: int
    user_id: List[int]
