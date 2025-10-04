from django.shortcuts import render, redirect
from profile.forms.personal import PersonalProfileForm


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
