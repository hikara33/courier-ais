FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:0.11 /uv /usr/local/bin/uv
ENV PYTHONUNBUFFERED=1 UV_LINK_MODE=copy PATH="/srv/.venv/bin:$PATH"
WORKDIR /srv

COPY core/pyproject.toml core/uv.lock ./
RUN uv sync --frozen --no-dev

COPY common ./common
COPY core/app ./app

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
