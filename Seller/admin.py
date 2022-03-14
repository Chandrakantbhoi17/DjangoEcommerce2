from django.contrib import admin
from .models import Product, ProductReview, SellerDetail,SellerSlider,Category,SubCategory,Productsize,Trend

admin.site.register(SellerDetail)
admin.site.register(SellerSlider)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(ProductReview)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['product_id2','category','subcategory','price','price_not',]

@admin.register(Productsize)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display=['product','product_size','product_quantity']

@admin.register(Trend)
class Trend(admin.ModelAdmin):
    list_diplay=['product']
