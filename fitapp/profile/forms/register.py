from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from fitapp.profile.models.choices import RolesChoices


class UserRegisterForm(UserCreationForm):
    role = forms.ChoiceField(
        choices=[
            (RolesChoices.ALUNO, "Aluno"),
            (RolesChoices.NUTRICIONISTA, "Nutricionista"),
            (RolesChoices.PERSONAL, "Personal Trainer"),
        ],
        label="Tipo de Usuário",
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "role"]

    def save(self, commit=True):
        user = super().save(commit)
        role = self.cleaned_data.get("role")

        if commit:
            from fitapp.profile.models import Profile

            profile, _ = Profile.objects.get_or_create(user=user)
            profile.role = role
            profile.save()

        return user
