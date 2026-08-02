from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.dialects.postgresql import UUID
import uuid
from .base import Base


class Currency(Base):
    __tablename__ = "Currency"

    id = Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    currency = Column("currency", String)
    code = Column("code", String)
    bid = Column("bid", Float)
    ask = Column("ask", Float)
    ingest_date = Column("ingest_date", Date)
    path_to_source= Column("path_to_source", String)

    def __init__(self, currency, code, bid, ask, ingest_date, path_to_source):
        self.currency = currency
        self.code = code
        self.bid = bid 
        self.ask = ask 
        self.ingest_date = ingest_date
        self.path_to_source = path_to_source