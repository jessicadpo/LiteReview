""""Module containing forms for the LiteReview"""

from django import forms


class LoginForm(forms.Form):
    """Copied from https://medium.com/@devsumitg/django-auth-user-signup-and-login-7b424dae7fab"""
    username = forms.CharField(label=False, min_length=1, max_length=150,
        widget=forms.TextInput(attrs={'class': 'login-input', 'placeholder': 'Username'}))
    password = forms.CharField(label=False,
        widget=forms.PasswordInput(attrs={'class': 'login-input', 'placeholder': 'Password'}))
