from fastapi import APIRouter, HTTPException
from typing import List
from models.user import User, UserResponse
from database import manager

users = APIRouter()

@users.post('/signup', response_model=UserResponse, status_code=201)
def create_user(payload: User):
    cast_id = db_manager.add_cast(payload)

    response = {
        'id': cast_id,
        **payload.dict()
    }

    redirect(payload)

    return response
