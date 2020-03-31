from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import StreamingHttpResponse
from accounts.forms import RegistrationForm
from .models import UserProfile
import requests
import cv2
import numpy as np

# Create your views here.
def home(request):
    numbers = [1,2,3,4,5]
    name ='Aaron Moran'

    args = {'myName': name, 'numbers': numbers}
    return render(request, 'accounts/home.html', args)

# Fully working adding users and images

def register(request):
    global imageName
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
            imageName ="./facialrecognition/media/images/"+name+".png"
            print(obj)
          
    else:
        form = RegistrationForm()
    context['form'] = form
    return render(request, 'accounts/register.html', context)

def takePhoto(request):
    context = {}
    capture = cv2.VideoCapture(0)

    while True:
        # Show camera window
        ret, frame = capture.read()
        cv2.imshow("Take profile picture", frame)

        # Save on pressing "Spacebar" then exit
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            cv2.imwrite(imageName,  frame)
            cv2.destroyAllWindows()
            break

    # When everything done, release the capture
    capture.release()

    form = RegistrationForm()
    context['form'] = form
    return redirect('/login')