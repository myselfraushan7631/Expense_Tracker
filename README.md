# 💰 Automated Personal Expense Tracker

This project helps track your expenses by reading bank/credit card CSV files, cleaning and categorizing them, and storing them in a database.  
It also includes a Streamlit dashboard for visualization.

---

## 🚀 Features
- Extract transactions from CSV files
- Clean and categorize expenses (e.g., Starbucks → Coffee, Uber → Transport)
- Store transactions in **MongoDB ** (or SQLite  if configured)
- Visualize spending habits with **Streamlit**

---

## 🛠️ Tech Stack
- Python (Pandas, Streamlit)
- SQLite (default) or MongoDB Atlas
- Cron / Task Scheduler for automation

---

## 📂 Project Structure
expense_tracker/
│── main.py # ETL pipeline
│── db_setup.py # Database setup
│── config.py # Configurations
│── transactions/ # Place your CSV files here
│── expense_dashboard.py # Streamlit dashboard
│── README.md # Project documentation


---

## ⚙️ Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/expense_tracker.git
   cd expense_tracker


Create virtual environment & install dependencies:

python -m venv .venv
.venv\Scripts\activate   # (Windows)
pip install -r requirements.txt


Setup database:

python db_setup.py


Add your CSV files to transactions/

Run ETL pipeline:

python main.py


Start dashboard:

streamlit run expense_dashboard.py

📊 Example CSV format
Date,Description,Amount
2025-09-01,Starbucks,-5.50
2025-09-02,Uber,-12.00
2025-09-03,Salary,2000.00
