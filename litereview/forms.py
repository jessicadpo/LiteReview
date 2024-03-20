""""Module containing forms for the LiteReview"""


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class SignUpForm(UserCreationForm):  # pylint: disable=too-many-ancestors
    """
    Copied from: https://www.javatpoint.com/django-usercreationform
    With some modifications
    """
    username = forms.CharField(label=False, min_length=1, max_length=150, widget=forms.TextInput(
        attrs={'class': 'signup-input', 'placeholder': 'Username'}))
    email = forms.EmailField(label=False, widget=forms.EmailInput(
        attrs={'class': 'signup-input', 'placeholder': 'Email'}))
    password1 = forms.CharField(label=False, widget=forms.PasswordInput(
        attrs={'class': 'signup-input', 'placeholder': 'Password'}))
    password2 = forms.CharField(label=False, widget=forms.PasswordInput(
        attrs={'class': 'signup-input', 'placeholder': 'Confirm Password'}))

    def clean_username(self):
        """prevents duplicate usernames"""
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username=username)
        if new.count():
            raise ValidationError("User Already Exist")
        return username

    def clean_email(self):
        """prevents duplicate emails"""
        # resolve issues in another branch, doesn't work yet
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError("Email Already Exist")
        return email

    def clean_password2(self):  #
        """prevents mismatching password/confirms"""
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2

    def save(self, commit=True):
        """saves cleaned data for the form"""
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user


class LoginForm(forms.Form):
    """Copied from https://medium.com/@devsumitg/django-auth-user-signup-and-login-7b424dae7fab"""
    username = forms.CharField(label=False, min_length=1, max_length=150,
        widget=forms.TextInput(attrs={'class': 'login-input', 'placeholder': 'Username'}))
    password = forms.CharField(label=False,
        widget=forms.PasswordInput(attrs={'class': 'login-input', 'placeholder': 'Password'}))
