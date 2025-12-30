import streamlit as st
from generate_data import generate_data
from forecasting.prophet_forecaster import forecast_product

st.set_page_config(page_title="Jan 2026 Forecast", layout="wide")
st.title("📦 Demand Forecast — January 2026")

# Load historical data (till Dec 2025)
df = generate_data()

st.caption("Model trained on data till **31-12-2025**")

# Select product
product = st.selectbox(
    "Select Product",
    sorted(df["product"].unique())
)

# Forecast Jan 2026 (31 days)
forecast = forecast_product(df, product, days=31)

# ✅ Keep ONLY Jan 2026
jan_2026_forecast = forecast.tail(31)

st.subheader("📈 Predicted Demand — Jan 2026")
st.line_chart(
    jan_2026_forecast.set_index("ds")["yhat"]
)

st.info("""
**Explanation**
• Historical data ends on 31-12-2025  
• Forecast shows ONLY 01-01-2026 → 31-01-2026  
• Each point = predicted daily demand
""")
