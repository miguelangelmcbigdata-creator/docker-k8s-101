# Step 03 - Ver Pods y Nodos (troubleshooting)

## Objetivo del step

Seguir el flujo "Viewing Pods and Nodes" para inspeccionar lo desplegado.

## Fundamento del step

Antes de exponer la app, necesitas dominar `get`, `describe`, `logs` y `exec`.

## Ejecucion guiada

### 1) Ver estado general

```bash
kubectl get nodes
kubectl -n k8s-basics get pods
```

### 2) Inspeccionar pod en detalle

```bash
kubectl -n k8s-basics describe pods
```

### 3) Revisar logs

```bash
kubectl -n k8s-basics logs -l app=kubernetes-bootcamp
```

### 4) Acceder al pod con exec

```bash
POD_NAME="$(kubectl -n k8s-basics get pods -o go-template='{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}' | head -n 1)"
kubectl -n k8s-basics exec "$POD_NAME" -- env
```

## Que validas y que debes ver

- Eventos de scheduling en `describe`.
- Logs del contenedor disponibles.
- Variables de entorno visibles por `exec`.

## Errores comunes

- No usar `-n k8s-basics`.
- Ejecutar `exec` antes de que el pod este en `Running`.

## Reto

Abrir shell en el pod y hacer `curl http://localhost:8080`.

## Solucion del reto

```bash
kubectl -n k8s-basics exec -ti "$POD_NAME" -- bash
curl http://localhost:8080
exit
```

## Navegacion del libro

- [Anterior](02-crear-deployment-con-manifiestos.md)
- [Siguiente](04-exponer-app-con-service.md)
