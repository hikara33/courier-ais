from fastapi import FastAPI

from app.modules.identity.api import router as identity_router
from app.modules.couriers.api import router as couriers_router
from app.modules.orders.api import router as orders_router
from app.modules.partners.api import router as partners_router
from app.modules.admin.api import router as admin_router
from app.modules.reports.api import router as reports_router

app = FastAPI(title="Курьерская АИС: Ядро")

app.include_router(identity_router)
app.include_router(couriers_router)
app.include_router(orders_router)
app.include_router(partners_router)
app.include_router(admin_router)
app.include_router(reports_router)


@app.get("/health", tags=["service"])
def health() -> dict:
    return {"service": "core", "status": "ok"}
