from django.urls import path

from . import views


app_name = 'store_basket'

urlpatterns = [
    path('summary/', views.basket_summary, name='basket-summary'), 
]