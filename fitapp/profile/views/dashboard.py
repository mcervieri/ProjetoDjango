from django.shortcuts import render


def dashboard(request):
    return render(request, "profile/dashboard.html")
