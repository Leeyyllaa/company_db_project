from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

if settings.database_url is None:
    raise ValueError("DATABASE_URL is not set in .env file")

# ساختن Engine برای PostgreSQL
engine = create_engine(
    settings.database_url,
    future=True,
)

# ساختن SessionLocal برای استفاده در FastAPI
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)
