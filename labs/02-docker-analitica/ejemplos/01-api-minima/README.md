# Ejemplo 01 - API minima

## Ejecutar

```bash
cd labs/02-docker-analitica/ejemplos/01-api-minima
docker build -t ejemplo-api-minima:1.0 .
docker run --rm -p 8000:8000 ejemplo-api-minima:1.0
```

## Probar

```bash
curl -sS http://localhost:8000/health
curl -sS "http://localhost:8000/predict?x=4"
```
