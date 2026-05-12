# Step 03 - Preparar manifiestos Kubernetes

## Objetivo del step

Definir manifiestos para:

- PostgreSQL stateful
- API conectada a PostgreSQL
- Service de API para acceso por `port-forward`
- CronJob ETL para carga periodica

## Fundamento del step

La API debe leer datos de DB, y la DB debe persistir. En kind, validar almacenamiento evita fallos tipicos con cargas stateful.

## Ejecucion guiada

### 1) Crear estructura de manifiestos

```bash
mkdir -p labs/04-k8s-analitica/trabajo/k8s-demo-manifests
```

### 2) Crear `00-namespace.yaml`

Archivo: `labs/04-k8s-analitica/trabajo/k8s-demo-manifests/00-namespace.yaml`

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: analytics-data
```

### 3) Crear `01-db.yaml` (StatefulSet + Service)

Archivo: `labs/04-k8s-analitica/trabajo/k8s-demo-manifests/01-db.yaml`

```yaml
apiVersion: v1
kind: Service
metadata:
  name: db
  namespace: analytics-data
spec:
  selector:
    app: db
  ports:
    - port: 5432
      targetPort: 5432
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: db
  namespace: analytics-data
  labels:
    app: db
spec:
  serviceName: db
  replicas: 1
  selector:
    matchLabels:
      app: db
  template:
    metadata:
      labels:
        app: db
    spec:
      containers:
        - name: postgres
          image: postgres:16
          env:
            - name: POSTGRES_DB
              value: analytics
            - name: POSTGRES_USER
              value: analytics
            - name: POSTGRES_PASSWORD
              value: analytics
          ports:
            - containerPort: 5432
          volumeMounts:
            - name: db-data
              mountPath: /var/lib/postgresql/data
  volumeClaimTemplates:
    - metadata:
        name: db-data
      spec:
        accessModes: ["ReadWriteOnce"]
        resources:
          requests:
            storage: 1Gi
```

### 4) Validar StorageClass en kind (importante para stateful)

```bash
kubectl get storageclass
```

Si no hay StorageClass default, el PVC quedara en `Pending`.

### 5) Crear `02-api.yaml`

Archivo: `labs/04-k8s-analitica/trabajo/k8s-demo-manifests/02-api.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
  namespace: analytics-data
  labels:
    app: api
spec:
  replicas: 2
  selector:
    matchLabels:
      app: api
  template:
    metadata:
      labels:
        app: api
    spec:
      containers:
        - name: api
          image: ghcr.io/TU_USUARIO/docker-k8s-101/api:latest
          env:
            - name: DATABASE_URL
              value: postgresql://analytics:analytics@db:5432/analytics
          ports:
            - containerPort: 8000
---
apiVersion: v1
kind: Service
metadata:
  name: api
  namespace: analytics-data
spec:
  selector:
    app: api
  ports:
    - port: 8000
      targetPort: 8000
  type: ClusterIP
```

### 6) Crear `03-etl-cronjob.yaml`

Archivo: `labs/04-k8s-analitica/trabajo/k8s-demo-manifests/03-etl-cronjob.yaml`

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: etl-cron
  namespace: analytics-data
spec:
  schedule: "*/2 * * * *"
  jobTemplate:
    spec:
      template:
        spec:
          restartPolicy: OnFailure
          containers:
            - name: etl
              image: ghcr.io/TU_USUARIO/docker-k8s-101/etl:latest
              env:
                - name: DATABASE_URL
                  value: postgresql://analytics:analytics@db:5432/analytics
```

## Que validas y que debes ver

- Existen `00-namespace.yaml`, `01-db.yaml`, `02-api.yaml`, `03-etl-cronjob.yaml`.
- DB service `db` y API service `api` con selectors coherentes.

```bash
ls -1 labs/04-k8s-analitica/trabajo/k8s-demo-manifests
```

## Errores comunes

- Olvidar reemplazar `TU_USUARIO` por tu cuenta.
- PVC de PostgreSQL en `Pending` por falta de StorageClass default.

## Reto

Cambiar frecuencia del CronJob a cada minuto para test rapido.

## Solucion del reto

Editar `schedule` en `03-etl-cronjob.yaml` a `"*/1 * * * *"`.

## Navegacion del libro

- [Anterior](02-crear-github-action-ghcr.md)
- [Siguiente](04-desplegar-en-kind.md)
