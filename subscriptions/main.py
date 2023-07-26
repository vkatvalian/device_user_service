from fastapi import FastAPI
from services.subscribers import subscriptions
from database import *

# metadata.create_all(get_connection())
app = FastAPI()

@app.on_event("startup")
def startup():
    get_connection()

app.include_router(subscriptions)
