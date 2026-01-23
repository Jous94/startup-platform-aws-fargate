import os

DB_HOST = os.getenv("DB_HOST", "")
DB_PORT = int(os.getenv("DB_PORT", "5432"))
DB_NAME = os.getenv("DB_NAME", "startup")
DB_USER = os.getenv("DB_USER", "startup")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")

def database_url() -> str:
    # SQLAlchemy URL format: postgresql+psycopg2://user:pass@host:port/db
    return f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
