# Ejemplo 03 - Stack completo con Compose

## Levantar API + DB

```bash
cd labs/02-docker-analitica/ejemplos/03-stack-compose
docker compose up --build
```

## Validar

```bash
curl -sS http://localhost:8000/health
curl -sS http://localhost:8000/db/ping
```

## Ejecutar ETL bajo demanda

```bash
docker compose --profile etl run --rm etl
```
