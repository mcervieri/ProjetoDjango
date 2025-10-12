from django import forms
from ..models import Profile
from ._mixins import TailwindFormMixin


class AlunoProfileForm(TailwindFormMixin, forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["height", "weight", "age", "goal", "bio", "photo"]
