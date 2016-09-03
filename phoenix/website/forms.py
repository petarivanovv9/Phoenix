from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from .helpers import get_or_none, validate_password


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={'class': 'pure-input-1', 'placeholder': 'Username', 'autofocus': ''}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'pure-input-1', 'placeholder': 'Password'}))


class RegisterForm(forms.Form):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'autofocus': ''})
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def clean_username(self):
        username = self.cleaned_data.get("username")
        user = get_or_none(User, username=username)
        if user is not None:
            raise ValidationError("User already exists.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get("password")
        self._validate_password_strength(password)
        return password

    def clean_email(self):
        email = self.cleaned_data.get("email")
        user = get_or_none(User, email=email)
        if user is not None:
            raise ValidationError("User already exists.")
        return email

    def save(self):
        user = User.objects.create_user(
                username=self.cleaned_data.get('username'),
                email=self.cleaned_data.get('email'),
                password=self.cleaned_data.get('password')
        )
        user.save()
        return user

    def _validate_password_strength(self, value):
        validate_password(value)
