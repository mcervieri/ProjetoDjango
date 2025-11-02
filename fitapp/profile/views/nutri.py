from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Profile
from ..forms.nutri import NutriProfileForm


@login_required
def complete_nutri(request):
    profile = request.user.profile

    if request.method == "POST":
        form = NutriProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            profile.is_completed = True
            profile.save()
            return redirect("profile:dashboard")
    else:
        form = NutriProfileForm(instance=profile)

    return render(request, "profile/complete_nutri.html", {"form": form})
