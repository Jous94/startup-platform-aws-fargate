import os


def database_url() -> str:
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432")
    name = os.getenv("DB_NAME", "startup")
    user = os.getenv("DB_USER", "startup")
    password = os.getenv("DB_PASSWORD", "startup")

    # Use psycopg (PostgreSQL driver v3) for SQLAlchemy
    return f"postgresql+psycopg://{user}:{password}@{host}:{port}/{name}"
