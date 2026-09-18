import yaml  # not declared in requirements.txt
from fastapi import FastAPI
app = FastAPI()
@app.get("/health")
def health():
    return {"ok": True, "yaml": yaml.__version__}
