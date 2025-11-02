from django.urls import path
from fitapp.profile.views import (
    dashboard,
    register,
    aluno,
    personal,
    nutri,
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
    path("complete/aluno/", aluno.complete_aluno, name="complete_aluno"),
    path("complete/personal/", personal.complete_personal, name="complete_personal"),
    path("complete/nutri/", nutri.complete_nutri, name="complete_nutri"),
    # 👤 PERFIL PESSOAL (visualizar / editar)
    path("meu-perfil/", account.me_detail, name="me_detail"),
    path("meu-perfil/editar/", account.me_edit, name="me_edit"),
]
