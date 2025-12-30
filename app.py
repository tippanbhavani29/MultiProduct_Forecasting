import streamlit as st
import pandas as pd
import os

from forecasting.prophet_forecaster import forecast_product
from inventory import calculate_inventory
from generate_data import generate_data

# --------------------------------------------------
# Streamlit page config
# --------------------------------------------------
st.set_page_config(
    page_title="Retail Forecasting Dashboard",
    layout="wide"
)

st.title("📦 Multi-Product Demand Forecasting Dashboard")

# --------------------------------------------------
# DATA LOADING
# --------------------------------------------------
DATA_PATH = "data/retail_sales.csv"

if os.path.exists(DATA_PATH):
    df = pd.read_csv(DATA_PATH)
    df["date"] = pd.to_datetime(df["date"])
    st.success("Loaded real sales data")
else:
    df = generate_data()
    st.warning("CSV not found. Using generated sample data")

st.caption("Model trained on data till **31-12-2025**")

# --------------------------------------------------
# UI: Product selection
# --------------------------------------------------
product = st.selectbox(
    "Select Product",
    sorted(df["product"].unique())
)

# --------------------------------------------------
# Forecasting (🔑 CHANGE: predict 31 days)
# --------------------------------------------------
forecast = forecast_product(df, product, days=31)

# 🔑 CHANGE: keep ONLY Jan 2026 predictions
future_forecast = forecast.tail(31)

# --------------------------------------------------
# Inventory calculation (use Jan 2026 only)
# --------------------------------------------------
inventory = calculate_inventory(future_forecast)

# --------------------------------------------------
# Visualization (ONLY Jan 2026)
# --------------------------------------------------
st.subheader("📈 Demand Forecast — January 2026")
st.line_chart(
    future_forecast.set_index("ds")["yhat"]
)

# --------------------------------------------------
# Metrics
# --------------------------------------------------
col1, col2, col3 = st.columns(3)

col1.metric(
    "Avg Daily Demand",
    inventory["avg_daily_demand"]
)

col2.metric(
    "Safety Stock",
    inventory["safety_stock"]
)

col3.metric(
    "Reorder Point",
    inventory["reorder_point"]
)

# --------------------------------------------------
# Explanation (typo fixed)
# --------------------------------------------------
st.info("""
**How to read this dashboard:**
- **yhat** → expected daily demand for Jan 2026  
- **Safety Stock** → buffer against uncertainty  
- **Reorder Point** → inventory level at which to reorder  
""")
