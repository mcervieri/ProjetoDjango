from django import forms
from fitapp.profile.models import Profile
from fitapp.profile.forms._mixins import AdminLTEFormMixin


class AlunoForm(AdminLTEFormMixin, forms.ModelForm):
    """Formulário de edição do perfil do Aluno."""

    class Meta:
        model = Profile
        fields = [
            "photo",
            "bio",
            "height",
            "weight",
            "age",
            "goal",
            "city",
        ]
        labels = {
            "photo": "Foto de Perfil",
            "bio": "Sobre você",
            "height": "Altura (cm)",
            "weight": "Peso (kg)",
            "age": "Idade",
            "goal": "Objetivo",
            "city": "Cidade",
        }
        help_texts = {
            "photo": "Envie uma foto quadrada (ex: 400x400px) para seu perfil.",
            "goal": "Ex: Ganho de massa, perda de peso, resistência...",
        }
