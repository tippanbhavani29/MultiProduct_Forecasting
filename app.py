import streamlit as st
import pandas as pd

from forecasting.prophet_forecaster import forecast_product
from inventory import calculate_inventory

st.set_page_config("Retail Forecasting Dashboard", layout="wide")
st.title("📦 Multi-Product Demand Forecasting Dashboard")

from generate_data import generate_data
df = generate_data()


product = st.selectbox("Select Product", df["product"].unique())

forecast = forecast_product(df, product)
inventory = calculate_inventory(forecast)

st.subheader("📈 30-Day Demand Forecast")
st.line_chart(forecast.set_index("ds")["yhat"])

col1, col2, col3 = st.columns(3)

col1.metric("Avg Daily Demand", inventory["avg_daily_demand"])
col2.metric("Safety Stock", inventory["safety_stock"])
col3.metric("Reorder Point", inventory["reorder_point"])

st.info("""
• yhat → expected demand  
• Safety stock → protection buffer  
• Reorder point → when to reorder inventory
""")
