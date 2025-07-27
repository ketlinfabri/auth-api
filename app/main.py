from fastapi import FastAPI
from app.handlers import user_auth


app = FastAPI(
    title="Revenda de Veículos | Autenticação de Usuários",
    description="FIAP - FASE 3 | API de Autenticação",
    version="1.0.0",
    docs_url="/docs",
    redoc_url=None,
    openapi_url="/openapi.json"
)

app.include_router(user_auth.router, prefix="/api")

