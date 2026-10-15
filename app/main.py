from backend.core.config import CONNECTION_STRING
from backend.models.currency import Base
from backend.db.session import engine
from sqlalchemy import create_engine

def main():

    # If tables do not exist, create them
    Base.metadata.create_all(engine) 
    