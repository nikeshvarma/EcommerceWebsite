from django import forms
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()


class SignUpForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
