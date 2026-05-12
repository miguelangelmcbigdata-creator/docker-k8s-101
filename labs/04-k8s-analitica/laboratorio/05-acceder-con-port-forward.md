# Step 05 - Acceder con port-forward desde el host

## Objetivo del step

Exponer la API localmente y validar en navegador que responde datos de la DB.

## Fundamento del step

`port-forward` permite demostrar la integracion end-to-end sin Ingress: navegador -> API -> PostgreSQL.

## Ejecucion guiada

### 1) Abrir port-forward (terminal 1)

```bash
kubectl -n analytics-data port-forward service/api 8088:8000
```

### 2) Probar desde host (terminal 2)

```bash
curl -sS http://127.0.0.1:8088/health
curl -sS http://127.0.0.1:8088/metrics
```

### 3) Validar en navegador

Abre:

`http://127.0.0.1:8088/metrics`

## Que validas y que debes ver

- `health` responde `ok`.
- `metrics` responde JSON (puede estar vacio antes del ETL).
- Sin errores 5xx/timeout.

## Errores comunes

- Puerto local ocupado (`8088`).
- Ejecutar `port-forward` al service incorrecto.

## Reto

Usar un puerto alternativo local (`8099`) para la API.

## Solucion del reto

```bash
kubectl -n analytics-data port-forward service/api 8099:8000
curl -sS http://127.0.0.1:8099/health
```

## Navegacion del libro

- [Anterior](04-desplegar-en-kind.md)
- [Siguiente](06-validacion-final-y-limpieza.md)
