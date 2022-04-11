from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, "login_view", {})

def register_view(request):
    return render(request, "register_view.html", {})