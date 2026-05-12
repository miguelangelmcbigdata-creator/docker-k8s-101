# Deployment + Service + Port-forward en kind

## Objetivo

Preparar el despliegue de la app publicada en GHCR dentro de kind y visualizarla desde el host.

## Recursos Kubernetes que usaremos

### Namespace

Aisla los recursos del laboratorio para limpieza y lectura de estado.

### Deployment

Define la imagen a ejecutar, replicas y puertos del contenedor.

### Service (ClusterIP)

Da endpoint estable interno. Lo expondremos localmente con `kubectl port-forward`.

## Por que usar `port-forward` en este lab

- Evita complejidad de Ingress para un primer despliegue.
- Funciona igual en Codespaces, Linux, macOS y WSL.
- Hace visible la app en navegador sin abrir NodePorts.

## Validaciones operativas clave

1. `kubectl get pods` -> `Running`.
2. `kubectl rollout status` -> deployment estable.
3. `kubectl get svc` -> service presente.
4. `port-forward` activo en terminal.
5. Navegador/curl responde.

## Checklist de troubleshooting

- `ImagePullBackOff` -> nombre/tag de imagen incorrecto o paquete privado.
- `CrashLoopBackOff` -> revisar `kubectl logs`.
- Service sin endpoints -> selector no coincide con labels del pod.
- `port-forward` caido -> reiniciar comando y verificar namespace.

# LABORATORIO

- [01-crear-app-contenedora.md](laboratorio/01-crear-app-contenedora.md)

## Navegacion del libro

- [Anterior](02-cronjob-etl-programado.md)
- [Siguiente](laboratorio/01-crear-app-contenedora.md)
