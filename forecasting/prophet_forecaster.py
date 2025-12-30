import pandas as pd
from prophet import Prophet

def get_festivals():
    return pd.DataFrame({
        "holiday": ["diwali", "new_year"],
        "ds": ["2023-11-12", "2024-01-01"],
        "lower_window": [-2, 0],
        "upper_window": [3, 1]
    })

def forecast_product(df, product, days=30):
    product_df = df[df["product"] == product]
    product_df = product_df.rename(columns={"date": "ds", "sales": "y"})

    model = Prophet(
        weekly_seasonality=True,
        yearly_seasonality=True,
        holidays=get_festivals()
    )

    model.fit(product_df)

    future = model.make_future_dataframe(periods=days)
    forecast = model.predict(future)

    return forecast
