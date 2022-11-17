from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.


def index(request):

    # user = User.objects.get()
    context = {}
    return render(request, 'core/index.html', context)