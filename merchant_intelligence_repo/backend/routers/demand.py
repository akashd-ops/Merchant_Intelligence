from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from ml.impute_stockouts import impute
from ml.train_demand import train
from ml.predict_demand import predict_waste
import models

router = APIRouter()

@router.post("/train/{merchant_id}")
def train_model(merchant_id: int, db: Session = Depends(get_db)):
    impute(merchant_id, db)
    metrics = train(merchant_id, db)
    return metrics

@router.get("/waste/{merchant_id}")
def waste(merchant_id: int, db: Session = Depends(get_db)):
    products = db.query(models.Product).filter_by(merchant_id=merchant_id).all()
    stockouts = db.query(models.Stockout).all()
    result = predict_waste(products, stockouts)
    return result
