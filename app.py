import platform
import numpy as np
import psycopg2  # noqa: F401  (needs libpq at import time)
from fastapi import FastAPI
app = FastAPI()
@app.get("/health")
def health():
    return {"ok": True, "python": platform.python_version(), "psycopg2": psycopg2.__version__.split()[0]}
