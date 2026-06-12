merchant-intelligence/
├── README.md
├── .gitignore
├── requirements.txt
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── seed_db.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── merchants.py
│   │   ├── bills.py
│   │   ├── demand.py
│   │   └── products.py
│   ├── ml/
│   │   ├── __init__.py
│   │   ├── impute_stockouts.py
│   │   ├── train_demand.py
│   │   └── predict_demand.py
│   ├── ocr/
│   │   ├── __init__.py
│   │   └── extract.py
│   └── uploads/          ← gitignored, created on first run
│
├── frontend/
│   └── index.html        ← the prototype HTML
│
└── data/
    └── .gitkeep          ← merchants.db lives here, gitignored
