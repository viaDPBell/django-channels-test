from rest_framework.urls import path

from account.views import StoreLoginCV

urlpatterns = [
    path("store/login", StoreLoginCV.as_view()),
]
