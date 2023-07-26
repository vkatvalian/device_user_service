from typing import List
from fastapi import APIRouter, HTTPException
from models.subscriptions import UserModel, SubResponse, Subscribers
from database import conn

subscriptions = APIRouter()

# hardcoded model for the subscriptions
country_currency = {
    'us': 'dollar',
    'am': 'amd',
    'fr': 'euro'
}

device_os = {
    'ios': 'apple',
    'android': 'samsung',
    'manjaro': 'pinephone'
}

@subscriptions.post('/add', response_model=SubResponse, status_code=201)
def create_movie(payload: UserModel):
    subout = Subout
    subs = Subscribers

    # this part is hardoded will not do in normal case
    rs = get_connection().execute(f"SELECT * FROM sub_plan WHERE company = 'apple' and currency = '{country_currency[payload.country]}'")
    res = rs.mappings().all()
    subs.id = res[0].id
    subs.user_id = payload.id
    rs = get_connection().execute(f'INSERT INTO subscriber VALUES({subs.id}, ARRAY [{subs.user_id}])')
    subout.currency = res[0].currency
    subout.company = res[0].company

    response = {
        'plan': subout.company,
        'currency': subout.currency,
        **payload.dict()
    }

    return response
