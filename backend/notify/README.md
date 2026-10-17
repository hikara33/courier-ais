# Сервис «Уведомления»

Схема БД: `notify` (учётная запись `notify_user` видит только её).

Модули:
- `app/modules/messaging/` — M12 Push и e-mail
- `app/modules/webhooks/` — M13 Вебхуки партнёрам

Внутри каждого модуля три слоя: `api.py` → `service.py` → `repository.py`.
Вызывать вниз можно, вверх и «через слой» — нельзя.
