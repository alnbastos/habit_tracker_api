FROM python:3.12-slim

WORKDIR /app

# Dependências de sistema
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# Dependências Python
COPY pyproject.toml poetry.lock* /app/
RUN pip install --upgrade pip \
 && pip install poetry \
 && poetry config virtualenvs.create false \
 && poetry install --no-root --no-interaction --no-ansi

# Código da aplicação
COPY . /app

# Permissão pro entrypoint
RUN chmod +x /app/entrypoint.sh

EXPOSE 8000
