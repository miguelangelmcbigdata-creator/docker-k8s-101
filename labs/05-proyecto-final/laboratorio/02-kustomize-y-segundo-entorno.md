# Step 02 - Dos overlays y version de imagenes

## Objetivo del step

Dejar de tratar el cluster como un solo entorno implicito: **dos perfiles** reutilizando el mismo `base`, y una politica clara de **tag de imagen** visible en Kustomize.

## Fundamento

En el lab 4 los manifiestos suelen ser planos y pensados para una sola prueba. En produccion minima se espera poder decir "este es el overlay de demo con menos replicas" o "aqui fijamos la imagen `0.2.0`" sin buscar y reemplazar en medio del Deployment.

## Ejecucion guiada

### 1) Overlay `local` (referencia al base)

Archivo `k8s/overlays/local/kustomization.yaml`:

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - ../../base
```

Opcional: anade `namespace:` si quieres fijar el namespace por overlay en lugar de confiar solo en el YAML del namespace (elige una sola estrategia y documentala en el README).

Comprueba:

```bash
cd labs/05-proyecto-final/trabajo/proyecto-final
kubectl kustomize k8s/overlays/local
```

### 2) Overlay `demo` con parche distinto

Crea `k8s/overlays/demo/replicas-api.yaml` como parche estrategico del Deployment de la API (ajusta `name` y `namespace` a los tuyos si difieren):

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
  namespace: analytics-data
spec:
  replicas: 1
```

Archivo `k8s/overlays/demo/kustomization.yaml`:

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - ../../base
patches:
  - path: replicas-api.yaml
```

Comprueba la **diferencia** de replicas entre builds (inspecciona el fragmento del Deployment en la salida de ambos comandos):

```bash
kubectl kustomize k8s/overlays/local | grep -A2 "replicas:"
kubectl kustomize k8s/overlays/demo | grep -A2 "replicas:"
```

### 3) Fijar imagenes con Kustomize (recomendado)

En `k8s/overlays/local/kustomization.yaml`, anade un bloque `images:` que apunte a tus imagenes reales. Ejemplo de forma (sustituye nombres y tags):

```yaml
images:
  - name: ghcr.io/TU_USUARIO/docker-k8s-101/api
    newTag: "0.1.0"
  - name: ghcr.io/TU_USUARIO/docker-k8s-101/etl
    newTag: "0.1.0"
```

Los `name` deben coincidir con la imagen **sin tag** que aparece en tus Deployments/CronJobs para que Kustomize sustituya correctamente.

### 4) Desplegar un overlay en kind

```bash
kubectl apply -k k8s/overlays/local
kubectl -n analytics-data rollout status deployment/api
```

(Si tu namespace tiene otro nombre, adapta el comando.)

## Que validas y que debes ver

- Los dos overlays construyen sin error.
- El overlay `demo` muestra **menos replicas** (o otro cambio documentado) que `local`.
- Tras `apply -k`, pods de API y la DB llegan a estado estable.

## Errores comunes

- Parche con `metadata.name` que no coincide con el Deployment real.
- Bloque `images:` con nombre de imagen distinto al del YAML base (Kustomize no sustituye nada y crees que "falla").

## Reto

En `demo`, anade un segundo parche que cambie la `schedule` del CronJob a una cadencia mas lenta (por ejemplo cada 15 minutos) para no saturar el cluster en exposiciones.

## Navegacion del libro

- [Anterior](01-heredar-y-empaquetar.md)
- [Siguiente](03-operacion-evidencias-y-entrega.md)
