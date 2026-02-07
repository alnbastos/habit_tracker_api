#!/bin/sh
set -e

echo "⏳ Waiting for database..."
until pg_isready -h db -p 5432 -U postgres; do
  echo "Postgres is unavailable - sleeping"
  sleep 2
done

# inicializa Aerich apenas se ainda não existir config
if [ ! -f "./migrations/aerich.ini" ]; then
    echo "🚀 Initializing Aerich..."
    aerich init -t app.configs.database.TORTOISE_ORM
    aerich init-db
fi

echo "🚀 Running migrations..."
aerich migrate
aerich upgrade

echo "✅ Starting API..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
