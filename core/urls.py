from django.contrib import admin
from django.urls import path, include
from . import views
from .views import index

app_name = 'core'

urlpatterns = [
    path('', views.index, name='home'),
   

]