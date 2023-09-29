from django.forms import ModelForm,widgets
from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm 

class UserForm(UserCreationForm):
    class Meta:
         model = get_user_model()
         fields = ['username', 'email', 'password1']
         widgets = {
             'username': forms.TextInput(attrs={'class': 'form-control'}),
             'email': forms.EmailInput(attrs={'class': 'form-control'}),
             'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
             'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
         }
class UserLoginForm(AuthenticationForm):
      
      widgets={
           'username': forms.TextInput(attrs={'class': 'form-control'}),
           'password': forms.PasswordInput(attrs={'class': 'form-control'}),
      }