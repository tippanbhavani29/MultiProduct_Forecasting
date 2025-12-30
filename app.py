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
# DATA LOADING (ROBUST LOGIC)
# --------------------------------------------------
# 1) If CSV exists → use it
# 2) Else → generate synthetic data
# --------------------------------------------------

DATA_PATH = "data/retail_sales.csv"

if os.path.exists(DATA_PATH):
    df = pd.read_csv(DATA_PATH)
    df["date"] = pd.to_datetime(df["date"])
    st.success("Loaded real sales data")
else:
    df = generate_data()
    st.warning("CSV not found. Using generated sample data")

# --------------------------------------------------
# UI: Product selection
# --------------------------------------------------
product = st.selectbox(
    "Select Product",
    sorted(df["product"].unique())
)

# --------------------------------------------------
# Forecasting
# --------------------------------------------------
forecast = forecast_product(df, product)

# --------------------------------------------------
# Inventory calculation
# --------------------------------------------------
inventory = calculate_inventory(forecast)

# --------------------------------------------------
# Visualization
# --------------------------------------------------
st.subheader("📈 30-Day Demand Forecast")
st.line_chart(
    forecast.set_index("ds")["yhat"]
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
# Explanation
# --------------------------------------------------
st.info("""
**How to read this dashboard:**
- **yhat** → expected daily demand  
- **Safety Stock** → buffer against uncertainty  
- **Reorder Point** → inventory level at which to reorder  
""")
