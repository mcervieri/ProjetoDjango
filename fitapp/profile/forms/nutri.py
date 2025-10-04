from django import forms
from profile.models import Profile


class NutriProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["height", "weight", "age", "goal", "crn", "city", "specialty"]
