from fastapi import FastAPI
from .api import router as api_router
from app.models.database import Base, engine

# Crea las tablas en la base de datos si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluir el router principal con todas las rutas
app.include_router(api_router)
