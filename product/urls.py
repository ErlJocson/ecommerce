from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('store/', store_view, name='store'),
    path('order/', order_view, name='order'),
]