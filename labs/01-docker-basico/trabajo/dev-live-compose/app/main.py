from flask import Flask, jsonify
from datetime import datetime, timezone

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify({"status": "ok", "version": "v1"})

@app.get("/message")
def message():
    return jsonify({"message": "Mensaje actualizado con compose"})

@app.get("/time")
def get_time():
    return jsonify({"utc": datetime.now(timezone.utc).isoformat()})