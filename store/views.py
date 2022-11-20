from django.shortcuts import get_object_or_404, render

from .models import Category, Product

# Create your views here.

def all_products(request):
    products = Product.objects.filter(is_active=True)
    category_dropdown = Category.objects.all()
    context = {'products': products, 'category_dropdown': category_dropdown}
    return render(request, 'store/products/all-products.html', context)


def product_detail(request, slug):
    # Singlular Product
    product = get_object_or_404(Product, slug=slug, in_stock=True )
     # More items section
    product_gallery = Product.objects.all()
    # Categories
    category = Category.objects.all()
    category_dropdown = Category.objects.all()


    context = {'product': product, 'product_gallery': product_gallery, 'category': category, 'category_dropdown': category_dropdown}    
    return render(request, 'store/products/product-detail.html', context)

def category_detail(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    category_dropdown = Category.objects.all()
    prodcuts = Product.objects.filter(category=category)
    context = {'category': category, 'products': prodcuts, 'category_dropdown': category_dropdown}
    return render(request, 'store/products/category.html', context)