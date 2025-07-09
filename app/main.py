from fastapi import FastAPI
from app.routes import transactions

app = FastAPI(title="Smart Budgeting Assistant")

app.include_router(transactions.router, prefix="/transactions")

