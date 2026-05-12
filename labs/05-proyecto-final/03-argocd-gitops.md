# Argo CD y GitOps en el proyecto final

## Objetivo

Cerrar el circulo **declaracion en Git -> estado deseado en cluster**: Argo CD vigila un path del repositorio (tu overlay Kustomize) y aplica o muestra deriva respecto a lo declarado.

## Que aporta respecto a `kubectl apply -k`

- `kubectl` es imperativo desde tu portatil: quien ejecuta debe recordar comando, rama y path.
- **Argo CD** mantiene un inventario continuo: revision de Git, diffs, historial de sync y politicas (manual vs automatico).

En el proyecto final debes **convivir** con ambos: el runbook documenta `kubectl` para depuracion y rescate; Argo CD documenta **como se despliega la linea oficial** desde Git.

## Requisitos practicos (curso 101)

1. **Repositorio accesible desde el cluster**: en `kind` el plan mas simple es un fork **publico** en GitHub con el path del overlay ya subido (`git push`). Repos privados exigen credenciales en Argo CD; quedan como extension.
2. **El recurso `Application` no debe vivir dentro del mismo Kustomize que despliega la app**, para no mezclar el namespace `analytics-data` con el control plane de Argo (`argocd`). Convencion del curso: carpeta `gitops/` al mismo nivel que `k8s/`, aplicada una vez con `kubectl apply -f`.
3. **Primera sync**: si ya tenias recursos creados a mano con los mismos nombres, Argo puede mostrar `OutOfSync` por anotaciones o labels que el controlador anade. Lo habitual en evaluacion es **cluster limpio** o borrar el namespace de la app antes de delegar en Argo.
4. **GitHub Codespaces**: al hacer `kubectl port-forward` hacia un puerto local (por ejemplo `8443`), la plataforma **detecta el puerto** y ofrece abrirlo en el navegador con una URL del dominio del Codespace (`*.app.github.dev`). Usa esa URL en el navegador; no hace falta que coincida con `127.0.0.1` desde tu equipo.

## Piezas minimas

- Namespace `argocd` con el [manifest oficial de instalacion](https://argo-cd.readthedocs.io/en/stable/getting_started/#1-install-argo-cd) (version `stable` del curso; en produccion se fija version).
- Un `Application` con `spec.source.path` apuntando a `.../k8s/overlays/local` (o el overlay que acuerdes con el instructor).
- Acceso a la UI o CLI para ver estado **Healthy / Synced**.

## Continuar

- [04-criterios-de-entrega.md](04-criterios-de-entrega.md)

## Navegacion del libro

- [Anterior](02-versionado-kustomize-y-runbook.md)
- [Siguiente](04-criterios-de-entrega.md)
