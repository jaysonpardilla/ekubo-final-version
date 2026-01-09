# core/asgi.py
import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# This line is crucial. It sets up Django's application registry.
# It should be called after the settings module is defined.
django.setup()

# Now, you can safely import your routing.
# The 'chat' app and its dependencies are now loaded.
import importlib
import sys
import types

# Some channel package variants may not expose `DEFAULT_CHANNEL_LAYER`.
# Provide a safe fallback on the channels module so importing
# `channels.generic.websocket` (used by our consumers) doesn't raise
# ImportError during startup in environments with package mismatches.
try:
    ch_mod = importlib.import_module('channels')
    if not hasattr(ch_mod, 'DEFAULT_CHANNEL_LAYER'):
        setattr(ch_mod, 'DEFAULT_CHANNEL_LAYER', None)
except Exception:
    # If importing channels itself fails in a non-fatal way, create a
    # lightweight placeholder module so downstream imports expecting the
    # attribute won't crash at import time. This preserves runtime
    # behavior while we diagnose package mismatches.
    mod = types.ModuleType('channels')
    mod.DEFAULT_CHANNEL_LAYER = None
    sys.modules['channels'] = mod

from core.chat.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    ),
})