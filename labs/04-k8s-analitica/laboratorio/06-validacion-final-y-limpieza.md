# Step 06 - Validacion final y limpieza

## Objetivo del step

Validar que el CronJob ETL alimenta la DB y que la API refleja esos datos; luego limpiar entorno.

## Fundamento del step

Este cierre prueba el flujo completo: ETL cronico -> PostgreSQL -> API consultable por navegador.

## Ejecucion guiada

### 1) Aplicar CronJob ETL

```bash
kubectl apply -f labs/04-k8s-analitica/trabajo/k8s-demo-manifests/03-etl-cronjob.yaml
kubectl -n analytics-data get cronjobs
```

### 2) Esperar ejecucion del CronJob y revisar jobs

```bash
kubectl -n analytics-data get jobs --watch
```

### 3) Ver logs de una ejecucion ETL

```bash
kubectl -n analytics-data logs job/$(kubectl -n analytics-data get jobs -o name | tail -n 1 | cut -d/ -f2)
```

### 4) Validar API con datos cargados

Con `port-forward` de API activo:

```bash
curl -sS http://127.0.0.1:8088/metrics
```

### 5) Limpiar recursos del laboratorio

```bash
kubectl delete -f labs/04-k8s-analitica/trabajo/k8s-demo-manifests/03-etl-cronjob.yaml
kubectl delete -f labs/04-k8s-analitica/trabajo/k8s-demo-manifests/02-api.yaml
kubectl delete -f labs/04-k8s-analitica/trabajo/k8s-demo-manifests/01-db.yaml
kubectl delete -f labs/04-k8s-analitica/trabajo/k8s-demo-manifests/00-namespace.yaml
```

## Que validas y que debes ver

- CronJob ejecuta jobs y estos terminan en `Completed`.
- `/metrics` devuelve datos insertados por ETL.
- Namespace eliminado al final.

## Errores comunes

- No esperar al primer ciclo del cron y validar demasiado pronto.
- Mantener terminales con `port-forward` abiertos tras limpiar.

## Reto

Disparar una ejecucion manual del cron sin esperar ventana temporal.

## Solucion del reto

```bash
kubectl -n analytics-data create job --from=cronjob/etl-cron etl-manual-$(date +%s)
kubectl -n analytics-data get jobs
```

## Navegacion del libro

- [Anterior](05-acceder-con-port-forward.md)
- [Siguiente](../../05-proyecto-final/README.md)
