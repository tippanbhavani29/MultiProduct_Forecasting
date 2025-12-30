def calculate_inventory(forecast, lead_time_days=7, service_level=0.95):
    avg_demand = forecast["yhat"][-30:].mean()
    demand_std = forecast["yhat"][-30:].std()

    safety_stock = 1.65 * demand_std  # 95% service level
    reorder_point = avg_demand * lead_time_days + safety_stock

    return {
        "avg_daily_demand": int(avg_demand),
        "safety_stock": int(safety_stock),
        "reorder_point": int(reorder_point)
    }
