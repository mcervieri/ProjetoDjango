from django import forms
from django.contrib.auth.models import User
from ..models import Profile
from ..models.choices import RolesChoices
from ._mixins import TailwindFormMixin
from django.core.exceptions import ValidationError


class UserRegisterForm(TailwindFormMixin, forms.ModelForm):
    password1 = forms.CharField(label="Senha", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirmação de Senha", widget=forms.PasswordInput
    )
    role = forms.ChoiceField(
        choices=[
            (r.value, r.label)
            for r in RolesChoices
            if r.value != RolesChoices.ADMIN  # 🔒 não permite admin na tela
        ]
    )

    class Meta:
        model = User
        fields = ["username", "email"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email and User.objects.filter(email__iexact=email).exists():
            raise ValidationError("Este e-mail já está em uso.")
        return email

    def clean_password2(self):
        p1 = self.cleaned_data.get("password1")
        p2 = self.cleaned_data.get("password2")
        if p1 and p2 and p1 != p2:
            raise ValidationError("As senhas não coincidem.")
        return p2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            Profile.objects.create(user=user, role=self.cleaned_data["role"])
        return user
