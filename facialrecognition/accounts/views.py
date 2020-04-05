from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import StreamingHttpResponse
from accounts.forms import RegistrationForm
from .models import UserProfile
import face_recognition
import requests
import cv2
import numpy as numpy
from PIL import Image as img, ImageDraw
import fnmatch
import os

# Create your views here.


def home(request):
    numbers = [1, 2, 3, 4, 5]
    name = 'Aaron Moran'

    args = {'myName': name, 'numbers': numbers}
    return render(request, 'accounts/home.html', args)

# Fully working adding users and images


def register(request):
    global imageName
    global name
    global known_face_name
    context = {}
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            img = form.cleaned_data.get("images")
            obj = UserProfile.objects.create(
                title=name,
                img=img
            )
            obj.save()
            imageName = "./facialrecognition/media/images/"+name+"UserProfilePicture.png"  #creates the image name to save in the images folder
            known_face_names = name  
            print(obj)
          

    else:
        form = RegistrationForm()
    context['form'] = form
    return render(request, 'accounts/register.html', context)


def takePhoto(request):
    context = {}
    for filename in os.listdir("./facialrecognition/media/images/"):  #Searches for image starting with the username
        if fnmatch.fnmatch(filename, '*'+name+'.png'):
            print (filename)
            Reg_Photo = face_recognition.load_image_file("./facialrecognition/media/images/"+filename)
   
    Reg_Photo_encoding = face_recognition.face_encodings(Reg_Photo)[0]

    Known_face_encoding = [
        Reg_Photo_encoding
    ]
    capture = cv2.VideoCapture(0)

    while True:
        ret, frame = capture.read()
        cv2.imshow("Take profile picture", frame)
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            cv2.imwrite(imageName, frame)
            cv2.destroyAllWindows()
            break

    VerificationPhoto = face_recognition.load_image_file(imageName)

    face_locations = face_recognition.face_locations(VerificationPhoto)
    face_encoding = face_recognition.face_encodings(VerificationPhoto, face_locations)

    pil_image = img.fromarray(VerificationPhoto)

    draw = ImageDraw.Draw(pil_image)

    for(top, right, bottom, left), face_encoding in zip(face_locations, face_encoding):
        matches = face_recognition.compare_faces(
        Known_face_encoding, face_encoding)

        

    if True in matches:
       first_match_index = matches.index(True)

       draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 0))
       text_width, text_height = draw.textsize(name)
       draw.rectangle(((left, bottom - text_height), (right, bottom+5)),fill=(0, 0, 0), outline=(0, 0, 0))
       draw.text((left + 6, bottom - text_height),name, fill=(255, 255, 255, 255))
       del draw

       print("Thank you for registering " + name)

       pil_image.show()
       form = RegistrationForm()
       context['form'] = form
       return redirect('/login')   #If the images are verified the user will be brought to the login page
    
    else:
        form = RegistrationForm()
        print("The picture you uploaded was not clear enough or was not you")  #If the pictures do not match the user wil be brought back to the register page
        context['form'] = form
        return redirect('/register')
