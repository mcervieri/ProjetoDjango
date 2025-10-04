from django import forms
from django.contrib.auth.models import User
from models.choices import RolesChoices, Profile


class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(label="Senha", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirmação de Senha", widget=forms.PasswordInput
    )
    role = forms.ChoiceField(choices=RolesChoices.choices)

    class Meta:
        model = User
        fields = ["username", "email"]

    def clean_password2(self):
        p1 = self.cleaned_data.get("password1")
        p2 = self.cleaned_data.get("password2")
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("As senhas não coincidem.")
        return p2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            Profile.objects.create(user=user, role=self.cleaned_data["role"])
        return user
