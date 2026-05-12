# Step 01 - Heredar el laboratorio 4 y empaquetar

## Objetivo del step

Crear `labs/05-proyecto-final/trabajo/proyecto-final/` como **caja de salida** del curso: codigo y manifiestos ya validados en el modulo 4, copiados y ordenados, sin rehacer la logica de la API ni del ETL.

## Prerrequisito

Haber completado el laboratorio del modulo 4 hasta tener apps y YAML estables en:

- `labs/04-k8s-analitica/trabajo/apps/api`
- `labs/04-k8s-analitica/trabajo/apps/etl`
- `labs/04-k8s-analitica/trabajo/k8s-demo-manifests/*.yaml`

## Ejecucion guiada

### 1) Crear arbol del proyecto final

```bash
mkdir -p labs/05-proyecto-final/trabajo/proyecto-final/{api,etl,k8s/base,k8s/overlays/local,k8s/overlays/demo,docs,gitops}
```

### 2) Copiar aplicaciones desde el lab 4

```bash
cp -a labs/04-k8s-analitica/trabajo/apps/api/. labs/05-proyecto-final/trabajo/proyecto-final/api/
cp -a labs/04-k8s-analitica/trabajo/apps/etl/. labs/05-proyecto-final/trabajo/proyecto-final/etl/
```

Si tu lab 4 uso otra ruta, adapta los origenes; lo importante es que **no reescribas** el stack desde cero.

### 3) Copiar manifiestos Kubernetes al `base`

```bash
cp labs/04-k8s-analitica/trabajo/k8s-demo-manifests/*.yaml labs/05-proyecto-final/trabajo/proyecto-final/k8s/base/
```

### 4) Crear `k8s/base/kustomization.yaml`

Incluye los cuatro recursos en el mismo orden que aplicabas con `-f` (namespace primero):

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - 00-namespace.yaml
  - 01-db.yaml
  - 02-api.yaml
  - 03-etl-cronjob.yaml
```

Comprueba que el arbol compila:

```bash
cd labs/05-proyecto-final/trabajo/proyecto-final
kubectl kustomize k8s/base
```

### 5) README del proyecto

Crea `labs/05-proyecto-final/trabajo/proyecto-final/README.md` con al menos:

- Una frase que diga que **continua el laboratorio del modulo 4** (con rutas del repo).
- Diagrama o lista de componentes: API, PostgreSQL, ETL batch, cluster `kind`.
- Tabla "componente / imagen / proposito".

**Que estamos haciendo aqui**

- Separar "experimentacion del lab 4" de "entrega del curso" para poder revisar y versionar sin mezclar carpetas.

### 6) Sitio para el runbook

Crea `labs/05-proyecto-final/trabajo/proyecto-final/docs/operaciones.md` vacio o con titulos: lo completaras en el step 03.

## Que validas y que debes ver

- `kubectl kustomize k8s/base` genera YAML sin error.
- Las imagenes en `02-api.yaml` y `03-etl-cronjob.yaml` siguen siendo las que realmente construyes o publicas (mismo `TU_USUARIO`/registry que en el lab 4).

## Errores comunes

- Copiar solo parte de los YAML y que falte el namespace o el CronJob.
- Rutas relativas ejecutando comandos desde un directorio distinto a `proyecto-final/`.

## Reto

Anade a `k8s/base/kustomization.yaml` un `commonLabels` con `app.kubernetes.io/part-of: proyecto-final` y verifica con `kubectl kustomize` que las etiquetas aparecen en los recursos soportados.

## Navegacion del libro

- [Anterior](../04-criterios-de-entrega.md)
- [Siguiente](02-kustomize-y-segundo-entorno.md)
