from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, "home_view.html", {
        "title":"Home"
    })

def store_view(request):
    return render(request, "store_view.html", {
        "title":"Store"
    })

def order_view(request):
    return render(request, "order_view.html", {
        "title":"Order"
    })