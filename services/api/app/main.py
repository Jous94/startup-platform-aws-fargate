from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from sqlalchemy import select
from sqlalchemy.exc import OperationalError

from .db import Base, SessionLocal, engine
from .models import Dataset

app = FastAPI(title="Startup Platform API")


class DatasetIn(BaseModel):
    name: str
    description: str | None = None


@app.on_event("startup")
def startup() -> None:
    # Initialize database schema for demo environments.
    # In production, use migrations (e.g. Alembic) instead of create_all().
    try:
        Base.metadata.create_all(bind=engine)
    except OperationalError:
        # Allow the API to start even if the database is temporarily unavailable.
        pass


@app.get("/health")
def health():
    # Include database connectivity in the health signal.
    try:
        with engine.connect() as conn:
            conn.exec_driver_sql("SELECT 1")
        return {"status": "ok"}
    except OperationalError:
        return {"status": "degraded", "db": "unreachable"}
