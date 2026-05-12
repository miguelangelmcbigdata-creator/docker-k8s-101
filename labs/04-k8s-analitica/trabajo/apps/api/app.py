import os
import psycopg
from flask import Flask, jsonify

app = Flask(__name__)
DATABASE_URL = os.environ["DATABASE_URL"]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT metric, value FROM metrics ORDER BY metric")
            rows = [{"metric": m, "value": v1} for m, v1 in cur.fetchall()]
    return jsonify(rows)