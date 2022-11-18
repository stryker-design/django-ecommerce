from django.shortcuts import render
from django.contrib.auth.models import User
from store.models import Category, Product
# Create your views here.


def index(request):
    category_dropdwon = Category.objects.all()
    products = Product.objects.filter(best_seller=True)
    context = {'category_dropdown': category_dropdwon, 'products': products}
    return render(request, 'core/index.html', context)