import os
from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI(title="analytics-stack")
DATABASE_URL = os.environ["DATABASE_URL"]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/db/ping")
def db_ping():
    engine = create_engine(DATABASE_URL)
    with engine.connect() as conn:
        one = conn.execute(text("SELECT 1")).scalar_one()
    return {"db": int(one)}


@app.get("/metrics")
def metrics():
    engine = create_engine(DATABASE_URL)
    with engine.connect() as conn:
        rows = conn.execute(
            text("SELECT metric, value FROM metrics ORDER BY metric ASC")
        ).mappings().all()
    return {"items": rows}
