from django.shortcuts import render, redirect
from profile.forms.nutri import NutriProfileForm


def complete_nutri(request):
    profile = request.user.profile
    if request.method == "POST":
        form = NutriProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect(
                "home"
            )  # redireciona pra página inicial (ajusta se tiver outra)
    else:
        form = NutriProfileForm(instance=profile)
    return render(request, "profile/complete_nutri.html", {"form": form})
