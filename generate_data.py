import pandas as pd
import numpy as np

def generate_data():
    np.random.seed(42)

    dates = pd.date_range("2024-01-01", "2025-12-31")

    products = ["Product_A", "Product_B", "Product_C"]

    rows = []

    for product in products:
        base = np.random.randint(80, 150)
        trend = np.linspace(0, 40, len(dates))
        weekly = 10 * np.sin(2 * np.pi * dates.dayofweek / 7)
        noise = np.random.normal(0, 8, len(dates))

        sales = base + trend + weekly + noise

        for d, s in zip(dates, sales):
            rows.append([d, product, max(10, int(s))])

    # ✅ ONLY return DataFrame — NO FILE I/O
    return  pd.DataFrame(rows, columns=["date", "product", "sales"])

