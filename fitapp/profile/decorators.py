from functools import wraps
from django.shortcuts import redirect


def require_completed_profile(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        user = request.user

        if user.is_superuser:
            return view_func(request, *args, **kwargs)

        profile = getattr(user, "profile", None)
        if not profile:
            return redirect("profile:complete_aluno")

        if not getattr(profile, "is_completed", False):
            role = (profile.role or "").lower()
            if role == "aluno":
                return redirect("profile:complete_aluno")
            elif role == "nutricionista":
                return redirect("profile:complete_nutri")
            elif role == "personal":
                return redirect("profile:complete_personal")
            else:
                return redirect("profile:complete_aluno")

        return view_func(request, *args, **kwargs)

    return wrapper
