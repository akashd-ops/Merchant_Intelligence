# ocr/extract.py — stub, returns demo products; swap with Tesseract/Vision later
def extract_products(file_path, merchant_id, db):
    from models import Product
    existing = db.query(Product).filter_by(merchant_id=merchant_id).all()
    return [{"name": p.name, "category": p.category,
             "purchase_price": p.purchase_price, "selling_price": p.selling_price,
             "frequency": p.frequency, "qty": p.daily_order_qty} for p in existing]
