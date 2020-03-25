from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegistrationForm
from .models import UserProfile

# Create your views here.
def home(request):
    numbers = [1,2,3,4,5]
    name ='Aaron Moran'

    args = {'myName': name, 'numbers': numbers}
    return render(request, 'accounts/home.html', args)

# Trying to get images adding on the User side.
# NOT NULL constraint failed: accounts_userprofile.user_id

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/account/')
    else:
        form = RegistrationForm() 
    args = {'form': form}
    return render(request, 'accounts/register.html', args)