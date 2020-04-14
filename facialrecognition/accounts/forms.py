from django import  forms
# from django.db import models 
# from django.contrib.auth.models import User
# from .models import UserProfile
# from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(forms.Form):
    name = forms.CharField()
    images = forms.ImageField(required=True)

class LoginForm(forms.Form):
    username = forms.CharField()

