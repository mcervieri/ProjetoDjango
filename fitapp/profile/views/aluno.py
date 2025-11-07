from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from fitapp.profile.forms.aluno import AlunoForm
from fitapp.profile.models.choices import RolesChoices


@login_required
def aluno_detail(request):
    """Exibe o perfil do aluno logado."""
    aluno = request.user.profile

    if aluno.role.strip().lower() != RolesChoices.ALUNO.strip().lower():
        return redirect("profile:dashboard")

    return render(request, "aluno/detail.html", {"aluno": aluno})


@login_required
def aluno_edit(request):
    """Permite editar os dados do aluno logado."""
    aluno = request.user.profile

    if aluno.role.strip().lower() != RolesChoices.ALUNO.strip().lower():
        return redirect("profile:dashboard")

    form = AlunoForm(request.POST or None, request.FILES or None, instance=aluno)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("profile:aluno_profile")

    return render(request, "aluno/edit.html", {"form": form})
