import csv
from datetime import datetime
from app.models import Transaction

def load_csv(file_path: str, db):
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            txn = Transaction(
                transaction_id=int(row['transaction_id']),
                date=datetime.strptime(row['date'], "%Y-%m-%d").date(),
                amount=float(row['amount']),
                merchant=row['merchant'],
                description=row['description']
            )
            db.add(txn)
        db.commit()


