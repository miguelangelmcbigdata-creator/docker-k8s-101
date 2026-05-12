# Versionado, Kustomize y runbook

## Objetivo

Alinear **tres cosas** que en el laboratorio 4 suelen quedar implicitas: que imagen corre, que manifiesto la referencia y como lo explicas a quien llega despues.

## Versionado imagen-manifiesto

- El laboratorio 4 ya te lleva a `:latest` o a tags en GHCR. En el proyecto final debes **fijar una linea base de version** (por ejemplo `0.1.0` o el tag que hayas publicado) y reflejarla en los recursos que consuma Kustomize.
- Kustomize permite **sustituir la imagen** sin editar a mano el Deployment linea a linea usando el bloque `images:` en `kustomization.yaml`. Es la forma recomendada de demostrar que entiendes el flujo "tag nuevo -> manifiesto -> apply".

## Kustomize como contrato de entrega

- `base/` contiene el conjunto minimo comun (namespace, DB, API, CronJob).
- Cada `overlays/<nombre>/` debe poder construirse aisladamente:

```bash
kustomize build k8s/overlays/local
kustomize build k8s/overlays/demo
```

- La diferencia entre overlays debe ser **intencional**: replicas, limites de recursos, frecuencia del cron de prueba, prefijos de labels, etc. No basta con duplicar el mismo YAML en dos carpetas.

## Runbook (`docs/operaciones.md`)

Documento corto (una o dos paginas) que responda sin ambigueded:

1. Prerrequisitos (cluster, namespace, secreto de pull si aplica).
2. Comando unico de despliegue (`kubectl apply -k ...`).
3. Comandos de comprobacion (`get pods`, `rollout status`, prueba HTTP con `port-forward`).
4. Como lanzar **una ejecucion manual** del ETL desde el CronJob.
5. Como hacer **rollback** del Deployment de la API y como verificar que volvio la revision anterior.
6. Como **eliminar** el despliegue sin dejar PVCs huérfanos si eso aplica a tu manifiesto.
7. Tras el lab de Argo CD: seccion **GitOps** (repo, rama, `Application`, sync, deriva frente a `kubectl edit`).

## Continuar

- [03-argocd-gitops.md](03-argocd-gitops.md)

## Navegacion del libro

- [Anterior](01-definicion-del-proyecto.md)
- [Siguiente](03-argocd-gitops.md)
