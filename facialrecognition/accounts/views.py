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

# Fully working adding users and images

def register(request):
    context = {}
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            img = form.cleaned_data.get("images")
            obj = UserProfile.objects.create(
                title = name,
                img = img
            )
            obj.save()
            print(obj)
    else:
        form = RegistrationForm()
    context['form'] = form
    return render(request, 'accounts/register.html', context)

