import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range(start="2023-01-01", end="2024-01-01")
products = ["Product_A", "Product_B", "Product_C"]

data = []

for product in products:
    base = np.random.randint(80, 150)
    trend = np.linspace(0, 40, len(dates))

    weekly_seasonality = 10 * np.sin(2 * np.pi * dates.dayofweek / 7)
    noise = np.random.normal(0, 8, len(dates))

    sales = base + trend + weekly_seasonality + noise

    for d, s in zip(dates, sales):
        data.append([d, product, max(10, int(s))])

df = pd.DataFrame(data, columns=["date", "product", "sales"])
df.to_csv("data/retail_sales.csv", index=False)

print("✅ Synthetic retail_sales.csv generated")
