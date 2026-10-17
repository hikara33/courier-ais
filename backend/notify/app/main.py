"""Сервис «Уведомления»: точка входа."""
from fastapi import FastAPI

from app.modules.messaging.api import router as messaging_router
from app.modules.webhooks.api import router as webhooks_router

app = FastAPI(title="Курьерская АИС: Уведомления")

app.include_router(messaging_router)
app.include_router(webhooks_router)


@app.get("/health", tags=["service"])
def health() -> dict:
    return {"service": "notify", "status": "ok"}
