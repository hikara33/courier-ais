# Сервис «Трекинг»

Схема БД: `tracking` (учётная запись `tracking_user` видит только её).

Модули:
- `app/modules/ingest/` — M9 Приём геопозиции
- `app/modules/broadcast/` — M10 Трансляция положения
- `app/modules/storage/` — M11 Хранение треков

Внутри каждого модуля три слоя: `api.py` → `service.py` → `repository.py`.
Вызывать вниз можно, вверх и «через слой» — нельзя.
