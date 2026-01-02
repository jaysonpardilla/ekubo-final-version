#!/bin/bash
set -e

# Change to the project directory (where manage.py is located)
cd /app/core

# Run migrations and collect static files
python manage.py migrate --noinput
python manage.py collectstatic --noinput

# Start ASGI server (Daphne). Render provides $PORT.
# Module path is relative to the project directory (/app/core)
exec daphne -b 0.0.0.0 -p ${PORT:-8000} core.asgi:application
