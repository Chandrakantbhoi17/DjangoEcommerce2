from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('Seller/Dashboard',views.Dashboard,name="dashboard"),
    path('Seller/AddProduct',views.AddProduct,name='addproduct'),
    path('Seller/Account',views.Accountsetting,name="accountsetting"),
    path('Seller/ChangePassword',views.change_password,name="changepass"),
    path('Seller/BankDetails',views.BankDetails,name='bankdetail'),
    path('Seller/Getsubcategory',views.GetSubcategory),
    path('Test/',views.Test),
    
]
