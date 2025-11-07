from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from fitapp.profile.forms.personal import PersonalForm
from fitapp.profile.models import Profile
from fitapp.profile.models.choices import RolesChoices


@login_required
def personal_detail(request):
    """Exibe o perfil do personal trainer logado."""
    personal = request.user.profile
    return render(request, "personal/detail.html", {"personal": personal})


@login_required
def personal_edit(request):
    """Permite editar os dados do personal trainer logado."""
    personal = request.user.profile
    form = PersonalForm(request.POST or None, request.FILES or None, instance=personal)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("profile:personal_profile")

    return render(request, "personal/edit.html", {"form": form})
