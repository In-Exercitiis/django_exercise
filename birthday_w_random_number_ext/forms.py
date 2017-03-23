from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import BirthdayWRandomNumberExt


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username']


class BirthdayWRandomNumberExtForm(ModelForm):
    class Meta:
        model = BirthdayWRandomNumberExt
        fields = ['birthday']
