from django import forms
from fitapp.profile.models import Profile
from fitapp.profile.forms._mixins import AdminLTEFormMixin


class NutriForm(AdminLTEFormMixin, forms.ModelForm):
    """Formulário de edição do perfil de Nutricionista."""

    class Meta:
        model = Profile
        fields = [
            "photo",
            "bio",
            "height",
            "weight",
            "age",
            "goal",
            "crn",
            "specialty",
            "city",
        ]
        labels = {
            "photo": "Foto de Perfil",
            "bio": "Sobre você",
            "height": "Altura (cm)",
            "weight": "Peso (kg)",
            "age": "Idade",
            "goal": "Objetivo Profissional",
            "crn": "CRN (Registro Profissional)",
            "specialty": "Especialidade",
            "city": "Cidade de Atuação",
        }
        help_texts = {
            "photo": "Envie uma foto quadrada (ex: 400x400px) para seu perfil.",
            "goal": "Ex: Auxiliar pacientes com emagrecimento, hipertrofia, etc.",
            "specialty": "Ex: Nutrição esportiva, clínica, funcional...",
            "crn": "Informe seu número de registro no Conselho Regional de Nutricionistas.",
        }
