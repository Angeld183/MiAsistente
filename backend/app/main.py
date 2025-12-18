from fastapi import FastAPI
from app.routes.convert import router as convert_router
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Mi Asistente - Convertidor")

# Todas las rutas de convert estarán bajo /convert
app.include_router(convert_router, prefix="/convert")
app.mount("/", StaticFiles(directory="app/static", html=True), name="frontend")
