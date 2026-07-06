from fastapi import FastAPI
from app.core.supabase import supabase

app = FastAPI(
    title="Organizador do Professor API",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "status": "online",
        "mensagem": "API do Organizador do Professor"
    }

@app.get("/health")
def health():
    return {
        "api": "online",
        "supabase": "conectado"
    }