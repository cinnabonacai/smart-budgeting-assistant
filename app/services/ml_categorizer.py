import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
from sqlalchemy.orm import Session
from app.models import Transaction

# Train model from labeled CSV
def train_model(csv_path="data/transactions.csv", model_path="model.pkl"):
    # Load data
    df = pd.read_csv(csv_path)

    # Combine merchant + description as input text
    df["text"] = df["merchant"].fillna('') + " " + df["description"].fillna('')
    X = df["text"]
    y = df["category"]

    # Vectorize input
    vectorizer = TfidfVectorizer()
    X_vec = vectorizer.fit_transform(X)

    # Train model
    model = LogisticRegression(max_iter=200)
    model.fit(X_vec, y)

    # Save model and vectorizer
    joblib.dump((model, vectorizer), model_path)
    return f"Model trained and saved to {model_path}"

# Predict categories using trained model
def predict_categories(db: Session, model_path="model.pkl"):
    # Load model and vectorizer
    model, vectorizer = joblib.load(model_path)

    results = []
    txns = db.query(Transaction).all()

    for txn in txns:
        text = (txn.merchant or "") + " " + (txn.description or "")
        X_vec = vectorizer.transform([text])
        category = model.predict(X_vec)[0]

        results.append({
            "transaction_id": txn.transaction_id,
            "merchant": txn.merchant,
            "amount": txn.amount,
            "date": txn.date,
            "predicted_category": category
        })

    return results

