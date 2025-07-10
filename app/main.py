from fastapi import FastAPI
from app.routes import transactions
from app.routes import suggestions

app = FastAPI(title="Smart Budgeting Assistant")

app.include_router(transactions.router, prefix="/transactions")
app.include_router(suggestions.router, prefix="/suggestions")
