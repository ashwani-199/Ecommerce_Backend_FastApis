from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Generator

# Correct SQLite database URL (removed trailing colon)
SQLALCHEMY_DATABASE_URL = "sqlite:///./db.sqlite3"

# Create engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Base class for models
Base = declarative_base()

# Create tables (after models are defined)
# ⚠️ Important: This should be called only after all models are imported
# Example: Base.metadata.create_all(bind=engine)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency for database session
def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

        db.close()
