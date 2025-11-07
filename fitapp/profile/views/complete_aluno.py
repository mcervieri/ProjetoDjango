from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from fitapp.profile.forms.aluno import AlunoForm


@login_required
def complete_aluno(request):
    """Formulário de complementação do perfil do aluno (primeiro acesso)."""
    profile = request.user.profile

    if request.method == "POST":
        form = AlunoForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            profile.is_completed = True
            profile.save()
            return redirect("profile:dashboard")
    else:
        form = AlunoForm(instance=profile)

    return render(request, "aluno/complete.html", {"form": form})
