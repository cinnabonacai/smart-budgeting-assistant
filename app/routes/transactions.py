from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils.csv_loader import load_csv
from app.database import SessionLocal
from app.models import Transaction

router = APIRouter()

# Reusable DB session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Load transactions from CSV
@router.get("/load")
def load_data(db: Session = Depends(get_db)):
    load_csv("data/transactions.csv", db)
    return {"message": "Transactions loaded"}

# Clear transactions table (for testing)
@router.delete("/clear")
def clear_transactions(db: Session = Depends(get_db)):
    db.query(Transaction).delete()
    db.commit()
    return {"message": "All transactions cleared"}

