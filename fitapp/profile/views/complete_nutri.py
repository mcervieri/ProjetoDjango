from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from fitapp.profile.forms.nutri import NutriForm


@login_required
def complete_nutri(request):
    """Formulário de complementação do perfil do Nutricionista."""
    profile = request.user.profile

    if request.method == "POST":
        form = NutriForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            profile.is_completed = True
            profile.save()
            return redirect("profile:dashboard")
    else:
        form = NutriForm(instance=profile)

    return render(request, "nutri/complete.html", {"form": form})
