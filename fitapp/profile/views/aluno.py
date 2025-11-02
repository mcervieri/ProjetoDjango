from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Profile
from ..forms.aluno import AlunoProfileForm


@login_required
def complete_aluno(request):
    profile = request.user.profile

    if request.method == "POST":
        form = AlunoProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            profile.is_completed = True
            profile.save()
            return redirect("profile:dashboard")
    else:
        form = AlunoProfileForm(instance=profile)

    return render(request, "profile/complete_aluno.html", {"form": form})
