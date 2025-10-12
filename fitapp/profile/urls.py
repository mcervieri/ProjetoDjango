from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import dashboard, register, aluno, nutri, personal, account

app_name = "profile"

urlpatterns = [
    # Autenticação
    path("login/", LoginView.as_view(template_name="profile/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="profile:login"), name="logout"),
    path("register/", register.register, name="register"),
    # Dashboard (após logar)
    path("dashboard/", dashboard.dashboard, name="dashboard"),
    # Completar dados conforme role
    path("complete/aluno/", aluno.complete_aluno, name="complete_aluno"),
    path("complete/nutri/", nutri.complete_nutri, name="complete_nutri"),
    path("complete/personal/", personal.complete_personal, name="complete_personal"),
    # Páginas pessoais
    path("meu-perfil/", account.me_detail, name="me_detail"),
    path("meu-perfil/editar/", account.me_edit, name="me_edit"),
    # Sucesso genérico
    path("success/", register.success, name="success"),
]
