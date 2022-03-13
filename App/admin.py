from django.contrib import admin
from .models import Cart, EmailOtp,UserDetail

@admin.register(EmailOtp)
class  OtpAdmin(admin.ModelAdmin):
    list_display=['user','otp']
@admin.register(UserDetail)
class UserDetailAdmin(admin.ModelAdmin):
    list_display=['user','is_verified']
admin.site.register(Cart)

