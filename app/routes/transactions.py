from fastapi import APIRouter
from app.utils.csv_loader import load_csv

router = APIRouter()

@router.get("/load")
def load_data():
    load_csv("data/transactions.csv")
    return {"message": "Transactions loaded"}


