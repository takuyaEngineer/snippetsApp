from django.shortcuts import render, redirect
from common.views import ComSessionCheck
from django.conf import settings

# Create your views here.

def top(request):
    return render(request, 'top/index.html')