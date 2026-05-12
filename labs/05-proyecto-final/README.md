# Modulo 5 - Proyecto final (cierre sobre el laboratorio 4)

## Relacion con el modulo anterior

En el **laboratorio del modulo 4** ya construyes y validas el flujo completo en Kubernetes: apps contenedorizadas, imagenes en GHCR, manifiestos (namespace, PostgreSQL stateful, API, CronJob ETL), despliegue en `kind`, `port-forward` y comprobacion de datos.

El **proyecto final no repite ese trabajo**. Asume que el laboratorio 4 esta **terminado y funcionando**. Tu entrega consiste en **tomar ese resultado**, **ordenarlo como repositorio entregable** y **darle forma de producto minimo**: Kustomize con varios entornos, versionado coherente imagen-manifiesto, **GitOps con Argo CD**, documentacion de operacion y paquete de evidencias revisable por otra persona.

## Capitulos del modulo

1. [01-definicion-del-proyecto.md](01-definicion-del-proyecto.md)
2. [02-versionado-kustomize-y-runbook.md](02-versionado-kustomize-y-runbook.md)
3. [03-argocd-gitops.md](03-argocd-gitops.md)
4. [04-criterios-de-entrega.md](04-criterios-de-entrega.md)

# LABORATORIO

Directorio: `labs/05-proyecto-final/laboratorio/`

1. [01-heredar-y-empaquetar.md](laboratorio/01-heredar-y-empaquetar.md)
2. [02-kustomize-y-segundo-entorno.md](laboratorio/02-kustomize-y-segundo-entorno.md)
3. [03-operacion-evidencias-y-entrega.md](laboratorio/03-operacion-evidencias-y-entrega.md)
4. [04-argocd-instalacion-y-application.md](laboratorio/04-argocd-instalacion-y-application.md)

## Navegacion del libro

- [Anterior](../04-k8s-analitica/laboratorio/06-validacion-final-y-limpieza.md)
- [Siguiente](01-definicion-del-proyecto.md)
