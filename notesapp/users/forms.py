from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={"class": "input-box title-info-size"}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "input-box title-info-size"}))
    password2 = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput(attrs={"class": "input-box title-info-size"}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={"class": "input-box title-info-size"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "input-box title-info-size"}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

