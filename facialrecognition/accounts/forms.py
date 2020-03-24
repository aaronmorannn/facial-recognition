from django import  forms
from django.db import models 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(forms.ModelForm):
    # user = forms.CharField(max_length = 25, required=True)
    image = forms.ImageField(required=False) 
    
    def __str__(self): 
        return self.user 

    class Meta:
        model = User
        fields = ("username",)

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']


        if commit:
            user.save()

        return user