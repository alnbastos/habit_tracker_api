#!/bin/sh
set -e

echo "⏳ Waiting for database..."
until pg_isready -h $DB_HOST -p 5432 -U $DB_USER; do
  echo "Postgres is unavailable - sleeping"
  sleep 2
done

echo "🚀 Running migrations..."
aerich upgrade

echo "✅ Starting API..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
