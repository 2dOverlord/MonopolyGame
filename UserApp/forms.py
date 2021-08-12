from django import forms

from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, UserCreationForm
from django.contrib.auth import authenticate

from .models import CustomUser


class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60)
    form = CustomUser()
    pk = form.get_id()

    class Meta:
        model = CustomUser
        fields = ("email",'first_name','last_name', "username", "password1", "password2", 'date_birth')


class CustomUserAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'password')

    def clean(self):

        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username, password=password):
            raise forms.ValidationError("Invalid login")

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control' }))
    first_name = forms.CharField(max_length=100, widget = forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget = forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget = forms.TextInput(attrs={'class': 'form-control'}))

    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password','image')


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget = forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password1 = forms.CharField(max_length=100, widget = forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password2 = forms.CharField(max_length=100, widget = forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    
    class Meta:
        model = CustomUser
        fields = ('old_password', 'new_password1', 'new_password2')