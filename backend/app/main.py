# app/main.py
from fastapi import FastAPI
from app.routes.convert import router as convert_router

app = FastAPI(title="Mi Asistente - Convertidor")

# Todas las rutas de convert estarán bajo /convert
app.include_router(convert_router, prefix="/convert")