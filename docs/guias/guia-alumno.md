# Guia del Alumno

## Flujo de trabajo

1. Haz fork del repositorio.
2. Abre tu fork en Codespaces.
3. Cuando un lab use `kubectl port-forward` (por ejemplo Argo CD en el puerto **8443**), revisa la pestaña **Ports**: GitHub suele ofrecer **Open in Browser** con una URL `*.app.github.dev`; usala en lugar de asumir solo `127.0.0.1` desde fuera del Codespace.
4. Completa cada lab en orden.
5. Guarda evidencias en una carpeta `entregas/`.

## Regla de oro

No avances de modulo hasta completar el checklist del lab actual.

El **proyecto final** (modulo 5) parte del **laboratorio terminado del modulo 4**: no es un segundo despliegue distinto; es empaquetar, documentar y operar lo ya validado. El tramo de **Argo CD** exige un fork **publico** (o credenciales acordadas) para que el cluster pueda clonar el repositorio.
