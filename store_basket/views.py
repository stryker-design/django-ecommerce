from django.shortcuts import render, redirect
from django.http import JsonResponse
import json

from . models import *



def basket_summary(request):
    context = {}
    return render(request, 'store/basket/basket-summary.html', context)



