from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from fitapp.profile.forms.nutri import NutriForm
from fitapp.profile.models import Profile
from fitapp.profile.models.choices import RolesChoices


@login_required
def nutri_detail(request):
    """Exibe o perfil do nutricionista logado."""
    nutri = get_object_or_404(
        Profile, user=request.user, role=RolesChoices.NUTRICIONISTA
    )
    return render(request, "nutri/detail.html", {"nutri": nutri})


@login_required
def nutri_edit(request):
    """Permite editar os dados do nutricionista logado."""
    nutri = get_object_or_404(
        Profile, user=request.user, role=RolesChoices.NUTRICIONISTA
    )
    form = NutriForm(request.POST or None, request.FILES or None, instance=nutri)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("profile:nutri_detail")

    return render(request, "nutri/edit.html", {"form": form})
