from django.shortcuts import render
from .models import Product, Category

# Create your views here.

def all_products(request):
    products = Product.objects.all()
    context = {'products': products}
    
    return render(request, 'shop/all-products.html', context)