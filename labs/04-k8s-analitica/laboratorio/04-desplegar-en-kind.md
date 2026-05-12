# Step 04 - Desplegar en kind

## Objetivo del step

Aplicar DB + API en kind y validar que la API levanta conectando con la DB stateful.

## Fundamento del step

Este step valida el punto critico del lab: API viva usando una base desplegada en Kubernetes.

## Ejecucion guiada

### 1) Aplicar recursos

```bash
kubectl apply -f labs/04-k8s-analitica/trabajo/k8s-demo-manifests/00-namespace.yaml
kubectl apply -f labs/04-k8s-analitica/trabajo/k8s-demo-manifests/01-db.yaml
kubectl apply -f labs/04-k8s-analitica/trabajo/k8s-demo-manifests/02-api.yaml
```

### 2) Verificar estado de DB (stateful)

```bash
kubectl -n analytics-data get statefulset,pods,pvc
kubectl -n analytics-data rollout status statefulset/db
```

### 3) Verificar rollout de API

```bash
kubectl -n analytics-data rollout status deployment/api
```

### 4) Revisar estado final

```bash
kubectl -n analytics-data get deploy,sts,pods,svc,pvc
```

## Que validas y que debes ver

- `statefulset/db` en `Ready`.
- PVC bound para PostgreSQL.
- `deployment/api` en `Available`.

## Errores comunes

- `PVC Pending` por problema de storage class.
- `api` en CrashLoopBackOff por `DATABASE_URL` incorrecta.

## Reto

Comprobar que API ve la DB consultando logs.

## Solucion del reto

```bash
kubectl -n analytics-data logs deploy/api
```

## Navegacion del libro

- [Anterior](03-preparar-manifiestos-kubernetes.md)
- [Siguiente](05-acceder-con-port-forward.md)
