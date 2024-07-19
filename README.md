# Gestión de Docker con Makefile

Este proyecto utiliza Docker y Docker Compose para gestionar los contenedores. El `Makefile` proporciona una serie de comandos para facilitar la administración de los contenedores y las imágenes.

## Estructura del Makefile

El `Makefile` incluye varios comandos para construir, iniciar, detener y gestionar los contenedores. Los comandos están diseñados para trabajar con Docker Compose en la carpeta `backend`.

### Comandos

- **`back-build`**: Construye las imágenes de Docker.
  
  ```bash
  make back-build
  make back-up
  make back-down
  make back-migrate
  make back-logs
  make back-all
  make back-reload





