from django.shortcuts import render, redirect
from django.contrib.auth import login
from ..forms.register import UserRegisterForm
from ..models import Profile
from ..models.choices import RolesChoices


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            profile = Profile.objects.get(user=user)
            role = profile.role

            if role == RolesChoices.ALUNO:
                return redirect("profile:complete_aluno")
            elif role == RolesChoices.NUTRICIONISTA:
                return redirect("profile:complete_nutri")
            elif role == RolesChoices.PERSONAL:
                return redirect("profile:complete_personal")

            return redirect("profile:dashboard")
    else:
        form = UserRegisterForm()

    return render(request, "profile/register.html", {"form": form})
