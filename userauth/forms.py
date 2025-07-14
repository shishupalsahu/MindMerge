from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta():
        model = User
        fields = ('first_name','last_name','username','email', 'password1', 'password2')
        widgets = {
            'first_name': forms.TextInput(attrs={'required': True}),
            'last_name': forms.TextInput(attrs={'required': True}),
            'username': forms.TextInput(),
            'email': forms.EmailInput(),
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }


class CustomUserLoginForm(AuthenticationForm):
    class Meta():
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(),
            'password': forms.PasswordInput(),
        }