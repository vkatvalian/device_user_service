import os

from sqlalchemy import (MetaData, create_engine)

DATABASE_URI = ""

engine = create_engine(DATABASE_URI)
metadata = MetaData()

def get_connection():
    return create_engine(DATABASE_URI)
