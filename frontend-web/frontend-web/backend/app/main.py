from fastapi import FastAPI
from app.routes.convert import router as convert_router
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI(title="Mi Asistente - Convertidor")

# Rutas de backend
app.include_router(convert_router, prefix="/convert")

# Servir Angular en la raíz
app.mount("/", StaticFiles(directory="app/static", html=True), name="frontend")

# Fallback: devolver siempre index.html para rutas no encontradas
@app.get("/{full_path:path}")
async def frontend_fallback(full_path: str):
    index_path = os.path.join("app", "static", "index.html")
    return FileResponse(index_path)