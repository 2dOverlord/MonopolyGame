from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import CustomUser


class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60)

    class Meta:
        model = CustomUser
        fields = ("email",'first_name','last_name', "username", "password1", "password2", 'date_birth')


class CustomUserAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    def clean(self):

        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid login")