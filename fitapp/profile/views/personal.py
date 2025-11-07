from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from fitapp.profile.forms.personal import PersonalForm
from fitapp.profile.models.choices import RolesChoices


@login_required
def personal_detail(request):
    """Exibe o perfil do personal trainer logado e seus alunos vinculados."""
    personal = request.user.profile

    if personal.role.strip().lower() != RolesChoices.PERSONAL.strip().lower():
        return redirect("profile:dashboard")

    alunos = (
        personal.alunos_personal.all() if hasattr(personal, "alunos_personal") else []
    )

    return render(
        request,
        "personal/detail.html",
        {
            "personal": personal,
            "alunos": alunos,
        },
    )


@login_required
def personal_edit(request):
    """Permite editar os dados do personal trainer logado."""
    personal = request.user.profile

    if personal.role.strip().lower() != RolesChoices.PERSONAL.strip().lower():
        return redirect("profile:dashboard")

    form = PersonalForm(request.POST or None, request.FILES or None, instance=personal)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("profile:personal_profile")

    return render(request, "personal/edit.html", {"form": form})
