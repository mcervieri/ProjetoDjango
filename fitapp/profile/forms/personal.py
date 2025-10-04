from django import forms
from profile.models import Profile


class PersonalProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["height", "weight", "age", "goal", "cref", "city", "specialty"]
