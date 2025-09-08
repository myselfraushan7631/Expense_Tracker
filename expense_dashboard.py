import sqlite3
import pandas as pd
import streamlit as st
from config import DB_PATH
def load_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM transactions", conn)
    conn.close()
    return df

st.title("💰 Personal Expense Tracker")

df = load_data()

if df.empty:
    st.warning("No transactions found! Run ETL first.")
else:
    st.subheader("📊 Transactions")
    st.dataframe(df)
    st.subheader("📌 Spending by Category")
    category_sum = df.groupby("category")["amount"].sum().reset_index()
    st.bar_chart(category_sum.set_index("category"))
    st.subheader("📈 Spending Over Time")
    time_series = df.groupby("date")["amount"].sum().reset_index()
    st.line_chart(time_series.set_index("date"))
