# Definir la imagen de Docker Compose
BACK-DIR = ./backend/
BACK-DOCKER_COMPOSE = docker-compose -f $(BACK-DIR)/docker-compose.yml

# Comando para construir las imágenes
back-build:
	$(BACK-DOCKER_COMPOSE) build

# Comando para iniciar los contenedores en segundo plano
back-up:
	$(BACK-DOCKER_COMPOSE) up -d

# Comando para detener y eliminar los contenedores
back-down:
	$(BACK-DOCKER_COMPOSE) down

# Comando para ejecutar migraciones y otros comandos necesarios
back-migrate:
	$(BACK-DOCKER_COMPOSE) run --rm web alembic upgrade head

# Comando para ver los logs de los contenedores
back-logs:
	$(BACK-DOCKER_COMPOSE) logs -f

# Comando para construir, iniciar, ejecutar migraciones y ver logs
back-all: back-build back-up back-migrate back-logs
back-reload: back-down back-up