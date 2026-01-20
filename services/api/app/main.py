from fastapi import FastAPI

app = FastAPI(title="Startup Platform API")

@app.get("/")
def root() -> dict:
  return {"message": "Startup Platform API is running"}

@app.get("/health")
def health() -> dict:
  return {"status": "ok"}
