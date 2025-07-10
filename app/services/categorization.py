from sqlalchemy.orm import Session
from app.models import Transaction

# Simple rule-based categorization by merchant keywords
CATEGORY_RULES = {
    "starbucks": "Food & Drink",
    "whole foods": "Groceries",
    "uber": "Transport",
    "spotify": "Subscription",
    "netflix": "Subscription",
    "amazon": "Shopping",
    "gym": "Fitness",
    "panera": "Food & Drink",
    "target": "Household",
    "landlord": "Rent",
    "apple": "Digital Services",
    "company payroll": "Income",
}

def categorize_transactions(db: Session):
    categorized = []

    transactions = db.query(Transaction).all()
    for txn in transactions:
        merchant = txn.merchant.lower()
        category = "Other"

        for keyword, cat in CATEGORY_RULES.items():
            if keyword in merchant:
                category = cat
                break

        categorized.append({
            "transaction_id": txn.transaction_id,
            "merchant": txn.merchant,
            "amount": txn.amount,
            "date": txn.date,
            "category": category
        })

    return categorized

def summarize_by_category(db: Session):
    category_totals = {}
    transactions = db.query(Transaction).all()

    for txn in transactions:
        merchant = txn.merchant.lower()
        category = "Other"

        for keyword, cat in CATEGORY_RULES.items():
            if keyword in merchant:
                category = cat
                break

        category_totals[category] = category_totals.get(category, 0) + txn.amount

    return category_totals

