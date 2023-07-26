from models.user import User
from database import *
from sqlalchemy import insert

def add_user(payload: User):
    usr = users_table.insert().values(name = payload.name, device = payload.device, country = payload.country)
    cn = get_connection()
    conn = cn.connect()
    conn.execute(usr)
