# Ejemplo - Web Hola Mundo con Nginx

Proyecto minimo para practicar build/push de imagen en GitHub Actions.

## Estructura

- `index.html`
- `nginx.conf`
- `Dockerfile`
- `.dockerignore`

## Probar en local

```bash
docker build -t nginx-hola-mundo:local .
docker run --rm -p 8085:80 nginx-hola-mundo:local
```

Abre `http://localhost:8085`.

## Tag sugerido para GHCR

```bash
docker tag nginx-hola-mundo:local ghcr.io/TU_USUARIO/docker-k8s-101/nginx-hola-mundo:latest
```
