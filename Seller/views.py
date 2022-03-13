from multiprocessing.sharedctypes import Value
from unicodedata import category
from unittest import result
from xml.etree.ElementTree import QName
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from .forms import AddproductForm,UpdateSellerDetailForm,UpdateSellerAccountDetail
from .models import Category, Product, Productsize, SellerDetail, SellerSlider, SubCategory
from App.forms import UpdateUserForm
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.conf import settings




@login_required
def Dashboard(request):
    SellerDetail(user=request.user).save()
    
    
    return render(request,'Seller/index.html')
@login_required
def AddProduct(request):
    if request.method=='POST':
       
        addprod=AddproductForm(request.POST,request.FILES)
        p_name=request.POST.get('productname')
        shop=request.user
        category=request.POST.get('category')
        subcategory=request.POST.get('subcategory')
        description=request.POST.get('Description')
        img=request.FILES.get('image')

        price=request.POST.get('price')
        price_not=request.POST.get('price_not')
        gst=request.POST.get('gst')
        sizeitem=request.POST.get('Sizeitems')
        
      
        if bool(int(category)) and bool(int(subcategory)) and  description and  img:
               
               
               category=Category.objects.get(pk=category)
               subcategory=SubCategory.objects.get(pk=subcategory)
               if Product.objects.all():
                  product_id2=Product.objects.all().last().product_id2
                  pd=product_id2[2:]
                  product_id2='pd'+str(hex(int(pd,16)+1))
               else:
                  product_id2='pd'+hex(0)
               Product(product_id2=product_id2,productname=p_name,shop=shop,category=category,subcategory=subcategory,image=img,price=price,price_not=price_not,gst=gst,Description=description).save()
               product=Product.objects.get(product_id2=product_id2)
               for i in range(1,int(sizeitem)+1):
                   product_size=request.POST.get(f'prodsize{i}')
                   product_quantity=request.POST.get(f'prodquantity{i}')
  
                   Productsize(product=product,product_size=product_size,product_quantity=int(product_quantity)).save()
               messages.success(request,'Product Added')
                     

    else:
        
    
        addprod=AddproductForm()
    Myproduct={item for item in  Product.objects.all() if request.user==item.shop}
   
    

    
    category=Category.objects.all()
    return render(request,'Seller/addprod.html',{'addprod':addprod,'category':category,'Myproduct':Myproduct})
@login_required
def Accountsetting(request):
    if request.method=='POST':

        s_form=UpdateSellerDetailForm(request.POST,request.FILES,instance=request.user.sellerdetail)
        u_form=UpdateUserForm(request.POST,instance=request.user)
        if s_form.is_valid():
            s_form.save()
        if u_form.is_valid():
             u_form.save()
    else:
        u_form=UpdateUserForm(instance=request.user)
        s_form=UpdateSellerDetailForm(instance=request.user.sellerdetail)

    return render(request,'Seller/account_base.html',{'s_form':s_form,'u_form':u_form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            messages.success(request, 'Your password was successfully updated!')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'Seller/changepass.html', {'form':form})

@login_required
def BankDetails(request):
    form=UpdateSellerAccountDetail(request.POST,instance=request.user.sellerdetail)
    if form.is_valid():
        form.save()
    form=UpdateSellerAccountDetail(instance=request.user.sellerdetail)
    return render(request,'Seller/bankdetail.html',{'form':form})

@login_required
def GetSubcategory(request):
     catid=request.GET.get('catid')
     category=Category.objects.get(pk=catid)
     subcategory=category.subcategory_set.all()
     return render(request,'Seller/sublog.html',{'subcategory':subcategory})




def Test(request):

    
    return render(request,'Seller/test.html')
  
    











































































































































































































































































































































































































