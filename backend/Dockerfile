
FROM python:3.12

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requisitos y los instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación
COPY . .

# Instala wait-for-it
RUN apt-get update && apt-get install -y curl && \
    curl -o /usr/local/bin/wait-for-it https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh && \
    chmod +x /usr/local/bin/wait-for-it

# Comando para ejecutar las migraciones y la aplicación
ENTRYPOINT ["sh", "-c", "wait-for-it db:5432 -- alembic revision --autogenerate -m 'first migration' && alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
