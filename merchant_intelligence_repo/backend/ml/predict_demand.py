# ml/predict_demand.py
def predict_waste(products, stockouts):
    result = []
    so_by_product = {}
    for s in stockouts:
        so_by_product.setdefault(s.product_id, []).append(s)

    for p in sorted(products, key=lambda x: -(x.daily_order_qty or 0)):
        lost = sum(s.estimated_lost_units for s in so_by_product.get(p.id, []))
        corrected = max(1, round((p.demand_estimated or p.daily_order_qty) - lost / 30))
        waste_pct = round((1 - corrected / (p.daily_order_qty or 1)) * 100)
        daily_saving = round((p.daily_order_qty - corrected) * p.purchase_price * 0.9)
        result.append({
            "product": p.name, "category": p.category,
            "current_daily": p.daily_order_qty, "corrected_daily": corrected,
            "weekly": corrected * 7, "monthly": corrected * 30,
            "waste_pct": max(0, waste_pct),
            "daily_saving": max(0, daily_saving),
        })
    return sorted(result, key=lambda x: -x["waste_pct"])
