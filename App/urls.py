from django.urls import path
from .import views
from django.contrib.auth import views as auth_views 


urlpatterns = [
    path('',views.Home,name='home'),
    path('Login/',views.Login,name='login'),
    path('Register/',views.Register,name='register'),
    path('Logout/',views.Logout,name="logout"),
    path('Password_reset/',auth_views.PasswordResetView.as_view(template_name='App/password_reset.html'),name='Passwordreset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='App/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="App/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='App/password_reset_complete.html'), name='password_reset_complete'),      

   
   
  
]