# Gestión de Docker con Makefile

Este proyecto utiliza Docker Compose para gestionar los contenedores. El `Makefile` proporciona una serie de comandos para facilitar la administración de los contenedores.

## Estructura del Makefile

El `Makefile` incluye varios comandos para construir, iniciar, detener y gestionar los contenedores. Los comandos están diseñados para trabajar con Docker Compose en la carpeta `backend`.

### Comandos

- **`back-build`**: Construye las imágenes de Docker.
- **`back-up`**: Inicia los contenedores en segundo plano.
- **`back-down`**: Detiene y elimina los contenedores.
- **`back-migrate`**: Ejecuta las migraciones de Alembic dentro del contenedor web.
- **`back-logs`**: Muestra los logs de los contenedores en tiempo real.
- **`back-all`**: Ejecuta los siguientes pasos en orden: construir imágenes, iniciar contenedores, ejecutar migraciones y mostrar logs.
- **`back-reload`**: Detiene y elimina los contenedores, luego los vuelve a iniciar.





