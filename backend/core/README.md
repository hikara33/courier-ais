# Сервис «Ядро»

Схема БД: `core` (учётная запись `core_user` видит только её).

Модули:
- `app/modules/identity/` — M1 Идентификация и доступ
- `app/modules/couriers/` — M2 Курьеры и смены
- `app/modules/orders/` — M3 Заказы (единственный, кто меняет заказ)
- `app/modules/partners/` — M4 Партнёры и API-интеграция
- `app/modules/admin/` — M5 Администрирование
- `app/modules/reports/` — M6 Отчётность

Внутри каждого модуля три слоя: `api.py` → `service.py` → `repository.py`.
Вызывать вниз можно, вверх и «через слой» — нельзя.
