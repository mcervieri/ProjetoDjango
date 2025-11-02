from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Profile
from ..forms.personal import PersonalProfileForm


@login_required
def complete_personal(request):
    profile = request.user.profile

    if request.method == "POST":
        form = PersonalProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            profile.is_completed = True
            profile.save()
            return redirect("profile:dashboard")
    else:
        form = PersonalProfileForm(instance=profile)

    return render(request, "profile/complete_personal.html", {"form": form})
