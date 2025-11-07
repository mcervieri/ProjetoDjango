from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from fitapp.profile.models.choices import RolesChoices


class UserRegisterForm(UserCreationForm):
    role = forms.ChoiceField(
        choices=[
            ("", "Selecione uma opção"),
            (RolesChoices.ALUNO, "Aluno"),
            (RolesChoices.NUTRICIONISTA, "Nutricionista"),
            (RolesChoices.PERSONAL, "Personal Trainer"),
        ],
        label="Tipo de Usuário",
        required=True,
        error_messages={
            "required": "Por favor, selecione o tipo de usuário.",
        },
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "role"]
        labels = {
            "username": "Nome de Usuário",
            "email": "E-mail",
            "password1": "Senha",
            "password2": "Confirmação de Senha",
            "role": "Tipo de Usuário",
        }
        help_texts = {
            "username": "Obrigatório. Apenas letras, números e @/./+/-/_",
            "password1": (
                "A senha deve conter pelo menos 8 caracteres, "
                "não pode ser apenas numérica, "
                "e não pode ser muito semelhante ao seu nome de usuário."
            ),
            "password2": "Digite a mesma senha para confirmação.",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.pop("required", None)

    def clean(self):
        cleaned_data = super().clean()
        missing_fields = [name for name, value in cleaned_data.items() if not value]

        if missing_fields:
            raise forms.ValidationError(
                "Por favor, preencha todos os campos obrigatórios."
            )

        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email:
            raise forms.ValidationError("O campo de e-mail é obrigatório.")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Já existe uma conta com este e-mail.")
        return email

    def save(self, commit=True):
        user = super().save(commit)
        role = self.cleaned_data.get("role")

        if commit:
            from fitapp.profile.models import Profile

            profile, _ = Profile.objects.get_or_create(user=user)
            profile.role = role
            profile.save()

        return user
