from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60)

    class Meta:
        model = CustomUser
        fields = ("email", "username", "first_name", "last_name", "password1", "password2")
