from xml.etree.ElementTree import tostring
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
import os
from django.http import FileResponse
from PIL import Image
# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import Resume
from django.contrib.auth.models import User

@login_required
def home(request):
    if request.method=='POST':
        print("This is the page")
    else:
        list_resume=Resume.objects.filter(user=request.user.id)
        # pdf=list_resume.get()
        print(list_resume)
        return render(request,'backend/main.html',{"resume":list_resume})

@login_required
def save_file(request):
    if request.method=='POST':
        name=request.POST.get('name')
        pdf=request.FILES.get('pdf')
        # print(request.POST)
        user=User.objects.get(pk=request.user.id) 
        pdf.name=request.user.username+' '+name+'.pdf'
        resume=Resume.objects.create(name=name,file=pdf,user=user)
        resume.save()
        obj=Resume.objects.filter(user=user)
    return redirect('main')

def download_pdf(request,username,name):
    print("YAha tak aa raha hai")
    print(name)
    fname=username+' '+name+'.pdf'
    fname=fname.replace(" ", "_")
    filepath = os.path.join('media/pdf', fname)
    print(fname)
    
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')


def open_pdf(request,username,name):
    obj=Resume.objects.filter(user=User.objects.get(username=username))
    resume=obj.get(name=name)
    pdf=resume.file
    print(pdf)
    return HttpResponse(pdf.read(),content_type='application/pdf')

@login_required
def Logout(request):
    print("yaha yal tp aa raha hai")
    logout(request)
    print("THis is redirecting to the page")
    return redirect('home')