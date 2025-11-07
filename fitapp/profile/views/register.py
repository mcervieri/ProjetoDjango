from django.shortcuts import render, redirect
from django.contrib.auth import login
from ..forms.register import UserRegisterForm
from ..models import Profile
from ..models.choices import RolesChoices


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)

            # 🟢 Atualiza o profile recém-criado com o role escolhido
            role = form.cleaned_data.get("role")
            profile = user.profile
            profile.role = role.upper() if isinstance(role, str) else role
            profile.save()

            # 🔄 Redireciona conforme o tipo de usuário
            if profile.role == RolesChoices.ALUNO:
                return redirect("profile:complete_aluno")
            elif profile.role == RolesChoices.NUTRICIONISTA:
                return redirect("profile:complete_nutri")
            elif profile.role == RolesChoices.PERSONAL:
                return redirect("profile:complete_personal")

            return redirect("profile:dashboard")
    else:
        form = UserRegisterForm()

    return render(request, "profile/register.html", {"form": form})
