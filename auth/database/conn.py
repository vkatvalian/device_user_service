import os

from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine)

DATABASE_URI = "postgresql://picverse:fedidb@localhost:5432/fedidb?sslmode=disable"

metadata = MetaData()

users_table = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(50)),
    Column('device', String(20)),
    Column('country', String(20)),
)

def get_connection():
    return create_engine(DATABASE_URI)
