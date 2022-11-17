from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('products/all-products', views.all_products, name='all-products'),
    path('products/<slug:slug>', views.all_products, name='product-detail'),

]