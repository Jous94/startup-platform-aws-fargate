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
    # Create tables for the demo environment.
    # For production, use a migration tool (e.g. Alembic).
    Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    # Check DB connectivity as part of health signal.
    try:
        with engine.connect() as conn:
            conn.exec_driver_sql("SELECT 1")
        return {"status": "ok"}
    except OperationalError:
        return {"status": "degraded", "db": "unreachable"}

@app.get("/")
def root():
    return {"message": "Startup Platform API is running (with Postgres)"}

@app.post("/datasets")
def create_dataset(payload: DatasetIn):
    with SessionLocal() as db:
        ds = Dataset(name=payload.name, description=payload.description)
        db.add(ds)
        db.commit()
        db.refresh(ds)
        return {"id": ds.id, "name": ds.name, "description": ds.description}

@app.get("/datasets")
def list_datasets():
    with SessionLocal() as db:
        rows = db.execute(select(Dataset).order_by(Dataset.id.desc())).scalars().all()
        return [{"id": r.id, "name": r.name, "description": r.description} for r in rows]

@app.get("/datasets/{dataset_id}")
def get_dataset(dataset_id: int):
    with SessionLocal() as db:
        ds = db.get(Dataset, dataset_id)
        if not ds:
            raise HTTPException(status_code=404, detail="Dataset not found")
        return {"id": ds.id, "name": ds.name, "description": ds.description}
