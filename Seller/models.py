from itertools import product
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User


class SellerDetail(models.Model):
	SEX_CHOICES = (("Male",'Male'),("Female",'Female'),("Other",'Other'))
	STATE_CHOICES = (
		("Andaman & Nicobar Islands",'Andaman & Nicobar Islands'),
		("Andhra Pradesh",'Andhra Pradesh'),
		("Arunachal Pradesh",'Arunachal Pradesh'),
		("Assam",'Assam'),
		("Bihar",'Bihar'),
		("Chandigarh",'Chandigarh'),
		("Chhattisgarh",'Chhattisgarh'),
		("Dadra & Nagar Haveli",'Dadra & Nagar Haveli'),
		("Daman and Diu",'Daman and Diu'),
		("Delhi",'Delhi'),
		("Goa",'Goa'),
		("Gujarat",'Gujarat'),
		("Haryana",'Haryana'),
		("Himachal Pradesh",'Himachal Pradesh'),
		("Jammu & Kashmir",'Jammu & Kashmir'),
		("Jharkhand",'Jharkhand'),
		("Karnataka",'Karnataka'),
		("Kerala",'Kerala'),
		("Lakshadweep",'Lakshadweep'),
		("Madhya Pradesh",'Madhya Pradesh'),
		("Maharashtra",'Maharashtra'),
		("Manipur",'Manipur'),
		("Meghalaya",'Meghalaya'),
		("Mizoram",'Mizoram'),
		("Nagaland",'Nagaland'),
		("Odisha",'Odisha'),
		("Puducherry",'Puducherry'),
		("Punjab",'Punjab'),
		("Rajasthan",'Rajasthan'),
		("Sikkim",'Sikkim'),
		("Tamil Nadu",'Tamil Nadu'),
		("Telangana",'Telangana'),
		("Tripura",'Tripura'),
		("Uttarakhand",'Uttarakhand'),
		("Uttar Pradesh",'Uttar Pradesh'),
		("West Bengal",'West Bengal'),
		)
	user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
	photo = models.ImageField(default='User_photos/default.png',upload_to='User_photos')
	mobile = models.CharField(max_length=10,null=True)
	gst_Number = models.CharField(max_length=15,null=True)
	shop_Name = models.CharField(max_length=500,null=True)
	alternate_mobile = models.CharField(max_length=10,null=True,blank=True)
	shop_Address= models.TextField()
	pincode = models.CharField(max_length=6, null=True)
	landmark = models.CharField(max_length=500, null=True, blank=True)
	locality = models.CharField(max_length=100, null=True, blank=True)
	city = models.CharField(max_length=100, null=True, blank=True)
	state = models.CharField(max_length=50,choices=STATE_CHOICES, null=True)
	account_Holder_Name = models.CharField(max_length=50, null=True)
	account_Number = models.CharField(max_length=20, null=True)
	ifsc_Code = models.CharField(max_length=11, null=True)
class Category(models.Model):
	categoey_name = models.CharField(max_length=50, default="")
	def __str__(self):
    		return self.categoey_name


class SubCategory(models.Model):
    categoryname=models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_name = models.CharField(max_length=50, default="")

	
	

	
	
	




	

class Product(models.Model):
	GST_CHOICES=(("0",'0'),("3",'3'),("5",'5'),("12",'12'),("18",'18'),("28",'28'))
	product_id= models.BigAutoField(primary_key=True)
	product_id2= models.CharField(max_length=100,default='')
	shop=models.ForeignKey(User, on_delete=models.CASCADE,default='')
	product_name= models.CharField(max_length=100)
	category=models.ForeignKey(Category,on_delete=models.CASCADE)
	subcategory=models.ForeignKey(SubCategory, default="", verbose_name="Category", on_delete=models.SET_DEFAULT, null=True)
	price=models.IntegerField(default=0)
	price_not = models.IntegerField(default=999)
	Description= models.TextField()
	gst = models.CharField(default='0',max_length=3,choices=GST_CHOICES)
	pub_date = models.DateField(auto_now=True)
	image=models.ImageField(upload_to='products/images', default="",null=True)


class SellerSlider(models.Model):
	name = models.CharField(max_length=50, default = "", null=True)
	image = models.ImageField(upload_to='seller_slider_img')
	url = models.CharField(max_length=200, default = "#", null=True)

class Productsize(models.Model):
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	product_size=models.CharField(max_length=2,null=True,blank=True)
	product_quantity=models.PositiveIntegerField(null=True,blank=True)


	
