# Курьерская АИС

Автоматизированная информационная система курьерской фирмы

Архитектура: четыре укрупнённых сервиса за шлюзом Nginx, общая шина событий RabbitMQ, PostgreSQL + PostGIS

## Структура

```
backend/
  core/        Ядро: пользователи, курьеры и смены, заказы, партнёры, админ, отчёты
  dispatch/    Диспетчеризация: автоназначение, маршруты и геокодирование
  tracking/    Трекинг: приём и трансляция геопозиции, хранение треков
  notify/      Уведомления: push, e-mail, вебхуки партнёрам
  common/      Общие контракты (события, настройки)
mobile/        Мобильное приложение (React Native): клиент и курьер
admin-web/     Веб-панель администратора
deploy/        Конфигурация Nginx, PostgreSQL, RabbitMQ
docs/          Документация, OpenAPI
tests/         Сквозные тесты
```

## Запуск

```bash
cp .env.example .env     
docker compose up --build
```

Проверка: http://localhost/health. Состояние сервисов: `docker compose ps` (у всех должно быть `healthy`).

Панель администратора по адресу http://localhost/ появится после сборки фронтенда, а в разработке открывается через dev-сервер. Подробности:
- бэкенд: [backend/README.md](backend/README.md)
- веб-панель: [admin-web/README.md](admin-web/README.md)
- мобильное приложение: [mobile/README.md](mobile/README.md)

Файл `.env` у каждого свой и в Git не попадает. Шаблон — `.env.example`.

## Работа с репозиторием
См. [CONTRIBUTING.md](CONTRIBUTING.md). Архитектурные правила — [docs/architecture.md](docs/architecture.md).