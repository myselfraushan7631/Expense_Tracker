import os
import pandas as pd
from config import DB_PATH, CATEGORIES
from pymongo import MongoClient           
from config import MONGO_URI 
def extract_data(folder="transactions"):
    files = [f for f in os.listdir(folder) if f.endswith(".csv")]
    if not files:
        raise FileNotFoundError("No CSV files found in transactions folder!")
    latest_file = max([os.path.join(folder, f) for f in files], key=os.path.getctime)
    print(f"📂 Reading file: {latest_file}")
    df = pd.read_csv(latest_file)
    return df
def transform_data(df):
    df = df.rename(columns={
        "Date": "date",
        "Description": "description",
        "Amount": "amount"
    })
    df = df[["date", "description", "amount"]]
    df["date"] = pd.to_datetime(df["date"])
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    def categorize(desc):
        for keyword, category in CATEGORIES.items():
            if keyword.lower() in str(desc).lower():
                return category
        return "Other"

    df["category"] = df["description"].apply(categorize)
    return df
def load_data(df):
    client = MongoClient(MONGO_URI)
    db = client["expense_tracker"]
    transactions = db["transactions"]
    transactions.insert_many(df.to_dict("records"))
    print("✅ Data loaded into MongoDB.")


def run_etl():
    df = extract_data()
    df = transform_data(df)
    load_data(df)

if __name__ == "__main__":
    run_etl()
