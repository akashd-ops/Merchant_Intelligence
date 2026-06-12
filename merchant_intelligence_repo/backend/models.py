from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from database import Base

class Merchant(Base):
    __tablename__ = "merchants"
    id         = Column(Integer, primary_key=True, index=True)
    name       = Column(String)
    mobile     = Column(String)
    shop_name  = Column(String)
    shop_type  = Column(String)

class Product(Base):
    __tablename__ = "products"
    id               = Column(Integer, primary_key=True, index=True)
    merchant_id      = Column(Integer, ForeignKey("merchants.id"))
    name             = Column(String)
    category         = Column(String)
    purchase_price   = Column(Float)
    selling_price    = Column(Float)
    frequency        = Column(String)   # daily/weekly/monthly
    daily_order_qty  = Column(Float)
    demand_estimated = Column(Float, nullable=True)

class Bill(Base):
    __tablename__ = "bills"
    id          = Column(Integer, primary_key=True, index=True)
    merchant_id = Column(Integer, ForeignKey("merchants.id"))
    period      = Column(String)   # daily/weekly/monthly
    bill_date   = Column(String)
    file_path   = Column(String)

class Stockout(Base):
    __tablename__ = "stockouts"
    id                  = Column(Integer, primary_key=True, index=True)
    product_id          = Column(Integer, ForeignKey("products.id"))
    date                = Column(String)
    hours_out_of_stock  = Column(Float)
    estimated_lost_units= Column(Float)
