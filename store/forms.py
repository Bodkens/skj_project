from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, UsernameField, UserChangeForm
from django.contrib.auth.models import User


class CustomerRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = UsernameField(widget=forms.TextInput(attrs={"class": "form-control"}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput(attrs={"class": "form-control"}))


class CustomerLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']

    username = UsernameField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))


class CustomerChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']

    old_password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    new_password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    new_password2 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))
