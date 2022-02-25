from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from .forms import UserAuthenticationForm,RegisterForm
from django.contrib import messages
def Home(request):
    return render(request,'App/base.html')

def Login(request):
    if request.method=='POST':
        fm=UserAuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/')
    else:
        fm=UserAuthenticationForm()
    return render(request,'App/login.html',{'form':fm})

def Register(request):
    if request.method=='POST':
        fm=RegisterForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=RegisterForm()
    return render(request,'App/register.html',{'form':fm})


def Logout(request):
    messages.success(request,'Thanks for spending some quality time with the our service.')
    logout(request)
    return HttpResponseRedirect(reverse('login'))



    