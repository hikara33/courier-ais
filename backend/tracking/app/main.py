"""Сервис «Трекинг»: точка входа."""
from fastapi import FastAPI

from app.modules.ingest.api import router as ingest_router
from app.modules.broadcast.api import router as broadcast_router
from app.modules.storage.api import router as storage_router

app = FastAPI(title="Курьерская АИС: Трекинг")

app.include_router(ingest_router)
app.include_router(broadcast_router)
app.include_router(storage_router)


@app.get("/health", tags=["service"])
def health() -> dict:
    return {"service": "tracking", "status": "ok"}
