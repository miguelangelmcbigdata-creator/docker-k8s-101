# Ejemplo 02 - ETL batch

## Ejecutar

```bash
cd labs/02-docker-analitica/ejemplos/02-etl-batch
docker build -t ejemplo-etl-batch:1.0 .
docker run --rm -v "$PWD/output:/app/output" ejemplo-etl-batch:1.0
```

## Validar

```bash
cat output/resumen.csv
```
