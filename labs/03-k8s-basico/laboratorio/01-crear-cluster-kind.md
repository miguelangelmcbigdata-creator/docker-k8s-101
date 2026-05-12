# Step 01 - Crear cluster local con kind

## Objetivo del step

Crear el cluster Kubernetes base para todo el laboratorio.

## Fundamento del step

Sin cluster no hay API de Kubernetes a la que aplicar manifiestos. Empezamos por el mismo punto que el tutorial oficial: tener un cluster operativo.

## Ejecucion guiada

### 1) Crear cluster

```bash
kind create cluster
```

### 2) Verificar contexto y nodo

```bash
kubectl config current-context
kubectl get nodes
```

## Que validas y que debes ver

- `kubectl get nodes` muestra al menos un nodo en `Ready`.
- `kubectl` responde con version de cliente y servidor.

```bash
kubectl version
```

## Errores comunes

- Docker no levantado en local.
- Kind no instalado o no en `PATH`.

## Reto

Asigna nombre al cluster para futuras clases (`k8s-101`) y verifica el contexto.

## Solucion del reto

```bash
kind create cluster --name k8s-101
kubectl config get-contexts | rg kind-k8s-101
```

## Navegacion del libro

- [Anterior](../README.md)
- [Siguiente](02-crear-deployment-con-manifiestos.md)
