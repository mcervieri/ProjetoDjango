from django import forms
from ..models import Profile
from ._mixins import AdminLTEFormMixin


class AlunoProfileForm(AdminLTEFormMixin, forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["height", "weight", "age", "goal", "bio", "photo"]
