from django.shortcuts import render, redirect
from django.http import JsonResponse
import json



def basket_summary(request):
    context = {}
    return render(request, 'store/basket/basket-summary.html', context)

def updateItem(request):
    data = json.loads(request.body)
    return JsonResponse('Item was added', safe=False)

