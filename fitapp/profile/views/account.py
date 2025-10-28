from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from ..forms.aluno import AlunoProfileForm
from ..forms.nutri import NutriProfileForm
from ..forms.personal import PersonalProfileForm


@login_required
def me_detail(request):
    user_obj = request.user
    return render(request, "profile/detail.html", {"user_obj": user_obj})


@login_required
def me_edit(request):
    user = request.user
    profile = user.profile

    form_cls = {
        "aluno": AlunoProfileForm,
        "nutricionista": NutriProfileForm,
        "personal": PersonalProfileForm,
    }.get(profile.role, AlunoProfileForm)

    if request.method == "POST":
        form = form_cls(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Seu perfil foi atualizado com sucesso!")
            return redirect("profile:me_detail")
    else:
        form = form_cls(instance=profile)

    return render(request, "profile/edit.html", {"form": form, "user_obj": user})


def logout_on_login(request):
    """
    Garante que, se o usuário acessar /profile/login/ enquanto ainda está logado,
    ele será deslogado automaticamente e redirecionado para a tela de login limpa.
    """
    if request.user.is_authenticated:
        logout(request)
    return redirect("profile:login")
