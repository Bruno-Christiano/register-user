# main.py
from fastapi import FastAPI
from app.routes.people import router as people_router

app = FastAPI(title="Minha API de Exemplo",
    description="Esta API permite a criação e listagem de pessoas. O propósito é demonstrar o uso básico do FastAPI.",
    version="1.0.0")

app.include_router(people_router, prefix="/api", tags=["People"])