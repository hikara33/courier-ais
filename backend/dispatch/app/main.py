"""Сервис «Диспетчеризация»: точка входа."""
from fastapi import FastAPI

from app.modules.assignment.api import router as assignment_router
from app.modules.routing.api import router as routing_router

app = FastAPI(title="Курьерская АИС: Диспетчеризация")

app.include_router(assignment_router)
app.include_router(routing_router)


@app.get("/health", tags=["service"])
def health() -> dict:
    return {"service": "dispatch", "status": "ok"}
