# Compose API + DB + ETL

## Por qué este capítulo es importante

En un caso real, API y ETL dependen de una base de datos. Docker Compose permite modelar ese sistema como una unidad: dependencias, red y variables de entorno.

## Patrón de arquitectura

- `db`: persistencia transaccional,
- `api`: capa de servicio,
- `etl`: carga y actualización de datos.

Esto reproduce un flujo típico de analítica operacional.

## Código intercalado: stack completo

`docker-compose.yml`:

```yaml
services:
  db:
    image: postgres:16
    env_file: .env
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U $$POSTGRES_USER -d $$POSTGRES_DB"]
      interval: 5s
      timeout: 5s
      retries: 10

  api:
    build: ./api
    env_file: .env
    depends_on:
      db:
        condition: service_healthy
    ports:
      - "8000:8000"

  etl:
    build: ./etl
    env_file: .env
    depends_on:
      db:
        condition: service_healthy
    profiles:
      - etl

volumes:
  pgdata:
```

Fundamento técnico de decisiones clave:

- `healthcheck` en DB evita carreras de arranque,
- `depends_on` con condición de salud reduce fallos intermitentes,
- `profiles` permite ejecutar ETL solo cuando corresponde.

## Ejemplo ejecutable

Ruta: `labs/02-docker-analitica/ejemplos/03-stack-compose`

### Levantar API + DB

```bash
cd labs/02-docker-analitica/ejemplos/03-stack-compose
docker compose up --build
```

### Validar endpoints

```bash
curl -sS http://localhost:8000/health
curl -sS http://localhost:8000/db/ping
```

### Ejecutar ETL bajo demanda

```bash
docker compose --profile etl run --rm etl
```

## Qué debes observar al ejecutar

- API responde incluso tras reinicios del stack,
- `db/ping` confirma conectividad real,
- ETL termina limpio y deja trazabilidad en logs.

## Errores típicos

- usar `localhost` dentro de contenedores en lugar de `db`,
- olvidar `.env` o variables incompletas,
- no esperar salud de Postgres antes de levantar API/ETL.

# LABORATORIO

- [01-estructura-stack.md](laboratorio/01-estructura-stack.md)

## Navegacion del libro

- [Anterior](02-etl-batch-con-docker.md)
- [Siguiente](laboratorio/01-estructura-stack.md)
