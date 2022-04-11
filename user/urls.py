from .views import *
from django.urls import path

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_view, name="register"),
]