from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.backend.core.config import CONNECTION_STRING
from models.base import Base


engine = create_engine(CONNECTION_STRING)
SessionLocal = sessionmaker(bind=engine, autocommit=False)


def get_session():
    Base.metadata.create_all(bind=engine)
    return SessionLocal