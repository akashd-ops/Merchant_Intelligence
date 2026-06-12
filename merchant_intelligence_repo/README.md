# Merchant Intelligence

Retail analytics prototype — bill upload, demand forecasting, wastage reduction, bundle generation.

## Quick start

```bash
pip install -r requirements.txt
cd backend && python seed_db.py
uvicorn main:app --reload --port 8000
# open frontend/index.html in browser
```

## Stack
- **Frontend** — single HTML file, no build step
- **Backend** — FastAPI + SQLite (SQLAlchemy)
- **ML** — XGBoost demand model, joblib pickle
- **OCR** — stub in `ocr/extract.py`, swap Tesseract/Vision later
