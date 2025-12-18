from fastapi import FastAPI
from app.routes.convert import router as convert_router
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI(title="Mi Asistente - Convertidor")

# Rutas de backend
app.include_router(convert_router, prefix="/convert")
