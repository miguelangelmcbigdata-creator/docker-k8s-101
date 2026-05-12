# ETL batch con Docker

## Por qué este capítulo es importante

Muchos procesos analíticos no son servicios web: son tareas batch que leen datos, transforman y escriben resultados. Contenerizar ETL evita diferencias de entorno entre máquinas y facilita ejecución repetible.

## Patrón de diseño

Separar ETL de la API permite:

- planificar ejecuciones sin impactar API,
- versionar lógica de datos de forma independiente,
- depurar errores de transformación de forma aislada.

## Código intercalado: ETL reproducible

Archivo `etl.py`:

```python
from pathlib import Path
import pandas as pd

IN_FILE = Path("input/ventas.csv")
OUT_FILE = Path("output/resumen.csv")


def main() -> None:
    df = pd.read_csv(IN_FILE)
    resumen = (
        df.groupby("categoria", as_index=False)["monto"]
        .sum()
        .rename(columns={"monto": "monto_total"})
    )
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    resumen.to_csv(OUT_FILE, index=False)
    print("ETL OK")
    print(resumen)
```

Fundamento técnico:

- entrada y salida explícitas (`input/` y `output/`),
- transformación determinista y verificable,
- resultado auditable en CSV.

Archivo `Dockerfile`:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY etl.py .
COPY input ./input
CMD ["python", "-u", "etl.py"]
```

## Ejemplo ejecutable

Ruta: `labs/02-docker-analitica/ejemplos/02-etl-batch`

```bash
cd labs/02-docker-analitica/ejemplos/02-etl-batch
docker build -t ejemplo-etl-batch:1.0 .
docker run --rm -v "$PWD/output:/app/output" ejemplo-etl-batch:1.0
```

Validación:

```bash
cat output/resumen.csv
```

## Qué debes observar al ejecutar

- salida de logs con `ETL OK`,
- archivo `resumen.csv` persistido en host,
- totales coherentes por categoría.

## Errores típicos

- ruta de entrada incorrecta,
- permisos de escritura en carpeta `output`,
- columnas de CSV no alineadas con el script.

## Navegacion del libro

- [Anterior](01-api-fastapi-con-docker.md)
- [Siguiente](03-compose-api-db-etl.md)
