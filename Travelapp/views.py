from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . models import Table1,Table2
# Create your views here.


def Home(request):
    return render(request,"Home.html")

def index(request):
    obj = Table1.objects.all()
    obj1 = Table2.objects.all()

    return render(request,"index.html",{'result':obj,'results':obj1})

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user=auth.authenticate(username=username,email=email,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid")
            return redirect('Login')
    return render(request,"Login.html")


def Registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username is taken")
                return redirect('Registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email is taken")
                return redirect('Registration')
            else:
                user=User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password)
                user.save()
                return redirect('Login')
        else:
            messages.info(request,"Password doesn't matching")
            return redirect('Registration')

        return redirect('/')

    return render(request,"Registration.html")

def Logout(request):
    auth.logout(request)
    return redirect('/')


