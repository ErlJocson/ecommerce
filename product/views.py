from django.shortcuts import render
from .models import Order, Product

def home_view(request):
    products = Product.objects.exclude(id=request.user.id)
    return render(request, "home_view.html", {
        "title":"Home",
        "products":products,
    })

def store_view(request):
    store = Product.objects.filter(id=request.user.id)
    return render(request, "store_view.html", {
        "title":"Store",
        "store":store,
    })

def order_view(request):
    orders = Order.objects.filter(id=request.user.id)
    return render(request, "order_view.html", {
        "title":"Order",
        "orders":orders,
    })