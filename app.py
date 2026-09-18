import os
from fastapi import FastAPI
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")
app = FastAPI()
@app.get("/health")
def health():
    return {"ok": True}
