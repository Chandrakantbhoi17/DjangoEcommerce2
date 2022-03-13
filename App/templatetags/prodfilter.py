from django import template

from Seller.models import Trend

register=template.Library()
def GetLatest1(cat,slice):
    AllProd=[]
    for i in cat.product_set.all():
        AllProd.append(i)
    return AllProd[::int(slice)]
register.filter('GetLatest',GetLatest1)


def TrendLatest1(data,slice):
    TrendProd=[]
    for i in data:
        TrendProd.append(i)
    return TrendProd[::int(slice)]
register.filter('TrendLatest',TrendLatest1)
