from fastapi import FastAPI
from service.users import users
from database.conn import *

metadata.create_all(get_connection())

app = FastAPI()

@app.on_event("startup")
def startup():
    get_connection()
    print(get_connection())

app.include_router(users)
