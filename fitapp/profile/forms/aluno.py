from django import forms
from fitapp.profile.models import Profile
from fitapp.profile.models.choices import RolesChoices


class AlunoForm(forms.ModelForm):
    personal = forms.ModelChoiceField(
        queryset=Profile.objects.filter(role=RolesChoices.PERSONAL),
        required=False,
        label="Personal Trainer",
        widget=forms.Select(attrs={"class": "form-control fitapp-input"}),
    )

    nutricionista = forms.ModelChoiceField(
        queryset=Profile.objects.filter(role=RolesChoices.NUTRICIONISTA),
        required=False,
        label="Nutricionista",
        widget=forms.Select(attrs={"class": "form-control fitapp-input"}),
    )

    class Meta:
        model = Profile
        fields = [
            "photo",
            "age",
            "height",
            "weight",
            "goal",
            "bio",
            "personal",
            "nutricionista",
        ]
        labels = {
            "photo": "Foto de Perfil",
            "age": "Idade",
            "height": "Altura (cm)",
            "weight": "Peso (kg)",
            "goal": "Meta",
            "bio": "Sobre você",
            "personal": "Personal Trainer",
            "nutricionista": "Nutricionista",
        }
        widgets = {
            field: forms.TextInput(attrs={"class": "form-control fitapp-input"})
            for field in ["age", "height", "weight", "goal"]
        } | {
            "bio": forms.Textarea(
                attrs={"class": "form-control fitapp-input", "rows": 3}
            ),
            "photo": forms.ClearableFileInput(
                attrs={"class": "form-control fitapp-input"}
            ),
        }
