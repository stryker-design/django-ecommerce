from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import json

from store.models import Product
from .basket import Basket




def basket_summary(request):
    context = {}
    return render(request, 'store/basket/basket-summary.html', context)


# def basket_add(request):
#     # Bringing Basket class from basket.py into view
#     basket = Basket(request)

#     if request.POST.get('action') == 'post':
#         product_id = int(request.POST.get('productid'))
#         # Finding the product in DB & passing ID from product_id that gets the ID from AJAX
#         product = get_object_or_404(Product, id=product_id)

#         # Adding/saving product id to session
#         basket.add(product=product)
#         response = JsonResponse({'test': 'data'})
#         return response

def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)

        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        return response


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response


def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        basket.update(product=product_id, qty=product_qty)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response

