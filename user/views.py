from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, "login_view.html", {
        "title":"Login"
    })

def register_view(request):
    return render(request, "register_view.html", {
        "title":"Register"
    })