from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from fitapp.profile.forms.nutri import NutriForm
from fitapp.profile.models.choices import RolesChoices


@login_required
def nutri_detail(request):
    """Exibe o perfil do nutricionista logado e seus alunos vinculados."""
    nutri = request.user.profile

    if nutri.role.strip().lower() != RolesChoices.NUTRICIONISTA.strip().lower():
        return redirect("profile:dashboard")

    alunos = (
        nutri.alunos_nutricionista.all()
        if hasattr(nutri, "alunos_nutricionista")
        else []
    )

    return render(
        request,
        "nutri/detail.html",
        {
            "nutri": nutri,
            "alunos": alunos,
        },
    )


@login_required
def nutri_edit(request):
    """Permite editar os dados do nutricionista logado."""
    nutri = request.user.profile

    if nutri.role.strip().lower() != RolesChoices.NUTRICIONISTA.strip().lower():
        return redirect("profile:dashboard")

    form = NutriForm(request.POST or None, request.FILES or None, instance=nutri)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("profile:nutri_profile")

    return render(request, "nutri/edit.html", {"form": form})
