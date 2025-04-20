# main.py
from fastapi import FastAPI
from routes.people import router as people_router
from db.init_db import init_db
from contextlib import asynccontextmanager


@asynccontextmanager 
async def lifespan(app: FastAPI):
    # 🔥 Aqui você inicializa o banco
    print("Iniciando o banco de dados...")
    await init_db()
    print("Banco iniciado com sucesso!")
    yield
    # 🔚 Aqui poderia fechar conexões, limpar recursos etc (se precisar)

app = FastAPI(title="Minha API de Exemplo",
    description="Esta API permite a criação e listagem de pessoas. O propósito é demonstrar o uso básico do FastAPI.",
    version="1.0.0", 
    lifespan=lifespan)

app.include_router(people_router, prefix="/api", tags=["People"])