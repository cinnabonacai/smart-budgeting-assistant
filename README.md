# Smart Budgeting Assistant 💸

A personal finance backend API that ingests transaction data, detects recurring subscriptions, categorizes expenses, and summarizes spending by category.

## 🚀 Features

- ✅ Upload transactions via CSV
- 🔁 Detect recurring subscriptions (e.g., Netflix, Spotify)
- 🧠 Rule-based categorization (e.g., Food, Transport, Subscriptions)
- 📊 Category spend summary (e.g., total spent on Subscriptions)
- 🔧 Built with FastAPI, PostgreSQL, SQLAlchemy

## 📂 Folder Structure

```
smart-budgeting-assistant/
├── app/
│   ├── routes/
│   ├── services/
│   ├── utils/
│   ├── models.py
│   └── database.py
├── data/
│   └── transactions.csv
├── create_tables.py
├── requirements.txt
└── README.md
```

## 📦 API Endpoints

| Method | Endpoint                       | Description                            |
|--------|--------------------------------|----------------------------------------|
| GET    | `/transactions/load`           | Load CSV transactions into the database |
| DELETE | `/transactions/clear`          | Clear all transactions                 |
| GET    | `/suggestions/subscriptions`   | Detect recurring subscriptions         |
| GET    | `/suggestions/categorized`     | Return categorized transactions        |
| GET    | `/suggestions/summary`         | Return total spent per category        |

## 📊 Sample Output

**GET `/suggestions/summary`**
```json
{
  "Subscription": -75.94,
  "Transport": -20.0
}
```

## 🛠️ Tech Stack

- **FastAPI** — API Framework
- **PostgreSQL** — Transaction database
- **SQLAlchemy** — ORM
- **cURL / Swagger UI** — Testing interface

## 📌 Getting Started

```bash
# Clone the repo
git clone https://github.com/cinnabonacai/smart-budgeting-assistant.git

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create database tables
python create_tables.py

# Start server
uvicorn app.main:app --reload
```

## ✨ Next Features (WIP)

- ML-based categorizer
- Date filters (e.g., month/year)
- Frontend dashboard
- Auth & multi-user support

