
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


from .models import Product,SellerDetail,Productsize

class AddproductForm(forms.ModelForm):
    class Meta:
        
        model=Product
        fields="__all__"
        
class UpdateSellerDetailForm(forms.ModelForm):
    class Meta:
        model=SellerDetail
        fields = [
			'photo',
			'mobile',
			'shop_Name',
			'gst_Number',
			'alternate_mobile',
			'shop_Address',
			'pincode',
			'landmark',
			'locality',
			'city',
			'state',
		]
        
class UpdateSellerAccountDetail(forms.ModelForm):
    class Meta:
        model=SellerDetail
        fields=['account_Number','account_Holder_Name','ifsc_Code']

class SellerSignUp(UserCreationForm):
	first_name=forms.CharField(widget=forms.TextInput())
	last_name=forms.CharField(widget=forms.TextInput())
	username=forms.CharField(widget=forms.TextInput())
	Shopname=forms.CharField(widget=forms.TextInput())
	GstNumber=forms.CharField(widget=forms.TextInput())

	password1=forms.CharField(label="Password",widget=forms.PasswordInput())
	password2=forms.CharField(label="Password(confirm)",widget=forms.PasswordInput())
	class Meta:
		model=User
		fields=['first_name','last_name','Shopname','GstNumber','username','password1','password2']

class ProductSizeForm(forms.ModelForm):
	class Meta:
		model=Productsize
		fields=['product','product_size','product_quantity']  






