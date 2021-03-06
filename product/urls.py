from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('store/', store_view, name='store'),
    path('order/', order_view, name='order'),
    path('product/<int:id>', product_view, name='product'),
    path('order/<int:id>', order_now, name='order_now'),
    path('add-product/', add_product, name='add-product'),
    path('remove-product/<int:id>', delete_product, name="delete-product"),
    path('cancel-order/<int:product_id>/<int:order_id>', cancel_order, name='cancel-order'),
    path('edit-product/<int:id>', edit_view, name='edit-product')
]