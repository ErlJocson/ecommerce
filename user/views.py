from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout as django_logout
from django.contrib import messages

def login_view(request):
    if request.user.is_authenticated:
        messages.success(request, 'You are authenticated as ' + request.user.username)
        return redirect('home')

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, "There was an error!")
    return render(request, "login_view.html", {
        "title":"Login"
    })

def register_view(request):
    if request.user.is_authenticated:
        messages.success(request, 'You are authenticated as ' + request.user.username)
        return redirect('home')
        
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            try:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=password,
                )
                user.save()
                login(request, user)
                return redirect('home')
            except:
                messages.warning(request, 'There was an error!')
        messages.warning(request, 'Password do not match!')
    return render(request, "register_view.html", {
        "title":"Register"
    })

def logout(request):
    django_logout(request)
    messages.success(request, 'Logout success')
    return redirect('home')