from fastapi import FastAPI 
from app.routes.convert import router as convert_router 
from fastapi import FastAPI
from app.routes import convert

app = FastAPI()
app.include_router(convert.router)
app = FastAPI(title="Mi Asistente - Convertidor") 
app.include_router(convert_router, prefix="/convert")