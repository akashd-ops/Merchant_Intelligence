from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routers import merchants, bills, demand, products
from database import engine
import models, os

models.Base.metadata.create_all(bind=engine)
os.makedirs("uploads", exist_ok=True)

app = FastAPI(title="Merchant Intelligence API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

app.include_router(merchants.router, prefix="/merchants", tags=["merchants"])
app.include_router(bills.router,     prefix="/bills",     tags=["bills"])
app.include_router(demand.router,    prefix="/demand",    tags=["demand"])
app.include_router(products.router,  prefix="/products",  tags=["products"])
