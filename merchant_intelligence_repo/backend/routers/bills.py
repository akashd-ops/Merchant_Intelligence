from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session
from database import get_db
from ocr.extract import extract_products
import models, os, shutil

router = APIRouter()

@router.post("/upload")
async def upload(
    file: UploadFile = File(...),
    merchant_id: int = Form(...),
    period: str = Form(...),
    bill_date: str = Form(...)  ,
    db: Session = Depends(get_db)
):
    path = f"uploads/{merchant_id}/{period}/"
    os.makedirs(path, exist_ok=True)
    fpath = path + file.filename
    with open(fpath, "wb") as f:
        shutil.copyfileobj(file.file, f)

    db.add(models.Bill(merchant_id=merchant_id, period=period, bill_date=bill_date, file_path=fpath))
    db.commit()

    products = extract_products(fpath, merchant_id, db)
    return {"products": products}
