import os
from fastapi import FastAPI

app = FastAPI(title="CLI Cloud FastAPI proof")

@app.get("/")
def root():
    return {"ok": True, "framework": "fastapi", "marker": "clicloud-fastapi-e2e-ready"}

@app.get("/health")
def health():
    return {"ok": True, "framework": "fastapi", "databaseConfigured": bool(os.getenv("DATABASE_URL"))}
