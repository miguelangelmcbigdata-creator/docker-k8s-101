# Step 04 - Argo CD: instalacion y Application

## Objetivo del step

Exponer el mismo overlay Kustomize que ya validaste por `kubectl`, ahora como **fuente unica declarada en Git** que Argo CD reconcilia contra el cluster.

## Prerrequisitos

- Overlay `k8s/overlays/local` (o el que uses) **subido a un remoto** que el cluster pueda clonar (fork publico en GitHub es el camino por defecto del curso).
- Si acabas de aplicar el mismo manifiesto a mano, conviene **borrar el namespace de la aplicacion** (`analytics-data` en el lab de referencia) y dejar que Argo lo recree, para evitar estados confusos de propiedad de recursos.

## Ejecucion guiada

### 1) Instalar Argo CD (manifest oficial)

```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl -n argocd rollout status deploy/argocd-server
```

### 2) Obtener contrasena inicial de admin

```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d && echo
```

Usuario por defecto: `admin`.

### 3) Acceso a la UI (port-forward)

En una terminal dedicada:

```bash
kubectl port-forward svc/argocd-server -n argocd 8443:443
```

- **GitHub Codespaces** (flujo recomendado del curso): el entorno **detecta el puerto 8443** y muestra aviso en la pestaña *Ports* / notificacion *Open in Browser*. Abre la URL que te ofrezca (suele ser `https://<nombre>-8443.app.github.dev` o similar): es el **mapeo automatico** del puerto local al dominio del Codespace. Acepta el aviso del certificado autofirmado si el navegador lo pide.
- **Maquina local** (Docker Desktop + `kind` en tu PC): abre `https://127.0.0.1:8443` con el mismo aviso de certificado.

### 4) Carpeta `gitops/` fuera del Kustomize de la app

Si no la creaste en el step 01:

```bash
mkdir -p labs/05-proyecto-final/trabajo/proyecto-final/gitops
```

**Importante**: los YAML de `gitops/` **no** deben listarse en `k8s/base/kustomization.yaml` ni en overlays de la app. Son recursos de control que viven en el cluster bajo `argocd` (o el namespace que indique el propio recurso).

### 5) Crear el recurso `Application`

Crea `labs/05-proyecto-final/trabajo/proyecto-final/gitops/argocd-application.yaml` sustituyendo `TU_USUARIO` y revisando `targetRevision` y `path`:

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: proyecto-final-local
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/TU_USUARIO/docker-k8s-101.git
    targetRevision: main
    path: labs/05-proyecto-final/trabajo/proyecto-final/k8s/overlays/local
  destination:
    server: https://kubernetes.default.svc
    namespace: analytics-data
  syncPolicy:
    syncOptions:
      - CreateNamespace=true
```

- `repoURL`: HTTPS del fork (sin credenciales en el archivo; repo publico).
- `path`: debe existir en esa revision de Git.
- `namespace` en `destination`: namespace por defecto para recursos que no traigan `metadata.namespace`; tus YAML del lab 4 ya fijan `analytics-data`, pero declararlo aqui deja claro el contrato.

### 6) Registrar la Application en el cluster

Con el fichero ya **commiteado y pusheado** al remoto que referencia `repoURL` (Argo clona desde Git, no desde tu disco):

```bash
kubectl apply -f labs/05-proyecto-final/trabajo/proyecto-final/gitops/argocd-application.yaml
```

### 7) Sincronizar

Desde la UI: aplicacion `proyecto-final-local` -> **SYNC** (primera vez suele ser manual con politica por defecto).

Por CLI (si instalaste `argocd`):

```bash
argocd login 127.0.0.1:8443 --username admin --password <pega-password> --insecure
argocd app sync proyecto-final-local
```

Ejecuta estos comandos **en la misma terminal o entorno donde corre el port-forward** (por ejemplo dentro del Codespace): ahi `127.0.0.1:8443` sigue siendo valido. O con el plugin de kubectl si lo tienes configurado; el curso no lo exige.

### 8) Comprobar estado

```bash
kubectl -n argocd get application proyecto-final-local -o wide
kubectl -n analytics-data get pods,svc
```

## Extender `docs/operaciones.md`

Anade una seccion **GitOps (Argo CD)** con:

1. URL del repo y rama que consume el `Application`.
2. Como abrir la UI en **Codespace** (puerto reenviado / dominio `*.app.github.dev`) o en local (`127.0.0.1`).
3. Comando o pantalla para **sync manual** y como comprobar **Synced / Healthy**.
4. Como pausar o borrar la Application sin tumbar Argo CD entero (`kubectl delete -f gitops/argocd-application.yaml`).
5. Aviso: cambios en cluster con `kubectl edit` sin commit generan **deriva**; Argo lo mostrara como `OutOfSync`.

## Que validas y que debes ver

- Pods de `argocd` en `Running`.
- `Application` con fase exitosa tras sync y workloads de la app en el namespace esperado.

## Errores comunes

- En **Codespace**, intentar abrir solo `https://127.0.0.1:8443` desde el navegador de tu portatil sin usar la URL publica que genera la pestaña *Ports* (el tunel no es la misma interfaz que en local).
- `path` en Git distinto al de tu maquina (mayusculas, carpeta `trabajo` olvidada).
- Repo privado sin credencial: Argo falla al clonar; usar fork publico o documentar limitacion con el instructor.
- Aplicar el `Application` antes de hacer `git push`: Argo clona una revision donde aun no existe el path.

## Evidencia para `entregas/`

Guarda `argocd-application-get.txt` con la salida de:

```bash
kubectl -n argocd get application proyecto-final-local -o yaml
```

(puedes truncar campos largos si el instructor lo permite).

## Navegacion del libro

- [Anterior](03-operacion-evidencias-y-entrega.md)
- [Siguiente](../04-criterios-de-entrega.md)
