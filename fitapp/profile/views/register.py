from django.shortcuts import render, redirect
from django.contrib.auth import login
from ..forms.register import UserRegisterForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            role = user.profile.role
            if role == "aluno":
                return redirect("profile:complete_aluno")
            elif role == "nutricionista":
                return redirect("profile:complete_nutri")
            elif role == "personal":
                return redirect("profile:complete_personal")
    else:
        form = UserRegisterForm()
    return render(request, "profile/register.html", {"form": form})


def success(request):
    return render(request, "profile/success.html")
