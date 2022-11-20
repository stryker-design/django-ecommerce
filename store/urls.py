from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('products/all-products', views.all_products, name='all-products'),
    path('<slug:slug>/', views.product_detail, name='product-detail'),
    path('shop/<slug:category_slug>/', views.category_detail, name='category-detail'),

]