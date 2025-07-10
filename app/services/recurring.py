from sqlalchemy.orm import Session
from app.models import Transaction
from collections import defaultdict
from datetime import timedelta

def detect_recurring_subscriptions(db: Session):
    recurring = []
    grouped = defaultdict(list)

    # Step 1: Group transactions by (merchant, amount)
    txns = db.query(Transaction).order_by(Transaction.date).all()
    for txn in txns:
        key = (txn.merchant.lower(), round(txn.amount, 2))
        grouped[key].append(txn)

    # Step 2: Look for ~monthly recurrence
    for (merchant, amount), txn_list in grouped.items():
        if len(txn_list) < 3:
            continue  # Need at least 3 to assume a pattern

        intervals = []
        for i in range(1, len(txn_list)):
            delta = (txn_list[i].date - txn_list[i - 1].date).days
            intervals.append(delta)

        avg_interval = sum(intervals) / len(intervals)
        if 28 <= avg_interval <= 32:
            recurring.append({
                "merchant": merchant,
                "amount": amount,
                "occurrences": len(txn_list),
                "average_interval_days": avg_interval,
            })

    return recurring

