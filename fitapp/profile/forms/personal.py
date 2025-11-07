from django import forms
from fitapp.profile.models import Profile
from fitapp.profile.forms._mixins import AdminLTEFormMixin


class PersonalForm(AdminLTEFormMixin, forms.ModelForm):
    """Formulário de edição do perfil de Personal Trainer."""

    class Meta:
        model = Profile
        fields = [
            "photo",
            "bio",
            "height",
            "weight",
            "age",
            "goal",
            "cref",
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
            "cref": "CREF (Registro Profissional)",
            "specialty": "Especialidade",
            "city": "Cidade de Atuação",
        }
        help_texts = {
            "photo": "Envie uma foto quadrada (ex: 400x400px) para seu perfil.",
            "goal": "Ex: Treinamento funcional, musculação, condicionamento físico...",
            "specialty": "Ex: Treinamento de força, reabilitação, emagrecimento...",
            "cref": "Informe seu número de registro no Conselho Regional de Educação Física.",
        }
        widgets = {
            "photo": forms.ClearableFileInput(
                attrs={"class": "form-control fitapp-input"}
            ),
            "bio": forms.Textarea(
                attrs={"class": "form-control fitapp-input", "rows": 3}
            ),
            "height": forms.NumberInput(attrs={"class": "form-control fitapp-input"}),
            "weight": forms.NumberInput(attrs={"class": "form-control fitapp-input"}),
            "age": forms.NumberInput(attrs={"class": "form-control fitapp-input"}),
            "goal": forms.TextInput(attrs={"class": "form-control fitapp-input"}),
            "cref": forms.TextInput(attrs={"class": "form-control fitapp-input"}),
            "specialty": forms.TextInput(attrs={"class": "form-control fitapp-input"}),
            "city": forms.TextInput(attrs={"class": "form-control fitapp-input"}),
        }
