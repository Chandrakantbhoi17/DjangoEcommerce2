
from itertools import product
from unicodedata import category
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from Seller.models import Productsize, SellerSlider,Trend,Category,SubCategory
from Seller.forms import SellerSignUp
from .forms import UserAuthenticationForm,RegisterForm
from django.contrib import messages
import smtplib
from django.contrib.auth.models import User
import random 
from .models import Cart, EmailOtp
from Seller.models import Category,SubCategory,Product,SellerDetail
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
     slider=SellerSlider.objects.all()
     category=Category.objects.all()
     AllProd=Category.objects.all()[:2]
     trend=Trend.objects.all()
     
     return render(request,'App/index.html',{'AllProd':AllProd,'category':category,'range':range(1,5),'slider':slider,'trend':trend})
def ProductView(request,id):
    product=Product.objects.get(product_id=id)
    sizes=[item for item in Productsize.objects.filter(product=product) if item.product_quantity!=0]
    
    
    return render(request,'App/productview.html',{'sizes':sizes,'product':product})

def ViewAll(request,category):
    if category=="trend":
        trend=Trend.objects.all()
        param={'trend':trend}
    if category.lower() in [item.categoey_name.lower() for item in  Category.objects.all()]:
        cat=Category.objects.filter(categoey_name=category).first()
        param={"cat":cat}
  
        
 
    return render(request,'App/viewall.html',param)

def order_now(request):
    return HttpResponse('hiii')
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


def Filter(request,sub):
   
    subcat=SubCategory.objects.filter(sub_name=sub).first()
    
    

    
    return render(request,'App/filter.html',{'sub':subcat})
@login_required
def add_to_cart(request):
    if request.method=="GET":
        prod_id=int(request.GET.get("prodid"))
        prodsize=request.GET.get('prodsize')
        Cart(user=request.user,product_id=prod_id,product_size=prodsize,quantity=1).save()
    return redirect("/cart")
   
@login_required
def cart(request):
    total=0.0
    products=[]
    tax=0.0
    for i in [item for item in Cart.objects.all() if request.user==item.user]:
        temptotal=i.quantity*Product.objects.filter(product_id=i.product_id).first().price
        total+=temptotal
        tax+=temptotal*int(Product.objects.filter(product_id=i.product_id)[0].gst)/100
    for id in [ item.product_id for item in Cart.objects.all() if item.user==request.user]:
        prod=Product.objects.filter(product_id=id)
        products.append(prod)
    data={
        "products":products,
        "total":total,
        "tax":tax,
        "shipping":70,
        'subtotal':total+tax+70
    }
    return render(request,"App/cart.html",data)
    
def SellersignUp(request):
    if request.method=='POST':
    
        form=SellerSignUp(request.POST)
        if form.is_valid():
            form.save()
            uname=request.POST.get('username')
            user=User.objects.filter(username=uname).first()
            user.is_staff=True
            SellerDetail(user=user).save()
            user.save()
    else:
        form=SellerSignUp()
    category=Category.objects.all()    
    return render(request,'App/sellersignup.html',{'form':form,'category':category})

def Search(request):
    query=request.GET['query'].lower()
    splitedquery=query.lower().split()[:2][::-1]
    Value=[]
    prod=[]
    product=[]
    if len(query) is not 0:
         for i in Product.objects.all():
             if query in i.productname.lower() or query in  i.Description.lower() :
                 prod.append(i.product_id)

         if len(prod)==0:
            
            for i in Product.objects.all():
                for j in splitedquery:
                    if j in i.productname.lower() or query in  i.Description.lower():
                        prod.append(i.product_id)
        
       

         for i in prod:
            if i not in Value:
                Value.append(i)
         for id in Value:
            p=Product.objects.filter(product_id=id).first()
            product.append(p)
         products=product[::-1]
    return render(request,'App/search.html',{'products':products})
    
   
    




    





























