# Бэкенд: как работать

Четыре независимых сервиса. У каждого свой `pyproject.toml` (зависимости) и `uv.lock` (точные версии, **коммитится**). Общий код лежит в `common/`.

Менеджер пакетов: [uv](https://docs.astral.sh/uv/) (установка: `pip install uv` или инструкция на сайте).

## Запуск одного сервиса без Docker (для отладки)

```bash
cd backend/core
uv sync                                              # создаст .venv и поставит зависимости
PYTHONPATH=.. uv run uvicorn app.main:app --reload   # http://localhost:8000/docs
```

`PYTHONPATH=..` нужен, чтобы находился пакет `common`. В Docker он лежит рядом с `app`, там ничего задавать не надо.

## Добавить зависимость

```bash
cd backend/core
uv add sqlalchemy          # обновит pyproject.toml и uv.lock
uv add --dev pytest        # зависимость только для разработки
```

Изменённые `pyproject.toml` и `uv.lock` коммитятся вместе с кодом, иначе Docker-сборка у коллег не совпадёт с вашей.

## Запуск всего бэкенда

Из корня репозитория: `docker compose up --build`. Образы собираются через `uv sync --frozen` по `uv.lock`, то есть версии одинаковые у всех.