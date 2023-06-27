from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.utils import timezone
from django.http import HttpRequest

from rest_framework import status, generics, permissions, response


class StoreLoginCV(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request: HttpRequest, *args, **kwargs) -> response.Response:
        email = request.data["email"]
        password = request.data["password"]

        user = authenticate(request, email=email, password=password)

        if user is None:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)
        login(request, user)
        # TODO: 필요 시 유저 데이터 내려주기
        res = response.Response(status=status.HTTP_200_OK)

        res.set_cookie(
            key=settings.AUTH_USER_ID_COOKIE,
            value=user.id,
            domain=settings.AUTH_COOKIE_DOMAIN,
            expires=timezone.now() + settings.AUTH_COOKIE_AGE,
            secure=settings.AUTH_COOKIE_SECURE,
            httponly=False,
            samesite=settings.AUTH_COOKIE_SAMESITE,
        )

        return res
