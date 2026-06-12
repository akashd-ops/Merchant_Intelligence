from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import models

router = APIRouter()

@router.get("/bundles/{merchant_id}")
def bundles(merchant_id: int, db: Session = Depends(get_db)):
    prods = db.query(models.Product).filter_by(merchant_id=merchant_id).all()
    by_cat = {}
    for p in prods:
        by_cat.setdefault(p.category, []).append(p)

    result = []
    for cat, ps in by_cat.items():
        if len(ps) < 2:
            continue
        s = sorted(ps, key=lambda x: x.selling_price - x.purchase_price, reverse=True)
        hi, lo = s[0], s[-1]
        base_mrp = hi.selling_price + lo.selling_price
        custom_mrp = round(base_mrp * 1.5)
        result.append({"category": cat, "high": hi.name, "low": lo.name,
                        "base_mrp": base_mrp, "custom_mrp": custom_mrp,
                        "cost": hi.purchase_price + lo.purchase_price,
                        "margin": custom_mrp - (hi.purchase_price + lo.purchase_price)})
    return result

@router.get("/private-label/{merchant_id}")
def private_label(merchant_id: int, db: Session = Depends(get_db)):
    prods = db.query(models.Product).filter_by(merchant_id=merchant_id).all()
    by_cat = {}
    for p in prods:
        by_cat.setdefault(p.category, []).append(p)

    result = []
    for cat, ps in by_cat.items():
        if len(ps) < 2:
            continue
        items = ps[:3]
        base_mrp = sum(p.selling_price for p in items)
        base_cost = sum(p.purchase_price for p in items)
        cost_pkg = round(base_cost * 1.05)
        custom_mrp = round(base_mrp * 1.5)
        after_discount = round(custom_mrp * 0.8)
        result.append({"category": cat, "products": [p.name for p in items],
                        "cost_with_packaging": cost_pkg, "custom_mrp": custom_mrp,
                        "after_discount": after_discount, "net_margin": after_discount - cost_pkg})
    return result
