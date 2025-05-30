#!/bin/sh

echo "Esperando a que PostgreSQL esté disponible..."
while ! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
  sleep 1
done

echo "PostgreSQL está listo"

python manage.py migrate

exec "$@"
