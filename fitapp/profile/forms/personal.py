from django import forms
from ..models import Profile
from ._mixins import AdminLTEFormMixin


class PersonalProfileForm(AdminLTEFormMixin, forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "height",
            "weight",
            "age",
            "goal",
            "cref",
            "city",
            "specialty",
            "bio",
            "photo",
        ]
