from math import prod
from django import template


from Seller.models import Product, Trend,ProductReview
from  App.models import Cart


register=template.Library()
def GetLatest1(cat,slice):
    AllProd=[]
    for i in cat.product_set.all():
        AllProd.append(i)
    return AllProd[::int(slice)]
register.filter('GetLatest',GetLatest1)


def TrendLatest1(data,slice):
    TrendProd=[]
    print(data,slice)
    for i in data:
        TrendProd.append(i)
    return TrendProd[::int(slice)]
register.filter('TrendLatest',TrendLatest1)

def Review(prodid,slice):
    prodreviews=[]
    prod=Product.objects.filter(product_id=prodid)[0]
    for i in ProductReview.objects.filter(product=prod):
        prodreviews.append(i)
    return prodreviews[::-1][:int(slice)]
    
register.filter('Reviews',Review)


