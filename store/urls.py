from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('products/all-products', views.product_all, name='all-products'),
    path('item/<slug:slug>/', views.product_detail, name='product-detail'),
    path('search/<slug:category_slug>/', views.category_detail, name='category-detail'),

]