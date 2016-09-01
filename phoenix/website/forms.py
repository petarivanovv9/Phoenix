from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'autofocus': ''}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
