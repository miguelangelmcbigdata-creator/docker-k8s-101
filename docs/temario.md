# Temario del Curso (20h)

## Modulo 1 - Fundamentos (2h)

- Que es un contenedor y diferencias con VM.
- Problemas reales en analitica: dependencias y reproducibilidad.
- Introduccion conceptual a Docker y Kubernetes.

## Modulo 2 - Docker Basico (6h)

- Primeros comandos y ciclo de vida del contenedor.
- Imagenes vs contenedores, Docker Hub.
- Dockerfile basico: `FROM`, `RUN`, `COPY`, `CMD`.
- Volumenes y redes.
- Lab: Jupyter en Docker.
- Lab: PostgreSQL + Python.
- Lab: imagen propia para analitica.

## Modulo 3 - Docker para Analitica (4h)

- Pipelines simples en contenedores.
- ETL batch y variables de entorno.
- Docker Compose multi-servicio.
- Lab: API (FastAPI) + BD.
- Lab: pipeline de datos en contenedor.

## Modulo 4 - Kubernetes Inicial (5h)

- Que problema resuelve Kubernetes.
- Conceptos: Pod, Deployment, Service.
- Flujo Docker -> Kubernetes.
- `kubectl` y YAML basico.
- Lab: desplegar, exponer y escalar una aplicacion.

## Modulo 5 - Kubernetes para Analitica (4h)

- Jobs y CronJobs para ETL.
- ConfigMaps y Secrets.
- Lab: Job de proceso de datos.
- Lab: CronJob programado.
- Lab: configuracion externa.

## Modulo 6 - Integracion Real (3h)

- Flujo completo de desarrollo local a Kubernetes.
- Buenas practicas de versionado y reproducibilidad.
- Introduccion ligera a EKS/GKE/AKS.
- Lab final: dar forma operativa al stack del modulo 4 (Kustomize multi-overlay, runbook, Argo CD, evidencias); alineado con `labs/05-proyecto-final`.
