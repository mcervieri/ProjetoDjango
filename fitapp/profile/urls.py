from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import dashboard, register, aluno, nutri, personal

app_name = "profile"

urlpatterns = [
    path("register/", register.register, name="register"),
    path("dashboard/", dashboard.dashboard, name="dashboard"),
    path("login/", LoginView.as_view(template_name="profile/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="profile:register"), name="logout"),
    path("complete/aluno/", aluno.complete_aluno, name="complete_aluno"),
    path("complete/nutri/", nutri.complete_nutri, name="complete_nutri"),
    path("complete/personal/", personal.complete_personal, name="complete_personal"),
    path("success/", register.success, name="success"),
]
