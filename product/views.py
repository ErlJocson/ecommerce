import os
from django.shortcuts import render
from .models import Order, Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home_view(request):
    products = Product.objects.all()
    if not products:
        messages.warning(request, 'There are no items for sale.')
    return render(request, "home_view.html", {
        "title":"Home",
        "products":products,
    })

@login_required
def store_view(request):
    store = Product.objects.all()
    if not store:
        messages.warning(request, 'You are not selling anything.')
    return render(request, "store_view.html", {
        "title":"Store",
        "store":store,
    })

@login_required
def order_view(request):
    orders = Order.objects.filter(id=request.user.id)
    if not orders:
        messages.warning(request, 'There are no orders yet.')
    return render(request, "order_view.html", {
        "title":"Order",
        "orders":orders,
    })