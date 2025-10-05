from django.shortcuts import render, redirect
from ..forms.aluno import AlunoProfileForm


def complete_aluno(request):
    profile = request.user.profile
    if request.method == "POST":
        form = AlunoProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = AlunoProfileForm(instance=profile)
    return render(request, "profile/complete_aluno.html", {"form": form})
