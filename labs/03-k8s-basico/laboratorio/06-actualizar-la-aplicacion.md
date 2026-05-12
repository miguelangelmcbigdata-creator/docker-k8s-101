# Step 06 - Actualizar la aplicacion (rolling update)

## Objetivo del step

Replicar "Performing a Rolling Update" con cambio de imagen via manifiesto y `apply`.

## Fundamento del step

Actualizar por manifiestos garantiza trazabilidad del cambio y facilita rollback.

## Ejecucion guiada

### 1) Cambiar configuracion del Deployment (rolling update real)

Si no existe bloque `env` en el contenedor, anadelo. Si ya existe, actualiza `APP_VERSION`.

En `labs/03-k8s-basico/trabajo/k8s/manifests/01-deployment.yaml`, cambia:

```yaml
env:
  - name: APP_VERSION
    value: v1
```

por:

```yaml
env:
  - name: APP_VERSION
    value: v2
```

### 2) Aplicar cambio

```bash
kubectl apply -f labs/03-k8s-basico/trabajo/k8s/manifests/01-deployment.yaml
```

### 3) Seguir rollout

```bash
kubectl -n k8s-basics rollout status deployment/kubernetes-bootcamp
kubectl -n k8s-basics get pods -l app=kubernetes-bootcamp
```

### 4) Verificar version en uso

Si no tienes `rg` instalado:

```bash
sudo apt-get update && sudo apt-get install -y ripgrep
```

Alternativa sin instalar nada extra:

```bash
kubectl -n k8s-basics get deployment kubernetes-bootcamp -o yaml | grep -E "APP_VERSION|value:"
```

Con `rg`:

```bash
kubectl -n k8s-basics get deployment kubernetes-bootcamp -o yaml | rg "APP_VERSION|value:"
```

## Que validas y que debes ver

- Rollout completado sin downtime perceptible.
- Pods recreados con la nueva configuracion (`APP_VERSION=v2`).

## Errores comunes

- YAML mal indentado en bloque `env`.
- No esperar a `rollout status` antes de validar.

## Reto

Haz rollback a la version anterior.

## Solucion del reto

```bash
kubectl -n k8s-basics rollout undo deployment/kubernetes-bootcamp
kubectl -n k8s-basics rollout status deployment/kubernetes-bootcamp
```

## Navegacion del libro

- [Anterior](05-escalar-la-aplicacion.md)
- [Siguiente](../../04-k8s-analitica/README.md)
