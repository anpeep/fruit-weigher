# useraccounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

class CustomSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise ValidationError("Your password must contain at least 8 characters.")
        if not re.search(r'[A-Z]', password1):
            raise ValidationError("Your password must contain at least one uppercase letter.")
        if not re.search(r'[a-z]', password1):
            raise ValidationError("Your password must contain at least one lowercase letter.")
        if not re.search(r'[0-9]', password1):
            raise ValidationError("Your password must contain at least one number.")
        if password1.lower() in ["password", "123456", "abcdef"]:
            raise ValidationError("Your password is too common. Please choose a more secure password.")
        return password1
