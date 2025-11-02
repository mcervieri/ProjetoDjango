from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def require_completed_profile(view_func):
    @login_required
    def wrapper(request, *args, **kwargs):
        profile = request.user.profile
        if not profile.is_completed:
            if profile.role == "aluno":
                return redirect("profile:complete_aluno")
            elif profile.role == "nutricionista":
                return redirect("profile:complete_nutri")
            elif profile.role == "personal":
                return redirect("profile:complete_personal")
        return view_func(request, *args, **kwargs)

    return wrapper
