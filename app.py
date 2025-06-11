# app.py
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Retail Sales Dashboard", layout="wide")

@st.cache_data
def load_data():
    return pd.read_parquet('data/sales_data.parquet')

df = load_data()

st.title("🛒 Retail Sales Overview")
st.dataframe(df.head(50))

st.metric("Total Revenue", f"${df['total_price'].sum():,.2f}")
