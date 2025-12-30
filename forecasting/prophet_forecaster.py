from prophet import Prophet

def forecast_product(df, product, days=31):
    product_df = df[df["product"] == product].copy()
    product_df = product_df.rename(columns={
        "date": "ds",
        "sales": "y"
    })

    model = Prophet(
        weekly_seasonality=True,
        yearly_seasonality=True
    )

    model.fit(product_df)

    # Predict next 31 days (Jan 2026)
    future = model.make_future_dataframe(periods=days, freq="D")
    forecast = model.predict(future)

    return forecast
