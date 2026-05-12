# API FastAPI con Docker

## Por qué este capítulo es importante

En analítica moderna no basta con generar datos: también necesitas exponer resultados y modelos por HTTP para que otras aplicaciones los consuman. Una API contenerizada te da reproducibilidad y despliegue predecible.

## Patrón de diseño

Separar la API en su propio servicio aporta:

- ciclo de vida independiente,
- escalado independiente,
- despliegue independiente del ETL.

## Código intercalado: servicio mínimo

Archivo `app/main.py`:

```python
from fastapi import FastAPI

app = FastAPI(title="api-minima")

@app.get("/health")
def health():
    return {"status": "ok", "service": "api-minima"}

@app.get("/predict")
def predict(x: float = 0.0):
    y = 2.5 * x + 1
    return {"x": x, "prediction": y}
```

Qué demuestra este código:

- endpoint técnico (`/health`) para observabilidad,
- endpoint funcional (`/predict`) para consumo de negocio.

Archivo `Dockerfile`:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Fundamento del Dockerfile:

- base ligera y estable,
- instalación de dependencias separada para aprovechar caché,
- ejecución explícita de `uvicorn` en puerto estándar de app.

## Ejemplo ejecutable

Ruta: `labs/02-docker-analitica/ejemplos/01-api-minima`

```bash
cd labs/02-docker-analitica/ejemplos/01-api-minima
docker build -t ejemplo-api-minima:1.0 .
docker run --rm -p 8000:8000 ejemplo-api-minima:1.0
```

Validación:

```bash
curl -sS http://localhost:8000/health
curl -sS "http://localhost:8000/predict?x=4"
```

## Qué debes observar al ejecutar

- contenedor en estado `Up` mientras la API está activa,
- respuestas JSON consistentes,
- logs limpios sin reinicios.

## Errores típicos

- puerto ocupado en host,
- dependencia faltante en `requirements.txt`,
- ruta de módulo incorrecta en `uvicorn`.

## Navegacion del libro

- [Anterior](README.md)
- [Siguiente](02-etl-batch-con-docker.md)
