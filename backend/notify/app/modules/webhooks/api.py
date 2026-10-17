"""Слой API модуля: HTTP-маршруты. Только разбор запроса и вызов service.py."""
from fastapi import APIRouter

router = APIRouter(prefix="/internal/webhooks", tags=["webhooks"])
