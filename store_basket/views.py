from django.shortcuts import render, redirect

def basket_summary(request):
    context = {}
    return render(request, 'store/basket/basket-summary.html', context)
