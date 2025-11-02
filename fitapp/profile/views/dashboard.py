# dashboard.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..decorators import require_completed_profile


@login_required
@require_completed_profile
def dashboard(request):
    return render(request, "profile/dashboard.html")
