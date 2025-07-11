from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.services.recurring import detect_recurring_subscriptions
from app.services.categorization import categorize_transactions
from app.services.categorization import summarize_by_category
from app.services.ml_categorizer import predict_categories


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/subscriptions")
def get_subscriptions(db: Session = Depends(get_db)):
    return detect_recurring_subscriptions(db)

@router.get("/categorized")
def get_categorized_transactions(db: Session = Depends(get_db)):
    return categorize_transactions(db)

@router.get("/summary")
def get_category_summary(db: Session = Depends(get_db)):
    return summarize_by_category(db)

@router.get("/ml-categorized")
def get_ml_categorized(db: Session = Depends(get_db)):
    return predict_categories(db)
