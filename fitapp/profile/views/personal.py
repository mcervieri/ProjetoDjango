from django.shortcuts import render, redirect
from ..forms.personal import PersonalProfileForm
from django.contrib.auth.decorators import login_required


@login_required
def complete_personal(request):
    profile = request.user.profile
    if request.method == "POST":
        form = PersonalProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect(
                "home"
            )  # redireciona pra página inicial (ajusta se precisar)
    else:
        form = PersonalProfileForm(instance=profile)
    return render(request, "profile/complete_personal.html", {"form": form})
