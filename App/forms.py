from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserAuthenticationForm(AuthenticationForm):
    username=forms.CharField(max_length=100,label='Username:',widget=forms.TextInput(),error_messages={'required':'Please enter username'})
    password=forms.CharField(max_length=100,label='Password:',widget=forms.PasswordInput(),error_messages={'required':'Please enter password'})
    class Meta:
        model=User
        fields=['username','password']
class RegisterForm(UserCreationForm):
    first_name=forms.CharField(max_length=100,label='Firstname:',widget=forms.TextInput(),error_messages={'required':'Please enter firstname'})
    last_name=forms.CharField(max_length=100,label='Lastname:',widget=forms.TextInput(),error_messages={'required':'Please enter lastname'})
    username=forms.CharField(max_length=100,label='Username:',widget=forms.TextInput(),error_messages={'required':'Please enter username'})
    password1=forms.CharField(max_length=100,label='Password:',widget=forms.PasswordInput(),error_messages={'required':'Please enter password'})
    password2=forms.CharField(max_length=100,label='Password(Confirm):',widget=forms.PasswordInput(),error_messages={'required':'Please enter password(confirm)'})
    class Meta:
        model=User
        fields=['first_name','last_name','username','password1','password2']