#!/bin/bash
set -e

# Run migrations and collect static files
python core/manage.py migrate --noinput
python core/manage.py collectstatic --noinput

# Start ASGI server (Daphne). Render provides $PORT.
# Ensure the Python path includes the inner project directory so apps
# (like `chat`) can be imported both when running manage.py and Daphne.
export PYTHONPATH="/app/core:${PYTHONPATH:-}"
cd /app
exec daphne -b 0.0.0.0 -p ${PORT:-8000} core.core.asgi:application
