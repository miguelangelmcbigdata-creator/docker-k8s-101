from fastapi import FastAPI

app = FastAPI(title="api-minima")


@app.get("/health")
def health():
    return {"status": "ok", "service": "api-minima"}


@app.get("/predict")
def predict(x: float = 0.0):
    # Demo simple para analitica: modelo lineal ficticio.
    y = 2.5 * x + 1
    return {"x": x, "prediction": y}
