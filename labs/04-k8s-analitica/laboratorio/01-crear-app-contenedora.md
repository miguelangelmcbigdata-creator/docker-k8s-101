# Step 01 - Crear estructura multi-app (api + etl)

## Objetivo del step

Crear las dos apps del laboratorio dentro del repositorio:

- `api`: expone datos desde PostgreSQL.
- `etl`: carga datos periodicamente en PostgreSQL.

## Fundamento del step

Sin separar `api` y `etl` no puedes automatizar pipelines por carpeta ni desplegar responsabilidades distintas en Kubernetes.

## Ejecucion guiada

### 1) Crear estructura de proyecto

```bash
mkdir -p labs/04-k8s-analitica/trabajo/apps/api
mkdir -p labs/04-k8s-analitica/trabajo/apps/etl
```

### 2) Crear contenido de la API

Archivo: `labs/04-k8s-analitica/trabajo/apps/api/app.py`

```python
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
            rows = [{"metric": m, "value": v} for m, v in cur.fetchall()]
    return jsonify(rows)
```

Archivo: `labs/04-k8s-analitica/trabajo/apps/api/requirements.txt`

```text
flask==3.0.3
psycopg[binary]==3.2.3
gunicorn==23.0.0
```

Archivo: `labs/04-k8s-analitica/trabajo/apps/api/Dockerfile`

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
```

### 3) Crear contenido del ETL

Archivo: `labs/04-k8s-analitica/trabajo/apps/etl/etl.py`

```python
import os
import random
import psycopg

DATABASE_URL = os.environ["DATABASE_URL"]

def main():
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute("CREATE TABLE IF NOT EXISTS metrics (metric text, value int)")
            cur.execute("DELETE FROM metrics")
            cur.execute("INSERT INTO metrics VALUES (%s,%s)", ("visitas", random.randint(50, 200)))
            cur.execute("INSERT INTO metrics VALUES (%s,%s)", ("ventas", random.randint(1, 20)))
        conn.commit()
    print("ETL OK")

if __name__ == "__main__":
    main()
```

Archivo: `labs/04-k8s-analitica/trabajo/apps/etl/requirements.txt`

```text
psycopg[binary]==3.2.3
```

Archivo: `labs/04-k8s-analitica/trabajo/apps/etl/Dockerfile`

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY etl.py .
CMD ["python", "etl.py"]
```

### 4) Build local de validacion

```bash
docker build -t k8s-demo-api:local labs/04-k8s-analitica/trabajo/apps/api
docker build -t k8s-demo-etl:local labs/04-k8s-analitica/trabajo/apps/etl
```

## Que validas y que debes ver

- Las dos imagenes se construyen sin errores (`api` y `etl`).

## Errores comunes

- Mezclar codigo de API y ETL en la misma carpeta.
- Rutas de `docker build` apuntando a carpeta incorrecta.

## Reto

Cambia el endpoint `/health` para devolver version `v1` y reconstruye la imagen de API.

## Solucion del reto

Editar `app.py` y volver a ejecutar `docker build` de API.

## Navegacion del libro

- [Anterior](../03-configmap-y-secret.md)
- [Siguiente](02-crear-github-action-ghcr.md)
