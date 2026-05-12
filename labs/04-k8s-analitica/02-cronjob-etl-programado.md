# GitHub Actions + GHCR para imagen publica

## Objetivo

Diseñar un pipeline CI que construya y publique automaticamente la imagen de la app en GHCR.

## Pipeline objetivo (por aplicacion)

Cada app tendra su workflow:

- `04-api-image.yml`
- `04-etl-image.yml`

Cada workflow construye y publica solo su imagen cuando hay cambios en su carpeta.

## Eventos recomendados

- `push` a `main` con filtro por `paths`.
- `pull_request` con filtro por `paths` (validacion temprana).
- `push` de tags `v*` para releases.

1. Checkout del repositorio.
2. Login en GHCR con `GITHUB_TOKEN`.
3. Generacion de metadata/tags.
4. Build y push de la imagen.

## Estructura recomendada de cada workflow

Archivo: `.github/workflows/04-k8s-app-image.yml`

Elementos clave:

- **Trigger**: `push` a `main` y `workflow_dispatch`.
- **Permisos**: `packages: write`.
- **Action base**: `docker/build-push-action`.

## Etiquetado recomendado por imagen

Usa al menos dos tags:

- `latest` para demostracion rapida.
- `sha-<short>` para trazabilidad exacta.
- `vX.Y.Z` para release semantica.

## Versionado conjunto API + ETL

Puedes releasear ambas con el mismo tag:

```bash
git tag v1.2.0
git push origin v1.2.0
```

Resultado esperado:

- `ghcr.io/<owner>/docker-k8s-101/api:v1.2.0`
- `ghcr.io/<owner>/docker-k8s-101/etl:v1.2.0`

## Ejemplo de convencion de imagen

`ghcr.io/<owner>/docker-k8s-101/api:latest`

## Publico vs privado en GHCR

Para este laboratorio:

- Paquete en **public** para evitar gestion de tokens en clase.
- Aun siendo publico, el push sigue autenticado por Action.

## Validaciones importantes tras ejecutar la Action

- Workflow en verde.
- Imagen visible en la pestaña *Packages* del repo/owner.
- Pull local exitoso:

```bash
docker pull ghcr.io/<owner>/docker-k8s-101/api:latest
docker pull ghcr.io/<owner>/docker-k8s-101/etl:latest
```

## Continuar

- [03-configmap-y-secret.md](03-configmap-y-secret.md)

## Navegacion del libro

- [Anterior](01-job-etl-una-ejecucion.md)
- [Siguiente](03-configmap-y-secret.md)
