#!/bin/sh
set -e

echo "⏳ Waiting for database..."
sleep 2

echo "🚀 Running migrations..."
aerich upgrade || aerich init -t app.configs.database.TORTOISE_ORM

echo "✅ Starting API..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
