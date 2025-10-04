from django import forms
from profile.models import Profile


class AlunoProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["height", "weight", "age", "goal"]
