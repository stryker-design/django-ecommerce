from django.urls import path

from . import views


app_name = 'store_basket'

urlpatterns = [
    path('', views.basket_summary, name='basket-summary'), 
    path('add/', views.basket_add, name='basket_add'),
]