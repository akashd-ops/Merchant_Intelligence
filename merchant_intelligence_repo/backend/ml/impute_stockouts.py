# ml/impute_stockouts.py
def impute(merchant_id, db):
    from models import Product, Stockout
    import pandas as pd
    products = db.query(Product).filter_by(merchant_id=merchant_id).all()
    for p in products:
        stockouts = db.query(Stockout).filter_by(product_id=p.id).all()
        lost = sum(s.estimated_lost_units for s in stockouts)
        p.demand_estimated = p.daily_order_qty + lost / 30
    db.commit()
