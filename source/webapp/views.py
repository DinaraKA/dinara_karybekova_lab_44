from django.shortcuts import render
from webapp.models import Product


def index_view(request):
    products = Product.objects.filter(amount__gt=0).order_by('name','category')
    return render(request, 'index.html', context={
        'products': products
    })



