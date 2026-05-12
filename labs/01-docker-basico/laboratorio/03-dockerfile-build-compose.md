# Step 03 - Entorno dev con Docker Compose (build context, volumen, puerto y auto-refresh)

## Objetivo del step

Montar un entorno de desarrollo con `docker compose` donde puedas modificar código local y ver el cambio reflejado sin reconstruir manualmente en cada edición.

## Fundamento del step

Este step integra los conceptos clave de trabajo diario con Compose:

- `build.context`: define qué carpeta usa Docker para construir la imagen.
- `build.dockerfile`: permite controlar qué Dockerfile usa el servicio.
- `volumes` (bind mount): comparte código local dentro del contenedor.
- `ports`: publica el servicio para consumirlo desde host/Codespace.
- modo debug/reload: el proceso recarga al detectar cambios de código.

## Descripcion del laboratorio

Vas a crear una mini API Flask y ejecutarla con `docker compose`. El servicio se construye con `build: context`, expone puerto y monta el código para auto-refresh.

## Ejecución guiada

### 1) Crear estructura del proyecto

```bash
mkdir -p labs/01-docker-basico/trabajo/dev-live-compose/app
```

Crea `labs/01-docker-basico/trabajo/dev-live-compose/requirements.txt`:

```text
flask==3.0.3
```

Crea `labs/01-docker-basico/trabajo/dev-live-compose/app/main.py`:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify({"status": "ok", "version": "v1"})

@app.get("/message")
def message():
    return jsonify({"message": "Hola desde dev-live-compose"})
```

### 2) Crear Dockerfile

Crea `labs/01-docker-basico/trabajo/dev-live-compose/Dockerfile`:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app
ENV FLASK_APP=app/main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8000
CMD ["flask", "run", "--debug"]
```

### 3) Crear `docker-compose.yml` con build context

Crea `labs/01-docker-basico/trabajo/dev-live-compose/docker-compose.yml`:

```yaml
services:
  api:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8010:8000"
    volumes:
      - ./app:/app/app
    environment:
      - FLASK_ENV=development
```

Por qué este diseño:

- `context: .` permite usar `requirements.txt`, `Dockerfile` y `app/` del proyecto.
- `volumes: ./app:/app/app` evita rebuild para cambios de código.
- `ports` publica la API en `localhost:8010`.

### 4) Levantar con Compose

```bash
cd labs/01-docker-basico/trabajo/dev-live-compose
docker compose up --build
```

### 5) Validar servicio

En otra terminal:

```bash
curl -sS http://localhost:8010/health
curl -sS http://localhost:8010/message
```

### 6) Probar auto-refresh

Sin detener `docker compose up`, modifica en `app/main.py`:

```python
return jsonify({"message": "Hola desde dev-live-compose"})
```

por:

```python
return jsonify({"message": "Mensaje actualizado con compose"})
```

Valida de nuevo:

```bash
curl -sS http://localhost:8010/message
```

## Qué validas y qué debes ver

- Compose construye imagen desde `build.context` sin errores.
- Servicio `api` queda en estado `running`.
- Endpoint responde por puerto `8010`.
- Al guardar cambios en `app/main.py`, la respuesta cambia sin rebuild manual.

## Errores comunes

- `build context` incorrecto: `COPY` falla en Dockerfile.
- ruta de volumen errónea: cambios locales no impactan en contenedor.
- puerto ocupado: cambiar `8010:8000` por otro puerto host.

## Reto

Añade endpoint `GET /time` que devuelva hora UTC y verifica que aparece sin reiniciar Compose.

## Solucion del reto

Añade en `app/main.py`:

```python
from datetime import datetime, timezone

@app.get("/time")
def get_time():
    return jsonify({"utc": datetime.now(timezone.utc).isoformat()})
```

Valida:

```bash
curl -sS http://localhost:8010/time
```

## Navegacion del libro

- [Anterior](02-interactividad-volumenes-puertos.md)
- [Siguiente](../../02-docker-analitica/README.md)
