from django.urls import path
from fitapp.profile.views import (
    dashboard,
    register,
    aluno,
    complete_aluno,
    personal,
    complete_personal,
    nutri,
    complete_nutri,
    account,
    auth,
)

app_name = "profile"

urlpatterns = [
    # 🟢 LOGIN — limpa sessão anterior antes de exibir a tela
    path("login/", auth.login_view, name="login"),
    # 🔴 LOGOUT — permite GET e POST (sem erro 405)
    path("logout/", auth.logout_view, name="logout"),
    # 🧾 REGISTRO
    path("register/", register.register, name="register"),
    # 📊 DASHBOARD
    path("dashboard/", dashboard.dashboard, name="dashboard"),
    # 👥 COMPLETAR DADOS (conforme a role)
    path("complete/aluno/", complete_aluno.complete_aluno, name="complete_aluno"),
    path(
        "complete/personal/",
        complete_personal.complete_personal,
        name="complete_personal",
    ),
    path("complete/nutri/", complete_nutri.complete_nutri, name="complete_nutri"),
    # 👤 PERFIS (visualizar / editar)
    path("aluno/", aluno.aluno_detail, name="aluno_profile"),
    path("aluno/editar/", aluno.aluno_edit, name="aluno_edit"),
    path("nutri/", nutri.nutri_detail, name="nutri_profile"),
    path("nutri/editar/", nutri.nutri_edit, name="nutri_edit"),
    path("personal/", personal.personal_detail, name="personal_profile"),
    path("personal/editar/", personal.personal_edit, name="personal_edit"),
]
