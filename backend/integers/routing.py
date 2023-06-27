from django.urls import path
from .consumers import WSConsumer

# [DRF] : url 요청 이벤트 핸들러는 views.py에서 처리
# [Django-channels] : url 요청 이벤트 핸들러는 consumers.py에서 처리

ws_urlpatterns = [
    path("ws/some_url", WSConsumer.as_asgi()),
]
