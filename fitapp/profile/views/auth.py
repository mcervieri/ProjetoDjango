from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# LOGIN
def login_view(request):
    # 🔹 Garante que o usuário será deslogado ao abrir a tela de login
    if request.user.is_authenticated:
        logout(request)
        request.session.flush()

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("profile:dashboard")
        else:
            messages.error(request, "Usuário ou senha inválidos.")
            return render(request, "profile/login.html")

    return render(request, "profile/login.html")


# LOGOUT
def logout_view(request):
    if request.method in ["GET", "POST"]:
        logout(request)
        request.session.flush()
    return redirect("profile:login")
