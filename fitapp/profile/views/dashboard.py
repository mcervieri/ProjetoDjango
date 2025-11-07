from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..decorators import require_completed_profile


@login_required
@require_completed_profile
def dashboard(request):
    """Renderiza o dashboard conforme o tipo de usuário (role)."""
    role = getattr(request.user.profile, "role", "").upper()

    if role == "NUTRICIONISTA":
        template = "nutri/dashboard.html"
    elif role == "PERSONAL":
        template = "personal/dashboard.html"
    else:
        template = "aluno/dashboard.html"

    return render(request, template, {"user": request.user})
