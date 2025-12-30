# 📦 Multi-Product Demand Forecasting Dashboard

## 📌 Project Overview

This project is a **real-world retail demand forecasting system** that predicts **future daily sales for multiple products** and converts those forecasts into **inventory planning decisions**.

The solution is designed for **business users** and presented through an **interactive Streamlit dashboard**.

---

## 🎯 Business Problem

Retail and e-commerce companies must answer:

> **How much inventory should we stock for each product in the next 30–60 days?**

Poor forecasting leads to:

* ❌ Stock-outs (lost sales)
* ❌ Over-stocking (financial loss)
* ❌ Poor festival planning

---

## ✅ Solution

This project:

* Forecasts **daily demand per product**
* Accounts for **trend, seasonality, and festivals**
* Converts forecasts into:

  * Average demand
  * Safety stock
  * Reorder point
* Displays insights via an **interactive dashboard**

---

## 🧠 Key Features

* 📈 Time series forecasting using Prophet
* 🛍️ Multiple product forecasting (one model per product)
* 🎉 Festival effects (Diwali, New Year)
* 📦 Inventory optimization logic
* 🖥️ Streamlit dashboard for decision-making
* 🔄 Synthetic data generator for testing

---

## 🏗️ Project Architecture

```
Historical Sales Data
        ↓
Product-wise Forecasting
        ↓
Uncertainty & Seasonality Modeling
        ↓
Inventory Calculations
        ↓
Interactive Dashboard
```

---

## 📂 Project Structure

```
multi-product-demand-forecasting/
│
├── data/
│   └── retail_sales.csv
│
├── forecasting/
│   └── prophet_forecaster.py
│
├── app.py
├── generate_data.py
├── inventory.py
├── requirements.txt
└── README.md
```

---

## 📊 Dataset Description

| Column  | Description             |
| ------- | ----------------------- |
| date    | Transaction date        |
| product | Product identifier      |
| sales   | Units sold on that date |

📌 Data format mirrors **real POS / ERP systems**

---

## ⚙️ Technologies Used

* Python
* Prophet (Time Series Forecasting)
* Streamlit (Dashboard)
* Pandas & NumPy
* Matplotlib

---

## 🧪 How Forecasting Works (Simple Explanation)

Each product is forecasted **independently**:

* Prophet learns:

  * 📈 Trend (growth/decline)
  * 📆 Weekly & yearly seasonality
  * 🎉 Festival effects
* Output includes:

  * Expected demand (`yhat`)
  * Lower & upper confidence bounds

---

## 📦 Inventory Logic Explained

| Metric           | Meaning                   |
| ---------------- | ------------------------- |
| Avg Daily Demand | Expected daily sales      |
| Safety Stock     | Buffer for uncertainty    |
| Reorder Point    | When to reorder inventory |

📌 These calculations are **standard supply-chain practices**

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone <repo-url>
cd multi-product-demand-forecasting
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Generate synthetic data (optional)

```bash
python generate_data.py
```

### 5️⃣ Run Streamlit app

```bash
streamlit run app.py
```

---

## 🖥️ Dashboard Output

The dashboard allows users to:

* Select a product
* View 30-day demand forecast
* See inventory recommendations
* Make stocking decisions instantly

---

## 🧠 Business Impact

* ✔ Reduced stock-outs
* ✔ Optimized inventory planning
* ✔ Better festival preparation
* ✔ Faster decision-making

---

## 🔮 Future Enhancements

* Forecast accuracy metrics (MAE, MAPE)
* Promotion & discount effects
* Multi-store forecasting
* Model comparison (Prophet vs ARIMA)
* Cloud deployment


## 📌 Author

**Tippanwar bhavani**
Aspiring Data Scientist | Time Series & Forecasting
📍 GitHub | LinkedIn

---

 "# MultiProduct-Forecating" 
"# MultiProduct-Forecating" 
"# MultiProduct-Forecating" 
"# MultiProduct-Forecating" 
"# MultiProduct-Forecasting" 
