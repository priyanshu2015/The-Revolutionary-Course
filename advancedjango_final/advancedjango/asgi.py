"""
ASGI config for advancedjango project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
import django
from channels.http import AsgiHandler
from django.core.asgi import get_asgi_application
from django.core.wsgi import get_wsgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "advancedjango.settings")
django.setup()
from chatapp.routing import websocket_urlpatterns

from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({
    "http": get_asgi_application(), 
 
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
