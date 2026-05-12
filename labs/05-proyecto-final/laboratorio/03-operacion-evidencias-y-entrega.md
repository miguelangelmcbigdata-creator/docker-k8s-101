# Step 03 - Operacion, evidencias y entrega

## Objetivo del step

Cerrar el curso con **criterio de operaciones**: cualquier companero debe poder reproducir despliegue, validacion y rollback leyendo solo tu documentacion y el repo.

## Ejecucion guiada

### 1) Completar `docs/operaciones.md`

En `labs/05-proyecto-final/trabajo/proyecto-final/docs/operaciones.md` incluye secciones con comandos reales (copiados de tu terminal, sin placeholders genericos salvo `TU_USUARIO` donde aplique):

1. Despliegue: `kubectl apply -k k8s/overlays/<cual usas por defecto>`.
2. Espera a DB y API: `kubectl get pods`, `rollout status`.
3. Acceso a la API: `kubectl port-forward` y `curl` a `/health` (o ruta equivalente).
4. **Job manual** desde el CronJob (mismo truco que en el lab 4): `kubectl create job --from=cronjob/...`.
5. **Rollback**: tras un cambio trivial en la API (por ejemplo subir replicas con `kubectl edit` o reaplicar un parche), ejecuta `kubectl rollout undo deployment/api -n ...` y muestra como comprobas la revision.
6. Limpieza: `kubectl delete -k ...` y comprobacion de que no quedan recursos colgados (o explica por que conservas el PVC).

### 2) Carpeta de evidencias

Crea `entregas/proyecto-final/` en la raiz del repo (o la ruta que acuerde el instructor) y guarda:

- `build-local.txt` y `build-demo.txt`: salida de `kubectl kustomize` para cada overlay (puede ser larga; vale truncar con comentario "omitido por tamano" si el instructor lo permite).
- `get-pods.txt`: salida de `kubectl get pods,svc -n ...` con el cluster en estado sano.
- `etl-logs.txt`: fragmento representativo de logs del job ETL.
- `health.txt`: respuesta del endpoint de salud.

### 3) Version de entrega

- Crea un commit con mensaje claro, por ejemplo `Entrega proyecto final curso`.
- Opcional: etiqueta git `proyecto-final-0.1.0` alineada con los tags de imagen del README.

### 4) Checklist final (autoevaluacion)

- README del `proyecto-final` enlaza al lab 4 y describe overlays.
- Dos overlays distintos y utilizados en documentacion.
- Runbook probado por ti mismo paso a paso una ultima vez (sin improvisar en la entrega).

## Errores comunes

- Documentar solo capturas sin comandos reproducibles.
- Evidencias tomadas en otro namespace o cluster distinto al descrito en el README.

## Reto

Anade al README una seccion "Limitaciones conocidas" (por ejemplo credenciales en claro en YAML de clase, falta de ingress, etc.) para demostrar criterio de seguridad y deuda tecnica.

## Navegacion del libro

- [Anterior](02-kustomize-y-segundo-entorno.md)
- [Siguiente](04-argocd-instalacion-y-application.md)
