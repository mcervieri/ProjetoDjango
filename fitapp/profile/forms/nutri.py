from django import forms
from ..models import Profile
from ._mixins import AdminLTEFormMixin


class NutriProfileForm(AdminLTEFormMixin, forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "height",
            "weight",
            "age",
            "goal",
            "crn",
            "city",
            "specialty",
            "bio",
            "photo",
        ]
