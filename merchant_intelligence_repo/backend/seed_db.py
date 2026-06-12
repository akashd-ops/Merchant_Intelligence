from database import engine, SessionLocal
import models, os

os.makedirs("../data", exist_ok=True)
models.Base.metadata.create_all(bind=engine)
db = SessionLocal()

m = models.Merchant(name="Debashish Mahata", mobile="9876543210", shop_name="Banga Laxmi Bhandar", shop_type="Kirana / General store")
db.add(m); db.flush()

PRODUCTS = [
    ("Amul Milk 500ml","Dairy",22,26,"Daily",120),
    ("Tata Salt 1kg","Staples",18,22,"Weekly",12),
    ("Parle-G 100g","Snacks",9,10,"Weekly",30),
    ("Sunflower Oil 1L","Oils",110,125,"Monthly",2),
    ("Maggi Noodles 70g","Snacks",12,14,"Weekly",22),
    ("Bread (local)","Bakery",28,32,"Daily",40),
    ("Tomatoes 1kg","Vegetables",35,42,"Daily",30),
    ("Lays Classic 26g","Snacks",14,16,"Weekly",30),
]
for name,cat,pp,sp,freq,qty in PRODUCTS:
    db.add(models.Product(merchant_id=m.id,name=name,category=cat,purchase_price=pp,selling_price=sp,frequency=freq,daily_order_qty=qty))

db.add(models.Stockout(product_id=1,date="2024-06-03",hours_out_of_stock=5,estimated_lost_units=38))
db.add(models.Stockout(product_id=7,date="2024-06-06",hours_out_of_stock=10,estimated_lost_units=30))
db.add(models.Stockout(product_id=6,date="2024-06-08",hours_out_of_stock=5,estimated_lost_units=22))

db.commit(); db.close()
print("DB seeded.")
