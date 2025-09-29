FROM python:3.13-slim AS builder

ENV POETRY_NO_INTERACTION=1
ENV POETRY_VIRTUALENVS_IN_PROJECT=1
WORKDIR /app

RUN pip install poetry
COPY poetry.lock pyproject.toml ./

RUN poetry install --only main --no-root

FROM python:3.13-slim

WORKDIR /app
COPY --from=builder /app/.venv ./.venv
ENV PATH="/app/.venv/bin:$PATH"
COPY src ./src
COPY main.py .
CMD ["python", "main.py"]