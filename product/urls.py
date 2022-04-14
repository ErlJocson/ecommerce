from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('store/', store_view, name='store'),
    path('order/', order_view, name='order'),
    path('product/<int:id>', product_view, name='product'),
    path('order/<int:id>', order_now, name='order_now')
]