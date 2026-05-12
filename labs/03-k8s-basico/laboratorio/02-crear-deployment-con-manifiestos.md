# Step 02 - Crear Deployment con manifiestos

## Objetivo del step

Replicar "Using kubectl to Create a Deployment" con enfoque declarativo (`YAML + apply`).

## Fundamento del step

En lugar de `kubectl create deployment`, definimos recursos en archivo para que sean versionables y repetibles.

## Ejecucion guiada

### 1) Crear carpeta de manifiestos

```bash
mkdir -p labs/03-k8s-basico/trabajo/k8s/manifests
```

### 2) Crear namespace

Archivo: `labs/03-k8s-basico/trabajo/k8s/manifests/00-namespace.yaml`

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: k8s-basics
```

### 3) Crear deployment

Archivo: `labs/03-k8s-basico/trabajo/k8s/manifests/01-deployment.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: kubernetes-bootcamp
  namespace: k8s-basics
  labels:
    app: kubernetes-bootcamp
spec:
  replicas: 1
  selector:
    matchLabels:
      app: kubernetes-bootcamp
  template:
    metadata:
      labels:
        app: kubernetes-bootcamp
    spec:
      containers:
        - name: kubernetes-bootcamp
          image: gcr.io/google-samples/kubernetes-bootcamp:v1
          ports:
            - containerPort: 8080
```

### 4) Aplicar recursos

```bash
kubectl apply -f labs/03-k8s-basico/trabajo/k8s/manifests/00-namespace.yaml
kubectl apply -f labs/03-k8s-basico/trabajo/k8s/manifests/01-deployment.yaml
```

## Que validas y que debes ver

- Deployment creado en namespace `k8s-basics`.
- Pod en estado `Running`.

```bash
kubectl -n k8s-basics get deployments,pods
```

## Errores comunes

- Namespace omitido dentro del Deployment.
- Imagen mal escrita.

## Reto

Sube replicas a 2 editando el YAML y reaplica.

## Solucion del reto

```bash
kubectl apply -f labs/03-k8s-basico/trabajo/k8s/manifests/01-deployment.yaml
kubectl -n k8s-basics get pods -l app=kubernetes-bootcamp
```

## Navegacion del libro

- [Anterior](01-crear-cluster-kind.md)
- [Siguiente](03-ver-pods-y-nodos.md)
