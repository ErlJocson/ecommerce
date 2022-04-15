import os
from django.shortcuts import redirect, render
from .models import Order, Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

def home_view(request):
    products = Product.objects.filter(stock__gte = 1)
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
    productToAdd.stock = productToAdd.stock - 1
    productToAdd.save()

    orderToAdd = Order(
        product=productToAdd,
        user=request.user
    )
    orderToAdd.save()
    messages.success(request, 'New order added.')
    return redirect('order')

def add_product(request):
    if request.method == "POST":
        name    = request.POST['name']
        details = request.POST['details']
        price   = request.POST['price']
        stock   = request.POST['stock']
        image   = request.FILES['image']
        seller  = User.objects.get(id=request.user.id)

        productToAdd = Product(
            name    = name,
            details = details,
            price   = price,
            stock   = stock,
            image   = image,
            seller  = seller,
        )
        productToAdd.save() 
        messages.success(request, 'Product added.')
        return redirect('home')
    return render(request, 'add_product.html', {
        "title":"Add product"
    })

@login_required
def delete_product(request, id):
    productToDelete = Product.objects.get(id=id)
    productToDelete.delete()
    messages.success(request, 'Product delete.')
    return redirect('store')
