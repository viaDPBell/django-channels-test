"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator

# import integers.routing
import chat.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

# application = ProtocolTypeRouter({"http": get_asgi_application()})
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(  # 채널 서버에 연결될때 연결 유형 검사 지정, Websocket 연결(ws:// or wss://)인 경우에 연결이 제공
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(  # 현재 인증된 사용자 확인
                URLRouter(chat.routing.websocket_urlpatterns),
            ),
        ),
    }
)
