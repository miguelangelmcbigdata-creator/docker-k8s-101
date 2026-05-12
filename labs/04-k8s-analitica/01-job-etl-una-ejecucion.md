# Arquitectura del flujo CI/CD a Kubernetes local

## Objetivo

Entender el flujo completo que vamos a implementar en este modulo:

1. App dentro del repositorio.
2. Build de imagen con GitHub Actions.
3. Publicacion en GHCR (publica).
4. Despliegue en kind con manifiestos.
5. Acceso por `port-forward` al `Service`.

## Por que este enfoque es importante

Este flujo replica una cadena de valor real de plataforma:

- **Repositorio** como fuente de verdad (codigo + manifiestos + pipeline).
- **Contenedor inmutable** para ejecutar igual en cualquier entorno.
- **Registro de imagenes** para distribuir artefactos.
- **Kubernetes declarativo** para operar por estado deseado.

## Componentes y responsabilidades

### App

Servicio web sencillo para que el foco este en plataforma y no en logica de negocio.

### Dockerfile

Define como empaquetar la app para ejecutarse en cualquier nodo Kubernetes.

### GitHub Actions

Automatiza build y push al cambiar `main`. Evita builds manuales inconsistentes.

### GHCR (GitHub Container Registry)

Repositorio de imagenes versionadas. Usaremos visibilidad publica para simplificar el laboratorio.

### Deployment + Service

- `Deployment` mantiene replicas.
- `Service` da endpoint estable para enrutar trafico a los pods.

## Flujo operativo (resumen)

1. Haces push a `main`.
2. Action construye imagen y publica `ghcr.io/<owner>/<repo>/<imagen>:<tag>`.
3. En kind, aplicas manifiestos que referencian esa imagen.
4. Verificas `pods`, `deployment`, `service`.
5. Abres `port-forward` y ves la app en navegador.

## Riesgos habituales y mitigacion

- Tag mutable (`latest`) sin trazabilidad -> usar tags por commit o version.
- Pull fallido por imagen privada -> paquete GHCR publico.
- Divergencia entre entorno local y cluster -> contenedor reproducible y manifiestos versionados.

## Continuar

- [02-cronjob-etl-programado.md](02-cronjob-etl-programado.md)

## Navegacion del libro

- [Anterior](README.md)
- [Siguiente](02-cronjob-etl-programado.md)
