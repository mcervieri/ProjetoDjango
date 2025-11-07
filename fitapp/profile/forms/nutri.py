from django import forms
from fitapp.profile.models import Profile


class NutriForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["photo", "crn", "city", "specialty", "bio"]
        labels = {
            "photo": "Foto de Perfil",
            "crn": "CRN",
            "city": "Cidade",
            "specialty": "Especialidade",
            "bio": "Sobre você",
        }
        widgets = {
            field: forms.TextInput(attrs={"class": "form-control fitapp-input"})
            for field in ["crn", "city", "specialty"]
        } | {
            "bio": forms.Textarea(
                attrs={"class": "form-control fitapp-input", "rows": 3}
            ),
            "photo": forms.ClearableFileInput(
                attrs={"class": "form-control fitapp-input"}
            ),
        }
