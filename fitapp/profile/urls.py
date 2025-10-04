from django.urls import path
from .views import register, aluno, nutri, personal

app_name = "profile"

urlpatterns = [
    path("register/", register.register, name="register"),
    path("complete/aluno/", aluno.complete_aluno, name="complete_aluno"),
    path("complete/nutri/", nutri.complete_nutri, name="complete_nutri"),
    path("complete/personal/", personal.complete_personal, name="complete_personal"),
    path("success/", register.success, name="success"),
]
