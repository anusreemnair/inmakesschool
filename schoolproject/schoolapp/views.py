# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import AuthenticationForm
# from django.shortcuts import render,redirect

from django.contrib import auth
from django.core.checks import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")



def register(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exists")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,"password does not match")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")


def forms(request):
    return render(request, 'forms.html')

def newpage(request):
    return render(request, 'newpage.html')