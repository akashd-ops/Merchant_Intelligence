from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import get_db
import models

router = APIRouter()

class MerchantIn(BaseModel):
    name: str; mobile: str; shop_name: str; shop_type: str

@router.post("/")
def create(m: MerchantIn, db: Session = Depends(get_db)):
    row = models.Merchant(**m.dict())
    db.add(row); db.commit(); db.refresh(row)
    return {"id": row.id}

@router.get("/{merchant_id}")
def get(merchant_id: int, db: Session = Depends(get_db)):
    return db.query(models.Merchant).filter_by(id=merchant_id).first()
