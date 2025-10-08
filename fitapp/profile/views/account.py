from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import transaction
from ..forms.aluno import AlunoProfileForm
from ..forms.nutri import NutriProfileForm
from ..forms.personal import PersonalProfileForm


# Helper: só superuser pode deletar
def is_admin(user):
    return user.is_superuser


@login_required
def edit_profile(request):
    profile = request.user.profile
    form_cls = {
        "aluno": AlunoProfileForm,
        "nutricionista": NutriProfileForm,
        "personal": PersonalProfileForm,
    }.get(profile.role, AlunoProfileForm)

    if request.method == "POST":
        form = form_cls(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil atualizado com sucesso!")
            return redirect("profile:dashboard")
    else:
        form = form_cls(instance=profile)

    return render(request, "profile/edit.html", {"form": form})


@user_passes_test(is_admin)
@transaction.atomic
def delete_account(request, user_id):
    """Apenas superuser pode excluir usuários"""
    user = get_object_or_404(User, pk=user_id)
    if request.method == "POST":
        username = user.username
        user.delete()
        messages.success(request, f"Usuário '{username}' excluído com sucesso.")
        return redirect("/admin/auth/user/")

    return render(request, "profile/confirm_delete.html", {"user": user})
