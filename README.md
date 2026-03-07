# Ecommerce Backend (FastAPI)

A simple ecommerce backend built with **FastAPI**, **SQLAlchemy**, and **SQLite**.

## 🚀 Features

- User authentication (JWT)
- Role-based accounts (admin / user)
- Products, Categories, Carts, and Cart Items
- SQLite database with SQLAlchemy ORM models
- Auto table creation on startup

## 🧩 Project Structure

- `app/` - application package
  - `models/` - SQLAlchemy models
  - `schemas/` - Pydantic request/response schemas
  - `routers/` - FastAPI routers (endpoints)
  - `services/` - business logic
  - `db/` - database setup
  - `core/` - configuration and security
  - `utils/` - shared utilities

- `main.py` - entrypoint to run FastAPI (uses `app/main.py`)
- `run.py` - alternate run script
- `db.sqlite3` - local SQLite database file

## 🛠️ Requirements

- Python 3.10+ (recommended)

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run locally

```bash
uvicorn app.main:app --reload
```

Then visit:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`


## 🗂 Database

The project uses SQLite (`db.sqlite3`) and automatically creates tables on startup via:

- `app/main.py` (calls `Base.metadata.create_all(bind=engine)`)

If you need to reset the database, delete `db.sqlite3` and restart the app.

## 🛡️ Notes

- The app currently defaults timestamps using SQLite-compatible `CURRENT_TIMESTAMP`.
- If you run into `sqlite3.OperationalError: unknown function: NOW()`, delete `db.sqlite3` and restart.

## ✅ Contributing

1. Create a new branch
2. Make changes
3. Open a PR

---

If you'd like help adding tests, docker support, or expanding the API (orders, payments, etc.), just ask!