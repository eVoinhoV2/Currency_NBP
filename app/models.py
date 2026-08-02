from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Currency(Base):
    __tablename__ = "Currency"

    id = Column(Integer, primary_key=True)
    currency = Column(String)
    code = Column(String)
    bid = Column(Float)
    ask = Column(Float)
    ingest_date = Column(Date)
    path_to_source= Column(String)