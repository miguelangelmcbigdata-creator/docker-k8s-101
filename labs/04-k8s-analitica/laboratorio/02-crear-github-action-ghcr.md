# Step 02 - GitHub Actions por app (push/pr/tag)

## Objetivo del step

Crear workflows independientes para `api` y `etl`, disparados por cambios en sus carpetas y por tags de release.

## Fundamento del step

En microservicios, cada app debe tener su propio pipeline. Asi puedes publicar solo la app que cambia o publicar ambas con el mismo tag de version.

## Ejecucion guiada

### 1) Crear carpeta de workflow

```bash
mkdir -p .github/workflows
```

### 2) Crear workflow para API

Archivo: `.github/workflows/04-api-image.yml`

```yaml
name: 04-api-image

on:
  push:
    branches: ["main"]
    tags:
      - "v*"
    paths:
      - "labs/04-k8s-analitica/trabajo/apps/api/**"
      - ".github/workflows/04-api-image.yml"
  pull_request:
    paths:
      - "labs/04-k8s-analitica/trabajo/apps/api/**"
      - ".github/workflows/04-api-image.yml"
  workflow_dispatch:

permissions:
  contents: read
  packages: write

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Login a GHCR
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Metadata de imagen
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ghcr.io/${{ github.repository_owner }}/docker-k8s-101/api
          tags: |
            type=raw,value=latest
            type=sha,prefix=sha-
            type=ref,event=tag

      - name: Build y push
        uses: docker/build-push-action@v6
        with:
          context: labs/04-k8s-analitica/trabajo/apps/api
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
```

### 3) Crear workflow para ETL

Archivo: `.github/workflows/04-etl-image.yml`

Mismo contenido que API, cambiando:

- nombre de workflow a `04-etl-image`
- paths a `trabajo/apps/etl/**`
- imagen a `ghcr.io/${{ github.repository_owner }}/docker-k8s-101/etl`
- contexto a `labs/04-k8s-analitica/trabajo/apps/etl`

### 4) Confirmar ejecucion de workflows

Haz commit y push de los cambios para lanzar la Action.

### 5) Marcar paquetes como publicos (solo primera vez)

En GitHub: `Packages` -> `api` y `etl` -> `Package settings` -> `Change visibility` -> `Public`.

### 6) Versionado conjunto (api + etl con mismo tag)

Cuando quieras release conjunto:

```bash
git tag v1.0.0
git push origin v1.0.0
```

Ambos workflows se disparan por `tags: v*` y publican `api:v1.0.0` y `etl:v1.0.0`.

## Que validas y que debes ver

- Workflow API y ETL en verde.
- Imagenes visibles en GHCR (`api` y `etl`) con `latest` y con tag de release.

## Errores comunes

- Definir un unico workflow para ambas apps y perder independencia de cambios.
- No incluir filtros `paths` y disparar builds innecesarios.

## Reto

Hacer una PR que cambie solo ETL y validar que solo corre workflow ETL.

## Solucion del reto

Revisa la pestaña Actions y comprueba que `04-api-image` no se ha ejecutado.

## Navegacion del libro

- [Anterior](01-crear-app-contenedora.md)
- [Siguiente](03-preparar-manifiestos-kubernetes.md)
