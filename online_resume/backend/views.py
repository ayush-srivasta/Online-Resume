import re
from xml.etree.ElementTree import tostring
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
import io
import os
import fitz
from PIL import Image
# Create your views here.
from django.contrib.auth.decorators import login_required

from .models import Resume
from .import image_pdf
from django.contrib.auth.models import User

@login_required
def home(request):
    if request.method=='POST':
        print("This is the page")
    else:
        list_resume=Resume.objects.filter(user=request.user.id)
        print(list_resume)
        return render(request,'backend/main.html',{"resume":list_resume})

@login_required
def save_file(request):
    if request.method=='POST':
        name=request.POST.get('name')
        pdf=request.FILES.get('pdf')
        print(request.POST)
        # print(pdf.name)
        # print(os.getcwd())
        # image=image_pdf.convert_pfd_image(pdf)
        
        # print(image)
        user=User.objects.get(pk=request.user.id) 
        resume=Resume.objects.create(name=name,file=pdf,user=user)
        resume.save()
        # print(resume)

    return HttpResponse("This is the page")




@login_required
def Logout(request):
    print("yaha yal tp aa raha hai")
    logout(request)
    print("THis is redirecting to the page")
    return redirect('home')