from app.database import Base, engine
from app.models import Transaction

# This will create the 'transactions' table in your smartbudget DB
Base.metadata.create_all(bind=engine)

