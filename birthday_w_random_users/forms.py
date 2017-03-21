from django.forms import HiddenInput, ModelForm
from .models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['birthday']
