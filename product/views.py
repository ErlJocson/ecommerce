from django.shortcuts import redirect, render
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
    store = Product.objects.filter(seller=request.user)
    if not store:
        messages.warning(request, 'You are not selling anything.')
    return render(request, "store_view.html", {
        "title":"Store",
        "store":store,
    })

@login_required
def order_view(request):
    orders = Order.objects.filter(user=request.user)
    if not orders:
        messages.warning(request, 'There are no orders yet.')
    return render(request, "order_view.html", {
        "title":"Order",
        "orders":orders,
    })

@login_required
def product_view(request, id):
    item = Product.objects.get(id=id)
    return render(request, 'product_view.html', {
        "title":"Product",
        "item":item
    })

@login_required
def order_now(request, id):
    productToAdd = Product.objects.get(id=id)
    orderToAdd = Order(
        product=productToAdd,
        user=request.user
    )
    orderToAdd.save()
    messages.success(request, 'New order added.')
    return redirect('order')