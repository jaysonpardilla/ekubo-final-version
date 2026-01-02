#!/bin/bash
set -e

# Run migrations and collect static files
python core/manage.py migrate --noinput
python core/manage.py collectstatic --noinput

# Start ASGI server (Daphne). Render provides $PORT.
exec daphne -b 0.0.0.0 -p ${PORT:-8000} core.core.asgi:application
