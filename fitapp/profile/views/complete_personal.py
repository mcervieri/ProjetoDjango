from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from fitapp.profile.forms.personal import PersonalForm


@login_required
def complete_personal(request):
    """Formulário de complementação do perfil do Personal Trainer."""
    profile = request.user.profile

    if request.method == "POST":
        form = PersonalForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            profile.is_completed = True
            profile.save()
            return redirect("profile:dashboard")
    else:
        form = PersonalForm(instance=profile)

    return render(request, "personal/complete.html", {"form": form})
