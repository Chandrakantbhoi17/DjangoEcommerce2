
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout

from Seller.models import SellerSlider
from Seller.forms import SellerSignUp
from .forms import UserAuthenticationForm,RegisterForm
from django.contrib import messages
import smtplib
from django.contrib.auth.models import User
import random 
from .models import EmailOtp
from Seller.models import Category,SubCategory
from django.conf import settings


def SendOtp(mail):
    r=random.randint(1000,9999)
    user=User.objects.filter(username=mail).first()
    
    EmailOtp(user=user,otp=mail).save()
   
    server=smtplib.SMTP('smtp.gmail.com',587)

    server.starttls()
    subject='DjangoEcommerce Password Reset'
    mailcontent=f'Your otp is :{r}'
    server.login('djangoecommerce25@gmail.com','Sabitabhoi7')
    msg='''Subject:{}\n\n{}'''.format(subject,mailcontent)
    server.sendmail('djangoecommerce25@gmail.com',mail,msg)


def Home(request):
     if request.user.is_staff:
        return redirect('dashboard')
     slider=SellerSlider.objects.all()
     category=Category.objects.all()
     mens=Category.objects.all().first()


     return render(request,'App/index.html',{'category':category,'slider':slider,'mens':mens})

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
    category=Category.objects.all()
    return render(request,'App/login.html',{'form':fm,'category':category})

def Register(request):
    if request.method=='POST':
        fm=RegisterForm(request.POST)
        if fm.is_valid():
            fm.save()
            uname=fm.cleaned_data['username']
            user=User.objects.filter(username=uname).first()
            user.email=uname
            user.save()
            SendOtp(uname)
            return HttpResponse('check mail')
    else:
        fm=RegisterForm()
    category=Category.objects.all()
    return render(request,'App/register.html',{'form':fm,'category':category})


def Logout(request):
    messages.success(request,'Thanks for spending some quality time with the our service.')
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def Filter(request,cat,sub):

    
    return render(request,'App/filter.html')

def SellersignUp(request):
    if request.method=='POST':
    
        form=SellerSignUp(request.POST)
     
      
        if form.is_valid():
            form.save()
            uname=request.POST.get('username')

            

            user=User.objects.filter(username=uname).first()
            user.is_staff=True
            user.save()
    else:
        form=SellerSignUp()
    category=Category.objects.all()    
    return render(request,'App/sellersignup.html',{'form':form,'category':category})
    




    