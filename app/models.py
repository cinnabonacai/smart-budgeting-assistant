from sqlalchemy import Column, Integer, String, Float, Date
from app.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(Integer, unique=True, index=True)
    date = Column(Date)
    amount = Column(Float)
    merchant = Column(String)
    description = Column(String)

