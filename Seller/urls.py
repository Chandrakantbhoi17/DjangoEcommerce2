from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('Seller/Dashboard',views.Dashboard,name="dashboard"),
    
]
