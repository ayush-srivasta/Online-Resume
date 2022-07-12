from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from django.contrib.auth import logout,authenticate,login
# Create your views here.
def home(request):
       
    # print(request.user.is_authenticated)
    if request.user.is_authenticated:
        return redirect('main')
    elif request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(request,username=username,password=password)
        if user is not None:
            print(user)
            login(request,user)
            return redirect('main')
        else:
            return HttpResponse("Something wrong")
    else:
        return render(request,"user/home.html")

def Logout(request):
    print("yaha yal tp aa raha hai")
    logout(request)
    print("THis is redirecting to the page")
    return redirect('home')