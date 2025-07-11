# Smart Budgeting Assistant 💸

A personal finance assistant that helps users track their expenses, detect recurring subscriptions, and visualize spending — powered by FastAPI and React.

---

## 🚀 Features

- ✅ Upload transactions via CSV  
- 🔁 Detect recurring subscriptions (e.g., Netflix, Spotify)  
- 🧠 Rule-based and ML-based categorization (e.g., Food, Transport, Subscriptions)  
- 📊 Category spend summary (e.g., total spent on Subscriptions)  
- 📆 Filter transactions by month and year  
- 🌐 React dashboard for data visualization  
- 🔧 Built with FastAPI, PostgreSQL, SQLAlchemy, and React  

---

## 📂 Folder Structure

```
smart-budgeting-assistant/
├── app/                       # FastAPI backend
│   ├── routes/
│   ├── services/
│   ├── utils/
│   ├── models.py
│   └── database.py
├── data/
│   └── transactions.csv
├── budgeting-dashboard/       # React frontend
│   └── src/Dashboard.jsx
├── create_tables.py
├── train_model.py             # ML model training script
├── model.pkl                  # Saved ML model
├── requirements.txt
└── README.md
```

---

## 📦 API Endpoints

| Method | Endpoint                         | Description                            |
|--------|----------------------------------|----------------------------------------|
| GET    | `/transactions/load`             | Load CSV transactions into the database |
| DELETE | `/transactions/clear`            | Clear all transactions                 |
| GET    | `/suggestions/subscriptions`     | Detect recurring subscriptions         |
| GET    | `/suggestions/categorized`       | Return categorized transactions        |
| GET    | `/suggestions/summary`           | Return total spent per category        |
| GET    | `/suggestions/ml-categorized`    | Predict categories using ML model      |
| GET    | `/suggestions/categorized?month=6&year=2025` | Filter by date                |

---

## 📊 Sample Output

**GET `/suggestions/summary`**
```json
{
  "Subscription": -75.94,
  "Transport": -20.0
}
```

**GET `/suggestions/ml-categorized`**
```json
[
  {
    "transaction_id": 1,
    "merchant": "Netflix",
    "amount": -12.99,
    "date": "2025-03-01",
    "predicted_category": "Subscription"
  },
  ...
]
```

---

## 🛠️ Tech Stack

- **FastAPI** — API Framework  
- **PostgreSQL** — Transaction database  
- **SQLAlchemy** — ORM  
- **React** — Frontend dashboard  
- **Chart.js** — Data visualization  
- **scikit-learn** — ML categorization  
- **cURL / Swagger UI** — Testing interface  

---

## 📌 Getting Started

### 📦 Backend

```bash
# Clone the repo
git clone https://github.com/cinnabonacai/smart-budgeting-assistant.git
cd smart-budgeting-assistant

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create PostgreSQL database
psql postgres
CREATE DATABASE smartbudget;
\q

# Create tables
python create_tables.py

# Train and save ML model
python train_model.py

# Start FastAPI server
uvicorn app.main:app --reload
```

### 💻 Frontend

```bash
# Go to frontend folder
cd budgeting-dashboard

# Install dependencies
npm install

# Start React dev server
npm start
```

---

## ✨ Future Features

- [ ] User authentication & multi-user support  
- [ ] Budget setting and alerts  
- [ ] Export reports (PDF/CSV)  
- [ ] Deployment to cloud (e.g., Render, Vercel)  

---




