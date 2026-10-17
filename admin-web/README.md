# Веб-панель администратора

Одностраничное веб-приложение (React + Vite). Исполняется **в браузере**; сервера у него нет. Nginx лишь раздаёт собранные файлы и пропускает запросы `/v1/...` к бэкенду.

## Два режима работы

**1. Разработка (каждый день).** Бэкенд поднимается в Docker, панель работает на dev-сервере Vite с горячей перезагрузкой:

```bash
# из корня репозитория
cp .env.example .env            # один раз
docker compose up --build -d    # бэкенд + Nginx на http://localhost

cd admin-web
npm install                     # один раз
npm run dev                     # панель на http://localhost:5173
```

В `vite.config.ts` запросы к API перенаправляются на Nginx, поэтому в коде используем относительные адреса (`fetch("/v1/orders")`), а CORS не нужен:

```ts
export default defineConfig({
  server: {
    proxy: {
      "/v1": "http://localhost",
      "/ws": { target: "ws://localhost", ws: true },
    },
  },
});
```

**2. Проверка «как в бою».** Собираем статику, и её раздаёт Nginx (так же будет на сервере):

```bash
cd admin-web && npm run build   # результат в admin-web/dist
cd .. && docker compose up -d   # панель на http://localhost/
```

Папка `dist/` в репозиторий не попадает.

Если на компьютере нет Docker, можно работать по контракту: описание API лежит в `docs/openapi/`.
