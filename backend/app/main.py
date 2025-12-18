from fastapi import FastAPI
from app.routes.convert import router as convert_router
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Mi Asistente - Convertidor")

# Rutas de backend
app.include_router(convert_router, prefix="/convert")

# Servir Angular en la raíz
app.mount("/", StaticFiles(directory="app/static", html=True), name="frontend")