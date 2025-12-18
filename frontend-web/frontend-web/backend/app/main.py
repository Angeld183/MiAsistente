from fastapi import FastAPI
from app.routes.convert import router as convert_router
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI(title="Mi Asistente - Convertidor")

# Rutas de backend
app.include_router(convert_router, prefix="/convert")

# Monta los archivos estáticos en /static
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Usa el fallback para servir Angular en cualquier ruta desconocida
@app.get("/{full_path:path}")
async def frontend_fallback(full_path: str):
    index_path = os.path.join("app", "static", "index.html")
    return FileResponse(index_path)